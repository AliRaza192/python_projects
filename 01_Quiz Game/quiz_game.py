print("Welcome to My Quiz Game!")

playing = input("Do you want to play? : ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")

score = 0

answer = input("What does CPU stand for? : ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorret!")

answer = input("What does GPU stand for? : ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorret!")

answer = input("What does RAM stand for? : ")
if answer.lower() == "random-access memory":
    print("Correct!")
    score += 1

else:
    print("Incorret!")

answer = input("What does API stand for? : ")
if answer.lower() == "application programming interface":
    print("Correct!")
    score += 1

else:
    print("Incorret!")

answer = input("What does GPT stand for ai? : ")
if answer.lower() == "generative pre-trained transformer":
    print("Correct!")
    score += 1

else:
    print("Incorret!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")