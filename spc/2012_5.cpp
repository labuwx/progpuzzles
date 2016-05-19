#include <pphelp.h>


num F(num n, num k, num s) {
    num e1, e2, e3, v, m;
    num sum = 0;
    numvec xs(k);
    for(num ni=0; ni < n; ni++) {
        e1 = s + ni*701;
        e2 = 1237;
        e3 = 345892;
        for (num &x: xs) {
            x = e1;
            v = (31*e1 + 103*e2 + 7*e3 + 500003) % 1000001;
            e1 = e2;
            e2 = e3;
            e3 = v;
        }
        m = median(xs);
        sum += m;
    }
    return sum;
}


int main() {
    cout << F(3, 5, 1000) << endl;
    cout << F(5, 11, 3333) << endl;
    cout << F(10, 1000001, 444) << endl;
    cout << F(1000, 1000001, 555) << endl;
    cout << F(200, 10000001, 666) << endl;
    cout << F(50, 50000001, 777) << endl;
}
