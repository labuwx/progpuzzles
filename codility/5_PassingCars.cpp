#define EAST 0
#define WEST 1


int solution(vector<int> &A) {
    int passcnt = 0, careast = 0;

    for (auto car: A) {
        if (car == EAST)
            careast++;
        else  // WEST
            passcnt += careast;
            if (passcnt > 1000000000)
                return -1;
    }

    return passcnt;
}
