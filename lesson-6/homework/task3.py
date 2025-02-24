import string
from collections import Counter

def get_or_create_file():
    filename = "sample.txt"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                raise FileNotFoundError
            return content
    except FileNotFoundError:
        text = input("File is missing or empty. Please enter text: ")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        return text

def clean_text(text):
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

def main():
    text = clean_text(get_or_create_file())
    word_counts = Counter(text.split())
    
    total_words = sum(word_counts.values())
    common_words = word_counts.most_common(5)
    
    print(f"Total words: {total_words}")
    print("Top words:")
    for word, count in common_words:
        print(f"{word} - {count} times")
    
    with open("word_count_report.txt", 'w', encoding='utf-8') as file:
        file.write(f"Total Words: {total_words}\nTop Words:\n")
        for word, count in common_words:
            file.write(f"{word} - {count}\n")
    print("Report saved to 'word_count_report.txt'")

if __name__ == "__main__":
    main()
