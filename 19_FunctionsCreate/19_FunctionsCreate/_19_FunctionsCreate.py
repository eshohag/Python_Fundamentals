#def printFunctions():
#    print("Helo World");
#    return;
#printFunctions();

#def main():
#    printFunctions();
#    return;

#def printFunctions():
#    print("Helo World");
#    return;
#main()


#def main():
#    nameList=["Shohag","Arif","Mamun"];
#    #printName(nameList)
#    name=input("ENter your append Name here\n")
#    nameList.append(name);
#    printName(nameList)
#    return;

#def printName(nameList):
#    for name in nameList:
#        print(name)
#    return;


#def main():
#    nameList=["Shohag","Arif","Mamun"];
#    #printName(nameList)
#    name="";
#    while name !="Done":
#        name=input("ENter your append Name here, If you not append then write Done:\n");
#        if name !="Done":
#            nameList.append(name);
        
#    print("Your Listed Name below\n");
#    printName(nameList);   #Print Name Methods here...
#    return;

#def printName(nameList):
#    nameList.sort();
#    nameList.reverse();
#    for name in nameList:
#        print(name)
#    return;

#main();



#def main():
#    nameList=getNames(); 
#    return  printName(nameList);

#def printName(nameList):
#    nameList.sort();
#    nameList.reverse();
#    for name in nameList:
#        print(name)
#    return;

#def getNames():
#    nameList=["Shohag","Arif","Mamun"];
#    name="";
#    while name !="Done":
#        name=input("ENter your append Name here, If you not append then write Done:\n");
#        if name !="Done":
#            nameList.append(name);
        
#    print("Your Listed Name below\n");
#    return nameList;

#main();




#def displayName(nameList):
#    nameList.sort();
#    nameList.reverse();
#    for name in nameList:
#        print(name)
#    return;

#def getNames():
#    nameList=["Shohag","Arif","Mamun"];
#    name="";
#    while name !="Done":
#        name=input("ENter your append Name here, If you not append then write Done:\n");
#        if name !="Done":
#            nameList.append(name);
        
#    print("Your Listed Name below\n");
#    return nameList;

##nameLists=getNames();
#displayName(getNames());



def displayName(nameList):
    nameList.sort();
    nameList.reverse();
    for name in nameList:       
        getNameWithMessage(name);
        return;

def getNames():
    nameList=["Shohag","Arif","Mamun"];
    name="";
    while name !="Done":
        name=input("ENter your append Name here, If you not append then write Done:\n");
        if name !="Done":
            nameList.append(name);
        
    print("Your Listed Name below\n");
    return nameList;

def getNameWithMessage(name):
    return print("Hello "+name+" ");

displayName(getNames());