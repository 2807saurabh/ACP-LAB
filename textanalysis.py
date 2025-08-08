text = input("Enter your text: ")

words = text.split()
total_words = len(words)

word_freq = {}
for word in words:
    word = word.lower()  
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:3]

vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1

print("\n--- Text Analysis Result ---")
print("Total number of words:", total_words)
print("\nWord Frequencies:")
for word, count in word_freq.items():
    print(f"{word}: {count}")
print("\nTop 3 most frequent words:")
for word, count in top_words:
    print(f"{word}: {count}")
print("\nTotal number of vowels:", vowel_count)
