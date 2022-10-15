// !!! Nice problem

vector<int> solution(int N, vector<int> &A) {
    vector<int> cnts(N);
    vector<int> age(N);
    int noped = 0;
    int M = 0;

    int m = 0;
    for (auto op: A) {
        if (op <= N) {
            if (age[op-1] < noped) {
                cnts[op-1] = M;
                age[op-1] = noped;
            }
            m = max(m, ++cnts[op-1]);
        }
        else {
            noped += 1;
            M = m;
        }
    }

    for (int i=0; i < N; i++) {
        if (age[i] < noped)
            cnts[i] = M;
    }

    return cnts;
}

