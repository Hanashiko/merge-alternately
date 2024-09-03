def mergeAlternately(word1: str, word2: str) -> str:
    result_word: str = ""
    length_of_words: int = len(word1) if len(word1) > len(word2) else len(word2) 
    for i in range(length_of_words):
        if i <= len(word1) - 1: 
            result_word += word1[i]
        if i <= len(word2) - 1:
            result_word += word2[i]
    return result_word


def main() -> None:
    print(mergeAlternately("abc", "pqr"))
    print(mergeAlternately("ab", "pqrs"))
    print(mergeAlternately("dfe", "beebda"))

if __name__ == "__main__":
    main()