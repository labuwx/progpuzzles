int solution(vector<int> &A) {
    int l = A.size();
    vector<bool> seen(l+1);

    for (auto k: A)
        seen[k-1] = true;

    for (int i=0; i<=l; i++)
        if (!seen[i])
            return i+1;
}
