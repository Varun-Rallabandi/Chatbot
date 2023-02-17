import random

responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.",
             "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.",
             "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don't count on it.", "Outlook not so good.", "My sources say no.", "Very doubtful."]

print("Welcome to Magic 8 Ball! Ask me anything, or press Q to quit.")

while True:
    question = input("> ")
    if question.lower() == 'q':
        print("Goodbye!")
        break
    else:
        print(random.choice(responses))