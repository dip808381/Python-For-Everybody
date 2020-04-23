hrs = input("Enter Hours:")
tms = input("Enter Rate Per Hour:")
try:
    h = float(hrs)
    t = float(tms)
except :
    print("Error, please input numeric value")
    quit()
if h > 40:
    print(40*t + (h - 40)*t*1.5)
else:
    print(40*t)
