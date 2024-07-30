year_input = input()
year = int(year_input)
is_MultFour = year%4
is_MultHundred = year%100
is_MultFourHundred = year%400

if((is_MultFour == 0 and is_MultHundred != 0) or is_MultFourHundred == 0):
    print(1)
else:
    print(0)