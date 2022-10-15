int solution(string &S) {
    int n = S.size();
    if (n % 2 == 0)
        return -1;

    int l = 0;
    for (; l < n / 2; l++) {
        int r = n - 1 - l;
        if (S[l] != S[r])
            return -1;
    }

    return l;
}
