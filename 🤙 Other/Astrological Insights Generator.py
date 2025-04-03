from datetime import datetime

# 1. Western Zodiac Sign
def get_zodiac_sign(birthdate):
    zodiac_signs = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21))
    ]
    month, day = birthdate.month, birthdate.day
    for sign, start, end in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "Unknown"

# 2. Chinese Zodiac Animal
def get_chinese_zodiac(year):
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", 
               "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    return animals[(year - 1900) % 12]

# 3. Native American Zodiac Sign
def get_native_american_zodiac(birthdate):
    zodiac_signs = [
        ("Otter", (1, 20), (2, 18)),
        ("Wolf", (2, 19), (3, 20)),
        ("Falcon", (3, 21), (4, 19)),
        ("Beaver", (4, 20), (5, 20)),
        ("Deer", (5, 21), (6, 20)),
        ("Woodpecker", (6, 21), (7, 21)),
        ("Salmon", (7, 22), (8, 21)),
        ("Bear", (8, 22), (9, 21)),
        ("Raven", (9, 22), (10, 22)),
        ("Snake", (10, 23), (11, 22)),
        ("Owl", (11, 23), (12, 21)),
        ("Goose", (12, 22), (1, 19))
    ]
    month, day = birthdate.month, birthdate.day
    for sign, start, end in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "Unknown"

# 4. Mayan Zodiac Sign
def get_mayan_zodiac_sign(birthdate):
    day_signs = [
        "Imix", "Ik'", "Ak'b'al", "K'an", "Chikchan", "Kimi", "Manik'",
        "Lamat", "Muluk", "Ok", "Chuwen", "Eb'", "B'en", "Ix", "Men",
        "K'ib", "Kab'an", "Etz'nab'", "Kawak", "Ajaw"
    ]
    
    # Dictionary mapping Mayan day signs to their English meanings
    english_meanings = {
        "Imix": "Crocodile",
        "Ik'": "Wind",
        "Ak'b'al": "Night",
        "K'an": "Seed",
        "Chikchan": "Serpent",
        "Kimi": "Death",
        "Manik'": "Deer",
        "Lamat": "Rabbit",
        "Muluk": "Water",
        "Ok": "Dog",
        "Chuwen": "Monkey",
        "Eb'": "Human",
        "B'en": "Maize",
        "Ix": "Jaguar",
        "Men": "Eagle",
        "K'ib": "Bat",
        "Kab'an": "Earth",
        "Etz'nab'": "Flint",
        "Kawak": "Storm",
        "Ajaw": "Sun"
    }

    # Compute the Julian Day Number (JDN) for the birthdate
    y = birthdate.year
    m = birthdate.month
    d = birthdate.day
    a = (14 - m) // 12
    y_adj = y + 4800 - a
    m_adj = m + 12 * a - 3
    jdn = d + ((153 * m_adj + 2) // 5) + 365 * y_adj + y_adj // 4 - y_adj // 100 + y_adj // 400 - 32045

    # Calculate Tzolkin number and day name using a common correlation formula
    tzolkin_number = ((jdn + 4) % 13) + 1
    tzolkin_day_sign = day_signs[(jdn + 16) % 20]
    english_meaning = english_meanings[tzolkin_day_sign]
    
    return f"{tzolkin_number} {tzolkin_day_sign} ({english_meaning})"


# 5. Egyptian Zodiac Sign
def get_egyptian_zodiac_sign(birthdate):
    egyptian_zodiac_signs = [
        ("Nile", [((1, 1), (1, 7)), ((6, 19), (6, 28)), ((9, 1), (9, 7)), ((11, 18), (11, 26))]),
        ("Amun-Ra", [((1, 8), (1, 21)), ((2, 1), (2, 11))]),
        ("Mut", [((1, 22), (1, 31)), ((9, 8), (9, 22))]),
        ("Geb", [((2, 12), (2, 29)), ((8, 20), (8, 31))]),
        ("Osiris", [((3, 1), (3, 10)), ((11, 27), (12, 18))]),
        ("Isis", [((3, 11), (3, 31)), ((10, 18), (10, 29)), ((12, 19), (12, 31))]),
        ("Thoth", [((4, 1), (4, 19)), ((11, 8), (11, 17))]),
        ("Horus", [((4, 20), (5, 7)), ((8, 12), (8, 19))]),
        ("Anubis", [((5, 8), (5, 27)), ((6, 29), (7, 13))]),
        ("Seth", [((5, 28), (6, 18)), ((9, 28), (10, 2))]),
        ("Bastet", [((7, 14), (7, 28)), ((9, 23), (9, 27)), ((10, 3), (10, 17))]),
        ("Sekhmet", [((7, 29), (8, 11)), ((10, 30), (11, 7))])
    ]
    month, day = birthdate.month, birthdate.day
    for sign, periods in egyptian_zodiac_signs:
        for start, end in periods:
            if (month > start[0] or (month == start[0] and day >= start[1])) and \
               (month < end[0] or (month == end[0] and day <= end[1])):
                return sign
    return "Unknown"

# 6. Celtic Tree Astrology Sign
def get_celtic_tree_sign(birthdate):
    celtic_tree_signs = [
        ("Birch", (12, 24), (1, 20)),
        ("Rowan", (1, 21), (2, 17)),
        ("Ash", (2, 18), (3, 17)),
        ("Alder", (3, 18), (4, 14)),
        ("Willow", (4, 15), (5, 12)),
        ("Hawthorn", (5, 13), (6, 9)),
        ("Oak", (6, 10), (7, 7)),
        ("Holly", (7, 8), (8, 4)),
        ("Hazel", (8, 5), (9, 1)),
        ("Vine", (9, 2), (9, 29)),
        ("Ivy", (9, 30), (10, 27)),
        ("Reed", (10, 28), (11, 24)),
        ("Elder", (11, 25), (12, 23))
    ]
    month, day = birthdate.month, birthdate.day
    for sign, start, end in celtic_tree_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "Unknown"

# 7. Birthstone
def get_birthstone(month):
    stones = ["Garnet", "Amethyst", "Bloodstone", "Diamond", "Emerald", 
              "Pearl", "Ruby", "Sardonyx", "Sapphire", "Opal", "Topaz", "Lapis Lazuli"]
    return stones[month - 1]

# 8. Life Path Number (Numerology)
def reduce_to_single_digit_or_master_number(number, final_reduction=True):
    if number in [11, 22, 33] and not final_reduction:
        return number
    while number > 9 and number not in [11, 22, 33]:
        number = sum(int(digit) for digit in str(number))
    return number

def calculate_life_path_number(birthdate):
    month = reduce_to_single_digit_or_master_number(birthdate.month, False)
    day = reduce_to_single_digit_or_master_number(birthdate.day, False)
    year_sum = sum(int(digit) for digit in str(birthdate.year))
    year = reduce_to_single_digit_or_master_number(year_sum, False)
    life_path_sum = month + day + year
    return reduce_to_single_digit_or_master_number(life_path_sum, True)

# 9. Tarot Birth Cards
def calculate_tarot_birth_cards(birthdate):
    major_arcana = [
        "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
        "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
        "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
        "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
        "Judgement", "The World"
    ]
    mm, dd, yy = birthdate.month, birthdate.day, birthdate.year % 100
    century = birthdate.year // 100
    total = mm + dd + century + yy
    if total >= 100:
        total = (total // 10) + (total % 10)
    while total > 21:
        total = sum(int(digit) for digit in str(total))
    first_card = major_arcana[total]
    if total > 9:
        total = sum(int(digit) for digit in str(total))
    second_card = major_arcana[total]
    return [first_card, second_card]

# 10. Feng Shui Kua Number
def calculate_kua_number(year, gender):
    last_two_digits = sum(int(digit) for digit in str(year)[-2:])
    while last_two_digits > 9:
        last_two_digits = sum(int(digit) for digit in str(last_two_digits))
    if gender.lower() == 'male':
        kua_number = 10 - last_two_digits
    elif gender.lower() == 'female':
        kua_number = (last_two_digits + 5) % 9
    if kua_number == 0:
        kua_number = 9
    return kua_number

def get_kua_group_and_directions(kua_number):
    east_group = [1, 3, 4, 9]
    west_group = [2, 5, 6, 7, 8]
    if kua_number in east_group:
        group = "East"
        auspicious = ["North", "South", "East", "Southeast"]
        inauspicious = ["West", "Northwest", "Southwest", "Northeast"]
    elif kua_number in west_group:
        group = "West"
        auspicious = ["West", "Northwest", "Southwest", "Northeast"]
        inauspicious = ["North", "South", "East", "Southeast"]
    else:
        group = "Unknown"
        auspicious = []
        inauspicious = []
    return group, auspicious, inauspicious

# Aesthetic display function for terminal output
def print_results(birthdate, gender):
    # Header
    print("\033[95m" + "=" * 60 + "\033[0m")
    print("\033[1m" + " Astrological Profile ".center(60) + "\033[0m")
    print("\033[95m" + "=" * 60 + "\033[0m")
    
    # Display each category with colored labels
    print("\033[96mWestern Zodiac Sign:\033[0m       ", get_zodiac_sign(birthdate))
    print("\033[96mChinese Zodiac Animal:\033[0m       ", get_chinese_zodiac(birthdate.year))
    print("\033[96mNative American Zodiac:\033[0m      ", get_native_american_zodiac(birthdate))
    print("\033[96mMayan Zodiac Sign:\033[0m           ", get_mayan_zodiac_sign(birthdate))
    print("\033[96mEgyptian Zodiac Sign:\033[0m        ", get_egyptian_zodiac_sign(birthdate))
    print("\033[96mCeltic Tree Astrology Sign:\033[0m  ", get_celtic_tree_sign(birthdate))
    print("\033[96mBirthstone:\033[0m                  ", get_birthstone(birthdate.month))
    print("\033[96mLife Path Number:\033[0m            ", calculate_life_path_number(birthdate))
    tarot_cards = calculate_tarot_birth_cards(birthdate)
    print("\033[96mTarot Birth Cards:\033[0m           ", ", ".join(tarot_cards))
    
    kua_number = calculate_kua_number(birthdate.year, gender)
    group, auspicious, inauspicious = get_kua_group_and_directions(kua_number)
    print("\033[96mFeng Shui Kua Number:\033[0m        ", kua_number)
    print("\033[96mKua Group:\033[0m                   ", group)
    print("\033[96mAuspicious Directions:\033[0m       ", ", ".join(auspicious))
    print("\033[96mInauspicious Directions:\033[0m     ", ", ".join(inauspicious))
    
    print("\033[95m" + "=" * 60 + "\033[0m")

# Main function to get user input and display the profile
def main():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    gender = input("Enter your gender (Male/Female): ")
    print_results(birthdate, gender)

if __name__ == "__main__":
    main()
