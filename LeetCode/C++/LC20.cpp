#include <stack>
#include <string>

using namespace std;

class Solution {
    public:
        bool isValid(string s){
            stack <char> para;

            if (s.length() == 0){
                return true;
            };

            for (int i = 0; i < s.length(); i++){
                if (s.at(i) == '('){
                    para.push(s.at(i));
                } else if (s.at(i) == '{'){
                    para.push(s.at(i));
                } else if (s.at(i) == '['){
                    para.push(s.at(i));
                } else {
                    if (para.empty()){
                        return false;
                    }
                    char leftBracket = para.top();
                    para.pop();
                    if (leftBracket == '('){
                        if (s.at(i) != ')'){
                            return false;
                        };
                    } else if (leftBracket == '{'){
                        if (s.at(i) != '}'){
                            return false;
                        };
                    } else if (leftBracket == '['){
                        if (s.at(i) != ']') {
                            return false;
                        };
                    }
                };
            };
            if (para.empty()){
                return true;
            } else {
                return false;
            };
        };
};