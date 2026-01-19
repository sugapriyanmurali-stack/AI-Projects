print("Welcome to AI Quiz.")
mode=input("Choose your difficulty(E/M/D):").upper()
score=500
if mode=="E":
    print("What is the largest peak in the world ?")
    ans=input("Answer:")
    if ans=="Mt.Everest":
        print("Correct Answer. \n +100")
        score+=100
    else:
        print("Wrong answer.\n -100")
        score-=100
elif mode=="M"
        