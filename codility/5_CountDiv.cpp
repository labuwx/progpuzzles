int solution(int A, int B, int K) {
    long long a = A, b = B, k = K;
    long long firstmult = a + k - a % k;
    long long n = max(b-firstmult, (long long)0) / k;
    n += !(a%k) + (firstmult <= b);
    return (int)n;
}
