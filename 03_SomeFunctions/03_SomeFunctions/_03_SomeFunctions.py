message="Hello world";
print(message.find("o"));   #find the length position
print(message.count('o'))   #Count The Matching Latter
print(message.capitalize())   #First Latter must Capital That is the Capitalize
print(message.replace("Hello","Hi,Shohag Hello "))   #Text Replace
print(message.center(160))   #left position forword 160 pixel  
print("Original Text- "+message+ "\nLower Case Methods or Functions Use After- "+message.lower()+"\n")   #Lower Latter
print("Original Text- "+message+ "\nUpper Case Methods or Functions Use After- "+message.upper()) #Upper Latter

formatString="Here is the {} {} this is the {} \n"
print(formatString.format("format","function","python"))

formatStringWithPosition="Here is the {2} {1} this is the {0}"
print(formatStringWithPosition.format("format","function","python"))

titleString="Here is the title function"
print(titleString.title())
