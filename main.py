from collections import Counter

def uniqueChar(ftext):
    words = ftext.split()
    char_dict = {}
    for word in words:
        counter = Counter(word)
        counter = sorted(counter.items(), key= lambda x:x[1])
        print(counter)
        print(counter[0])
        print(counter[0][0])
        if (counter[0][0] in char_dict) and (counter[0][1] == 1):
            char_dict[counter[0][0]] += 1
        else:
            char_dict[counter[0][0]] = 1

    print(char_dict)
    for element in char_dict:
        if char_dict[element] == 1:
            return element

    return "No unique symbol"



file = open("text.txt", "r")
text = file.read()
print("Answer: " + uniqueChar(text))