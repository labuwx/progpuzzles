int solution(vector<int> &A) {
    int N = A.size();
    int lb=0, rb=0;
    int depth_max=0;

    for (int l=0, r=N-1; l < r;) {
        lb = max(lb, A[l]);
        rb = max(rb, A[r]);
        int bmin = min(lb, rb);

        depth_max = max(depth_max, max(bmin - A[l], bmin - A[r]));

        if (lb < rb)
            l++;
        else
            r--;
    }

    return depth_max;
}
