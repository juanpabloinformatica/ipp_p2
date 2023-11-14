import os
import sys


from load_dictionary import dictionary2list

"""
Getting the palingrams in the dictionary
"""


# def get_palingrams(words: list|dict) -> list:
def get_palingrams(words: dict) -> list:
    """
    get palingrams of list of words
    """
    palingrams_list: list = []
    for word in words:
        reverse_word = word[::-1]
        word_length = len(word)
        if len(word) > 1:
            for index, _ in enumerate(word):
                if (
                    reverse_word[: word_length - index] == word[index:]
                    and reverse_word[word_length - index :] in words
                ):
                    palingrams_list.append(f"{word}:{reverse_word[word_length-index:]}")
                if (
                    reverse_word[word_length - index :] == word[:index]
                    and reverse_word[: word_length - index] in words
                ):
                    palingrams_list.append(f"{word}:{reverse_word[:word_length-index]}")

    return palingrams_list


def find_palingrams(words: list):
    """Find dictionary palingrams."""
    pali_list = []
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[: end - i] and rev_word[end - i :] in words:
                    pali_list.append(f"{word}, {rev_word[end - i :]}")
                if word[:i] == rev_word[end - i :] and rev_word[: end - i] in words:
                    pali_list.append(f"{rev_word[: end - i]}:{word} ")
    return pali_list


def palingram_file(filepath: str = os.path.abspath(os.path.join("."))):
    """
    Generate a file with the palingrams
    """
    filename: str = "palingram_file_2"
    ext: str = ".txt"
    # filepath: str = os.path.abspath(os.path.join(".", "2of4brif"))
    words = dictionary2list()

    try:
        with open(os.path.join(filepath, filename) + ext, "w") as file:
            palingrams = get_palingrams(set(words))
            palingrams_text: str = "\n".join(palingrams)
            file.write(palingrams_text)
    except FileExistsError as fee:
        print(f"error:\t{fee.strerror}")


def main() -> None:
    """
    Entry point

    """
    palingram_file()
    pass


if __name__ == "__main__":
    main()
    # test()
