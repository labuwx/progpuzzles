#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool *eratosthenes_sieve(unsigned long long n) {
    bool *pcheck = malloc(n * sizeof(bool));
    pcheck[0] = false;
    pcheck[1] = false;
    for (unsigned long long i = 2; i < n; i++)
        pcheck[i] = true;

    unsigned long long i = 2;
    while (i < n) {
        for (unsigned long long j = 2*i; j < n; j += i)
            pcheck[j] = false;

        i++;
        while (i < n && !pcheck[i])
            i++;
    }
    return pcheck;
}

unsigned long get_primes(bool *pcheck, unsigned long plimit, unsigned long **primes) {
    unsigned long pnum = 0;
    for (unsigned long n=0; n <= plimit; n++)
        if (pcheck[n])
            pnum++;

    *primes = malloc(pnum * sizeof(unsigned long));
    unsigned long i = 0;
    for (unsigned long n=0; n <= plimit; n++)
        if (pcheck[n]) {
            (*primes)[i] = n;
            i++;
        }

    return pnum;
}

unsigned long long concat(unsigned long long a, unsigned long long b) {
    unsigned long long m = 10;
    while (m <= b)
        m *= 10;
    return a * m + b;
}

int main(void) {
    unsigned long plimit = 30000;
    bool *pcheck = eratosthenes_sieve(concat(plimit, plimit));
    unsigned long *primes;
    unsigned long pnum = get_primes(pcheck, plimit, &primes);
    printf("%lu\n", pnum);
    printf("%lu\n", primes[pnum-1]);


    for (unsigned long s = 15; s < plimit; s += 2) {
        printf("%lu\n", s);

        for (unsigned long a = 0; a < pnum; a++) {
            unsigned long pa = primes[a];
            if (pa >= s) break;

            for (unsigned long b = a+1; b < pnum; b++) {
                unsigned long pb = primes[b];
                if (pa + pb >= s) break;

                for (unsigned long c = b+1; c < pnum; c++) {
                    unsigned long pc = primes[c];
                    if (pa + pb + pc >= s) break;

                    for (unsigned long d = c+1; d < pnum; d++) {
                        unsigned long pd = primes[d];
                        if (pa + pb + pc + pd >= s) break;
                        unsigned long pe = s-pa-pb-pc-pd;
                        if (pe <= pd) break;
                        if (!pcheck[pe]) continue;

                        if (pcheck[concat(pa, pb)] && pcheck[concat(pb, pa)] &&
                            pcheck[concat(pa, pc)] && pcheck[concat(pc, pa)] &&
                            pcheck[concat(pa, pd)] && pcheck[concat(pd, pa)] &&
                            pcheck[concat(pa, pe)] && pcheck[concat(pe, pa)] &&
                            pcheck[concat(pb, pc)] && pcheck[concat(pc, pb)] &&
                            pcheck[concat(pb, pd)] && pcheck[concat(pd, pb)] &&
                            pcheck[concat(pb, pe)] && pcheck[concat(pe, pb)] &&
                            pcheck[concat(pc, pd)] && pcheck[concat(pd, pc)] &&
                            pcheck[concat(pc, pe)] && pcheck[concat(pe, pc)] &&
                            pcheck[concat(pd, pe)] && pcheck[concat(pe, pd)])
                        {
                            printf("%lu\n", s);
                            return 0;
                        }
                    }
                }
            }
        }
    }

    printf("Done.\n");
    return 0;
}

