int solution(vector<int> &A) {
    int N = A.size();
    vector<bool> seen(N);

    for (auto x: A)
        if (1 <= x && x <= N)
            seen[x-1] = true;

    for (int i =0; i < N; i++)
        if (!seen[i])
            return i+1;

    return N+1;
}
