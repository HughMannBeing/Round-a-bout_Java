def string2Over(text):
    letters = []
    for letter in text:
        letters.append(letter)
    usedLetters = []
    roundabout = []
    place = 1
    for character in text:
        repetitionCounter = 0
        nextRepetitionCounter = 0
        commandCharacter = character
        if commandCharacter == ' ':
            commandCharacter = "Space"
        for letter in usedLetters:
            if character == letter:
                repetitionCounter += 1
        if repetitionCounter == 0:
            roundabout.append(('public void print', commandCharacter, '(){'))
        else:
            roundabout.append(('public void print', commandCharacter, str(repetitionCounter), '(){'))
        roundabout.append(('System.out.print("', character, '");'))
        usedLetters.append(character)
        if place != len(letters):
            nextCommandCharacter = letters[place]
            if nextCommandCharacter == ' ':
                nextCommandCharacter = 'Space'
            for letter in usedLetters:
                if letter == letters[place]:
                    nextRepetitionCounter += 1
            if nextRepetitionCounter == 0:
                roundabout.append(('print', nextCommandCharacter, '();'))
            else:
                roundabout.append(('print', nextCommandCharacter, str(nextRepetitionCounter), '();'))
            roundabout.append('}')
            roundabout.append('')
        else:
            roundabout.append('System.out.println();')
            roundabout.append('}')
        place += 1
    roundaboutString = str(roundabout)
    print(roundaboutString)