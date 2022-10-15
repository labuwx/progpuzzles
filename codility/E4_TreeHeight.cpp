int solution(tree * T) {
    if (!T) return -1;
    return max(solution(T->l), solution(T->r)) + 1 ;
}
