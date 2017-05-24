#counter=0;
#while counter<=10:
#    print(counter);
#    counter=counter+1;


counter=float(input("Starting Point\n"))
ending=float(input("Ending Point\n"))
while counter<=ending:
    print(counter);
    counter=counter+1; #Can't possible use counter++
                       #possible use counter+=1

answer=0;
while answer!=42:
    answer=float(input("What is the integer number?\n"))
print("Congratulations !  You are right.")