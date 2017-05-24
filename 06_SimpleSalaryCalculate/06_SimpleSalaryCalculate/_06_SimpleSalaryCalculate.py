basicSalary=input("Enter Your Salary Amount?\n");
percentageSalary=input("Eeter Your Bonus percentage?\n");    #jai input neya hok na keno shob string hishabe nibe data so pore convert korte hobe

bonusSalary=float(basicSalary)*float(percentageSalary)/100;

netSalary=float(basicSalary)+(bonusSalary);
string=str(netSalary)   #Convert to String from float
print("Your Net Salary ="+string)
print("Your Net Salary = {}".format(netSalary))   #Formated float data
