import csv
import math

class Lifter:
    def __init__(self, name, gender, bodyWeight, squat, bench, deadLift, total):
        self._name = name
        self._gender = gender
        self._bodyWeight = bodyWeight
        self._squat = squat
        self._bench = bench
        self._dl = deadLift
        self._total = total

    def name(self):
        return self._name

    def gender(self):
        return self._gender

    def bodyWeight(self):
        return self._bodyWeight

    def squat(self):
        return self._squat

    def bench(self):
        return self._bench

    def deadLift(self):
        return self._dl

    def total(self):
        return self._total

    def __str__(self):
        return '[' + self._name + ', ' + self._gender + ', '  + str(self._bodyWeight) + ', ' + str(self._squat) + ', ' + str(self._bench) + ', ' + str(self._dl) + ', ' + str(self._total) + ']'

    def __repr__(self):
        return '[' + self._name + ', ' + self._gender + ', ' + str(self._bodyWeight) + ', ' + str(self._squat) + ', ' + str(self._bench) + ', ' + str(self._dl) + ', ' + str(self._total) + ']'

    def __lt__(self, other):
        return self._name < other.name()

    def __gt__(self, other):
        return self._name > other.name()

    def __eq__(self, other):
        return self._name == other.name()

    def replace(self, weight, attribute):
        if attribute == 'bodyweight':
            self._bodyWeight = weight
        if attribute == "squat":
            self._squat = weight
        elif attribute == "bench":
            self._bench = weight
        elif attribute == "deadlift":
            self._dl = weight
        self._total = self._squat + self._bench + self._dl


class LiftersCollection:

    lines = [] #input from the file is temporarily stored here
    lifterNames = [] #record of all the lifter names for reference in double entries / printing

    def __init__(self, file):
        self._lifters = self.inputLifters(file)
        self._lifters.sort()

    def lifters(self):
        return self._lifters

    @classmethod
    def lifterNamesReturn(cls):
        return cls.lifterNames

    @classmethod
    def inputLifters(cls, file):

        lifters = []
        with open(file) as fileIn:
            fileIn.readline() #skips first line which is all titles
            lines = csv.reader(fileIn) #input all the data from the file into the temporary holding position
            for item in lines:
                # checking if there are entries in the respective categories, essentially ensuring conformity of variable types
                bodyweight = item[7]
                squat = item[13]
                bench = item[18]
                deadlift = item[23]
                total = item[24]
                if bodyweight == '':
                    bodyweight = 0
                if squat == '':
                    squat = 0
                if bench == '':
                    bench = 0
                if deadlift == '':
                    deadlift = 0
                if total == '':
                    total = 0
                bodyweight = float(bodyweight)
                squat = float(squat)
                bench = float(bench)
                deadlift = float(deadlift)
                total = float(total)
                if item[0] not in cls.lifterNames: #checks if the lifter already has an entry
                    lifters.append(Lifter(item[0], item[1], bodyweight, squat, bench, deadlift, total)) #adds object lifter to the list
                    # item[0] is name
                    # item[1] is gender
                    cls.lifterNames.append(item[0]) #adds name to future reference if there are double entries
                else:
                    p = cls.lifterNames.index(item[0])
                    if bodyweight > lifters[p].bodyWeight():
                        lifters[p].replace(bodyweight, "bodyweight")
                    if squat > lifters[p].squat():
                        lifters[p].replace(squat, "squat")
                    if bench > lifters[p].bench():
                        lifters[p].replace(bench, "bench")
                    if deadlift > lifters[p].deadLift():
                        lifters[p].replace(deadlift, "deadlift")
        return lifters

    def __len__(self):
        return len(self._lifters)

    def __getitem__(self, item):
        return self._lifters[item]

class Interface:

    @staticmethod
    def printHeader(headerLines):
        maxLength = 0
        for items in headerLines:
            if len(items) >= maxLength:
                maxLength = len(items)
        for items in headerLines:
            print(items.center(maxLength))
        print('-' * maxLength)

    @staticmethod
    def printMenu(menu):
        for items in menu:
            print("\t" + items)

    @staticmethod
    def getInput():
        return input("Enter the number of the function you wish to use: ")

    @staticmethod
    def inputErrorMessage():
        print("Sorry, that was an invalid input, please try again")

    @staticmethod
    def NameSearch():
        return input("Which lifter would you like to lookup today: ")

    @staticmethod
    def returnLifter(lifter):
        print('\nLIFTER DATACARD')
        print('-' * 30)
        print(f'Name: {lifter.name()}')
        print(f'Gender: {lifter.gender()}')
        print(f'Body Weight: {lifter.bodyWeight()}')
        print(f'Squat Record: {lifter.squat()}')
        print(f'Bench Record: {lifter.bench()}')
        print(f'Deadlift Record: {lifter.bench()}')
        print(f'Total Record: {lifter.total()}')

    @staticmethod
    def close():
        print('Thank You for Using LIFTERS COMPENDIUM 2019')

    @staticmethod
    def nonExistentLifter():
        print('This lifter does not exist')

    @staticmethod
    def gender():
        gender = input("Please enter the gender of lifter you are looking for as M for Male, F for Female, or B for Both: ").upper()
        while gender not in ["M", "F", "B"]:
            gender = input("Please enter their gender as M for Male, F for Female, or B for Both: ").upper()
        return gender

    @staticmethod
    def weight():
        weight = input("Please enter the weight range in kg of lifter that you are looking for in the format ##,##: ")
        weightRange = weight.split(',')
        check = False
        while not check:
            try:
                while not len(weightRange) == 2:
                    weight = input("Please enter the weight range in kg of lifter that you are looking for in the format ##,##: ")
                    weightRange = weight.split(',')
                weightRange[0] = float(weightRange[0])
                weightRange[1] = float(weightRange[1])
                check = True
            except ValueError:
                print("The given weight range was invalid, so weight has be excluded from this search")
                return [0, 999]
        return weightRange

    @staticmethod
    def liftWeight():
        weight = input("Please enter the weight range in kg of the lift you are looking for in the format ##,##: ")
        weightRange = weight.split(',')
        check = False
        while not check:
            try:
                while not len(weightRange) == 2:
                    weight = input("Please enter the weight range in kg of the lift you are looking for in the format ##,##: ")
                    weightRange = weight.split(',')
                weightRange[0] = float(weightRange[0])
                weightRange[1] = float(weightRange[1])
                check = True
            except ValueError:
                print("The given weight range was invalid, so no lifters have been returned")
                return [999, 999]
        return weightRange

    @staticmethod
    def liftersWeightReturn(lifters):
        print("The following lifters meet your specifications")
        for items in lifters:
            print(items.name())

    @staticmethod
    def getLiftType():
        choice = input("Please enter what type of lift you want to know about, S for Squat, B for Bench, D for Deadlift, and T for Total: ")
        while choice not in ["S", "B", "D", "T"]:
            choice = input("PLease enter what type of lift you want to know about, S for Squat, B for Bench, D for Deadlift, and T for Total: ")
        return choice

class Application:

    Header = ["LIFTERS COMPENDIUM 2019", "Based on a portion of data from https://www.kaggle.com/open-powerlifting/powerlifting-database", "Data accurate as of April 2019"]
    menu = ["\n Main Menu", "1. Lookup based on Name", "2. Lookup based on Body Weight & Gender", "3. Lookup based on Lifts", "4. Quit"]

    def __init__(self, data, interface):
        self._liftList = LiftersCollection(data) # where data is a filename of type csv
        self._interface = interface # where interface is an object of type Interface
        self._interface.printHeader(self.Header) #prints the headers
        self.Function()

    def Function(self):
        self._interface.printMenu(self.menu)
        userInput = self._interface.getInput()

        while userInput != '4':
            try:
                while int(userInput) > len(self.menu):
                    self._interface.inputErrorMessage()
                    userInput = self._interface.getInput()
            except ValueError:
                self._interface.inputErrorMessage()
            if userInput == '1':
                lifterName = self._interface.NameSearch()
                self.lifterLookupName(lifterName, self._liftList.lifters())
            elif userInput == '2':
                lifters = []
                gender = self._interface.gender()
                weight = self._interface.weight()
                for items in self._liftList:
                    if (items.gender() == gender or gender == "B") and int(weight[0]) <= items.bodyWeight() <= int(weight[1]):
                        lifters.append(items)
                lifters.sort()
                self._interface.liftersWeightReturn(lifters)
            elif userInput == '3':
                lifters = []
                lift = self._interface.getLiftType()
                weight = self._interface.liftWeight()
                if lift == "S":
                    for items in self._liftList:
                        if int(weight[0]) <= items.squat() <= int(weight[1]):
                            lifters.append(items)
                elif lift == "B":
                    for items in self._liftList:
                        if int(weight[0]) <= items.bench() <= int(weight[1]):
                            lifters.append(items)
                elif lift == "D":
                    for items in self._liftList:
                        if int(weight[0]) <= items.deadlift() <= int(weight[1]):
                            lifters.append(items)
                elif lift == "T":
                    for items in self._liftList:
                        if int(weight[0]) <= items.total() <= int(weight[1]):
                            lifters.append(items)
                lifters.sort()
                self._interface.liftersWeightReturn(lifters)
            self._interface.printMenu(self.menu)
            userInput = self._interface.getInput()
        self._interface.close()

    def lifterLookupName(self, name, LifterList):
        mid = math.floor(len(LifterList)/2)
        if len(LifterList) != 1:
            if name == LifterList[mid].name():
                self._interface.returnLifter(LifterList[mid])
                return None
            elif name <= LifterList[mid].name():
                self.lifterLookupName(name, LifterList[:mid])
            elif name >= LifterList[mid].name():
                self.lifterLookupName(name, LifterList[mid:])
        else:
            self._interface.nonExistentLifter()

interface = Interface()
application = Application("openpowerlifting.csv", interface)