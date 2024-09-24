# Kerry Sowers
length_1 = int(input("Enter the length of the first side: "))
length_2 = int(input("Enter the length of the second side: "))
length_3 = int(input("Enter the length of the third side: "))

if length_1 == length_2 == length_3:
    print("Equilateral")
elif length_1 == length_2 or length_1 == length_3 or length_2 == length_3:
    print("Equilateral")
elif length_1 != length_2 != length_3:
    print("Scalene")
else:
    print("what")
