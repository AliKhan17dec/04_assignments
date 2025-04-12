def main():
    fahrenheit = float(input("\033[1;3m Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {fahrenheit}F = {celsius:.2f}C")

if __name__ == "__main__":
    main()
