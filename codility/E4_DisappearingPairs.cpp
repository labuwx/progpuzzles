#include <vector>


string solution(string &S) {
    S = '<' + S + '>';
    int N = S.size();

    vector<int> next(N), prev(N);
    for (int i = 0; i < N; i++) {
        prev[i] = i-1;
        next[i] = i+1;
    }

    for (int i = 1; i < N; i = next[i]) {
        for (int j = prev[i]; 0 <= j; j = prev[j]) {
            if (S[i] == S[j]) {
                prev[next[i]] = prev[j];
                next[prev[j]] = next[i];
            }
            else
                break;
        }
    }

    string ss;
    for (int i = 0; i < N; i = next[i]) {
        auto c = S[i];
        if (c != '<' && c != '>')
            ss += c;
    }

    return ss;
}
