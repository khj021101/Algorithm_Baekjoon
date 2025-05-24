#include <stdio.h>
#include <stdlib.h>

int global_var = 10;        // 전역 변수 → Data 영역
const int const_var = 20;   // 상수 → Data 영역 (읽기 전용)

int main() {
    int local_var = 5;                     // 지역 변수 → Stack
    int* heap_var = (int*)malloc(4);      // 동적 할당 → Heap
    *heap_var = 42;

    printf("Hello, world!\n");            // 문자열 리터럴 → Data 영역
    printf("%d %d %d\n", global_var, const_var, *heap_var);

    free(heap_var);                       // 할당 해제
    return 0;
}