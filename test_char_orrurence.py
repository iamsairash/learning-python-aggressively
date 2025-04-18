sentence = "This is a sentence"

char_count = {}

for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

sorted_char_count = sorted(char_count.items(), key=lambda kv: kv[1], reverse=True)

print("The highest number of occurence is: ", sorted_char_count[0][0])
