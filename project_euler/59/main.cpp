#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{

    ifstream inf("../59/cipher1.txt");
    vector<char> str;

    int c;
    while(!inf.eof())
    {
        inf >> c;
        str.push_back((char)c);
    }
    inf.close();
    vector<char> key(3);
    vector<char> tmp(str.size());
    key[0]='g';
    key[1]='g';
    key[2]='a';
    bool b;
    for (char x='a'; x<='z'; x++)
        for (char y='a'; y<='z'; y++)
            for (char z='a'; z<='z'; z++)
        {

            key[0]=x;
            key[1]=y;
            key[2]=z;
            b=true;
            for (int i=0; i<str.size() && b; i++)
            {
                tmp[i]=str[i] ^ key[i%3];
                b&= (' '<=tmp[i] && tmp[i]<='z') || ('a'<=tmp[i] && tmp[i]<='z') || ('A'<=tmp[i] && tmp[i]<='Z');
            }
            if (b)
            {
                cout<<"*******************"<<x<<" "<<y<<" "<<z<<endl;
                for (int i=0; i<40; i++)
                    cout<<tmp[i];
                cout << endl;
            }
        }
    key[0]='g';
    key[1]='o';
    key[2]='d';
    unsigned long sum=0;
    for (int i=0; i<str.size(); i++)
    {
        tmp[i]=str[i] ^ key[i%3];
        sum+=tmp[i];
    }
    cout <<endl << endl;

    for (int i=0; i<tmp.size(); i++)
        cout<<tmp[i];
    cout <<endl << endl;
    cout<<sum-'&'<<endl;


    return 0;
}

