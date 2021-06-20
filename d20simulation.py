import random
import time


answer = ""

while True:

    def rolldie():
        if answer == 'y':
            # Generates a random dice value between 1 to 20.
            dieval = random.randrange(1, 20)
            print('Rolling..........')
            time.sleep(1.5)
            print('You rolled a natural', dieval)
            
            if dieval >= 10:
                time.sleep(0.8)
                print('Success')
            else:
                time.sleep(0.8)
                print("Failure!")

        elif answer == 'n':
            print("Then why are you here?")
            time.sleep(3)
            exit()
        else:
            print('****Invalid Answer!****')

    time.sleep(2)
    print(""" 
    < Would you like to roll a D20? > y/n""")
    answer = input()
    rolldie()