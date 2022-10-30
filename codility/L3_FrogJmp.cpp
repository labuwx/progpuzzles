int solution(int X, int Y, int D) {
    int diff = Y - X;
    if (diff % D == 0)
        return diff / D;
    else
        return (diff / D) + 1;
}
