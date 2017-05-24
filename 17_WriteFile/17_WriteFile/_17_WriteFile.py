fileName="Demo.txt";
#Write="w";
#file=open(fileName,mode=Write);

#Append="a";
#file=open(fileName,mode=Append);

#ReadWrite="w+";

#Write="w";
#file=open(fileName,mode=Write);
#file.write("Hi,There \n");
#file.write("How are You?");
#file.write("\nIIUC");
#file.close();



#Write="w";
#file=open(fileName,mode=Write);
#text=input("Enter Your Text here...\n");
#file.write(text);
#print("File Write Successfully");


Write="w";
file=open(fileName,mode=Write);
numberOfLine=int(input("How many Number of line you Write\n"));
for writeLine in range(numberOfLine): 
    lineNo=writeLine+1;
    text=input("Enter your Line No-"+str(lineNo)+"\n");
    file.write(text+"\n");

print("File Write Successfully");

