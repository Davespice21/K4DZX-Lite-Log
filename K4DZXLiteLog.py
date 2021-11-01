# David Spicer k4DZX
# K4DZX Lite Radio Log V1.0 10/31/2021

# Class Order
class Log:
    def setCall(self, call):
        self.call = call

    def setFreq(self, freq):
        self.freq = freq

    def setTime(self, time):
        self.time = time

    def setNumber(self, number):
        self.number = number

    def setSignalStrength(self, signalstrength):
        self.signalstrength = signalstrength

    def getCall(self):
        return self.call

    def getFreq(self):
        return self.freq

    def getTime(self):
        return self.time

    def getNumber(self):
        return self.number

    def getSignalStrength(self):
        return self.signalstrength
print("""*****************************************K4DZX Lite Radio Log******************************************V1.0""")
event = input("Enter Event Name: ")
# Main Menu
def mainmenu():

    print("""*****************************************K4DZX Lite Radio Log******************************************V1.0""")
    print(event)
    print       ("""1.Add Contact, 2.Edit Contact, 3.Delete Contact, 4.Save Contact Log, 5.Exit the Program""")
    print("{:>2} {:>15} {:>20} {:>30} {:>25}".format("Log Number:", "Call Sign:", "Frequency:","Signal Strength:", "Time:"))
    for log in logs:
        print("{:>2} {:>20} {:>20} {:>25} {:>35}".format(log.number, log.call, log.freq, log.signalstrength, log.time))
    selection = int(input(":"))
    return selection


# Add Log
def addContact(logs):
    print("Selection 1 Add Contact: ")
    number = int(input("Enter New Log Number: "))
    callsign = input("Enter Call Sign: ")
    freq = str(input("Enter Frequency: "))
    time = int(input("Enter Time: "))
    ss = str(input("Enter Signal Strength: "))
    log = Log()
    log.setCall(callsign)
    log.setFreq(freq)
    log.setNumber(number)
    log.setTime(time)
    log.setSignalStrength(ss)
    logs.append(log)
    return logs


# Function to edit log
def editContact(logs):
    print("Selection 2 Edit Contact")
    global i
    number = int(input("Enter Contact number to edit: "))
    red_card = 0
    for i in range(len(logs)):
        if logs[i].number == number:
            red_card = 1
            break
    if red_card == 0:
        print("Contact not found")
        return logs

    callsign = input("Enter Call Sign: ")
    freq = str(input("Enter Frequency: "))
    time = int(input("Enter Time: "))
    ss = str(input("Enter Signal Strength: "))
    logs[i].call = callsign
    logs[i].freq = freq
    logs[i].time = time
    logs[i].signalstrength = ss
    return logs


# function to delete contact
def deleteContact(logs):
    print("Selection 3 Delete Contact: ")
    global i
    number = int(input("Enter contact number to delete: "))
    red_card = 0
    for i in range(len(logs)):
        if logs[i].number == number:
            red_card = 1
            break
    if red_card == 0:
        print("Contact not found")
    else:
        del logs[i]
        print("Contact", number, "Deleted!")
    return logs


# function to save contacts in a file
def saveContact(logs):
    print("Selection 4 Save Contact Log")
    with open("Contact Log.txt", "w") as file:
        file.write("{:>2} {:>15} {:>20} {:>30} {:>25}\n".format("Log Number:", "Call Sign:", "Frequency:","Signal Strength:", "Time:"))
        for log in logs:
            file.write("{:>2} {:>20} {:>20} {:>25} {:>35}\n".format(log.number, log.call, log.freq, log.signalstrength, log.time))
        print("Contacts saved to Contact Log.txt")
    return logs


# List
logs = []
# While loop
while True:
    try:
        print("\n")
        selection = mainmenu()
        if (selection == 1):
            logs = addContact(logs)
        elif (selection == 2):
            logs = editContact(logs)
        elif (selection == 3):
            logs = deleteContact(logs)
        elif (selection == 4):
            logs = saveContact(logs)
        elif (selection == 5):
            print("Exiting program have a nice day!")
            break
        else:
            print("Invalid Entry! Please enter a number from 1-4 or 5 to exit")
    except ValueError:
        print("Error Enter a Numeric Number!")
