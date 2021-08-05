vNum = "1.0"
print("Collatz Conjecture One Test Case Emulator " + vNum)

testnum = int(input("What number should be tested?"))

def solveTestCase(inputno):
    solved = False
    while not solved:
        if (inputno % 2) == 0:
            inputno = inputno / 2
            print(int(inputno))
            if inputno == 1:
                solved = True
        else:
            inputno = (inputno * 3) + 1
            print(int(inputno))
            if inputno == 1:
                solved = True

print(testnum)
solveTestCase(testnum)