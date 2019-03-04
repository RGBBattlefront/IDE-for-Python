print("FileUtil : Installed")

#txt = open("DataFile.txt", "w+")
#txt.write("Background_Colour-(30,30,30).Dark_Colour-(0,0,0)")
#txt.close()


def changeVariableAdvanced(variable, change, DataSaveName):
    txt = open(DataSaveName + ".txt", "r")
    t = txt.readlines()[0].split(".")
    dataFile = t
    l = t
    for value in dataFile:
        data = value.split("-")
        
        if data[0] == variable:
            Index = dataFile.index(value) 
        

    print(Index)
    l.pop(Index)
    l.insert(Index, variable + "-" + change)
    string = ""
    for item in l:
        string += (item + ".")
    txt = open(DataSaveName + ".txt", "w")
    print(string[:-1])
    txt.write(string[:-1])
    txt.close()
    
def changeVariable(variable, change):
    txt = open("DataFile.txt", "r")
    t = txt.readlines()[0].split(".")
    dataFile = t
    l = t
    for value in dataFile:
        data = value.split("-")
        
        if data[0] == variable:
            Index = dataFile.index(value) #Its not finding it!
        

    print(Index)
    l.pop(Index)
    l.insert(Index, variable + "-" + change)
    string = ""
    for item in l:
        string += (item + ".")
    txt = open("DataFile.txt", "w")
    print(string[:-1])
    txt.write(string[:-1])
    txt.close()

def openVariable(variable):
    
    txt = open("DataFile.txt", "r")
    dataFile = (txt.readlines()[0]).split(".")
    txt.close()

    for value in dataFile:
        data = value.split("-")
        if data[0] == variable: return data[1]


        
    #that should work nice


def openVariableListItem(variable):
    
    txt = open("DataFile.txt", "r")
    dataFile = (txt.readlines()[0]).split(".")
    txt.close()

    for value in dataFile:
        data = value.split("-")
        if data[0] == variable: Data = data[1]

    DataListStringBased = Data.split(",")
    DataList = []

    for Eliment in range(len(DataListStringBased)):

        try:
           DataList.append(int(DataListStringBased[Eliment]))

        except:
            DataList.append(DataListStringBased[Eliment])

    return DataList



        
    #that should work nice
