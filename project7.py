original=input("Enter a sentance: ").strip().lower()
words=original.split()
new_words=[]
for word in words:
    if word[0] in "aeiou":
        new_word=word+"yay"
        new_words.append(new_word)
    else:
        vowel_pos=0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos=vowel_pos + 1
            else:
                break
        const=word[:vowel_pos]
        rest=word[vowel_pos:]
        new_word=rest+const+"ay"
        new_words.append(new_word)
output = " ".join(new_words)
print(output)
