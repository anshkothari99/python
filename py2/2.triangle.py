side_1 = int(input("lenght of side 1: "))
side_2 = int(input("lenght of side 2: "))
side_3 = int(input("lenght of side 3: "))
s = (side_3 + side_2 + side_1) / 2
area = (s * (s - side_1) * (s - side_2) * (s - side_3))**(1/2)
area = round(area, 2)
print("Area of traingles with sides", side_1, side_2, side_3, "is", area)
