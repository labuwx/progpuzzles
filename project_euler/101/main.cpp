#include <iostream>
#include <vector>

using namespace std;

vector<int> subs(vector<int> p)
{
    vector<int> seq(11);
    int x,s,y;
    for(int i=0; i<11; i++)
    {
        x=i+1;
        s=0;
        y=1;
        for(unsigned int i=0; i<p.size(); i++)
        {
          s+=p[i]*y;
         y*=x;
        }
        seq[i]=s;
    }
    return seq;
}



vector<int> interpol(vector<int> seq, int n)
{
    vector<int> p(11);


    return p;

}


int main()
{
    vector<int> gen(11);
    for(unsigned int i=0; i<gen.size(); i++)
        gen[i] = i%2==0 ? 1 : -1;
    vector<int> seq;
    seq=subs(gen);

    int diff=0;
    vector<int> tp, ts;
    int k;
    for(unsigned int i=1; i<11; i++)
    {
        tp=interpol(seq, i);
        ts=subs(tp);
        k=i;
        while(ts[k]==seq[k]) k++;
        diff+=ts[k];


    }




    cout << diff << endl;
    return 0;
}

