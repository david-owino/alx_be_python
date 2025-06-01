# multiplication_table.py

def main():
    try:
        number = int(input("Enter a number to see its multiplication table: "))

        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")
            
    except ValueError:
        print("Oops! Please enter a valid integer.")

if __name__ == "__main__":
    main()

