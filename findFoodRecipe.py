import os
import anthropic

def generatePrompt(foodList, foodQuantity):
    myMessage = "I have water, "
    for i in range(len(foodQuantity)):
        # print (foodList[i] + " " + foodQuantity[i], end =" ")
        myMessage+= foodQuantity[i] + " " + foodList[i]
        if i+1 == len(foodQuantity):
             myMessage+=" create a recipe using only the ingredients given, you do not use all of them but stick to the list given."
        else:
             myMessage+=", "
    return myMessage


print("Welcome to my program")

foodList = []
foodQuantity = []

userInput = ""
while userInput.casefold() != "n":
    userInput = input("Is there any ingredient you want to add to the list? Y/N\n")

    if userInput.casefold() == "n":
        break
    else :
            userInput = input("What is the ingredient?\n")
            foodList.append(userInput)
            userInput = input("How many " + foodList[-1] + " do you have?\n")
            foodQuantity.append(userInput)

# foodList = ["boneless chicken" , "eggs" , "cornstarch box", "flour bag", 
#             "orange juice bottle", "sugar box", "White vinegar", "soy sauce",
#             "ginger"]

# foodQuantity = ["4", "3", "1","1","1","1","2","2","2"]

print("Looking for recipes...\n")

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="YOUR KEY",
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    messages=[
        {"role": "user", "content": generatePrompt(foodList, foodQuantity)}
    ]
)

print(message.content)

while userInput != "0":
    userInput = input("Type 0 (zero) to exit the program:")
    if userInput == "0":
         exit()