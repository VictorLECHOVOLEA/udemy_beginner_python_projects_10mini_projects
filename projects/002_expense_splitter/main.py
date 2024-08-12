
# 1. Create the function
def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    # 2. Validate the amount of people
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than one.')

    # 3. Perform the calculation
    share_per_person: float = total_amount / number_of_people

    # 4. Format the results and display them
    print(f'Total expense: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')
    print(f'Each person should pay: {currency}{share_per_person:,.2f}')


# 5. Create a main entry point
def main() -> None:
    # 6. Try to get the user input and perform the calculation
    try:
        total_amount: float = float(input('Enter the total amount of the expense: '))
        number_of_people: int = int(input('Enter the number of people sharing the expense: '))

        # Call the function to calculate and display expenses
        calculate_split(total_amount, number_of_people, currency='€')

    except ValueError as e:
        print(f'Error: {e}')


# 7. Run the script
if __name__ == '__main__':
    main()


"""
Homework:
1. Edit the script to give the user the option to enter uneven splits, such as 20%, 40%, 40%.
2. Make it so that if the user encounters an error, the program nicely asks them to try again with
a proper value.

"""


"""
Enter the number of people sharing the expense: 3
Total expense: €120.00
Number of people: 3
Each person should pay: €40.00


Enter the total amount of the expense: 1
Enter the number of people sharing the expense: 1
Total expense: €1.00
Number of people: 1
Each person should pay: €1.00

Enter the total amount of the expense: 3
Enter the number of people sharing the expense: 2
Total expense: €3.00
Number of people: 2
Each person should pay: €1.50
"""

"""
improvements:
A short description of the program at the beginning
"""