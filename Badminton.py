print('''
*******************************************************************************
                 I\                                
                 I#\                              
                 I##\         Q  0               
 ________________I###\_________\/ G ______       
                 \####\           /|      \      
         O  0     \####\         | |       \      
        #--/       \####I        ^ ^        \     
       |\           \###I                    \    
       | |           \##I                     \    
 _____________________\#I______________________\   
*******************************************************************************
''')
print("Welcome to Badminton.")
print("Your mission is to WIN.\n")

first_choice = input("The attacker is preparing to hit the Shuttlecock with his racket. You have to predict what direction he will strike. Choose: Left or Right \n")

if first_choice == "Right":
  print("You failed.")
elif first_choice == "Left":
  print ("\nYou successfully hit the Shuttlecock.\n")
  second_choice = input("Which direction will you strike? Choose: Left or Right\n")
  if second_choice == "Right":
    print("The opponent predicted your decision. You failed.")
  elif second_choice == "Left":
    print("\nThe opponent failed to predict you. You have gained a point!\n")
    third_choice = input("\nThe opponent hopes to gain that point back with this last strike. What side will you protect? Choose: Left, Right or Middle\n")
    if third_choice == "Right":
      print("\nYou were unable to predict your opponent. You failed.")
    elif third_choice == "Left":
      print("\nYou were unable to predict your opponent. You failed.")
    elif third_choice == "Middle":
      print("\nYou successfully predicted your opponent. You win!")


