#include <iostream>

using namespace std;

typedef unsigned long long num;


int main() {


num N = 1000000000000;

num mod = 1000000000;

num min = mod;
num max = 0;


  for (num i=1; i<=N; ++i) {

          num val = ((i*123484321+1) % mod) + 1;
        if (val<min) min=val;
        if (max<val) max=val;

        if (i == 5 || i == 10000 || i == 100000000 || i==1000000000000)
                cout << i << " " << max - min << endl;

  }

}
