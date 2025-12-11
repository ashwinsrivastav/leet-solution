class Solution {
public:
   vector<int> leftRightDifference(vector<int>& nums) {
       int sum = 0;
       for (const auto& num : nums) {
           sum += num;
       }
       int leftSum = 0;
       for (int i = 0; i < nums.size(); i++) {
           int rightSum = sum - leftSum - nums[i]; 
           nums[i] = abs(leftSum - rightSum);
           leftSum += nums[i]; 
       }
       return nums;
   }
};