/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int pole_kwadratu(int a)
{
    int b;
    b = a*a;
    return b;
}

int obwod_kwadratu(int a)
{
    int c;
    c = a*4;
    return c;
}


int main()
{
    int a;
    cout << "podaj bok kwadratu";
    cin >> a;
    cout << "Obwód = ";
    cout << obwod_kwadratu(a)  << "\n";
    cout << "Pole = ";
    cout << pole_kwadratu(a);
}
