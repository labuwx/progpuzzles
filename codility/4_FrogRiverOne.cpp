#include <algorithm>
#include <climits>


int solution(int X, vector<int> &A) {
    vector<int> ffall(X, INT_MAX);
    for (int i = 0; i < A.size(); i++) {
        int pos = A[i] - 1;
        ffall[pos] = min(ffall[pos], i);
    }

    int mm = *std::max_element(std::begin(ffall), std::end(ffall));
    return mm < INT_MAX ? mm : -1;
}
