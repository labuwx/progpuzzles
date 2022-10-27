int solution(vector<int> &A) {
    int N = A.size();
    vector<bool> seen(N + 1);

    for (auto k: A) {
        if (1 <= k && k <= N+1)
            seen[k-1] = true;
    }

    for (int k = 1; k <= N+1; k++) {
        if (!seen[k-1])
            return k;
    }
}
