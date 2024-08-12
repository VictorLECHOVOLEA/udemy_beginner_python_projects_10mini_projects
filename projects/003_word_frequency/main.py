# 1. Import the necessary functionality
from collections import Counter
import re


# 2. Create a function for getting the word frequency in text
def get_frequency(text: str) -> list[tuple[str, int]]:
    # 3. Convert text to lowercase to ensure case-insensitivity
    lowered_text: str = text.lower()

    # 4. Use regular expression to find all words (alphanumeric and underscore)
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)

    # 5. Count word frequencies using Counter
    word_counts: Counter = Counter(words)

    # 6. Return the most common words as a tuple
    return word_counts.most_common()


# 7. Create a main entry point
def main() -> None:
    # 8. Get that user input
    text: str = input('Enter your text: ')
    word_frequencies: list[tuple[str, int]] = get_frequency(text)

    # 9. Display the results
    for word, count in word_frequencies:
        print(f'{word}: {count}')


# 10. Run the script
if __name__ == "__main__":
    main()

"""
Homework:
1. Create a function that allows the user to read a file directly (such as a txt)
so the user doesn't have to copy and paste text.

"""

"""
improvements:
A short description of the program at the beginning
Combine with ... what I proposed for summer practice project:)

Enter your text: ababccccdeefabc

Enter your text: asdwdfasfa asdw
asdwdfasfa: 1
asdw: 1


Enter your text: ana are mere, john are unelte, chris cunoaste python, java, javascript. E un senior python developer.
are: 2
python: 2
ana: 1
mere: 1
john: 1
unelte: 1
chris: 1
cunoaste: 1
java: 1
javascript: 1
e: 1
un: 1
senior: 1
developer: 1
"""