from functions import *

run = True
print("Initialising")

while run:
    raw = input("planner>")
    command = raw.split(" ")
    if command[0].lower == "exit":
        run = False
