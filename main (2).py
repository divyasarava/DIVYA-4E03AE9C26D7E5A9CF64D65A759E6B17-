def leapyear(year):
  if(year%4==0 and year%100!=0)or year%400==0:
    print(year,"is a leap year")
  else:
    print(year,"is not a leap year")
   
x = int(input("Enter The Year:"))
y = leapyear(x)