import sys;
import Calculator;
aNumber=float(input("Enter First Number "));
twoNumber=float(input("Enter Two Number "));


try:
    #result=aNumber/twoNumber;
    #print("Divided Result:  "+str(result));

    add=Calculator.addFunction(aNumber,twoNumber);
    substract=Calculator.substractFunction(aNumber,twoNumber);
    multiply=Calculator.multiplyFunction(aNumber,twoNumber);
    divide=Calculator.divideFunction(aNumber,twoNumber);

    print("Add Result:  "+str(add));
    print("Substract Result:  "+str(substract));
    print("Multiply Result:  "+str(multiply));
    print("Division Result:  "+str(divide));
         
except ZeroDivisionError:
     print("Zero division Error")
except:
    error=sys.exc_info()[0];
    print(error)
finally:
    print("Finally Keyword");




