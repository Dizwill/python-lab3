filePath = input("Enter the path to the .txt file: ")

try:
    numLines = 0
    totalChars = 0
    with open(filePath, 'r', encoding='utf-8') as file:
        for line in file:
            numLines += 1
            totalChars += len(line) - 1 if line.endswith('\n') else len(line)
        avgLength = totalChars / numLines if numLines > 0 else 0
    print("Lines:", numLines)
    print("Total Characters:", totalChars)
    print("Average Length:", round(avgLength, 2))
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print('An error occurred',e)