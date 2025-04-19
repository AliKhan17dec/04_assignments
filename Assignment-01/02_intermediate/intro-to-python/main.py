# Planet gravity multipliers
Mercury = 0.376
Venus = 0.889
Mars = 0.378
Jupiter = 2.36
Saturn = 1.081
Uranus = 0.815
Neptune = 1.14

# User input
earth = float(input("Enter a weight on Earth: "))
planet = input("Enter the planet you want to convert to: ").capitalize()

def cal():
    if planet == "Mercury":
        print(earth * Mercury)
    elif planet == "Venus":
        print(earth * Venus)
    elif planet == "Mars":
        print(earth * Mars)
    elif planet == "Jupiter":
        print(earth * Jupiter)
    elif planet == "Saturn":
        print(earth * Saturn)
    elif planet == "Uranus":
        print(earth * Uranus)
    elif planet == "Neptune":
        print(earth * Neptune)
    else:
        print("Invalid planet name.")

# Call the function
cal()
