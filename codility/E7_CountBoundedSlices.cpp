#include <climits>


int solution(int K, vector<int> &A) {
    int l = A.size();
    int c = 0;
    for (int i = 0; i < l; i++) {
        int m = INT_MAX, M = INT_MIN;
        for (int j = i; j < l; j++) {
            m = min(m, A[j]);
            M = max(M, A[j]);
            if (M - m <= K)
                c++;
            else
                break;
        }
        if (c > 1'000'000'000)
            return -1;
    }

    return c;
}
