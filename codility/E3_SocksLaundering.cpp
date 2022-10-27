#define CMAX 50


int solution(int K, vector<int> &C, vector<int> &D) {
    vector<int> cc(CMAX), dc(CMAX);
    int pc = 0;

    for (int x: C)
        cc[x - 1]++;
    for (int x: D)
        dc[x - 1]++;

    for (int x = 0; x < CMAX; x++) {
        pc += cc[x] / 2;
        cc[x] %= 2;

        if (cc[x] && dc[x] && K) {
            cc[x]--;
            dc[x]--;
            K--;
            pc++;
        }
    }

    for (int x = 0; x < CMAX && 1 < K; x++) {
        int t = min(K, dc[x]) / 2;
        pc += t;
        K -= 2 * t;
        dc[x] -= 2 * t;
    }

    return pc;
}
