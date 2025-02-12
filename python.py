# Print top border
print("#############")

#Words
words = [
    "luxuriant", "silly", "dizzy", "frightening", "blink", "silly", "enjoy", 
    "suspend", "blink", "reward", "blink", "fact", "debt", "marble", "blink", 
    "yak", "frightening", "suspend", "debt"
]

#Count occurrences of each word using a dictionary
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

#Generate the horizontal histogram
print("Horizontal histogram:")
for word, count in word_count.items():
    print(f"{word} |{'*' * count}")

# Print bottom border
print("#############")
