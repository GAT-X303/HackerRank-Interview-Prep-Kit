#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target){          

            map<int, int> diffMap;

            for (int i = 0; i < nums.size(); i++){  
                if (diffMap.find(nums[i]) == diffMap.end()){
                    int diff = target - nums[i];
                    diffMap.insert(pair<int, int>(diff,i));
                } else {   
                    vector <int>returnVector;
                    returnVector.push_back(diffMap.at(nums[i]));
                    returnVector.push_back(i);
                    return returnVector;
                };
            };
            vector <int>returnVector;
            return returnVector;
        };
};