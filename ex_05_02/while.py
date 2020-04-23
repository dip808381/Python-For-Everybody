num = 0
tot = 0.0
while True:
    val = input('Enter the Number: ')
    if val == 'done' :
        break
    try:
        val = float(val)
    except :
        print('Invalid Number')
    num = num + 1
    tot = tot + val
print(num, tot, tot/num)
