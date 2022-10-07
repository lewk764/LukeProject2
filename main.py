#Story Intro

#Set the stage for the adventure
print("~ Triboar Trail Adventures ~")
print("------------------------------")
print()
print("You are a new adventurer who has set out on their first adventure from the nearby city of Neverwinter. You make your way down the 'High Road' of the Sword Coast until you come to a fork in the road. A sign pointing down the trail that splits off to the east reads 'Triboar Trail - Phandalin 5 miles'. You decide to follow the Triboar Trail to the town of Phandalin where you have heard there is a lack of willing adventurers, but a surplus of quests.")
print()
print("After a few hours you arrive in the mining town of Phandalin. You take some time to rest and grab a much needed meal at the Stonehill Inn. Afterwards, you go to the town hall where you find a quest board with three quests that catch your eye.")
print()

#Provide the user with 3 quest options, and save their choice as a variable
print("Which quest will you choose:")
print("  A. Dwarven Excavation")
print("  B. Monster of Gnomengarde")
print("  C. Umbrage Hill Rescue")
questSelection = input(
  "Which quest will you take? Please enter either A B or C: ")
print("------------------------------")
print()

#Quest Option 1: Dwarven Excavation
if(questSelection == "A"):
  
  #Quest 1 introduction
  print("You pick up the flyer titled 'Dwarven Excavcation' which explains that a pair of Dwarves need help exploring a nearby ruin. You set off to this quest and arrive at the ruin in a few hours.")
  print()
  print("The pair of Dwarves you meet explain that they need someone to clear out the Ochre Jellies that are preventing them from exploring the ruin. They warn you that Ochre Jellies are immune to 'Paper Cuts' and 'Sky Sparks'. Your Dwarvish is a little rusty, so you aren't entirely sure what they mean by that. However, you agree to help the dwarves and grab a torch and enter the ruins.")
  print()
  
  #Quest 1 puzzle description and options
  print("Upon entering the ruins, you notice a group of yellowish blobs that start to slowly move towards you. How would you like to attack them?")
  print("  1. I want to slash them with my sword!")
  print("  2. I will cast a lightning spell at them!")
  print("  3. I will cast a frost spell at them!")
  ojAttack = input("Which attack option do you choose? Please enter either 1 2 or 3: ")
  ojAttack = int(ojAttack)
  print("------------------------------")
  print()
  
  #Quest 1 puzzle choice outcomes
  if(ojAttack == 1):
    print("You take a wide swing at one jelly with your longsword. At first you seem to be successful and are able to cut the monster in two. However, the two now smaller blobs continue to get closer. Before you can think, they attach onto you and begin to slowly absorb you into their bodies.")
    print()
    print("You have been defeated by the Ochre Jellies.")
  
  elif(ojAttack == 2):
    print("You let lightning flow from your fingertips directly at one of the jellies. The jelly stops moving and is steaming. However, the jelly then very quickly splits in two. The two smaller jellies are able to quickly flank you and they corner you before they begin to disolve you.")
    print()
    print("You have been defeated by the Ochre Jellies.")
  
  elif(ojAttack == 3):
    print("You release a beam of frost from your staff. The jellies begin to solidify before they shatter into hundreds of tiny yellow ice cubes.")
    print()
    print("The Ochre Jellies have been defeated, and the dwarves reward you with 50 gold!")

  else:
    print("You took too long to make a move, and the Jellies quickly overwhelmed you. You have been defeated.")

#Quest Option 2: Monster of Gnomengarde
elif(questSelection == "B"):
  print("You pick up the flyer titled 'Monster of Gnomengarde' which explains that a monster that takes the form of inanimate objects has been feeding on the Rock Gnomes of Gnomengarde, and they need someone to discover and slay this monster. You set off on this quest and arrive at Gnomengarde in a few hours.")
  print()
  
  #Quest 2 puzzle description and options
  print("As you arrive, the Gnomes of Gnomengarde explain their situation and tell you the last place they encountered this creature was in their library. They lead you to this room and you see a variety of objects that this creature could shapeshift into. How would you like to draw the creature out from hiding?")
  print("  A. Use one of the gnomes as bait.")
  print("  B. Light the Library on fire.")
  print("  C. Swing your sword at everything until it eventually attacks.")
  print("  D. Throw tiny pebbles at everything.")
  mimicChoice = input("Which tactic will you choose? Please enter either A B C or D: ")
  print("------------------------------")
  print()

  #Quest 2 puzzle choice outcomes
  if(mimicChoice == "A"):
    print("You turn around and grab one of the gnomes who lead you to the library, and throw it into the middle of the room. The monster quickly reveals itself and eats the gnome in one bite. You are able to slay the beast, but are quickly chased out of Gnomengarde by a mob of angry Gnomes.")
    print()
    print("Was this choice really worth it? After this, your adventuring career is probably over.")

  elif(mimicChoice == "B"):
    print("You cast the 'Firebolt' spell into the middle of the Library. The many shelves full of books instantly ignites and you hear the scream of the the creature burning alive. You turn around and see the look of absolute terror on the Gnomes faces.")
    print()
    print("You may have slain the monster, but you are also now an arsonist. After this, your adventuring career is probably over.")

  elif(mimicChoice == "C"):
    print("You go around the room swinging you sword into various objects. As you go to swing your now very dull sword into a chair, the chest behind you opens up to reveal many sets of sharp teeth.")
    print()
    print("Before you can react, the shapechanging monster latches onto you and eats you. You have been defeated.")

  elif(mimicChoice == "D"):
    print("You begin to throw tiny pebbles at everything you can see in the room. While the gnomes seem to think you have gone crazy, you notice that as you throw a pebble at a chest in the back of the room, the pebble seems to stick to the side of this chest.")
    print()
    print("Your time spent studying the monsters of this word did not go to waste. You knew that Mimics, a type of shapechanging monster, has a natural adhesive on the outside of it's body. You were able to identify the monster, and easily killed it.")
    print()
    print("The Gnomes thank you for slaying the beast and reward you with 50 gold!")

  else:
    print("You took too long to make a choice, and the beast quickly revealed itself and rushed you. Taken by suprise, the beast was able to consume you. You have been defeated.")

#Quest Option 3: Umbrage Hill Rescue
elif(questSelection == "C"):
  print("You pick up the flyer titled 'Umbrage Hill Rescue' which explains that the town healer has been trapped inside the windmill on Umbrage Hill by a pair of Manticores. You set off on this quest and arrive at Umbrage Hill in a few hours.")
  print()

  #Quest 2 puzzle description and options
  print("As you arrive you see the pair of Manticores which have nested outside the windmill. As you prepare to have what you believe would be a legendary battle with these beasts, one of them flies over you and says:")
  print()
  print("I know you have come for the healer. And I will grant you her freedome, if you can solve my riddle. Otherwise, I will eat you for dinner!")
  print()
  print("Here is my riddle:")
  print("  Double my number, I'm less than a score,")
  print("  Half my number is less than four.")
  print("  Add one to my double when bakers are near,")
  print("  Days of the week are still greater, I fear.")
  numRiddle = input("What is my number? (Please enter a whole number): ")
  numRiddle = int(numRiddle)
  print("------------------------------")
  print()

  #Quest 3 puzzle choice outcomes
  if(numRiddle == 6):
    print("You have solved my riddle. You are free to take the healer and leave!")
    print()
    print("You rescue the healer and return to the town, where she rewards you with 50 gold!")

  else:
      print(f"You tell the Manticore that his number is {numRiddle}.")
      print()
      print("The Manticore looks at you and says 'It seems we will be having an adventurer for   dinner!'")
      print("The Manticore swoops down and grabs you in it's claws. You will soon be eaten by the monster. You have been defeated.")

#Invalid Quest Option
else:
  print("You decided not to choose any of the three quests. Your adventure has come to an end.")