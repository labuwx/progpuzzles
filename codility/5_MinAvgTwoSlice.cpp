#include <limits>

int solution(vector<int> &A) {
    int N = A.size();
    vector<int> psum(N+1);
    for (int i=0; i<N; i++)
        psum[i+1] = psum[i] + A[i];

    int sp;
    double minavg = numeric_limits<double>::max();
    for (int i=0; i < N-1; i++)
        for (int j=i+1; j < N; j++) {
            int ssum = psum[j+1] - psum[i];
            double avg = (double)ssum / (double)(j-i+1);
            if (avg < minavg) {
                sp = i;
                minavg = avg;
            }
        }

    return sp;
}
