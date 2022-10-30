#include <numeric>
#include <climits>


int solution(vector<int> &A) {
    int l = A.size();
    long long s = std::accumulate(A.begin(), A.end(), 0);
    long long mindiff = LLONG_MAX;
    for (int i=0; i<l-1; i++) {
        s -= 2 * A[i];
        mindiff = min(mindiff, abs(s));
    }

    return mindiff;
}
