# How Many Numbers Are Smaller Than the Current

Challenge: <kbd>Easy</kbd>

## Description

Given a list `nums`, for each `nums[i]` find out how many numbers in the list are smaller than it. That is for each
`nums[i]` you have to count the number of valid `j's` such that `j != i` **and** `nums[j] < nums[i]`

Return the answer in a list.

### Example 1:
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]
    Explanation:
    For nums[0]=8 there exists four smaller numbers than it (1, 2, 2, and 3).
    For nums[1]=1 there does not exists any numbers smaller than it.
    For nums[2]=2 there exists one number smaller than it (1).
    For nums[3]=2 there exists one number smaller than it (1).
    For nums[4]=3 there exists three numbers smaller than it (1, 2 and 2).

### Example 2:
    Input: nums = [6,5,4,8]
    Output: [2,1,0,3]

### Example 3:
    Input: nums = [7,7,7,7]
    Output: [0,0,0,0]

### Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists
