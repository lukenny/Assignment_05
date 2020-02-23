#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Kenny Lu, 2020-Feb-21, Initial commit
#------------------------------------------#

# Declare variables

strChoice = '' # User input
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
lstObject = []

# Get user Input
print('---The Magic CD Inventory---\n')
while True:
    # Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        print("Goodbye, thank you for using Magic CD Inventory.") 
        break
    if strChoice == 'l':
        # Add the functionality of loading existing data
        fileName = input('Enter the filename of existing data: ')
        existingData = open(fileName, "r+")
        for line in existingData.readlines():
            line_split = line.strip().split(",")
            dicRow = {"ID":line_split[0], "Title":line_split[1], "Artist":line_split[2]}
            lstObject.append(dicRow) 
            print(str(line_split).replace("'", "")[1:-1], "added to the inventory." '\n')                               
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {"ID":strID, "Title":strTitle, "Artist":strArtist}
        lstObject.append(dicRow)
        print(lstObject, "added to the inventory.")
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstObject:
            print(*row.values(), sep = ', ')
            print("")
    elif strChoice == 'd':
        # Add functionality of deleting an entry
        if len(lstObject) != 0: 
            count = 0 
            for i in lstObject:
                print("(",count,")", i, sep='')
                count += 1    
            deleteEntry = int(input('\n' + "Which entry would you like to delete? " '\n'))
            lstObject.pop(deleteEntry)
            print("Entry #:", deleteEntry, "deleted")
            pass
        else:
            print("Sorry nothing to delete empty inventory." '\n')
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstObject:
            objFile.write(str(row['ID'] + "," + row['Title'] + "," + row['Artist'] + '\n'))
        objFile.close()
        print("File saved to CDInventory.txt." '\n')
    else:
        print('Please choose either l, a, i, d, s or x!')
