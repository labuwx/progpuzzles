int solution(vector<int> &A, vector<int> &B) {
    int N = A.size();
    int segcnt = 0, covered_to = -1;

    for (int i=0; i<N; i++) {
        if (A[i] > covered_to) {
            covered_to = B[i];
            segcnt++;
        }
    }

    return segcnt;
}
