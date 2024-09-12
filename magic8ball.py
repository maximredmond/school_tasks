import random
import time

answer1 = "Yes"
answer2 = "No"
answer3 = "Maybe"
answer4 = "Likely"
answer5 = "Unlikely"
answer6 = "Certainly"
answer7 = "I dont know"
answer8 = "Ask again later"

input("Ask me a question: ")
print("shaking...")
time.sleep(1)

choice = random.randint(1,8)

if choice == 1:
    print(answer1)
elif choice == 2:
    print(answer2)
elif choice == 2:
    print(answer3)
elif choice == 2:
    print(answer4)
elif choice == 2:
    print(answer5)
elif choice == 2:
    print(answer6)
elif choice == 2:
    print(answer7)
else:
    print(answer8)