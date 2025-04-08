import math
from collections import Counter

def shannon_entropy(text):
    freq = Counter(text)
    total_chars = len(text)

    entropy = 0
    for char, count in freq.items():
        probability = count / total_chars
        entropy -= probability * math.log2(probability)

    return entropy

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Example usage
if __name__ == "__main__":
    file_path = "input.txt" 
    text = read_text_from_file(file_path)

    entropy = shannon_entropy(text)
    print(f"Shannon entropy: {entropy:.4f} bits per character")

    total_entropy = entropy * len(text)
    print(f"Total entropy: {total_entropy:.2f} bits")
