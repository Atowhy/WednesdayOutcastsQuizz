import re
import csv
import os

def extract_strings(line, pattern):
    match = re.search(pattern, line)
    if match:
        return match.groups()
    return None

def main():
    input_file = "index.html"
    output_file = "questions.csv"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    rows = []
    current_question = None

    # Regex patterns
    question_pattern = r'question:\s*"(.*?)"'
    answer_pattern = r'text:\s*"(.*?)".*?species:\s*"(.*?)"'

    print("Parsing index.html...")
    
    for line in lines:
        # Check for question
        q_match = extract_strings(line, question_pattern)
        if q_match:
            current_question = q_match[0]
            # print(f"Found question: {current_question}")
            continue

        # Check for answer
        a_match = extract_strings(line, answer_pattern)
        if a_match and current_question:
            answer_text = a_match[0]
            species = a_match[1]
            rows.append([current_question, answer_text, species])
            # print(f"  Found answer: {species}")

    # Write to CSV
    print(f"Writing {len(rows)} rows to {output_file}...")
    try:
        with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Question', 'Answer', 'Species'])  # Header
            writer.writerows(rows)
        print("Success!")
    except Exception as e:
        print(f"Error writing CSV: {e}")

if __name__ == "__main__":
    main()
