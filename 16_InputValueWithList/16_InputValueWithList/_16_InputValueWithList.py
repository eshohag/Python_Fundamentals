person=[];
name=" ";
while name !="Done":
    name=input("Enter a Person Name (Quite this program Please Write Done)\n");
    if name !="Done":
        person.append(name);
    
print("Sorting List Name");
person.sort();
for aPerson in person:
    print(aPerson);



allNumber=[1,2,4,5,8,9,0,3];
allNumber.sort();
for number in allNumber:
    print(number);