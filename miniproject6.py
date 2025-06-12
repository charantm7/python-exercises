def num_of_vowels_and_consonants(string):
    vowels = 'aeiouAEIOU'
    num_vowels = 0
    num_consonants = 0

    for char in string :
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return num_vowels, num_consonants

string = input("Enter your string: ")
num_vowels, num_consonants = num_of_vowels_and_consonants(string)

print(f"Number of vowels in a string is: {num_vowels}")
print(f"Number of consonants in a string is: {num_consonants}")