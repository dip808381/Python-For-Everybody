hrs = input("Enter Hours:")
h = float(hrs)
tms = input("Enter Rate Per Hour:")
t = float(tms)
if h > 40:
    print(40*t + (h - 40)*t*1.5)
else:
    print(40*t)
