'''
Input: string containing path for text to read
Process: read file, update frequency table, write frequency
table to frequency.txt, return frequency table (dictionary)
Output: dictionary containing frequency table


'''
def createFrequencyTable(textPath):
    #CREATE DICT TO STORE COUNT OF CHARS
    alpha = " ,.0123456789abcdefghijklmnopqrstuvwxyz"
    alphaDict = {}
    for char in alpha:
        alphaDict[char] = 0
    #READ FILE AND UPDATE COUNT OF CHARS
    readFile = open(textPath, "r")
    while True:
        char = readFile.read(1)
        if not char:
            break
        if char.isspace():
            alphaDict[" "] += 1
        elif char.lower() in alpha:
            alphaDict[char.lower()] += 1
    readFile.close()
    #WRITE CHAR COUNTS TO NEW FILE
    writeFile = open("huffmanBonusAssignment/frequency.txt", "w")
    total_entries = len(alphaDict)
    for index, (key, val) in enumerate(alphaDict.items()):
        writeFile.write(key + ":" + str(val))
        if index < total_entries - 1:
            writeFile.write("\n")
    writeFile.close()
    #SORT DICTIONARY AND RETURN
    sortedDict = dict(sorted(alphaDict.items(), key=lambda item: item[1]))
    return sortedDict
    '''
    Issue: I get 3572 for the count of " " (i.e., the count for spaces),
    but the answer should be 3573.
    Update: Prof said it's not a big deal; the error shouldn't affect results.
    '''


textFile = "C:\Users\sarap\OneDrive\Documents\1. Uni Courses\CP312\CP312_bonus\test1.txt"
freqTable = createFrequencyTable(textFile)
print(tuple(freqTable.items())[97][1]) #used to print certain keys/values of alphaDict