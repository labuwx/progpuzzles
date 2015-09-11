#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main() {
  map<int, int> sols = map<int, int>();
  for (int a = 1; a < 500; ++a)
    for (int b = a; b < 1000; ++b) {
      int cs = a*a + b*b;
      int c = 0;
      while (c*c < cs) ++c;
      if ((c*c == cs) && (a + b + c <= 1000)) {
        cout << a << " " << b << " " << c << " " << a+b+c << endl;
        ++sols[a+b+c]; 
      }
    }

  int mxi = 0;
  int mxv = 0;

  for (int i = 0; i <=1000; ++i)
    if (sols[i] > mxv) {
      mxv = sols[i];
      mxi = i;
    }

  cout << mxv << " " << mxi << endl;

  return 0;
}
