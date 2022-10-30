int solution(int N) {
    int e = 1;
    while (e <= (N >> 1))
        e <<= 1;

    int cl=0, ml=0;
    while (e > 0) {
        if (e <= N) {
            ml = max(cl, ml);
            cl = 0;
            N -= e;
        }
        else
            cl += 1;
        e >>= 1;
    }

    return ml;
}
