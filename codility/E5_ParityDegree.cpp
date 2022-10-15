int solution(int N) {
    int k = 0;
    for (int i = 1; (1 << i) <= N; i++)
        if (N % (1 << i) == 0)
            k = i;
    return k;
}
