import nltk
import time
import random

nltk.download('words')
english_words = set(nltk.corpus.words.words())
lowercaseEnglishWords = [word.lower() for word in english_words]

#counts the words that contain the prompt
def countWPP(prompt):
  count = 0
  for word in lowercaseEnglishWords:
    if prompt.lower() in word:
      count += 1

  return count


# returns words that have prompt
def wordsInPrompt(prompt):
  outputList = []
  for word in lowercaseEnglishWords:
    if prompt.lower() in word:
      outputList.append(word)

  return outputList


#checks if a word exsists
def isWord(word):
  if word.lower() in english_words:
    return True
  else:
    return False

#creates prompts
def createPrompt(minWPP):
  testPrompt = 'dayubdluabduylakbdlukabdulyab'
  while countWPP(testPrompt) < minWPP:
    testPrompt = chr(random.randint(97,122)) + chr(random.randint(97,122))

  return testPrompt


#goes through one round of the game
def playGame():
    isOver = False
    minWPP = 'start'
    while not minWPP.isdigit():
        minWPP = input('Enter your desired minimum WPP: ')

    while not isOver:
        #individual prompt
        roundPrompt = createPrompt(int(minWPP))
        startTime = time.time()
        promptIsOver = False

        while promptIsOver == False:
            print(f'Prompt: {roundPrompt}')
            userWord = input(': ').lower()
            endTime = time.time()

            if roundPrompt not in userWord:
                print("Word does not contain prompt!")
                print()

            elif not isWord(userWord) or (userWord[-1] == 's' and not isWord(userWord[0:-2])):
                print("Not a word!")
                print()

            else:
                if endTime - startTime > 15:
                   print("Time > 15 secs")
                   print()
                   promptIsOver = True
                   isOver = True
                else:
                    print("Good!")
                    print()
                    promptIsOver = True

# Game Loop
while True:
  gameModeChoice = input(
    "Play game, find words in a prompt, count words in a prompt, create a prompt (type 1, 2, 3, or 4): "
  )
  if gameModeChoice == '1':
    #play word bomb
    playGame()

  elif gameModeChoice == '2':
    #find words in a prompt
    userWordPrompt = input('Prompt: ')
    for word in wordsInPrompt(userWordPrompt):
      print(word)
    print()

  elif gameModeChoice == '3':
    #count words in prompt
    userCountWordsInPrompt = input('Prompt: ')
    print(f'There are {countWPP(userCountWordsInPrompt)} words for that prompt')
    print()
  elif gameModeChoice == '4':
    userDesiredMinWPP = 'uhujiuj'
    while not userDesiredMinWPP.isdigit():
      userDesiredMinWPP = input('Enter your desired WPP: ')

    print(f'"{createPrompt(int(userDesiredMinWPP))}" has a minimum WPP of {userDesiredMinWPP}')
    print()
  else:
    print('You did not choose 1, 2, 3, or 4.')