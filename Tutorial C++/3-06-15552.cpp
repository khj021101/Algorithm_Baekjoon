#include <iostream>
int main(void){
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);
    long int T;
    std::cin >> T;
    for(long int i = 0; i<T ; i++){
        int A, B;
        std::cin >> A >> B;
        std::cout << A+B << '\n';
    }
}
