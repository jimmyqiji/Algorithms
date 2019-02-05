#include <string>

int solution(int N) {
    
    std::string s = std::to_string(N);
    // std::cout << s << std::endl;
    if(s.length() > 1){
        s[0] = '1';
        for(int i = 1; i < s.length(); i++) {
            s[i] = '0';
        }
        return stoi(s);
    }
    else {
        return 0;
    }
}
