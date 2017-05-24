#Working nested if with String
city=input("What do you live in City?\n").upper();
if city=="CHITTAGONG":
    print("This is the port city in Bangladesh\n");
elif city=="DHAKA":
    print("Dhaka is the capital of Bangladesh\n");
elif city=="RAJSHAHI":
    print("Largest City in Bangladesh");
else:
    print("ISN'T CITY in Bangladesh");


#WOrking nested if with numbers
mark=float(input("Enter your Result Mark?\n"));
if mark>=0and mark<=32:
    print("You are Failed's!");
elif  mark>=33and mark<=45:
     print("Gotted a B+ Grads Result!\n");
elif  mark>=46and mark<=59:
     print("Gotted a A- Grads Result!\n");
elif  mark>=60and mark<=79:
     print("Gotted a A Grads Result!\n");
elif  mark>=80and mark<=100:
     print("Gotted a A+ Grads Result!\n");
else :
    print("Invalid Marks")