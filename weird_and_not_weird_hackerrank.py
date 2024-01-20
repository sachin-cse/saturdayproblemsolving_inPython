n = int(input('Enter the value'))

if n % 2 != 0 or (n % 2 ==0 and n in range(6,21)):
    print("Weird")
elif n % 2 == 0 and ( n > 20  or n in range(2,6)):
    print("Not Weird")