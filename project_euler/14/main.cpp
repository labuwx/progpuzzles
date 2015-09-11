#include <iostream>
#include <map>

using namespace std;

map<unsigned long, unsigned long>  lenm;
unsigned long len(unsigned long n)
{
    unsigned long tmp;

    if (lenm.count(n)>0) tmp=lenm[n];
    else
    {

        tmp=n%2==0 ? len(n/2)+1 : len(3*n+1)+1;
        lenm[n]=tmp;
    }


    return tmp;

}


int main()
{
    lenm[1]=1;
    lenm[2]=2;
    lenm[4]=3;
    unsigned long mx=1;
    for(unsigned long i=500000+1;i<=1000000; i++)
    {
        if (len(i)>len(mx)) mx=i;

    }
    cout << mx << endl;
    return 0;
}

