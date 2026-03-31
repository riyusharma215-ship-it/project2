def main():
    print("Welcome to the Pattern Generator and Number Analyzer!")
    while True:
        print("\nSelect an option:")
        print("1. Generate a Pattern")
        print("2. Analyze a Range of Numbers")
        print("3. Exit")   
        choice = input("Enter your choice: ")
        if choice == '1':
            row_input = input("Enter the number of rows for the pattern: ")
            
        
            if not row_input.isdigit():
                print("Error: Please enter a valid positive integer.")
                continue
                
            rows = int(row_input)
            
            if rows <= 0:
                print("Error: Row count must be positive.")
                break 
            
            print("\nPattern:")
            for i in range(1, rows + 1):
                # Inner loop for columns (stars)
                for j in range(1, i + 1):
                    print("*", end="")
                print()       

        elif choice == '2':
            start_input = input("Enter the start of the range: ")
            end_input = input("Enter the end of the range: ")

            # Validation: checking if both are digits (handles positive integers)
            if not (start_input.isdigit() and end_input.isdigit()):
                print("Error: Please enter valid numbers.")
                continue

            start = int(start_input)
            end = int(end_input)

            if end < start:
                print("Error: The end of the range must be greater than the start.")
                continue

            total_sum = 0
            for num in range(start, end + 1):
                # Odd or Even check
                if num % 2 == 0:
                    print(f"Number {num} is Even")
                else:
                    print(f"Number {num} is Odd")
                if num == 0:
                    pass
                
                total_sum += num
            
            print(f"Sum of all numbers from {start} to {end} is: {total_sum}") 
        elif choice == '3':
            print("Thank you ! Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()   