#include <iostream>
#include <algorithm>

using namespace std;


bool ispalindrom(long n)
{
    bool b=true;
    if (n>=100000)
    {
        b&= (n/100000)==(n%10);
        n-=n/100000*100001;
        b&= (n/10000)==(n%100)/10;
        n-=n/10000*10010;
        b&= (n/1000)==(n%1000)/100;
    }
    else
    {
        b&= (n/10000)==(n%10);
        n-=n/10000*10001;
        b&= (n/1000)==(n%100)/10;

    }
    return b;

}

int main()
{
    long max=0;
    long tmp;
    for (long i=100; i<1000; i++)
        for(long j=100; j<1000; j++)
        {
            tmp=i*j;
            if (tmp>max && ispalindrom(tmp)) max=tmp;
        }
    cout << max << endl;
    return 0;
}

