
import csv

vNum = "1.0"
print("Collatz Conjecture Sequential Test Case Emulator " + vNum)

with open('collatzseq.csv', 'w', newline='') as file:
    fieldnames = ['Test_Number', 'Starting_Num', 'End_Num', 'Steps', 'Sequence']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

strtests = input("How many test cases should be run?")
tests = int(strtests)
strrangelow = input("Where should the range start?")
rangelow = int(strrangelow)
global curTest


def writetoCSV(testno, startingNo, solveNo, steps, seq):
    with open('collatzseq.csv', 'a', newline='') as file:
        fieldnames = ['Test_Number', 'Starting_Num', 'End_Num', 'Steps', 'Sequence']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Test_Number': testno, 'Starting_Num': startingNo, 'End_Num': solveNo,
                         'Steps': steps, 'Sequence': seq})


def runTest(noTests, low):
    global curTest
    curTest = 1
    startingNo = low

    for x in range(0, noTests):
        solveTestCase(curTest, startingNo)
        startingNo = startingNo + 1
        curTest = curTest + 1


def solveTestCase(testno, solveNo):
    solved = False
    startingNo = solveNo
    steps = 0
    seq = str(solveNo) + "(Starting);"

    while not solved:
        steps = steps + 1
        if (solveNo % 2) == 0:
            solveNo = solveNo / 2
            curseq = str(solveNo) + "(Even);"
            seq = seq + curseq
            if solveNo == 1:
                solved = True
        else:
            solveNo = (solveNo * 3) + 1
            curseq = str(solveNo) + "(Odd);"
            seq = seq + curseq
            if solveNo == 1:
                solved = True
    writetoCSV(testno, startingNo, solveNo, steps, seq)


runTest(tests, rangelow)
