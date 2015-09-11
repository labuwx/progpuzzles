#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<unsigned int> n(300);
    n[0]=1;
    int s=1;
    unsigned int carry;
    for (unsigned int i=1; i<=100; i++)
    {
        carry=0;
        for (int j=0; j<s; j++)
        {
            carry+=i*n[j];
            n[j]=carry%10;
            carry/=10;
        }
        while(carry!=0)
        {
            n[s]=carry%10;
            carry/=10;
            s++;
        }
    }

    unsigned long sum=0;
    for (int j=0; j<s; j++) sum+=n[j];
    cout << sum << endl;
    return 0;
}

