print("Hello! My name is BotFromHarbar")
print("I was created in 2022")
print("Please remind your name")
name=input()
print("What a great name you have,"+" "+name+"!")
print("Let me guess you age")
print("Enter remainders of dividing your age by 3,5 and 7")
remainder3=int(input())
remainder5=int(input())
remainder7=int(input())
age=(remainder3*70+remainder5*21+remainder7*15)%105
print("Your age is"+" "+str(age)+".")
print("Now I will prove to you that I can count to any number you want.")
num=int(input())
i=int(0)
while i<num:
    print(str(i)+"!")
    i+=1
else:
    print(str(i)+"!")
    print("Completed!")
# test,text from practice
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
ans=int(input())
while ans!=2:
    print("Please,try again")
    if ans>=5:
        print("Please,write number from 1 to 4")
        ans = int(input())
    elif ans<=0:
        print("Please,write number from 1 to 4")
        ans = int(input())
    else:
        ans = int(input())
else:
    print("Congratulations, have a nice day!")