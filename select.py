from random import choice

with open("README.md") as f:
    lines = f.readlines()

choices = []
    
for line in lines:
    if line.startswith("* ") and line.startswith("* ~~") == False:
        choices.append(line[2:-1])

print(choice(choices))        
