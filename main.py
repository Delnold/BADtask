from collections import Counter


def uniqueChar(ftext):
    words = ftext.split()
    char_dict = {}
    for word in words:
        counter = Counter(word)
        counter = sorted(counter.items(), key=lambda x: x[1])
        if (counter[0][0] in char_dict) and (counter[0][1] == 1):
            char_dict[counter[0][0]] += 1
        else:
            char_dict[counter[0][0]] = 1

    for element in char_dict:
        if char_dict[element] == 1:
            return element

    return "No unique symbol"


if __name__ == "__main__":
    with open("text.txt", mode="r", encoding="utf-8") as file:
        text = file.read()
        print("Answer: " + uniqueChar(text))
