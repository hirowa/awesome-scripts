import os
import time
from anthropic import Anthropic
import pandas as pd
import tempfile
import shutil

# API Setup
client = Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.getenv('ANTHROPIC_API_KEY'),
)

# Input CSV file
input_csv = os.path.normpath(input("Enter the path to the input CSV file: ")).strip().strip('"')

# API Rate Limits (modify these to suit your usage limits)
REQUESTS_PER_MINUTE = 4800  # 60 requests per minute
REQUEST_INTERVAL = 60 / REQUESTS_PER_MINUTE

def generate_prompt(prompt, output_a, output_b, output_c, output_d):
    """
    Create the prompt for the API call based on given parameters.
    """
    return f'''
    You are an expert LLM Outputs reviewer en grader. You have over 30 years of experience in inspecting and grading LLM Outputs for different industries.
    Your task is to grade the following LLM Outputs (A, B, C, D) using the [Rubric] below. ALWAYS grade all 4 outputs!!!
    Be extremely strict and hard in grading. Take note that grades above 90 are almost impossible!
    It's a competition between all 4 submissions, so they can't share the same grade!

    ### [Rubric] for Evaluating LLM Outputs
    #### 1. **Relevance to the Prompt (25 points)**
       - **25-20 points (Excellent)**: The response directly addresses all aspects of the prompt with relevant information and stays consistently on topic.
       - **19-15 points (Good)**: The response is mostly relevant to the prompt, addressing most aspects with minor deviations or omissions.
       - **14-10 points (Average)**: The response partially addresses the prompt but misses some key details or includes irrelevant information.
       - **9-5 points (Below Average)**: The response is only tangentially related to the prompt, with significant gaps in addressing key points.
       - **4-0 points (Poor)**: The response fails to address the prompt or is entirely off-topic.

    #### 2. **Accuracy of Information (25 points)**
       - **25-20 points (Excellent)**: All information presented is factually correct and supported by reliable knowledge.
       - **19-15 points (Good)**: Most information is accurate, with only minor factual errors or inaccuracies.
       - **14-10 points (Average)**: The response has a mix of accurate and slightly inaccurate information.
       - **9-5 points (Below Average)**: The response includes several inaccuracies or misleading statements.
       - **4-0 points (Poor)**: The response is largely inaccurate or contains major factual errors.

    #### 3. **Clarity and Coherence (20 points)**
       - **20-16 points (Excellent)**: The response is logically structured, easy to follow, and clearly communicates ideas.
       - **15-12 points (Good)**: The response is mostly clear and coherent, with minor instances of awkward phrasing or structure.
       - **11-8 points (Average)**: The response is somewhat coherent but may have unclear sections or disorganized ideas.
       - **7-4 points (Below Average)**: The response has significant issues with clarity, making it difficult to understand.
       - **3-0 points (Poor)**: The response is incoherent and hard to follow.

    #### 4. **Depth and Detail (15 points)**
       - **15-12 points (Excellent)**: The response provides thorough and well-elaborated information with appropriate detail.
       - **11-9 points (Good)**: The response is detailed but may lack depth in some areas.
       - **8-6 points (Average)**: The response has some detail but remains surface-level and may not sufficiently cover all aspects of the prompt.
       - **5-3 points (Below Average)**: The response lacks detail and depth, touching on topics superficially.
       - **2-0 points (Poor)**: The response is overly brief or lacks substantive information.

    #### 5. **Creativity and Originality (10 points)**
       - **10-8 points (Excellent)**: The response demonstrates a creative or unique approach, providing new insights or perspectives.
       - **7-6 points (Good)**: The response shows some creativity or original thought.
       - **5-4 points (Average)**: The response is standard with little originality but still effective.
       - **3-2 points (Below Average)**: The response lacks creativity or is formulaic.
       - **1-0 points (Poor)**: The response is entirely generic or unoriginal.

    #### 6. **Grammar and Spelling (5 points)**
       - **5 points (Excellent)**: The response is free of grammar and spelling errors.
       - **4 points (Good)**: The response has a few minor errors that do not impede understanding.
       - **3 points (Average)**: The response has noticeable errors but remains understandable.
       - **2 points (Below Average)**: The response has many errors that affect readability.
       - **1-0 points (Poor)**: The response is riddled with errors, severely impacting readability.

    ### Total Score: **100 points**
    **Interpretation of Scores:**
    - **90-100 points**: Exceptional quality, meets or exceeds expectations.
    - **75-89 points**: Strong quality, with room for minor improvements.
    - **60-74 points**: Adequate quality, needs moderate revision.
    - **40-59 points**: Below average, significant revision needed.
    - **0-39 points**: Inadequate, requires substantial improvement.

    ---Original Prompt---
    {prompt}
    ---End Original Prompt---

    ---Output A---
    {output_a}
    ---End Output A---

    ---Output B---
    {output_b}
    ---End Output B---

    ---Output C---
    {output_c}
    ---End Output C---

    ---Output D---
    {output_d}
    ---End Output D---

    [Grading Template]
    **Contender:** <output_letter>
    **Grade Reasoning:** <detailed but brief analysis>
    **Grade:** <value>
    ---
    '''

def call_api(prompt):
    """
    Call the Anthropic API with the generated prompt.
    """
    try:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4096,
            temperature=0.6,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text
    except Exception as e:
        print(f"Error calling API: {e}")
        return "Error"

def process_csv(input_file):
    """
    Process each row of the CSV, call the API, and save the output.
    """
    df = pd.read_csv(input_file)
    if 'Column 6' not in df.columns:
        df['Column 6'] = ''
    
    def process_row(row):
        if pd.notna(row['Column 6']) and row['Column 6'] != '':
            return row['Column 6']  # Skip already processed rows

        prompt = row['Column 1']
        output_a = row['Column 2']
        output_b = row['Column 3']
        output_c = row['Column 4']
        output_d = row['Column 5']
        
        prompt = generate_prompt(prompt, output_a, output_b, output_c, output_d)
        print(f"Processing row {row.name + 1}: Sending API request...")
        response = call_api(prompt)
        # Save CSV after processing each row
        df.at[row.name, 'Column 6'] = response
        df.to_csv(input_file, index=False)
        time.sleep(REQUEST_INTERVAL)  # Respect rate limits
        return response
    
    df.apply(lambda row: process_row(row) if pd.isna(row['Column 6']) or row['Column 6'] == '' else row['Column 6'], axis=1)

if __name__ == "__main__":
    process_csv(input_csv)
    print("Processing complete. Updated CSV saved.")