#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int p=0;
    double c;
    for (int a=1; a<1000 && p==0; a++)
        for(int b=a; b<1000 && p==0; b++)
        {
            c=sqrt(a*a+b*b);
            if ((double)a+(double)b+c==1000) p=(int)(a*b*c);
        }
    cout << p << endl;
    return 0;
}

