  
import diceModule
import datetime

roll1 = int(format(diceModule.roll(20)))
roll2 = int(format(diceModule.roll(12)))
roll3 = int(format(diceModule.roll(4)))

if isinstance(roll1, int) and isinstance(roll2, int) and isinstance(roll3, int):

    if roll1 >= 5:
        print("You hit the target ")
        if roll2 > 1 and roll3 == 4:
            print(" You hit the bullseye!! ")
        elif roll1 < 5:
            print("You missed the target")

    elif roll1 < 5:
        print("You missed the target ")

else:
    print("Invalid roll values")
    exit()

    


print("Current date and time: ", datetime.datetime.now())