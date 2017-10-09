import random
def string2Over(text):
    letters = []
    for letter in text:
        letters.append(letter)
    usedLetters = []
    methods = []
    place = 1
    for character in text:
        method = ''
        repetitionCounter = 0
        nextRepetitionCounter = 0
        commandCharacter = character
        if commandCharacter == ' ':
            commandCharacter = "Space"
        for letter in usedLetters:
            if character == letter:
                repetitionCounter += 1
        if repetitionCounter == 0:
            method += 'public void print'
            method += commandCharacter
            method += '(){\n'
        else:
            method += 'public void print'
            method += commandCharacter
            method += str(repetitionCounter)
            method += '(){\n'
        method += 'System.out.print("'
        method += character
        method += '");\n'
        usedLetters.append(character)
        if place != len(letters):
            nextCommandCharacter = letters[place]
            if nextCommandCharacter == ' ':
                nextCommandCharacter = 'Space'
            for letter in usedLetters:
                if letter == letters[place]:
                    nextRepetitionCounter += 1
            if nextRepetitionCounter == 0:
                method += 'print'
                method += nextCommandCharacter
                method += '();\n'
            else:
                method += 'print'
                method += nextCommandCharacter
                method += str(nextRepetitionCounter)
                method += '();\n'
            method += '}\n'
            method += '\n'
        else:
            method += 'System.out.println();\n'
            method += '}\n'
        place += 1
        methods.append(method)
    print('public void printPhrase(){')
    print('print', text[0], '();', sep = '')
    print('}')
    print()
    remainingCharacters = len(methods)
    for method in range(remainingCharacters):
        nextMethod = random.randint(0, (len(methods)-1))
        print(methods[nextMethod])
        methods.remove(methods[nextMethod])
        