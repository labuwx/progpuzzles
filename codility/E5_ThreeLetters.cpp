string solution(int A, int B) {
    string ac = "a", bc = "b";
    if (B < A) {
        swap(A, B);
        swap(ac, bc);
    }

    string s = "";

    while (B) {
        if (A < B) {
            s += bc;
            B--;
        }
        if (A > 0) {
            s += bc + ac;
            B--;
            A--;
        }
    }

    return s;
}
