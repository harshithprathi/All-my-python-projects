from random import choice
questions = ["Why we see a face on moon? ", "Why earth is round in shape? ", "Why sun appears small in size from Earth? "]
question = choice(questions)
answer = input(question).strip().lower()
while answer != "just because":
    answer = input("why ?: ")
print(" Oh...Ok")
