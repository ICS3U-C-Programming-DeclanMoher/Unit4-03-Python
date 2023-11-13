#!/usr/bin/env python3
# Created by: Declan.Moher
# Created on: Nov. 10, 2023
# This program checks powers of two of user_number


def main():
    # asks user
    user_number_str = input("Enter a positive number")
    try:
        # trying to put into a string
        user_number = int(user_number_str)
    except ValueError:
        print("Invalid Input")
    else:
        # telling user_number that its going to add one
        for counter in range(user_number + 1):
            # user_number to the power of two
            num_power = counter**2
            # printing final code
            print(f"{counter}^2: {num_power}")


if __name__ == "__main__":
    main()
