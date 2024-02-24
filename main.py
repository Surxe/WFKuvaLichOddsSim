import random
import os
from colorama import Style
simPrints = False

def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    command = 'cls'
  os.system(command)
clearConsole()

#guessed a number that is remaining in the pool
def guessNumber(slot, slotOptions):
  guess = random.sample(slotOptions[slot-1], 1)[0] #sample generates a list, grab the only item in list
  return guess

#print updates per attempt for debug
def printUpdate(attempt, slotOptions):
  print("Attempt:", attempt)
  print("Slot1:", slotOptions[1-1])
  print("Slot2:", slotOptions[2-1])
  print("Slot3:", slotOptions[3-1])
  print()

def copyMatrix(dataToCopy, whereToPaste):
  #print("dataToCopy:  ", dataToCopy) debug
  #print("whereToPaste:", whereToPaste) debug
  for col in range(len(dataToCopy[0])):
    for row in range(len(dataToCopy)):
      #print("Row:", row, "Col:", col) debug
      whereToPaste[row][col] = dataToCopy[row][col]

def buildMatrix(rows, cols): #makes matrix with rows and cols filled with 0
  matrix = [[0 for x in range(cols)] for y in range(rows)]
  return matrix

def buildLines(percent):
  increment= "|"
  string = ""

  numIncrements = round(percent/.3) #1 increment for every .3%
  for n in range(0, numIncrements):
    string = string + increment
  return string

def freeFirstReq(): #
  a=1

def test(numSims, slotOptions):
  totalAttempts = 0
  numEachAttempt =     []
  avgEachAttempt =     []
  percentEachAttempt = []
  correctOrder = [1, 2, 3]
  numSORows = len(slotOptions) #number of rows in slot options (for resetting/saving similar sized matrices)
  numSOCols = len(slotOptions[0]) #number of cols
  copy = buildMatrix(numSORows, numSOCols)
  copyMatrix(slotOptions, copy) #saving slotOptions array

  for s in range(numSims):
    if simPrints==True: print("Sim: ", s+1, " and ", round(s/numSims*100), "% done", sep='')
    attempt = 0
    wasLastCorrect = False
    currentSlot = 1
    slotOptions = buildMatrix(numSORows, numSOCols) #reset size of slotOptions to be reset to 'copy' values
    copyMatrix(copy, slotOptions) #reset slotOptions array

    while (len(slotOptions[3-1])>1):
      if (wasLastCorrect==False):
        attempt+= 1
      guess = guessNumber(currentSlot, slotOptions) #save the guess
      if simPrints==True: print("Guess", guess)
      if (guess == correctOrder[currentSlot-1]): #correct guess
        if simPrints==True: print("Correct Guess!")
        if (currentSlot-1+1<=2): #if there is a next slot
          for i in range(currentSlot, len(correctOrder)+1): #current slot to last slot
            slotOptions[i-1].remove(guess) #remove guessed number from all slots - reset down below
            #this needs to remove only after the free attempts, move most of test function into a new one
            #then call that whenever you attempt or free attempt, return a boolean to determine if
            #it should remove correct guess from future slots
  
        #make the correct guess the only option in slot
        slotOptions[currentSlot-1].clear()
        slotOptions[currentSlot-1].append(guess)

        currentSlot+=1 #advance to next slot
        wasLastCorrect= True #gets a free attempt
      else: #incorrect guess
        if simPrints==True: print("Incorrect Guess!")
        wasLastCorrect= False
        slotOptions[currentSlot-1].remove(guess)#remove guessed number from current slot
      if simPrints==True: printUpdate(attempt, slotOptions)
    totalAttempts+=attempt #track total attempts
    #increase size of array to accomodate the new highest number of attempts taken
    while (True):
      if (attempt-1) < len(numEachAttempt):
        numEachAttempt[attempt-1]+=1 #track the number of times that a sim with x attempts occurs
        break
      else:
        numEachAttempt.append(0) #if index error, increase length then try again
        avgEachAttempt.append(0)
        percentEachAttempt.append(0)
    
  avgAttempts = totalAttempts / numSims
  for a in range(len(numEachAttempt)):
    avgEachAttempt[a] = numEachAttempt[a]/numSims
    percentEachAttempt[a] = round(avgEachAttempt[a]*100, 1)
  
  print("Avg attempts taken:", avgAttempts)
  #print("numEachAttempt", numEachAttempt)
  print("Chance for x number of attempts to complete lich: ")

  for i in range(0, len(percentEachAttempt)):
    element = str(percentEachAttempt[i])+"%"
    print("{0:<2}".format(i+1), " attempts: ", "{0:<5}".format(element), "  ", buildLines(percentEachAttempt[i]), sep='')
    


#test one
print(Style.RESET_ALL+"All 3 reqs known on every attempt:"+Style.DIM)
numSims = 1000
slotOptions = [[1, 2, 3],
               [1, 2, 3],
               [1, 2, 3]]
print("Calculated # of attempts:", (50/3*1 + 100/3*2 + 100/3*3 + 50/3*4)/100) #16.66%, 33.33%, 33.33%, 16.66% total 100%
test(numSims, slotOptions)
print("\n\n")



#test two- 
print(Style.RESET_ALL+"No reqs were known on every attempt:"+Style.DIM)
numSims = 1000
slotOptions = [[1, 2, 3, 4, 5, 6, 7, 8],
               [1, 2, 3, 4, 5, 6, 7, 8],
               [1, 2, 3, 4, 5, 6, 7, 8]] 
print("Calculated # of attempts:", "TBD")
test(numSims, slotOptions)
print("\n\n")

