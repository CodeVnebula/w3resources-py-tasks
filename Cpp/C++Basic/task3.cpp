/*
3. Write a in C++ program to find the size of fundamental data types. 
Sample Output:
Find Size of fundamental data types : 
------------------------------------------ 
The sizeof(char) is : 1 bytes 
The sizeof(short) is : 2 bytes
The sizeof(int) is : 4 bytes 
The sizeof(long) is : 8 bytes 
The sizeof(long long) is : 8 bytes 
The sizeof(float) is : 4 bytes 
The sizeof(double) is : 8 bytes 
The sizeof(long double) is : 16 bytes 
The sizeof(bool) is : 1 bytes 

Link: https://www.w3resource.com/cpp-exercises/basic/cpp-basic-exercise-3.php
*/

// Solution

#include <iostream>
using namespace std;

int main()
{
    cout << "Find Size of fundamental data types : \n\n";
    cout << "The sizeof(char) is :" << sizeof(char) << endl;    
    cout << "The sizeof(short) is :" << sizeof(short) << endl;
    cout << "The sizeof(int) is : " << sizeof(int) << endl;
    cout << "The sizeof(long) is :" << sizeof(long) << endl;
    cout << "The sizeof(long long) is :" << sizeof(long long) << endl;
    cout << "The sizeof(float) is :" << sizeof(float) << endl;
    cout << "The sizeof(double) is :" << sizeof(double) << endl;
    cout << "The sizeof(long double) is :" << sizeof(long double) << endl;
    cout << "The sizeof(bool) is :"  << sizeof(bool) << endl << endl;   

    return 0;
}
