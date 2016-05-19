#include <algorithm>
#include <functional>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

typedef long long num;
typedef vector<num> numvec;

typedef double fnum;
typedef vector<fnum> fnumvec;


num spc_rand(num s, num n) {
    num e1, e2, e3, v;
    e1 = s;
    e2 = 1237;
    e3 = 345892;

    while (1 < n) {
        v = (31*e1 + 103*e2 + 7*e3 + 500003) % 1000001;
        e1 = e2;
        e2 = e3;
        e3 = v;
        --n;
    }

    return e1;
}


num median(numvec xs) {
    num len = xs.size();
    nth_element(xs.begin(), xs.begin() + len/2, xs.end());
    if (len % 2) {
        return xs[len/2];
    } else {
        nth_element(xs.begin(), xs.begin() + len/2 - 1, xs.end());
        return (xs[len/2 - 1] + xs[len/2]) / 2;
    }
}

