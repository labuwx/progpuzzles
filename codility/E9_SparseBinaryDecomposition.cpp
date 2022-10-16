int solution(int N) {
    int a = 0, b = 0;

    for (int i = 0; N > 0; i++) {
        int v = ((N & 1) << i);
        if (i % 2)
            a |= v;
        else
            b |= v;
        N >>= 1;
    }

    return a;
}
