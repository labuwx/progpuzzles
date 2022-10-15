#include <algorithm>
#include <limits>


int solution(vector<int> &A) {
    size_t l = A.size();
    if (l == 1) return A[0];

    vector<pair<int, size_t>> B(l);
    for (size_t i = 0; i < l; i++)
        B[i] = make_pair(A[i], i);
    sort(begin(B), end(B));
    B.push_back(make_pair(numeric_limits<int>::max(), 0));

    int ue, pe = numeric_limits<int>::max();
    size_t ui = numeric_limits<size_t>::max();

    for (size_t i = 0; i < l; i++) {
        if (pe != B[i].first && B[i].first != B[i+1].first && B[i].second < ui) {
            ue = B[i].first;
            ui = B[i].second;
        }
        pe = B[i].first;
    }

    return ui < l ? ue : -1;
}
