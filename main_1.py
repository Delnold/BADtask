from collections import deque


def uniqueChar(text: str) -> str:
    words = text.split()
    arr_chars = deque()
    for word in words:
        for char in word:
            if word.count(char) == 1:
                arr_chars.append(char)
                break
    for char in arr_chars:
        if arr_chars.count(char) == 1:
            return char
    return ""


if __name__ == "__main__":
    with open("text.txt", mode="r", encoding="utf-8") as file:
        text = file.read()
        print("Answer: " + uniqueChar(text))

