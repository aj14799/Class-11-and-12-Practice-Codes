side_a = float(input("Enter side1:"))
side_b = float(input("Enter side2:"))
side_c = float(input("Enter side3:"))
s = (side_a+side_b+side_c)/2
area = (s*(s-side_a)*(s-side_b)*(s-side_c))**1/2
print(area)
