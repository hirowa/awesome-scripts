$folderPath = "Change Path Here!"

$videos = Get-ChildItem -Path $folderPath -File | Where-Object { $_.Extension -match '\.mp4|\.mkv|\.avi|\.mov|\.wmv' }

$totalDuration = [timespan]::Zero
$videoList = @()

foreach ($video in $videos) {
    $shell = New-Object -ComObject Shell.Application
    $folder = $shell.Namespace($video.DirectoryName)
    $file = $folder.ParseName($video.Name)
    $durationString = $folder.GetDetailsOf($file, 27) -replace '[^0-9:]','' # Extract only the time values
    
    if ($durationString -match '^\d+:\d+(:\d+)?$') {
        $parts = $durationString -split ':'
        if ($parts.Count -eq 3) {
            $ts = New-TimeSpan -Hours $parts[0] -Minutes $parts[1] -Seconds $parts[2]
        } elseif ($parts.Count -eq 2) {
            $ts = New-TimeSpan -Minutes $parts[0] -Seconds $parts[1]
        }
        $totalDuration += $ts
        $videoList += [PSCustomObject]@{
            Name = $video.Name
            Duration = $durationString
        }
    }
}

$videoList | Format-Table -AutoSize
Write-Output "Total Duration: $($totalDuration.Hours)h $($totalDuration.Minutes)m $($totalDuration.Seconds)s"
