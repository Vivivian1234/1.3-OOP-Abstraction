from shapey import Circle, Rectangle, Square

def main():

    print("\nWelcome to Shapey.")

    while True:
        choice= input("Which shape would you like to calcualte?\n 1. Circle\n 2. Rectangle\n 3.Square\n")

        if choice == "1":
            radius = int(input("Enter circle radius: "))
            circle = Circle(radius)
            action = input("\nWhat could you like to calculate?\n 1. Area\n 2. Perimeter\n 3. Volume\n")
            if action == "1":
                print(f"Area: {circle.area():.2f}")
            elif action == "2":
                print(f"Perimeter: {circle.perimeter():.2f}")
            elif action == "3":
                print(f"Volume (Sphere): {circle.volume():.2f}\n")

        elif choice == "2":
            action = input("\nWhat could you like to calculate?\n 1. Area\n 2. Perimeter\n 3. Volume\n")
            if action == "1":
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                depth = 1
                rectangle = Rectangle(width, height, depth)
                print(f"Area: {rectangle.area():.2f}")
            elif action == "2":
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                depth = 1
                rectangle = Rectangle(width, height, depth)
                print(f"Perimeter: {rectangle.perimeter():.2f}")
            elif action == "3":
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                depth = int(input("Enter the depth of the rectangle (for volume): "))    
                rectangle = Rectangle(width, height, depth)
                print(f"Volume (Rectangular Prism): {rectangle.volume():.2f}\n")

        elif choice == "3":
            side = int(input("Enter side length: "))
            square = Square(side)
            action = input("\nWhat could you like to calculate?\n 1. Area\n 2. Perimeter\n 3. Volume\n")
            if action == "1":
                print(f"Area: {square.area():.2f}")
            elif action == "2":
                print(f"Perimeter: {square.perimeter():.2f}")
            elif action == "3":
                print(f"Volume (Square): {square.volume():.2f}\n")

        elif action == "4":
            print("\nThank you for using this program.\n")
            break
        else:
            print("\nInvalid input. Please try again.\n")

if __name__ == "__main__":
    main()
