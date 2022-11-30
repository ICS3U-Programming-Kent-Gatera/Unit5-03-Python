#!/usr/bin/env python3
# Created By: Kent Gatera
# Date: 10.26.22
# This program calculates the mean mark of a level


def calcMark(mark_level):
    match (mark_level):
        case "4+":
            return "97.5%"
        case "4":
            return "90.5%"
        case "4-":
            return "83%"
        case "3+":
            return "78%"
        case "3":
            return "74.5%"
        case "3-":
            return "71%"
        case "2+":
            return "68%"
        case "2":
            return "64.5%"
        case "2-":
            return "61%"
        case "1+":
            return "58%"
        case "1":
            return "54.5%"
        case "1-":
            return "51%"
        case "R":
            return "below 50%"
        case _:
            return "-1"


def main():
    user_level = str(input("What is your grade?: "))
    mean_percentage = calcMark(user_level)
    if mean_percentage == "-1":
        print("Please enter a valid level.")
    else:
        print(f"The middle mark of {user_level} is {mean_percentage}")


if __name__ == "__main__":
    main()
