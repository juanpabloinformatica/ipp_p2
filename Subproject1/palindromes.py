from load_dictionary import dictionary2list
import os

is_palindrome = lambda word: word == word[::-1]


def get_palindromes(words: list[str]) -> list[str]:
    return list(filter(is_palindrome, words))


def palindrome_file(filepath: str = os.path.abspath(os.path.join("."))):
    filename: str = "palindrome_file"
    ext: str = ".txt"
    # filepath: str = os.path.abspath(os.path.join(".", "2of4brif"))
    words = dictionary2list()
    try:
        with open(os.path.join(filepath, filename) + ext, "w") as file:
            palindromes: list[str] = get_palindromes(words)
            palindrome_text: str = "\n".join(palindromes)
            file.write(palindrome_text)
    except FileExistsError as fee:
        print(f"error:\t{fee.strerror}")


def main() -> None:
    palindrome_file()


if __name__ == "__main__":
    main()
