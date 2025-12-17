import geometry

print("1. Area of circle")
print("2. Area of rectangle")
print("3. Area of both")

choice = int(input("Enter the choice (1 or 2 or 3): "))

if choice == 1:
    radius = float(input("Enter the radius of circle: "))
    area = geometry.area_of_circle(radius)
    print("Area of circle =", area)

elif choice == 2:
    length = float(input("Enter the length of rectangle: "))
    breadth = float(input("Enter the breadth of rectangle: "))
    area = geometry.area_of_rectangle(length, breadth)
    print("Area of rectangle =", area)

elif choice == 3:
    radius = float(input("Enter the radius of circle: "))
    circle_area = geometry.area_of_circle(radius)

    length = float(input("Enter the length of rectangle: "))
    breadth = float(input("Enter the breadth of rectangle: "))
    rectangle_area = geometry.area_of_rectangle(length, breadth)

    print("Area of circle =", circle_area)
    print("Area of rectangle =", rectangle_area)

else:
    print("Invalid choice")
