from random import choice
from sys import argv

if len(argv) is not 2 or argv[1] not in ['movie', 'tv']:
    print("Usage: python " + __file__ + " (movie | tv)")
    exit(1)

with open("README.md") as f:
    lines = f.readlines()

mIndex = -1
tIndex = -1
for i, line in enumerate(lines):
    if line.startswith("# Movie"):
        mIndex = i + 3
    if line.startswith("# TV"):
        tIndex = i + 3

choices = []
if argv[1] == 'movie':
    for movie in lines[mIndex:tIndex - 4]:
        if movie.startswith("* ~~") is False:
            choices.append(movie[2:-1])
if argv[1] == 'tv':
    for show in lines[tIndex:]:
        if show.startswith("* ~~") is False:
            choices.append(show[2:-1])

print(choice(choices))        
