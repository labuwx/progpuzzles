#include <array>


vector<int> solution(string &S, vector<int> &P, vector<int> &Q) {
    int l = S.size();
    int m = P.size();
    vector<int> res(m);
    vector<array<int, 4>> imp(l);
    array<int, 4> cif = {-1, -1, -1, -1};
    for (int i = 0; i < l; i++) {
        switch (S[i]) {
            case 'A':
                cif[0] = i;
                break;
            case 'C':
                cif[1] = i;
                break;
            case 'G':
                cif[2] = i;
                break;
            case 'T':
                cif[3] = i;
                break;
        }
        imp[i] = cif;
    }

    for (int i=0; i<m; i++)
        for (int k=0; k<4; k++)
            if (imp[Q[i]][k] >= P[i]) {
                res[i] = k + 1;
                break;
            }

    return res;
}
