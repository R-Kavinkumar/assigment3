import re
txt=input()
pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@$&]).{6,12}$"
if re.search(pattern,txt):
    print("Valid")
else:
    print("Invalid")