name = input("What is your name ? : ").strip()
age = input("How old are you? : ").strip()
city = input("Where do you live ? : ").strip()
like = input("What u do to enjoy ? : ").strip()
about = "Your name is {}, you are {} years old. You live in {}, and you love {}."
output = about.format(name,age,city,like)
print(output)
