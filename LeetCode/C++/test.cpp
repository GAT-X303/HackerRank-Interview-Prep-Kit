#include <stdio.h>
#include <iostream>

#include "LC20.cpp"

using namespace std;

int main () {

    Solution sol1;

    string input = "]";

    bool ans = sol1.isValid(input);

    if (ans){
        cout << "True" << endl;
    } else {
        cout << "False" << endl;
    }

    return 0;
}