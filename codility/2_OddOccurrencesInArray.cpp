#include <algorithm>


int solution(vector<int> &A) {
    int l = A.size();
    if (l==1) return A[0];
    std::sort(A.begin(), A.end());

    for (int i=0; i<l-1; i+=2)
        if (A[i] != A[i+1])
            return A[i];

    return A[l-1];
}
