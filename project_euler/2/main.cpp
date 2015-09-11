#include <iostream>

using namespace std;

int main()
{
    long s=0;
    long f1, f2;
    f1=1;
    f2=1;
    while(f2<=4000000)
    {
        f2=f1+f2;
        f1=f2-f1;
        if (f2%2==0) s+=f2;

    }
    cout << s << endl;
    return 0;
}

