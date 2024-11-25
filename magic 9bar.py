############ This Is a Project For CodeCademy ###########
import random


#print(random_number)
while True:
  question1=(input("Question for magic 9bar:"))
  if question1.lower() == "quit":
    print("are u not gonna say safe to man nah?")
    break

  random_number = random.randint(1,9)
  if random_number == 1:
    print("yes, definitely")
  elif random_number == 2:
    print("could be still idrk")
  elif random_number == 3:
    print("no doubt g")
  elif random_number == 4:
    print("im too high right now ask man later...")
  elif random_number == 5:
    print("ask chat gpt, why u bothering me?")
  elif random_number == 6:
    print("nah if i tell you, u wont like it")
  elif random_number == 7:
    print("streets been saying, not really g")
  elif random_number == 8:
    print("its not looking good bruv")
  else:
    print("lowe it leave man alone")
