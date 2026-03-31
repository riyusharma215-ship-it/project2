# Pattern Generator and Number Analyzer

This Python application provides a simple command-line interface for generating visual patterns and performing basic numerical analysis on a user-defined range of integers.

---

## ## Features

The program offers three main functionalities accessible through a menu-driven system:

* **Generate a Pattern**: Creates a right-angled triangle pattern of asterisks (`*`) based on the number of rows specified by the user.
* **Analyze a Range of Numbers**: Iterates through a specified range of numbers to determine if each is **even** or **odd**, then calculates the **total sum** of the range.
* **Input Validation**: Includes checks to ensure users enter valid positive integers for patterns and logical ranges for numerical analysis.

---

## ## How to Use

### ### Prerequisites
* **Python 3.x** installed on your system.

### ### Running the Program
1.  Open your terminal or command prompt.
2.  Navigate to the directory containing `PRO2,py.py`.
3.  Run the script using the following command:
    `python "PRO2,py.py"`

### ### Navigation
Upon launching, follow the on-screen prompts:
* **Option 1**: Enter a positive integer to define the height of the star pattern.
* **Option 2**: Enter a start and end value. The program will list the parity of each number and the final sum.
* **Option 3**: Safely exit the application.

---

## ## Logic Overview

* **Pattern Generation**: Uses nested `for` loops where the outer loop handles rows and the inner loop handles the number of stars per row.
* **Number Analysis**: Utilizes the modulo operator (`num % 2 == 0`) to distinguish between even and odd numbers.
* **Error Handling**: The program uses `.isdigit()` to prevent crashes from non-numeric input and ensures the end of a range is not smaller than the start.


https://drive.google.com/file/d/1RRPwB7pwPxNdqeZNRUITNEpd_l8pTKQU/view?usp=drive_link
