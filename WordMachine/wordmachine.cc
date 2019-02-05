// you can use includes, for example:
// #include <algorithm>
#include <stack>
#include <string>
#include <iostream>
#include <sstream>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

// you can use includes, for example:
// #include <algorithm>
#include <stack>
#include <string>
#include <sstream>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(string &S) {
    // write your code in C++14 (g++ 6.2.0)
    std::stack<int> d;
    std::string c;
    std::stringstream ss(S);
    
    while(ss >> c){
        
    try{
        int k = stoi(c);
        if (k >= 0 && k <= 1048575){
            d.push(k);
        }
    }
    catch(...){
        int dsize = d.size();
        if(c == "DUP"){
            if(dsize > 0){
                d.push(d.top());
            }
            else{
                return -1;
            }
        }
        else if(c == "POP"){
            if(dsize > 0){
                d.pop();
            }
            else{
                return -1;
            }
        }
        else if(c == "+"){
            if(dsize >= 2){
                int a = d.top();
                d.pop();
                int b = d.top();
                d.pop();
                a = a + b;
                if (a >= 0 && a <= 1048575){
                    d.push(a);
                }
                else {
                    return -1;
                }
            }
            else {
                return -1;
            }
        }
        else if(c == "-"){
            if(dsize >= 2){
                int a = d.top();
                d.pop();
                int b = d.top();
                d.pop();
                a = a - b;
                if (a >= 0 && a <= 1048575){
                    d.push(a);
                }
                else {
                    return -1;
                }
            }
            else {
                return -1;
            }
        }
        else{
            return -1;
        }
        
    }
    }
    return d.top();
}

int main(){
    std::string S = "13 DUP 4 POP 5 DUP + DUP + -";
    std::cout << solution(S) << std::endl;
    return 0;
}
