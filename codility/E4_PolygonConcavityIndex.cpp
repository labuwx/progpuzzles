#include <climits>


#define LEFT (-1)
#define RIGHT 1
#define NODIR 0


int calcdir(Point2D &p1, Point2D &p2, Point2D &p3) {
    long long v1x = p2.x - p1.x;
    long long v1y = p2.y - p1.y;
    long long v1Lx = -v1y;  // left orthogonal of v1
    long long v1Ly = v1x;   // left orthogonal of v1
    long long v2x = p3.x - p2.x;
    long long v2y = p3.y - p2.y;

    long long dotp = v1Lx * v2x + v1Ly * v2y;

    int dir = NODIR;
    if (dotp > 0)
        dir = LEFT;
    else if (dotp < 0)
        dir = RIGHT;

    return dir;
}


int solution(vector<Point2D> &A) {
    int N = A.size();

    int xm = INT_MAX, ym = INT_MAX, im=-1;
    for (int i = 0; i < N; i++) {
        if (A[i].x < xm || (A[i].x == xm && A[i].y < ym)) {
            xm = A[i].x;
            ym = A[i].y;
            im = i;
        }
    }

    Point2D p1 = A[(im-1+N) % N], p2 = A[im], p3 = A[(im+1) % N];
    int domdir = calcdir(p1, p2, p3);

    for (int i = 0; i < N; i++) {
        p1 = A[i], p2 = A[(i+1) % N], p3 = A[(i+2) % N];
        int dir = calcdir(p1, p2, p3);
        if (dir != NODIR && dir != domdir)
            return (i+1) % N;
    }

    return -1;
}
