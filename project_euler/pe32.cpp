#include <iostream>
#include <set>
#include <vector>

using namespace std;

typedef unsigned long long num;
typedef vector<num> digitvector;

digitvector digits(unsigned int n) {
    auto dv = digitvector();
    
    while (n) {
        dv.push_back(n % 10);
        n /= 10;
    }
    
    return dv;
}

bool ispan(num a, num b, num c) {
    digitvector dv = digits(a);
    
    digitvector tdv;
    
    tdv = digits(b);
    dv.insert(dv.end(), tdv.begin(), tdv.end());

    tdv = digits(c);
    dv.insert(dv.end(), tdv.begin(), tdv.end());
    
    set<num> ds = set<num>(dv.begin(), dv.end());
    
    return (dv.size() == ds.size()) && (dv.size() == 9) && !ds.count(0);
}

num p10(num k) {
    num n = 1;
    
    for (num i = 0; i < k; ++i)
        n *= 10;
    
    return n;
}

int main() {
    
    set<num> ps = set<num>();
    
    for (num a = 1; a < p10(3); ++a)
        for (num b = a; b < p10(5); ++b)
            if (ispan(a, b, a * b)) {
                cout << a << " " << b << " " << a * b << endl;
                ps.insert(a * b);
            }
            
    num sum = 0;
    
    for (auto k: ps)
        sum += k;
            
    cout << endl << sum << endl;
    
    return 0;
}