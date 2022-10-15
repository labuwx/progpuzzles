#include <climits>


long long f(vector<int> &A, int k) {
    if (k < 0)
        return ((long long)INT_MIN)-3;
    else if (k >= A.size())
        return ((long long)INT_MAX)+3;
    else
        return A[k];
}


int solution(vector<int> &A) {
    int N = A.size();
    int c = 0, r=0;
    while (f(A, r) < 0) r++;
    int l = r-1;

    long long cabs = 0;
    if (f(A, r) == 0) c++;

    while (0 <= l || r <= N-1) {
        long long nabs = min(-f(A, l), f(A, r));
        if (nabs > cabs) {
            c++;
            cabs = nabs;
        }
        if (-f(A, l) <= cabs)
            l--;
        else if (f(A, r) <= cabs)
            r++;
    }

    return c;
}
