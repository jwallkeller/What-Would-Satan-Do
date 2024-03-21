import random

responses = []
responses.append("Not today, human!")
responses.append("I don't see that in the ashes.")
responses.append("When hell freezes over!")
responses.append("Hell yeah!")
responses.append("If you will it, so it shall be.")

print("Welcome to 'What Would Satan Do?', your Satanic Magic 8-ball!")
print("When you're finished, just type 'quit' and hit enter!")

name = input("\n  What is your name?")

question = ""

while question != "quit":
  question = input("\n  What can I answer for you today?")

  if question != "quit":
    answer = random.randint(0, len(responses)-1)
    print(responses[answer])

print("\nHail Satan and Hail " + name + "!")