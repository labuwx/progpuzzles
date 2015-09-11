#include <iostream>
#include <vector>


using namespace std;



int main()
{
    vector<unsigned int> n(1000);
    n[0]=1;
    int carry;
    int s=1;
    for (int i=0; i<1000; i++)
    {
        carry=0;
        for (int j=0; j<s; j++)
        {
            carry+=2*n[j];
            n[j]=carry%10;
            carry/=10;
        }
        if(carry!=0)
        {

            n[s]=carry%10;
            s++;

        }
    }
    unsigned long sum=0;
    for (int j=0; j<s; j++) sum+=n[j];
    cout << sum << endl;
    return 0;
}

