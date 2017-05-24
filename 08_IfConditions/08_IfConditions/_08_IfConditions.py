#If Statement with String

player=input("What is your favorite footboll palyer name?\n");
player1="Messi";
if player.upper()==player1.upper():
    print("King of Football");
    print("He is a famous person in the world");   
print("You cann't watch football");


#If with Numbers
deposit=float(input("How much do you want to deposit?\n"));   #input always string nput ney
if deposit>100:
     print("Enjoy your toaster!");
print("Have a nice day!"); 




deposit=input("How much do you want to deposit?\n");   #input always string nput ney
if float(deposit)>100:
     print("Enjoy your toaster!");
else:
     print("Enjoy your MUG!");
print("Have a nice day!"); 



freeToaster=False;
deposit=float(input("How much do you want to deposit?\n"));   #input always string nput ney
if deposit>100:
    freeToaster=True;
else:
     print("Enjoy your MUG!");

if freeToaster:
    print("Enjoy your toaster!");
print("Have a nice day!"); 