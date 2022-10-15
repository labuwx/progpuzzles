vector<int> solution(vector<int> &A, int K) {
    int l = A.size();
    if (!l) return A;

    for (int n = 0; n < K; n++) {
        int end = A[l-1];
        for (int i = l-1; i >= 1; i--) {
            A[i] = A[i-1];
        }
        A[0] = end;
    }

    return A;
}
