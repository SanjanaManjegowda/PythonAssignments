NoOfTerms= 50  #For User Input int(input("Enter Number of Values Required In Sequence"))
Num1=1         #First Value
Num2=1         #Second Value
counter=0
EvenNum=0      #Counter  for Printing only First 12 Even Fibonacci Series
if NoOfTerms<=0:
    print("Enter a Positive Number ")
elif NoOfTerms == 1:
    print("Fibbonacci Sequence",NoOfTerms)
else:
    print("Fibonacci Series:")
    while counter < NoOfTerms:
        if Num1%2==0 :
            if EvenNum!= 12:   
              print(Num1)
              EvenNum +=1
        lastVal=Num1+Num2
        #updating Next Value
        Num1=Num2
        Num2=lastVal
        counter +=  1

         

              
