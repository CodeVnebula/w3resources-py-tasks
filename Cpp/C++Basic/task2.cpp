/*
2. Write a program in C++ to print the sum of two numbers. 
Sample Output:
Print the sum of two numbers : 
----------------------------------- 
The sum of 29 and 30 is : 59

Link: https://www.w3resource.com/cpp-exercises/basic/cpp-basic-exercise-2.php
*/

// Solution

#include <iostream>
using namespace std;

int main()
{
    int num1, num2;
    cout << "Print the sum of two numbers :" << endl;
    cout << "Enter num1: "; cin >> num1; 
    cout << "Enter num2: "; cin >> num2;
    cout << "The sum of " << num1 << " and " << num2 << " is : " << num1 + num2;

    return 0;
}
