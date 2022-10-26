import art
print(art.unlock)
print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')
choice1 = input('Which side you want to go left or right??\n')
if choice1 == 'left':
  choice2 = input('''A lake a head
Enter "wait" to wait for a boat or enter "swim" to swim through a lake:\n''')
  if choice2 == 'wait':
    print(art.boat)
    choice3 = input('''Here you found a three doors of "red","green","yellow"
    enter which color door you want to open:\n''')
    if choice3 == 'red':
      print('''Burned by fire.💥💥
!!!!!Game Over!!!!!''')
    elif choice3 == 'green':
      print('''Eaten by beasts.
!!!!!Game Over!!!!!''')
    elif choice3 == 'yellow':
      print('You Win!')
    else:
      print('You messed up')
  elif choice2 == 'swim':
    print(art.trout)
  else:
    print('!!!!!Game Over!!!!!')
else:
  print('''you messed up!
!!!!!Game Over!!!!!''')

