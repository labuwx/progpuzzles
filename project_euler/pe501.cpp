#include <iostream>

using namespace std;

typedef unsigned long long num;

num p10(num k) {
    num n = 1;
    while(k) {
        n *= 10;
        --k;
    }
    return n;
}

int main() {
    num p = p10(12);
    for (num i = 1; i <= p; ++i) {
        
    }
    return 0;
}