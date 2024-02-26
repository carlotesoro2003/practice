year = int(input("Enter year: "))


if(year % 400 == 0) and (year % 100 == 0):  #if year divisible by 400 and 100
    print(year, "is a leap year")

elif(year % 4 == 0) and(year % 100 != 0): #year divisble by 4 but not 100
    print(year, "is a leap year")

else:
    print(year, "is not a leap year")
