#include <iostream>

using namespace std;

int main()
{
    float a;
    float b;
    float c;
    
    cout << "Wprowadź a";
    cin >> a;
    cout << "Wprowadź b";
    cin >> b;
    
    if(b==0||b==-0)
    {
        cout << "Nie dziel przez 0";
        return 0;
    }
    
    c = a/b;
    
    cout << a << " dzielone na " << b << " to " << c;
    return c;
}
