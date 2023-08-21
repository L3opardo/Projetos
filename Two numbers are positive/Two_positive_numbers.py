def check_positive(a , b, c):
    positives = 0

    if a > 0:
        positives += 1
    if b > 0:
        positives += 1
    if c > 0:
        positives += 1

    if positives == 2:
        return True
    else: 
        return False


num1 = int(input('numero:'))
num2 = int(input('numero:'))
num3 = int(input('numero:'))

print(check_positive(num1, num2, num3))
