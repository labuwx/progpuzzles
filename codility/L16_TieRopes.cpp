int solution(int K, vector<int> &A) {
    int clen = 0, ropecnt = 0;
    for (auto l: A) {
        clen += l;
        if (clen >= K) {
            ropecnt++;
            clen = 0;
        }
    }

    return ropecnt;
}
