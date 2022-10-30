#include <algorithm>


int solution(vector<int> &A) {
    vector<int> B = A;
    int N = A.size();
    sort(begin(B), end(B));
    int cnt = 0;
    for (int i=0; i<N; i++) {
        if (cnt > 0 && B[i] == B[i-1])
            cnt++;
        else
            cnt = 1;

        if (2 * cnt > N)
            for (int j=0; j<N; j++)
                if (A[j] == B[i])
                    return j;
    }

    return -1;
}
