public class Solution {
    public int majorityElement(int[] nums) {
    	//如果只有一个元素
        if(nums.length == 1){
            return nums[0];
        }
        //否则，先排序。majorityElement因为出现>=n/2,所以中间的数一定是
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}