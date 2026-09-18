word = input("Enter a word: ")

print("Letters:")
for letter in word:
    print(letter)

print("Numbered letters:")
count = 1
for letter in word:
    print(f"{count}. {letter}")
    count += 1

print(f"The word has {len(word)} letters.")
