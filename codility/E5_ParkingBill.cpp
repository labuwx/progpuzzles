#define HM_DELIM ":"


int ceil_div(int n, int d) {
    if (n % d)
        return n / d + 1;
    else
        return n / d;
}


int s2min(string &s) {
    string hs = s.substr(0, 2);
    string ms = s.substr(3, 2);
    int h = stoi(hs), m = stoi(ms);
    return 60 * h + m;
}


int solution(string &E, string &L) {
    int stay = s2min(L) - s2min(E);
    int cost = 2 + 3;
    cost += ceil_div(max(0, stay - 60), 60) * 4;
    return cost;
}
