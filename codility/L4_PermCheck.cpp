int solution(vector<int> &A) {
    int l = A.size();
    vector<bool> seen(l);

    for (auto x: A) {
        if (x <= l) {
            if (seen[x]) return 0;
            seen[x] = true;
        }
        else
            return 0;
    }

    return 1;
}
