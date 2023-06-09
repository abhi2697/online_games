import random
lst=["stone","paper","scissor"]
n=1
c_score=0
ur_score=0
print("we are going to play stone paper scissors")
while(n!=11):

    ur_response=input("enter your resposnse \n")
    c_response=random.choice(lst)
    if c_response== "stone" and ur_response == "paper":
        print(F"computer responded {c_response} you responded {ur_response}")
        print(f"you won this round{n}")
        ur_score+=1
        n+= 1
        print(f"your score{ur_score} computer score{c_score}")
    elif c_response == "stone" and ur_response == "scissor":
        print(F"computer responded {c_response} you responded {ur_response}")
        print(f"you loose this round {n}")
        c_score+= 1
        n += 1
        print(f"your score{ur_score} computer score{c_score}")
    elif c_response == "stone" and ur_response == "stone":
        print(F"computer responded {c_response} you responded {ur_response}")
        print(f" round {n} is draw")
        n += 1
        print(f"your score{ur_score} computer score{c_score}")
    elif c_response == "paper" and ur_response == "paper":
        print(F"computer responded {c_response} you responded {ur_response}")
        print(f" round {n} is draw")
        n += 1
        print(f"your score{ur_score} computer score{c_score}")
    elif c_response == "paper" and ur_response == "scissor":
        print(F"computer responded {c_response} you responded {ur_response}")
        print(f"you won this round{n}")
        ur_score += 1
        n += 1
        print(f"your score{ur_score} computer score{c_score}")
    elif c_response == "paper" and ur_response == "stone":
        print(F"computer responded {c_response} you responded {ur_response}")

        print(f"you loose this round {n}")
        c_score += 1
        n += 1
        print(f"your score{ur_score} computer score{c_score}")
    elif c_response == "scissor" and ur_response == "paper":
        print(F"computer responded {c_response} you responded {ur_response}")
        print(f"you loose this round { n}")
        c_score += 1
        n += 1
        print(f"your score{ur_score} computer score{c_score}")
    elif c_response == "scissor" and ur_response == "scissor":
        print(F"computer responded {c_response} you responded {ur_response}")
        print(f" round {n} is draw")
        n += 1
        print(f"your score{ur_score} computer score{c_score}")
    elif c_response == "scissor" and ur_response == "stone":
        print(F"computer responded {c_response} you responded {ur_response}")
        print(f"you won this round{n}")
        ur_score += 1
        n += 1
        print(f"your score{ur_score} computer score{c_score}")
    else:
        print("this is not a valid  resposnse,please try again")
        print(f"your response{ur_response},c resposnes{c_response}")
        n -=1

print(f"game over you won {ur_score}, you lost {c_score},draw {10-ur_score-c_score}")