#include <algorithm>


#define LSB(i) ((i) & -(i))


int fwt_get(vector<int> &t, int k) {
    int res = 0;
    k++;
    for (; k != 0; k -= LSB(k))
        res += t[k];
    return res;
}


void fwt_add(vector<int> &t, int k) {
    k++;
    for (; k < t.size(); k += LSB(k))
        t[k] += 1; 
}


int solution(vector<int> &A) {
    int l = A.size();

    vector<pair<int, int>> B(l);
    for (int i = 0; i < l; i++)
        B[i] = make_pair(A[i], i);
    sort(begin(B), end(B));

    int invc = 0;
    vector<int> ctree(l+1);
    for (int i = l - 1; i >= 0; i--) {
        int r = B[i].second;
        invc += fwt_get(ctree, r-1);

        if (invc > 1'000'000'000)
            return -1;

        fwt_add(ctree, r);
    }

    return invc;
}
