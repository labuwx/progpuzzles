#define NBits 30


int bitcount(int x) {
    int c = 0;
    while (x) {
        c += x % 2;
        x >>= 1;
    }
    return c;
}


int solution(int A, int B, int C) {
    int k_abc = bitcount(A | B | C);
    int k_ab = bitcount(A | B);
    int k_ac = bitcount(A | C);
    int k_bc = bitcount(B | C);
    int k_a = bitcount(A);
    int k_b = bitcount(B);
    int k_c = bitcount(C);

    int N_abc = 1 << (NBits - k_abc);
    int N_ab = 1 << (NBits - k_ab);
    int N_ac = 1 << (NBits - k_ac);
    int N_bc = 1 << (NBits - k_bc);
    int N_a = 1 << (NBits - k_a);
    int N_b = 1 << (NBits - k_b);
    int N_c = 1 << (NBits - k_c);

    int N = N_a + N_b + N_c - N_ab - N_ac - N_bc + N_abc;

    return N;
}
