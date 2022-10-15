#include <algorithm>


int leader(vector<int> &A) {
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


int solution(vector<int> &A) {
    int N = A.size();
    int ldri = leader(A);
    if (ldri == -1) return 0;
    int ldr = A[ldri];
    int ldr_cnt = 0;
    for (auto x: A) ldr_cnt += x == ldr;

    int eql = 0, left_ldr = 0;
    for (int i=0; i < N-1; i++) {
        if (A[i] == ldr) left_ldr++;
        if (2*left_ldr > (i+1) && 2*(ldr_cnt - left_ldr) > (N-1-i))
            eql++;
    }

    return eql;
}
