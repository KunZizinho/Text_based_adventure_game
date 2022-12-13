# Adventure game 
import time

print('Welcome to Santa Cruz Adventure Game!')
print('**************************************')
print('You are visiting Santa Cruz, California.')
print('You go on a evning hike alone in the mountains.')
print('You can pick one item to bring with you -')
print('map(m), flashlight(f), chocolate(c), rope(r) or stick(s)')
item = input('What do you choose?: ')
print('You hear a humming sound.')
choice_1 = input('Do you follow the sound? Enter Y or n: ')
while not(choice_1 == 'y' or choice_1 == 'n'):
    choice_1 = input('Invalid input. Please enter y or n: ')
if choice_1 == 'y':
    print('You keep moving closer to the sound.')
    print('The sound suddenly stops.')
    time.sleep(3)
    print('You are now LOST! ...')
    print('You try to call on your phone, but there is no signal!')
    direction = input('Which direction do you go?  Nort, South, West or East: ')
    if direction == 'Nort' or direction == 'north':
        print('You reached abandoned cabin.')
        if item == 'm':
            print('You can use the map to find your way home.')
            time.sleep(3)
            print('CONGRATULATIONS! You got out safely. You won the game.')
        else:
            print('If you had a map, you could have find tour way home.')
            time.sleep(3)
            print('------ You are still LOST! You lost the game -----')
    elif direction == 'South' or direction == 'south':
        print('You reach a river with a broken bridge.')
        if item == 's' or item == 'r':
            print('You have chosen the item that can fix the bridge.')
            print('You fixed the bridge, crossed over and find your way home.')
            time.sleep(3)
            print('CONGRATULATIONS! You got out safely. You won the game.')
        else:
            print('If you had a rope or a stick, you could have fix the bridge and find your way home.')
            time.sleep(3)
            print('------ You are still LOST! You lost the game -----')
    elif direction == 'West' or direction == 'west':
        print('You are walking in the dark and trip over a fallen log.')
        print('you have hurt your foot. You sit down and wait for help.')
        print('This could be a long time. You are still LOST!')
        time.sleep(3)
        print('------ You are still LOST! You lost the game -----')
    else:
        print('You reach the side of highway. It is dark.')
        if item == 'f':
            print('You use your flashlight to signal oncoming traffic for help.')
            print('A car stops and gives you a ride home.')
            time.sleep(3)
            print('CONGRATULATIONS! You got out safely. You won the game.')
        else:
            print('If you had a flashlight, you could have signal for help.')
            time.sleep(3)
            print('------ You are still LOST! You lost the game -----')
else:
    print('Good idea. You are not taking risks.')
    print('You start walking back to the starting point.')
    print('You realize you are LOST! ')
    print('The sound is behind you and its getting louder. You panic!')
action = input('Do you start running(r) or stop to make a call(c): ')
while action == 'c':
    print('The call does not go through.')
    action = input('Do you start running(r) or stop to make a call(c): ')
print('You are running fast. The sound gets really loud.')
print(' A woman on an electric scooter comes behind you.')

answer = input('She asks, Name my favorite computer programming language.: ')
if answer == 'Python' or answer == 'python':
    print('She says, Yes Python is my favorite computer programming language.')
    if item == 'c':
        print('If you have some chocolate, I can help you.')
        print('Luckily , you did ckoose correctly!')
        print('You give her the chocolate.')
        print('She helps you get home.')
        time.sleep(3)
        print('CONGRATULATIONS! You got out safely. You won the game.')
    else:
        print('If you had chosen that chocolate, She would have gave you a ride home.')
        print('She rides away, leaving youalone and lost.')
        time.sleep(3)
        print('------ You are still LOST! You lost the game -----')
else:
    print('She did not like your answer.')
    print('She rides away, leaving youalone and lost.')
    time.sleep(3)
    print('------ You are still LOST! You lost the game -----')
