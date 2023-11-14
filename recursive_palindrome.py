#  01234
# "SABAS"
# si  0 == 4
# si  1 == 3
# si  2 == 2
#
# hasta len(word)//2
def is_palindrome(word: str, word_length: int) -> bool:
    print(word[(-1) * word_length + 1])
    if word_length == len(word) // 2:
        return True
    if word[(-1) * word_length] == word[word_length - 1]:
        return is_palindrome(word, (word_length - 1))
    else:
        return False


if __name__ == "__main__":
    print(is_palindrome("dimeemid", len("dimeemid")))
