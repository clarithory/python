from sys import argv
script,user_name = argv
prompt = ">"

print(f"Hi{user_name},I'm the {script}script")
print("I'd like to ask you a few questions")
print(f"Do you like me{user_name}?")
like = input(prompt)
print(f"WHere do you live {user_name}?")
lives = input(prompt)