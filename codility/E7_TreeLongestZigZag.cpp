#define LEFT (-1)
#define RIGHT 1
#define NODIR 0
#define dir_change(d1, d2) ((d1) * (d2) < 0)


int s_inner(tree * T, int curr_dir) {
    int left_b = T->l ? s_inner(T->l, LEFT) + dir_change(curr_dir, LEFT) : 0;
    int right_b = T->r ? s_inner(T->r, RIGHT) + dir_change(curr_dir, RIGHT) : 0;

    return max(left_b, right_b);
}


int solution(tree * T) {
    return s_inner(T, NODIR);
}
