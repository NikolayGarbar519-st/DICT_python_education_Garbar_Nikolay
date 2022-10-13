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
    print(i)
    i+=1
else:
    print(str(i)+"!")