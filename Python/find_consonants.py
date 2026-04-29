def find_consonants(word):
    vowels="AEIOUaeiou"
    vowel=0
    consonants=0
    for char in word:
        if char.isalpha():
            if char in vowels:
                vowel +=1
            if char not in vowels:
                consonants +=1
    return f"vowels:{vowel} consonant:{consonants}"


print(find_consonants("shammas12"))