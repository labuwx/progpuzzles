int solution(vector<int> &A) {
    int i = 0, c = 0;
    for (; i != -1; i = A[i])
        c++;

    return c;
}
