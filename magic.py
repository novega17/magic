# testing
from random import choice
from time import sleep
choices=[
"Definitely",
"Yes",
"Probably",
"Maybe",
"Probably Not",
"No",
"Definitely Not",
"I don't know",
"Ask Later",
"I'm too tired"
]
while True:
    input("Ask the mighty 8-Ball a question\n> ")
    for i in range(0,3):
        print("Shaking...")
       # time.sleep(1)
    print(choice(choices))
