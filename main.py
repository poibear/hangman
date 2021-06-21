import os #To clear shell
from dotenv import load_dotenv #Import secrets from secret file
load_dotenv()
word = os.getenv("WORD")
hint = os.getenv("HINT")
lettersinstring = ''.join([str(i+" ") for i in ["a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  ]) #This is used to print out the "you have the following letters to choose from"
tries = 10 #How many tries user has

def getletters(word,whitelist,*args): #*args is a 1-value tuple containing 'lettersinstring' only set during the while loop
  try: whitelist[0] #Has the player guessed before? If the player hasn't guessed before, print out all 26 letters 
  except IndexError: 
    newword = 'Word: ' + str(''.join(['_ ' for i in word]))
    return newword #Return here, we do not want this code going below

  # If the player has guessed more than 1 time, then evaluate this code
  clue = ''.join(['_ ' if i not in whitelist else i for i in word]) # Clue is the letters the user has gotten. Written as "Word: ______"
  if clue == word: #If the letters the user has gotten correct is the entire word, then the user has won!
    raise ValueError(f"You Win! The word was {word}")
  letters_to_choose = ''.join([str(i) if i not in whitelist else ' ' for i in args[0]]) # Fancy list comprehension for giving "the following letters to choose from"
  
  return clue,whitelist,letters_to_choose #We are not printing here, we print when the code asks for it. The code has only asked for values.
  
  

whitelist=[] # What letters has the user picked (NOT just gotten correct)

print(getletters(word,whitelist),f"\nYou have the following letters to choose from:\n{lettersinstring}") # The first time, we print this generic first-time code


def hangman(word,whitelist,lettersinstring,tries): #main
  getletters(word,whitelist) # Evaluate Line 10

  while True: # "game loop"
    if tries == 0: # If the user has no tries left, well then that's too bad
      raise ValueError("No more tries left!") 
    ltr = input() # Get letter
    ltr = ltr.lower()
    if ltr.lower() == 'hint': #If the user asks for a hint, we give it to him
      print(hint)
      tries -= 1 #A hint costs a try, nothing is free
    if ltr.isalpha() is False or len(ltr) != 1: 
      print("Please select a single letter") #Make sure the user has given a single letter
      continue #Head back to the top, this will not reduce the player's tries
    if ltr in whitelist: #Has the user previously picked this letter?
      print("This letter has already been picked")
      continue
    else: whitelist.append(ltr) #If not, let's add the letter to whitelist
    if ltr not in word: 
      tries -= 1  #We deduct tries only if the player gets it wrong
    printed,whitelist,letterstochoose = getletters(word,whitelist,lettersinstring) #(see line 20) printed = clue, we update the whitelist based upon what getletters() sends back, letterstochoose is simply to print "You can pick the following letters:"
    os.system('cls') #Clear shell, makes it beautiful
    if ltr not in word: 
      print("Stuck? Type 'hint' for a hint!(It will cost you 1 try)") #If the player got it wrong, we, as any advertiser would, advertise our hint... only at a discount rate of 1 try
    print("Tries:",tries)
    print(f"\nWord:\n{printed}") #fstrings haha big brain
    print(f"You have the following letters to choose from:\n{letterstochoose}\n")
    
  return #I don't know why this is here but I guess it just is

hangman(word,whitelist,lettersinstring,tries) # Call main