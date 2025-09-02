#Computer Science Project - Artefact

#Please follow the step-by-step commented explanation of this programme by reading
#the comment before or 'above' of the line or block of code it refers to.
#For the unit testing and specific test cases please see the attached
#"ComputerScienceProject_UnitTesting" file.

import matplotlib.pyplot as plt #Install "matplotlib" library on your device.
import serial #Install "pyserial" module on your device.
import seaborn as sns ##Install "seaborn" module on your device.
import csv #In-built Python module.
import string #In-built Python module.
import os #In-built Python module

accountName = "           "
password = "       "
age = 0
expectation = 0
aim = 0
datapoint2 = 0

input1a = [35, 72, 89, 41, 68, 95]
input2a = [57, 23, 84, 63, 49, 76]
input3a = [92, 31, 78, 56, 99, 45]
input4a = [47, 90, 21, 59, 77, 94]
input5a = [64, 85, 27, 73, 38, 60]
input6a = [30, 70, 55, 81, 42, 88]
input7a = [98, 62, 37, 80, 25, 52]
input8a = [76, 22, 44, 69, 96, 34]
input9a = [53, 87, 67, 40, 71, 26]
input10a = [81, 93, 61, 28, 54, 79]
input11a = [20, 75, 51, 36, 66, 91]
input12a = [65, 82, 29, 43, 97, 50]
input13a = [39, 68, 89, 24, 58, 83]
input14a = [70, 41, 95, 52, 84, 31]
input15a = [56, 80, 23, 49, 76, 62]
input16a = [33, 97, 45, 72, 38, 65]
input17a = [59, 61, 10, 75, 83, 13]

input1b = [3, 7, 2, 8, 1, 9]
input2b = [5, 10, 4, 2, 1, 6]
input3b = [8, 3, 9, 7, 1, 4]
input4b = [6, 2, 10, 5, 3, 8]
input5b = [9, 4, 1, 10, 6, 2]
input6b = [7, 3, 8, 5, 1, 9]
input7b = [10, 6, 4, 7, 2, 3]
input8b = [2, 9, 3, 8, 4, 1]
input9b = [5, 10, 7, 1, 9, 3]
input10b = [8, 4, 6, 2, 10, 5]
input11b = [1, 7, 3, 9, 6, 2]
input12b = [4, 8, 5, 1, 10, 7]
input13b = [9, 2, 6, 3, 8, 4]
input14b = [7, 5, 10, 4, 2, 9]
input15b = [3, 6, 1, 9, 7, 5]
input16b = [10, 3, 8, 2, 6, 4]
input17b = [1, 7, 4, 5, 9, 2]

input1c = [1, 2, 3, 4, 5, 6]
input2c = [7, 8, 9, 10, 1, 2]
input3c = [3, 4, 5, 6, 7, 8]
input4c = [9, 10, 1, 2, 3, 4]
input5c = [5, 6, 7, 8, 9, 10]
input6c = [2, 3, 4, 5, 6, 7]
input7c = [8, 9, 10, 1, 2, 3]
input8c = [4, 5, 6, 7, 8, 9]
input9c = [10, 1, 2, 3, 4, 5]
input10c = [6, 7, 8, 9, 10, 1]
input11c = [3, 2, 1, 6, 5, 4]
input12c = [9, 8, 7, 10, 2, 1]
input13c = [4, 3, 2, 7, 6, 5]
input14c = [10, 9, 8, 1, 3, 2]
input15c = [5, 4, 3, 8, 7, 6]
input16c = [1, 10, 9, 2, 4, 3]
input17c = [6, 5, 4, 9, 8, 7]

input1d = [1, 3, 5, 7, 9, 10]
input2d = [2, 4, 6, 8, 10, 1]
input3d = [3, 5, 7, 9, 2, 4]
input4d = [4, 6, 8, 10, 3, 5]
input5d = [5, 7, 9, 1, 4, 6]
input6d = [6, 8, 10, 2, 5, 7]
input7d = [7, 9, 1, 3, 6, 8]
input8d = [8, 10, 2, 4, 7, 9]
input9d = [9, 1, 3, 5, 8, 10]
input10d = [10, 2, 4, 6, 9, 1]
input11d = [1, 4, 7, 10, 2, 5]
input12d = [2, 5, 8, 1, 3, 6]
input13d = [3, 6, 9, 2, 4, 7]
input14d = [4, 7, 10, 3, 5, 8]
input15d = [5, 8, 1, 4, 6, 9]
input16d = [6, 9, 2, 5, 7, 10]
input17d = [7, 10, 3, 6, 8, 1]


filePath = "ProjectTextFile.txt"


header = ["Account Name", "\t\tPassword", "\tAge", "\tExpectation", "  \tAim", "    Performance Rate (Jumps per min.)", "  Perceived Exertion", "  \tMood Score", "        \tEnergy Level", "\tTotal Time (min.)"]

row1 = [accountName, "\t\t", password, "\t", age, "\t", expectation, "  \t\t", aim, "\t", input1a, "\t", input1b, "  ", input1c, " ", input1d, "\t\t", datapoint2]

row2 = ["End_User#2!", "\t\tP@ssW2d", "\t45", "\t70", "\t\t9", "\t", input2a, "\t", input2b, "  ", input2c, " ", input2d, "\t182"]

row3 = ["Us3r_Acc0unt321", "\tCh@rm7Xy", "\t68", "\t66", "\t\t10", "\t", input3a, "\t", input3b, "  ", input3c, " ", input3d, "\t\t213"]

row4 = ["End_User#3!", "\t\tP@ssW2d1", "\t23", "\t89", "  \t\t3", "\t", input4a, "\t", input4b, "  ", input4c, " ", input4d, "\t793"]

row5 = ["Us3r_Acc0unt132", "\tCh@rm7Xy1", "\t18", "\t120", "  \t\t1", "\t", input5a, "\t", input5b, "  ", input5c, " ", input5d, "\t\t250"]

row6 = ["End_User#4!", "\t\tP@ssW2d2", "\t34", "\t97", "  \t\t5", "\t", input6a, "\t", input6b, "  ", input6c, " ", input6d, "\t\t53"]

row7 = ["Us3r_Acc0unt312", "\tCh@rm7Xy2", "\t76", "\t49", "  \t\t9", "\t", input7a, "\t", input7b, "  ", input7c, " ", input7d, "\t\t193"]

row8 = ["End_User#5!", "\t\tP@ssW2d3", "\t42", "\t55", "  \t\t12", "\t", input8a, "\t", input8b, "  ", input8c, " ", input8d, "\t\t454"]

row9 = ["Us3r_Acc0unt122", "\tCh@rm7Xy3", "\t69", "\t75", "  \t\t6", "\t", input9a, "\t", input9b, "  ", input9c, " ", input9d, "\t722"]

row10 = ["End_User#6!", "\t\tP@ssW2d4", "\t19", "\t89", "  \t\t4", "\t", input10a, "\t", input10b, "  ", input10c, " ", input10d, "\t863"]

row11 = ["Us3r_Acc0unt133", "\tCh@rm7Xy4", "\t22", "\t97", "  \t\t5", "\t", input11a, "\t", input11b, "  ", input11c, " ", input11d, "\t\t353"]

row12 = ["End_User#7!", "\t\tP@ssW2d5", "\t88", "\t67", "  \t\t11", "\t", input12a, "\t", input12b, "  ", input12c, " ", input12d, "\t\t111"]

row13 = ["Us3r_Acc0unt223", "\tCh@rm7Xy5", "\t54", "\t80", "  \t\t7", "\t", input13a, "\t", input13b, "  ", input13c, " ", input13d, "\t\t211"]

row14 = ["End_User#8!", "\t\tP@ssW2d6", "\t43", "\t75", "  \t\t6", "\t", input14a, "\t", input14b, "  ", input14c, " ", input14d, "\t566"]

row15 = ["Us3r_Acc0unt113", "\tCh@rm7Xy6", "\t65", "\t82", "  \t\t8", "\t", input15a, "\t", input15b, "  ", input15c, " ", input15d, "\t\t313"]

row16 = ["End_User#9!", "\t\tP@ssW2d7", "\t37", "\t92", "  \t\t3", "\t", input16a, "\t", input16b, "  ", input16c, " ", input16d, "\t152"]

row17 = ["Us3r_Acc0unt323", "\tCh@rm7Xy7", "\t29", "\t101", "  \t\t2", "\t", input17a, "\t", input17b, "  ", input17c, " ", input17d, "\t\t179"]

#Function to create the database in a csv file.

def writeToCSV():
    file = open(filePath, "w")
    file.close()
    file = open(filePath, "a", newline = "")
    dataBase = csv.writer(file)
    dataBase.writerow(header)
    dataBase.writerow(row1)
    dataBase.writerow(row2)
    dataBase.writerow(row3)
    dataBase.writerow(row4)
    dataBase.writerow(row5)
    dataBase.writerow(row6)
    dataBase.writerow(row7)
    dataBase.writerow(row8)
    dataBase.writerow(row9)
    dataBase.writerow(row10)
    dataBase.writerow(row11)
    dataBase.writerow(row12)
    dataBase.writerow(row13)
    dataBase.writerow(row14)
    dataBase.writerow(row15)
    dataBase.writerow(row16)
    dataBase.writerow(row17)
    file.close()
    
#Function that allows us to read the csv database whenever it is called.

def viewDatabase():
    writeToCSV()
    file = open(filePath, "r")
    dataIn = file.read()
    file.close()
    print(dataIn)
    print("\n\nTo view the database above to correct size, press and hold 'Ctrl' on your keyboard while scrolling the scroll wheel on the mouse.\n\n")

writeToCSV()
viewDatabase()

#To check whether the account name and/or password is already used by an existing user

def isItAlreadyInDataBase(personalDetail):
    reader = csv.reader(open('ProjectTextFile.txt'), delimiter=',') 
    for record in reader:
        for field in record:
            if field == personalDetail:
                return True

def logInProcedure(choice, accountName, password):
    count = 0
    while count == 0:
        if choice == 1:
            if isItAlreadyInDataBase(accountName):
                if isItAlreadyInDataBase(password):
                    print("\t\t\t", accountName, "welcome back to Fitness Master!\n\n")
                    count+=1
                else:
                    password = input("Your password is incorrect. Please enter a valid password:\n\n")
            else:
                accountName = str(input("Your account name is incorrect. Please enter a valid account name:\n\n"))
        elif choice == 2:
            if (len(accountName) < 4) or (len(accountName) >= 18):
                accountName = str(input("Please try again. The name can take maximum of 18 and minimum of 4 characters.\n\n"))   
            elif isItAlreadyInDataBase(accountName): 
                accountName = str(input("Please try again. This account name is already used.\n\n"))    
            else:
                if (len(password) >= 8) or (not (any(char.islower() for char in password))) or (not any(char.isupper() for char in password)) or (password.__contains__(" ")):
                    password = str(input("Please try again. The password must contain a maximum of 8 characters, one lower and one upper case letter, without a space.\n\n"))  
                elif not any(char not in string.ascii_letters + string.digits for char in password): #determines if at least one character in "newPassword" is not an alphanumeric character, indicating the presence of a special character.
                    password = str(input("Please try again. The password must contain at minimum one special character.\n\n"))
                elif isItAlreadyInDataBase(password): 
                    password = str(input("Please try again. This password is already used.\n\n"))
                else:
                    count+=1

start = str(input("Are you a new user (Yes/No)?\n\n"))

a = 0

while a == 0: 
    try:
        choice = int(input("Hi! If you have an account already Log In by entering '1'. Otherwise, Register by entering '2'.\n\n\t\t\t\t1. Log In\t\t\t2. Register\n\n"))
        if choice == 1:
            a += 1
        elif choice == 2:
            a += 1
        else:
            print("Invalid input. Please, enter either '1' for Log In or '2' for Register.\n\n")
    except (TypeError, ValueError, AssertionError):
        print("Invalid input. Please, enter either '1' for Log In or '2' for Register.\n\n")

if (start == "No") or (start == "no"):
    accountName = str(input("Enter your account name:\n\n")) 
    password = str(input("Enter your password:\n\n"))
elif start == "Yes" or (start == "yes"):
    accountName = str(input("\nCreate a new account name. The name can take maximum of 18 characters.\n\n")) 
    password = input("Create a strong password - one having a maximum of 8 characters, one lower and one upper case letter,\none number and one special character, without a space.\n\n")
    
logInProcedure(choice, accountName, password)

#Input validation for TypeError, ValueError, AssertionError and negative integers.

b = 0

while b == 0: 
    try:
        age = int(input("What is your age?\n\n"))
        if age > 0:
            b += 1
        else:
            print("Invalid input. Please, enter a positive number for age.\n\n")
    except (TypeError, ValueError, AssertionError):
        print("Invalid input. Please, enter a whole positive number for age.\n\n")

c = 0

while c == 0: 
    try:
        expectation = float(input("How many jumps per minute do you think you can do in a single exercise?\n\n"))
        if expectation > 0:
            c += 1
        else:
            print("Invalid input. Please, enter a positive decimal number correct to one decimal place for your performance expectation in jumps per minute.\n\n")
    except (TypeError, ValueError, AssertionError):
        print("Invalid input. Please, enter a positive decimal number correct to one decimal place for how many jumps you expect to be able to perform every minute.\n\n")

d = 0

while d == 0: 
    try:
        aim = int(input("How many weeks do you wish to use the exercise programme until getting fit, if exercising once daily?\n\n"))
        if aim > 0:
            d += 1
        else:
            print("Invalid input. Please, enter a positive whole number for how many weeks do you wish to exercise while using this app.\n\n")
    except (TypeError, ValueError, AssertionError):
        print("Invalid input. Please, enter a positive whole number for how many weeks do you expect to exercise while using this app.\n\n")

writeToCSV()

e = 0

while e == 0: 
    try:
        portNumber = int(input("Enter the correct port number of micro:bit USB serial device. To do this, go to Device Manager on your computer\nafter connecting your micro:bit to the device via a USB cable. There, you can find the COM number under\n'Ports (COM & LPT)'.\n\n"))
        if portNumber > 0:
            e += 1
        else:
            print("Invalid input. Please, enter a positive port number.\n\n")
    except (TypeError, ValueError, AssertionError):
        print("Invalid input. Please, enter a whole positive port number, such as '1' for COM1, or '6' for COM6.\n\n")
            
    #Creates the serial object to establish a cooncetion with micro:bit trpugh the USB cable.

    portName = ("COM" + str(portNumber))
    print("Your port name is " + str(portName) + ".\n\n")
    print("\t\t\t\t\t\tExercise instructions:\n")
    print("Restart micro:bit to initiate the timer and commence the exercise. The number of jumping jacks performed is counted.\nWhen you have finished exercising, press button A on micro:bit. The heart LED dispaly will indicate that you have reached\nthe end of exercise.\n\n")
    serialObject = serial.Serial()
    serialObject.baudrate = 115200
    serialObject.port = portName
    serialObject.open()

    #Data is received from the micro:bit and transformed.

    data1 = str(serialObject.readline())
    data1 = data1.replace("b", "")
    data1 = data1.replace("'", "")
    data1 = data1.replace(" ", "")
    data1 = data1.replace("\\r\\n", "")
    print(data1)

    data2 = str(serialObject.readline())
    data2 = data2.replace("b", "")
    data2 = data2.replace("'", "")
    data2 = data2.replace(" ", "")
    data2 = data2.replace("\\r\\n", "")
    print(data2)

    datapoint1 = int(data1[9:])
    datapoint2 = round((int(data2[13:]))/60, 1)

    #The recived data is stored on a csv file.

    file = open("data.csv", "w")
    file.close()
    file = open("data.csv", "a")
    file.write(data1+",")
    file.write(data2+",")
    file.close()

    file = open("data.csv", "r")
    dataIn =  file.read()
    file.close()
    print("\n\nThe exercise data above is stored to your csv file as: '", dataIn, "'.\n\n")

    #Input validation for TypeError, ValueError, AssertionError and negative integers.

    f = 0

    while f == 0: 
        try:
            percivedExertion = int(input("After the exercise, how would you rate your percived exertion on the scale 1 to 10: "))
            if percivedExertion > 0:
                f += 1
            else:
                print("Invalid input. Please, enter a positive whole number in the range 1 to 10 to indicate the level of your precived excertion.\n\n")
        except (TypeError, ValueError, AssertionError):
            print("Invalid input. Please, enter a positive whole number in the range 1 to 10 to indicate the level of your precived excertion.\n\n")
            
    g = 0

    while g == 0: 
        try:
            moodLevel = int(input("After the exercise, how would you rate your mood level on the scale 1 to 10: "))
            if moodLevel > 0:
                g += 1
            else:
                print("Invalid input. Please, enter a positive whole number in the range 1 to 10 to indicate your mood level after the exercise.\n\n")
        except (TypeError, ValueError, AssertionError):
            print("Invalid input. Please, enter a positive whole number in the range 1 to 10 to indicate your mood level after the exercise.\n\n")
            
    h = 0

    while h == 0: 
        try:
            energyLevel = int(input("Finally, after completing the exercise, how would you rate your energy level on the scale 1 to 10: "))
            print("\n\n")
            if energyLevel > 0:
                h += 1
            else:
                print("Invalid input. Please, enter a positive whole number in the range 1 to 10 to indicate your energy level after the exercise.\n\n")
        except (TypeError, ValueError, AssertionError):
            print("Invalid input. Please, enter a positive whole number in the range 1 to 10 to indicate your energy level after the exercise.\n\n")

    #The inputed values from user prompts are appended to the lists contained in the database, while "accountName", "password", "age", "expectation" and "aim"
    #variable values are also updated and then stored in database kept on a csv file.

    input1a.append(datapoint1)
    input1b.append(datapoint2)
    input1b.append(percivedExertion)
    input1c.append(moodLevel)
    input1d.append(energyLevel)

    header = ["Account Name", "\t\tPassword", "\tAge", "\tExpectation", "  \tAim", "    Performance Rate (Jumps per min.)", "  Perceived Exertion", "  \tMood Score", "        \tEnergy Level", "\tTotal Time (min.)"]

    row1 = [accountName, "\t\t", password, "\t", age, "\t", expectation, "  \t", aim, "\t", input1a, input1b, input1c, input1d, "  ", datapoint2]

    row2 = ["End_User#2!", "\t\tP@ssW2d", "\t45", "\t70", "\t\t9", "\t", input2a, "\t", input2b, "  ", input2c, " ", input2d, "\t182"]

    row3 = ["Us3r_Acc0unt321", "\tCh@rm7Xy", "\t68", "\t66", "\t\t10", "\t", input3a, "\t", input3b, "  ", input3c, " ", input3d, "\t\t213"]

    row4 = ["End_User#3!", "\t\tP@ssW2d1", "\t23", "\t89", "  \t\t3", "\t", input4a, "\t", input4b, "  ", input4c, " ", input4d, "\t793"]

    row5 = ["Us3r_Acc0unt132", "\tCh@rm7Xy1", "\t18", "\t120", "  \t\t1", "\t", input5a, "\t", input5b, "  ", input5c, " ", input5d, "\t\t250"]

    row6 = ["End_User#4!", "\t\tP@ssW2d2", "\t34", "\t97", "  \t\t5", "\t", input6a, "\t", input6b, "  ", input6c, " ", input6d, "\t\t53"]

    row7 = ["Us3r_Acc0unt312", "\tCh@rm7Xy2", "\t76", "\t49", "  \t\t9", "\t", input7a, "\t", input7b, "  ", input7c, " ", input7d, "\t\t193"]

    row8 = ["End_User#5!", "\t\tP@ssW2d3", "\t42", "\t55", "  \t\t12", "\t", input8a, "\t", input8b, "  ", input8c, " ", input8d, "\t\t454"]

    row9 = ["Us3r_Acc0unt122", "\tCh@rm7Xy3", "\t69", "\t75", "  \t\t6", "\t", input9a, "\t", input9b, "  ", input9c, " ", input9d, "\t722"]

    row10 = ["End_User#6!", "\t\tP@ssW2d4", "\t19", "\t89", "  \t\t4", "\t", input10a, "\t", input10b, "  ", input10c, " ", input10d, "\t863"]

    row11 = ["Us3r_Acc0unt133", "\tCh@rm7Xy4", "\t22", "\t97", "  \t\t5", "\t", input11a, "\t", input11b, "  ", input11c, " ", input11d, "\t\t353"]

    row12 = ["End_User#7!", "\t\tP@ssW2d5", "\t88", "\t67", "  \t\t11", "\t", input12a, "\t", input12b, "  ", input12c, " ", input12d, "\t\t111"]

    row13 = ["Us3r_Acc0unt223", "\tCh@rm7Xy5", "\t54", "\t80", "  \t\t7", "\t", input13a, "\t", input13b, "  ", input13c, " ", input13d, "\t\t211"]

    row14 = ["End_User#8!", "\t\tP@ssW2d6", "\t43", "\t75", "  \t\t6", "\t", input14a, "\t", input14b, "  ", input14c, " ", input14d, "\t566"]

    row15 = ["Us3r_Acc0unt113", "\tCh@rm7Xy6", "\t65", "\t82", "  \t\t8", "\t", input15a, "\t", input15b, "  ", input15c, " ", input15d, "\t\t313"]

    row16 = ["End_User#9!", "\t\tP@ssW2d7", "\t37", "\t92", "  \t\t3", "\t", input16a, "\t", input16b, "  ", input16c, " ", input16d, "\t152"]

    row17 = ["Us3r_Acc0unt323", "\tCh@rm7Xy7", "\t29", "\t101", "  \t\t2", "\t", input17a, "\t", input17b, "  ", input17c, " ", input17d, "\t\t179"]

    writeToCSV()
    viewDatabase()

    #Defining the diffrent measures for anlysisng data as functions. 

    def mean(listOfValues):
        sumValues = 0
        for item in listOfValues:
            sumValues += item
        mean = round(sumValues/len(listOfValues), 1)
        return mean

    def printMean(listOfValues):
        sumValues = 0
        for item in listOfValues:
            sumValues += item
        mean = round(sumValues/len(listOfValues), 1)
        print("The mean of the reference list:", mean, "\n\n")

    def minimum(listOfValues):
        listOfValues.sort()
        minValue = listOfValues[0]
        return minValue

    def printMinimum(listOfValues):
        listOfValues.sort()
        print(listOfValues, "\n\n")
        minValue = listOfValues[0]
        print("The minimum value in the reference list:", minValue, "\n\n")
        
    def maximum(listOfValues):
        listOfValues.sort()
        maxValue = listOfValues[-1]
        return maxValue
        
    def printMaximum(listOfValues):
        listOfValues.sort()
        print(listOfValues, "\n\n")
        maxValue = listOfValues[-1]
        print("The maximum value in the reference list:", maxValue, "\n\n")
        
    def median(listOfValues):
        listOfValues.sort()
        if len(listOfValues) % 2 == 0:
            middlePlusOne = len(listOfValues) // 2
            median = round((listOfValues[middlePlusOne-1] + listOfValues[middlePlusOne]) / 2, 1)
            return median
        else:
            middle = len(listOfValues) // 2
            median = float(listOfValues[middle])
            return median

    def printMedian(listOfValues):
        listOfValues.sort()
        print(listOfValues, "\n\n")
        if len(listOfValues) % 2 == 0:
            middlePlusOne = len(listOfValues) // 2
            median = round((listOfValues[middlePlusOne-1] + listOfValues[middlePlusOne]) / 2, 1)
            print("The median of the reference list:", median, "\n\n")
        else:
            middle = len(listOfValues) // 2
            median = float(listOfValues[middle])
            print("The median of the reference list:", median, "\n\n")

    #A display of statistical analysis for mean, median as well as minimum and maximum values for each field across the user record.

    print("Statistical analysis of the performance rate measured in jumps per minute:\n")

    print("\n_____________________________________________________________________________________\n")

    printMean(input1a)
    printMedian(input1a)
    printMinimum(input1a)
    printMaximum(input1a)

    print("\n_____________________________________________________________________________________\n")

    print("Statistical analysis of the perceived exertion measured on scale 1 to 10:\n")

    printMean(input1b)
    printMedian(input1b)
    printMinimum(input1b)
    printMaximum(input1b)

    print("\n_____________________________________________________________________________________\n")

    print("Statistical analysis of the mood score measured on scale 1 to 10:\n")

    printMean(input1c)
    printMedian(input1c)
    printMinimum(input1c)
    printMaximum(input1c)

    print("\n_____________________________________________________________________________________\n")

    print("Statistical analysis of the energy level measured on scale 1 to 10:\n")

    printMean(input1d)
    printMedian(input1d)
    printMinimum(input1d)
    printMaximum(input1d)

    print("\n_____________________________________________________________________________________\n")
     
    def frequencyAndMode(listOfValues):
        referenceList = []
        countList = []
        for item in listOfValues:
            if item not in referenceList:
                referenceList.append(item)
        for counting in referenceList:
            total = listOfValues.count(counting)
            countList.append(total)
        print("Reference list:\n\n", referenceList, "\n")
        print("Frequencies one to one respective to the reference list:\n\n", countList, "\n")
        maxFrequency = max(countList)
        maxFrequencyIndex = countList.index(maxFrequency)
        mode = referenceList[maxFrequencyIndex]
        print("The mode of the reference list:", mode,"\n\n")

    #An additional display of statistical analysis for frequency and mode as well as minimum and maximum values
    #taking into the account all of the data in the database from every user, and thus finding the most frequent,
    #highest and the lowest value in the database.

    print("\n-------------------------------------------------------------------------------------\n")

    print("\nStatistical analysis of all of the entires in the database, by field: \n")

    print("\n_____________________________________________________________________________________\n")

    print("For performance rate (jumps per min.):\n")

    freqTestA = input1a + input2a + input3a + input4a + input5a + input6a + input7a + input8a + input9a + input10a + input11a + input12a + input13a + input14a + input15a + input16a + input17a
    print(freqTestA)

    frequencyAndMode(freqTestA)
    printMinimum(freqTestA)
    printMaximum(freqTestA)

    print("\n_____________________________________________________________________________________\n")

    print("For perceived exertion:\n")

    freqTestB = input1b + input2b + input3b + input4b + input5b + input6b + input7b + input8b + input9b + input10b + input11b + input12b + input13b + input14b + input15b + input16b + input17b
    print(freqTestB)

    frequencyAndMode(freqTestB)
    printMinimum(freqTestB)
    printMaximum(freqTestB)

    print("\n_____________________________________________________________________________________\n")

    print("For mood score:\n")

    freqTestC = input1c + input2c + input3c + input4c + input5c + input6c + input7c + input8c + input9c + input10c + input11c + input12c + input13c + input14c + input15c + input16c + input17c
    print(freqTestC)

    frequencyAndMode(freqTestC)
    printMinimum(freqTestC)
    printMaximum(freqTestC)

    print("\n_____________________________________________________________________________________\n")

    print("For energy level:\n")

    freqTestD = input1d + input2d + input3d + input4d + input5d + input6d + input7d + input8d + input9d + input10d + input11d + input12d + input13d + input14d + input15d + input16d + input17d
    print(freqTestD)

    frequencyAndMode(freqTestD)
    printMinimum(freqTestD)
    printMaximum(freqTestD)

    print("\n_____________________________________________________________________________________\n\n")

    #First "what-if" question - What if the user mean score is below medium level of difficulty, or above medium level of difficulty but below the advanced level, or at or above the advanced level of difficulty?

    lowLevelOfDifficulty = 25
    moderateLevelOfDifficulty = 50
    highLevelOfDifficulty = 80
    advancedLevelOfDifficulty = 100

    def whatIfQuestion1(jumpRateMean, totalTimeExercised, jumpRateMaximumValue):
        if jumpRateMean < moderateLevelOfDifficulty:
            fitnessRecommendation = 12
            if totalTimeExercised >= 420:
                fitnessRecommendation += 3
                print("It looks like that according to your low value of mean performance indicating poor level of fitness,\nit will require", fitnessRecommendation, "weeks of consitent exercise to achieve the desired level of fitness.")
            else:
                fitnessRecommendation -= 1
                print("It looks like that according to your mean performance, it will require", fitnessRecommendation, "months of consitent exercise to achieve the desired level of fitness.")
            if jumpRateMaximumValue <= lowLevelOfDifficulty:
                print("Also, according to your highest performance value of", jumpRateMaximumValue, "we recommend to aim\nfor a low level of difficulty, i.e. to preform no more than", lowLevelOfDifficulty, "jumps per minute to prevent injury.")
            elif (jumpRateMaximumValue > lowLevelOfDifficulty) and (jumpRateMaximumValue <= highLevelOfDifficulty) :
                print("Also, according to your highest performance value of", jumpRateMaximumValue, "we recommend to aim\nfor a moderate level of difficulty, i.e. to preform no more than", moderateLevelOfDifficulty, "jumps per minute to prevent injury.")
            elif jumpRateMaximumValue > highLevelOfDifficulty:
                print("Also, according to your highest performance value of", jumpRateMaximumValue, "we recommend to aim\nfor a high level of difficulty, i.e. to preform no more than", highLevelOfDifficulty, "jumps per minute to prevent injury.")
        elif (jumpRateMean >= moderateLevelOfDifficulty) and (jumpRateMean < advancedLevelOfDifficulty):
            fitnessRecommendation = 8
            if totalTimeExercised >= 420:
                fitnessRecommendation += 1
                print("It looks like that according to your mean performance which appears to be low inspite of the long length of time you have been exercising,\nit will require", fitnessRecommendation, "weeks of additional consitent exercise to achieve the desired level of fitness.")
            else:
                if totalTimeExercised <= 180:
                    fitnessRecommendation -= 4
                    print("It looks like that according to your mean performance which is high in comparison to the small length if time you have been exercising,\nit will require", fitnessRecommendation, "weeks of consitent exercise to achieve the desired level of fitness.")
            if jumpRateMaximumValue <= lowLevelOfDifficulty:
                print("Also, according to your highest performance value of", jumpRateMaximumValue, "we recommend to aim\nfor a low level of difficulty, i.e. to preform no more than", lowLevelOfDifficulty, "jumps per minute to prevent injury.")
            elif (jumpRateMaximumValue > lowLevelOfDifficulty) and (jumpRateMaximumValue <= highLevelOfDifficulty) :
                print("Also, according to your highest performance value of", jumpRateMaximumValue, "we recommend to aim\nfor a moderate level of difficulty, i.e. to preform no more than", moderateLevelOfDifficulty, "jumps per minute to prevent injury.")
            elif jumpRateMaximumValue > highLevelOfDifficulty:
                print("Also, according to your highest performance value of", jumpRateMaximumValue, "we recommend to aim\nfor a high level of difficulty, i.e. to preform no more than", highLevelOfDifficulty, "jumps per minute to prevent injury.")
        elif jumpRateMean >= advancedLevelOfDifficulty:
            fitnessRecommendation = 3
            print("It looks like that according to your high value of mean performance which indicates already high fitness level,\nit will require", fitnessRecommendation, "weeks of consitent exercise to achieve the desired level of fitness.")
            if jumpRateMaximumValue <= lowLevelOfDifficulty:
                print("Also, according to your highest performance value of", jumpRateMaximumValue, "we recommend to aim\nfor a low level of difficulty, i.e. to preform no more than", lowLevelOfDifficulty, "jumps per minute to prevent injury.")
            elif (jumpRateMaximumValue > lowLevelOfDifficulty) and (jumpRateMaximumValue <= highLevelOfDifficulty) :
                print("Also, according to your highest performance value of", jumpRateMaximumValue, "we recommend to aim\nfor a moderate level of difficulty, i.e. to preform no more than", moderateLevelOfDifficulty, "jumps per minute to prevent injury.")
            elif jumpRateMaximumValue > highLevelOfDifficulty:
                print("Also, according to your highest performance value of", jumpRateMaximumValue, "we recommend to aim\nfor a high level of difficulty, i.e. to preform no more than", highLevelOfDifficulty, "jumps per minute to prevent injury.")
            
    whatIfQuestion1(mean(input1a), datapoint2, maximum(input1a))

    print("\n")

    #Second "what-if" question - What if the user mean score is below their expectations, or equal to or above their expectations and by what extent?

    def whatIfQuestion2(jumpRateMean, userExpectation, jumpRateMinimumValue, jumpRateMaximumValue):
        if jumpRateMean > userExpectation:
            print("\nIt seems that you are more fit then you expected. This is an indication of self-doubt and poor self-esteem.\nTo help you nurture your mental health, as well as physical health, you should instead think of yourself positively and aim high.\nNever forget to feel good about your achivements and progress.")
        elif jumpRateMean < userExpectation:
            print("\nIt seems that you are less fit then you expected to be. This is an indication that you have delayed to acknowledge\nphysical exercise as the quintessential aspect of a helathy daily routine. Yet, don't be disheartened! With consistent exercise you can get fit in no time!")
        elif jumpRateMean == userExpectation:
            print("Fantastic! It seems that your expectations perfectly match your mean exercise result, indicating at your realistic outlook\non your own fitness and your awarness of the importance of physical exercise.")
        userRange = (jumpRateMaximumValue - jumpRateMinimumValue) - (userExpectation - jumpRateMinimumValue)
        if userRange <= 5:
            print("There is only a small difference between actual range value (your lowest result subtracted from your highest result)\nand the expected range value (your lowest result subtracted from your expected result).\nThis is an indicator of good awarness of your current physical well-being and fitness.")
        elif (userRange > 5) and (userRange <= 20):
            print("There is some difference between actual range value (your lowest result subtracted from your highest result)\nand the expected range value (your lowest result subtracted from your expected result).\nThis is an indicator of a slight lack of awarness of your current physical well-being and fitness,\nwhich can be imroved with analysis of further exercise session results.")
        elif userRange >= 50:
            print("There is significant difference between actual range value (your lowest result subtracted from your highest result)\nand the expected range value (your lowest result subtracted from your expected result).\nThis is an indicator of a poor awarness of your current physical well-being and fitness. This programme can help this awarness\nto grow given that you use it to analyse your exercise data in the future.")

    whatIfQuestion2(mean(input1a), expectation, minimum(input1a), maximum(input1a))

    print("\n")

    #Third "what-if" question - What if the user's age is below 20, above 20 to 40 or above 40? How will age reflect on their exertion levels? 

    def whatIfQuestion3(ageValue, meanPercivedExertion, timeNeededToGetFit, medianValue):
        if (ageValue <= 20) and (timeNeededToGetFit < 8):
            print("It seems that according to your young age, your estimate of " + str(timeNeededToGetFit) + " weeks needed\nto get fit is realistic.")
            if meanPercivedExertion <= 5:
                print("This is supported by the fact that you find exercise minimally exerting,\nwith a mean exertion score of " + str(meanPercivedExertion) + ". This means it will take you less than average 8 weeks to get fit.")
            elif (meanPercivedExertion > 5) and (meanPercivedExertion <= 7):
                print("Yet you find exercise somewhat exerting,\nwith a mean exertion score of " + str(meanPercivedExertion) + ". This means it will take you the average 8 weeks to get fit.")
            elif meanPercivedExertion > 7:
                print("However this is contradicted by your very high exertion mean score of " + str(meanPercivedExertion) + ".\nThis means it will take you more than average 8 weeks to get fit, and that your fitness level is dangerously low.")
        elif (ageValue <= 20) and (timeNeededToGetFit > 8):
            print("It seems that according to your young age, your estimate of " + str(timeNeededToGetFit) + " weeks needed\nto get fit is unrealistic, as it is higher than the norm.")
            if meanPercivedExertion <= 5:
                print("This is supported by the fact that you find exercise minimally exerting,\nwith a mean exertion score of " + str(meanPercivedExertion) + ". This means it will take you less than average 8 weeks to get fit.")
            elif (meanPercivedExertion > 5) and (meanPercivedExertion <= 7):
                print("Yet you find exercise somewhat exerting,\nwith a mean exertion score of " + str(meanPercivedExertion) + ". This means it will take you the average 8 weeks to get fit.")
            elif meanPercivedExertion > 7:
                print("However this is contradicted by your very high exertion mean score of " + str(meanPercivedExertion) + ".\nThis means it will take you more than average 8 weeks to get fit, and that your fitness level is dangerously low.")
        elif ((ageValue <= 40) and (timeNeededToGetFit < 8)) or ((ageValue <= 40) and (timeNeededToGetFit > 8)):
            print("It seems that according to your middle age bracket, your estimate of " + str(timeNeededToGetFit) + " weeks needed\nto get fit could be realistic or unrealistic, depending on various factors.")
            if meanPercivedExertion <= 5:
                print("Given that you find exercise minimally exerting,\nwith a mean exertion score of " + str(meanPercivedExertion) + ".\nit will take you about 8 weeks to get fit due to your age bracket.")
            elif (meanPercivedExertion > 5) and (meanPercivedExertion <= 7):
                print("Given that you find exercise somewhat exerting,\nwith a mean exertion score of " + str(meanPercivedExertion) + ".\nit will take you more than 8 weeks to get fit due to your age bracket.")
            elif meanPercivedExertion > 7:
                print("Given that you find exercise extremely exerting,\nwith a mean exertion score of " + str(meanPercivedExertion) + ".\nit will take you about the maximum 12 weeks to get fit due to your age bracket.")
        elif (ageValue > 40) and (timeNeededToGetFit < 8):
            print("It seems that according to your older age bracket, your estimate of " + str(timeNeededToGetFit) + " weeks needed\nto get fit is very unrealistic, as this is much higher than the norm.")
            if meanPercivedExertion <= 5:
                print("Still, your mean excertion score of " + str(meanPercivedExertion) + " tells otherwise. It seems that\nyou are able to exercise without tiring and so 8 weeks or a bit more of exercise\nwill be sufficient to achive fitness, while taking your elder age into the consideration.")
            elif (meanPercivedExertion > 5) and (meanPercivedExertion <= 7):
                print("Your mean excertion score of " + str(meanPercivedExertion) + " is impressive, thought it shows presence of exertion.\nIt will thus take you about 12 weeks of exercise will be sufficient to achive fitness,\nwhile taking your elder age into the consideration.")
            elif meanPercivedExertion > 7:
                print("Given your age, the high exertion score of " + str(meanPercivedExertion) + " is quite normal and expected.\nDue to this, it will take you more than 12 weeks of exercise to achive fitness\nwithout causing injury, taking your elder age into the consideration.")
        elif (ageValue > 40) and (timeNeededToGetFit > 8):
            print("It seems that according to your older age bracket, your estimate of " + str(timeNeededToGetFit) + " weeks needed\nto get fit is quite realistic, as it is in line with the norm.")
            if meanPercivedExertion <= 5:
                print("With a mean exertion score of " + str(meanPercivedExertion) + ", it seems that you are able to exercise without tiring\nand so 8 weeks or a bit more of exercise will be sufficient to achive fitness,\nwhile taking your elder age into the consideration.")
            elif (meanPercivedExertion > 5) and (meanPercivedExertion <= 7):
                print("Your mean excertion score of " + str(meanPercivedExertion) + " is impressive, thought it shows presence of exertion.\nIt will thus take you about 12 weeks of exercise will be sufficient to achive fitness,\nwhile taking your elder age into the consideration.")
            elif meanPercivedExertion > 7:
                print("Given your age, the high exertion score of " + str(meanPercivedExertion) + " is quite normal and expected.\nDue to this, it will take you more than 12 weeks of exercise to achive fitness\nwithout causing injury, taking your elder age into the consideration.")

    whatIfQuestion3(age, mean(input1b), aim, median(input1b))

    print("\n")

    #Fourth "what-if" question - What if the user mean and median mood score together with their average reported energy level is high or low, and what are implications on user's ability to preform the exercise?

    def whatIfQuestion4(meanMoodScore, meanEnergyLevel, medianMoodScore, medianEnergyLevel, timeNeededToGetFit):
        if (meanMoodScore and meanEnergyLevel) < 5:
            print("Since both of your average mood score and energy level values after performing the exercise\nare quite small, you are finding it difficult to exercise strenously. Instead, try to exercise\nfor smaller periods of time per session.")
            if (medianMoodScore and medianEnergyLevel) < 5:
                timeNeededToGetFit += 1
                print("As your mean and median values for mood score and energy value are low, we recommend to prolongue the planned time\nwithin which you wanted to achieve fitness by a week to " + str(timeNeededToGetFit) + " weeks.")
            elif (medianMoodScore and medianEnergyLevel) >= 5:
                timeNeededToGetFit -= 1
                print("As your mean and median values for mood score and energy value are high, we recommend to decrease the planned time\nwithin which you wanted to achieve fitness by a week to " + str(timeNeededToGetFit) + " weeks.")
        elif (meanMoodScore and meanEnergyLevel) >= 5:
            print("Since both of your average mood score and energy level values after performing the exercise\nare quite large, you are finding it easy to exercise for the current level of difficulty.\nNow, try to perform more jumps per minute over shorter periods of time per session,\nsuch as " + str(moderateLevelOfDifficulty) + " jumps/min, " + str(highLevelOfDifficulty) + " jumps/min or " + str(advancedLevelOfDifficulty) + " jumps/min.")
            if (medianMoodScore and medianEnergyLevel) >= 5:
                timeNeededToGetFit -= 1
                print("As your mean and median values for mood score and energy value are high, we recommend to decrease the planned time\nwithin which you wanted to achieve fitness by a week to " + str(timeNeededToGetFit) + " weeks.")
            elif (medianMoodScore and medianEnergyLevel) < 5:
                timeNeededToGetFit += 1
                print("As your mean and median values for mood score and energy value are low, we recommend to prolongue the planned time\nwithin which you wanted to achieve fitness by a week to " + str(timeNeededToGetFit) + " weeks.")

    whatIfQuestion4(mean(input1c), mean(input1d), median(input1c), median(input1d), aim)

    print("\n")

    #Function to predict whether user's next exercise result will be higher, lower or equal to their latest reuslt.

    def findTrend(listOfValues):
        if len(listOfValues) >= 6: #Identifies a pattern in lists containing more than 6 items.
            firstAverage = firstAverage = round((sum(listOfValues[:3]))/3, 1) #Calculates the average for the first three items in the list, then the last three and compares them.
            secondAverage = round(((sum(listOfValues[-3:])))/3, 1)
            if firstAverage > secondAverage:
                trend = "decreasing"
                print("According to your previous exercise results, your average exercise score is " + str(trend) + " \nand hence, your next result is predicted to be smaller than your latest result of " + str(listOfValues[-1]) + ".")
            elif firstAverage < secondAverage:
                trend = "increasing"
                print("According to your previous exercise results, your average exercise score is " + str(trend) + " \nand hence, your next result is predicted to be bigger than your latest result of " + str(listOfValues[-1]) + ".")
            elif firstAverage == secondAverage:
                trend = "not changed"
                print("According to your previous exercise results, your average exercise score has " + str(trend) + " \nand hence, your next result is predicted to be equal to your latest result of " + str(listOfValues[-1]) + ".")
        else:
            pass

    findTrend(input1a)
        
    #Compares the maximum exercise score of the user with the highest exercise csore across all of the user's in the database and calculates the diffrence between them. This motivates the user to exercise harder.
        
    def motivation(highestOverallScore, usersHighestScore):
        if highestOverallScore > usersHighestScore:
            difference = highestOverallScore - usersHighestScore
            print("Your exercise score is " + str(difference) + " jumps per minute less than that of the highest scoring user. So keep climbing to the top!")
        elif highestOverallScore == usersHighestScore:
            print("Your exercise score in terms of jumps performed per minute is greatest among all users. Well done!")

    motivation(maximum(freqTestA), maximum(input1a))

    print("To interpret the above data analysis visually, please refer to the line graph and the pie chart displayed.")

    #Creating a graph on exercise performance:

    #Identifies the range of exercise sessions that are then marked on the x-axis of the graph, starting with 1.

    timeList = []

    for time in range(1, (len(input1a))+1):
        timeList.append(time)
        
    #Plots a line graph with a legend and a title. The subplot function is used to dispaly the two graphs together and determines their position.
        
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(timeList, input1a, marker='o')
    plt.xlabel("Number of Exercise Sessions")
    plt.ylabel("Performance Rate (Jumps per min.)")
    plt.title("Exercise Performance Graph")
    plt.legend(["Result of a Certain Exercise Session"], loc='upper left', fontsize='small')

    #Performance Rate (Jumps per min.)

    #Creating a graph on user's energy level after exercise:

    plt.subplot(1, 2, 2)  
    labels = ["Low Energy", "Regular Energy", "High Energy"]
    chartedData = []
    counter1 = 0
    counter2 = 0
    counter3 = 0

    #Processes data in the "input1d" list to fit within one of three cathegories: "Low Energy", "Regular Energy" and "High Energy".

    for item in input1d:
        if item < 5:
            counter1 += 1
        elif item == 5:
            counter2 += 1
        else:
            counter3 += 1
    chartedData.append(counter1)
    chartedData.append(counter2)
    chartedData.append(counter3)

    #Creates the pie chart. Here, the "autopct" is responsible for taging each pie chart sector with an automatically claculated proportion percentage.
    #Also, "colors=sns.color_palette('Set2')" contributes a more asthetically appealing colour pallet that improves the user interface experience.
    #Lastly, the layout is adjusted to prevent the overlapping of two graphs using "tight_layout" function.

    plt.pie(chartedData, labels=labels, autopct='%1.2f%%', colors=sns.color_palette('Set2'))
    plt.title("Post-Exercise Energy Levels Graph")

    plt.tight_layout() 
    plt.show()

    #Exit function: the user can choose to either exercise again or exit the programme.

    i = 0

    while i == 0: 
        try:
            termination = int(input("The data analysis is complete. If you want to exit the programme, please enter '1'. Otherwise, choose to exercise again by entering '2'.\n\n\t\t\t\t1. Exit\t\t\t2. Exercise Again\n\n"))
            if termination == 1:
                i += 1
                print("Thank you for using Fitness Master!")
            elif termination == 2:
                e = 0
                i += 1
            else:
                print("Invalid input. Please, enter either '1' to exit the programme or '2' to exercise again.\n\n")
        except (TypeError, ValueError, AssertionError):
            print("Invalid input. Please, enter either '1' to exit the programme or '2' to exercise again.\n\n")
