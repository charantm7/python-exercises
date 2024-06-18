def sentence_analysis(sentence):
    words = sentence.split()
    num_words = len(words)
    num_digits = sum(a.isdigit() for a in sentence)
    num_uppercase = sum(a.isupper() for a in sentence)
    num_lowercase = sum(a.islower() for a in sentence)
    return num_words, num_digits, num_uppercase, num_lowercase

sentence = input("Enter the sentence: ")
num_words, num_digits, num_uppercase, num_lowercase = sentence_analysis(sentence)

print(f"Number of words: {num_words} in a sentence")
print(f"Number of digits: {num_digits} in a sentence")
print(f"Number of uppercase: {num_uppercase} in a sentence")
print(f"Number of lowercase: {num_lowercase} in a sentence")