#include <deque>
#include <utility>


int solution(vector< vector<int> > &A) {
    int N = A.size();
    int M = A[0].size();
    vector<vector<bool>> reached(N, std::vector<bool>(M));

    int cc = 0;
    deque<pair<int, int>> q;
    for (int i=0; i < N; i++)
        for (int j=0; j < M; j++) {
            if (reached[i][j])
                continue;
            cc++;

            q.push_front(make_pair(i, j));
            while (!q.empty()) {
                pair<int, int> p = q[0];
                q.pop_front();
                int x = p.first, y = p.second;

                if (reached[x][y])
                    continue;
                else
                    reached[x][y] = true;

                if (0 < x && A[x][y] == A[x-1][y])
                    q.push_front(make_pair(x-1, y));
                if (0 < y && A[x][y] == A[x][y-1])
                    q.push_front(make_pair(x, y-1));
                if (x < N-1 && A[x][y] == A[x+1][y])
                    q.push_front(make_pair(x+1, y));
                if (y < M-1 && A[x][y] == A[x][y+1])
                    q.push_front(make_pair(x, y+1));
            }
        }

    return cc;
}
