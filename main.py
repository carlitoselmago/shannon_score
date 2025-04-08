import math
from collections import Counter
import sys

# Spanish letter frequencies in percentages
spanish_char_frequencies = {
    'A': 11.72,
    'Á': 0.44,
    'B': 1.49,
    'C': 3.87,
    'D': 4.67,
    'E': 13.72,
    'É': 0.36,
    'F': 0.69,
    'G': 1.00,
    'H': 1.18,
    'I': 5.28,
    'Í': 0.70,
    'J': 0.52,
    'K': 0.11,
    'L': 5.24,
    'M': 3.08,
    'N': 6.83,
    'Ñ': 0.17,
    'O': 8.44,
    'Ó': 0.76,
    'P': 2.89,
    'Q': 1.11,
    'R': 6.41,
    'S': 7.20,
    'T': 4.60,
    'U': 4.55,
    'Ü': 0.02,
    'Ú': 0.12,
    'V': 1.05,
    'W': 0.04,
    'X': 0.14,
    'Y': 1.09,
    'Z': 0.47
}

valid_chars = set(spanish_char_frequencies.keys())

def shannon_entropy(text):
    # Only count characters in our distribution
    filtered_text = [char for char in text if char in valid_chars]
    total_chars = len(filtered_text)
    freq = Counter(filtered_text)

    entropy = 0
    for char, count in freq.items():
        probability = count / total_chars
        entropy -= probability * math.log2(probability)

    return entropy, total_chars

def theoretical_entropy_from_distribution(freq_dict):
    entropy = 0
    for freq in freq_dict.values():
        p = freq / 100  # Convert percentage to probability
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Main script
if __name__ == "__main__":
    file_path = "input.txt" 
    try:
        text = read_text_from_file(file_path)
    except:
        print(f'First create a file for input with the name "{file_path}"')
        sys.exit()

    # Normalize: uppercase, remove newlines
    cleaned_text = text.upper().replace('\n', '')

    entropy, valid_count = shannon_entropy(cleaned_text)
    if valid_count == 0:
        print("No valid characters found in the text.")
        sys.exit()

    print(f"\nShannon entropy from text: {entropy:.4f} bits per character")
    print(f"Total entropy : {entropy * valid_count:.2f} bits")
    print(f"Number of valid characters: {valid_count}")

   
