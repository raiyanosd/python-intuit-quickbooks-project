print("Welcome to raiyan's quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0


answer = input("Are you single? ")
if answer.lower() == "yes":
    print('Correct')
    score +=1
else:
    print("Var me jao MADARCHOD")



answer = input("Is raiyan good? ")
if answer.lower() == "yes":
    print('Correct')
    score +=1
else:
    print("Var me jao MADARCHOD")

answer = input("Is he single? ")
if answer.lower() == "yes":
    print('Correct')
    score +=1
else:
    print("Var me jao MADARCHOD")

answer = input("Ever gone for date? ")
if answer.lower() == "yes":
    print('Correct')
    score +=1
else:
    print("Var me jao MADARCHOD")

answer = input("Do you like raiyan? ")
if answer.lower() == "yes":
    print('Correct')
    score +=1
else:
    print("Var me jao MADARCHOD")


    
print("You got" +  str(score) + " Questions correct! ")
print("You got" +  str((score/4)*100) + "%")
