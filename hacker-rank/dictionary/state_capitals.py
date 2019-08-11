import random
state_capital = {"Maharastra":"Mumbai","Karnataka":"Banglore","Gujrat":"Ahemdabad","Telangana":"Hyderabad","Rajasthan":"Jaipur","Madhya Pradesh":"Bhopal"}
states= list(state_capital.keys())
for i in [1,2,3]:
    state = random.choice(states)
    correctAnswer = state_capital[state]
    print("What is the capital of {0} ?".format(state))
    guessAnswer = input()
    if guessAnswer == correctAnswer:
        print ("Your guess is correct")
    else:
        print ("Your guess is incorrect")


