print("""
                           o                    
                       _---|         _ _ _ _ _ 
                    o   ---|     o   ]-I-I-I-[ 
   _ _ _ _ _ _  _---|      | _---|    \ ` ' / 
   ]-I-I-I-I-[   ---|      |  ---|    |.   | 
    \ `   '_/       |     / \    |    | /^\| 
     [*]  __|       ^    / ^ \   ^    | |*|| 
     |__   ,|      / \  /    `\ / \   | ===| 
  ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
  I_I__I_I__I_I  (====(_________)___|_|____|____
  \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_| 
   |[]      '|   | []  |`__  . [  \-\--|-|--/-/  
   |.   | |' |___|_____I___|___I___|---------| 
  / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] | 
 <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  
 ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===> 
 ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [ 
 <===>     ' ||||| |   |   | ||||.||  []   <===>
  \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/ 
   |      . _||||| |   |   | ||||.|| |     | |
../|' v . | .|||||/____|____\|||| /|. . | . ./
.|//\............/...........\........../../\\\
""")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

question_1 = input("You're at a cross road. Where you want to go?\n Type 'left' or 'right'\n")

if question_1 == 'right':
    question_2 = input("You come to a lake. Do you wait for boat or try to swim across?\n Type 'wait' or 'swim'\n")
    if question_2 == 'swim':
        print("You made a go for it and evaded the wolves lurking in the woods!")
        question_3 = input("You now come to 3 doors. One is red, the other is blue and the last one is yellow. Which one do you choose to enter\n Type 'red', 'blue' or 'yellow'\n")
        if question_3 == 'blue':
            print("You opened the blue door and you are greeted with Medusa the Gorgon, her green eyes flash and you turn to stone!\nGame Over!")
            print("""
  ____                         ___                 _ 
 / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)

""")
        elif question_3 == 'yellow':
            print("You opened the yellow door. You enter into pitch black nothingness. The door closes behind you!\nGame Over!")
            print("""
  ____                         ___                 _ 
 / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)

""")
        else:
            print("You opened the red door, a horde of treasure spills before your eyes!\nYou Win!")
            print("""

__   __                     _       _ 
\ \ / /__  _   _  __      _(_)_ __ | |
 \ V / _ \| | | | \ \ /\ / / | '_ \| |
  | | (_) | |_| |  \ V  V /| | | | |_|
  |_|\___/ \__,_|   \_/\_/ |_|_| |_(_)

                """)
    else:
        print("Whilst awaiting the boat a pack of wolves amushed you!\nGame Over!")
        print("""
  ____                         ___                 _ 
 / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)

""")        
else:
    print("You choose the wrong path!\nGame Over!")
    print("""
  ____                         ___                 _ 
 / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)

""")
