public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] indexArr = new int[2];
        int index1 = -2;
        int index2 = -2;
        int temp;

        HashMap<Integer, Integer> hash = new HashMap();
        for(int i = 0; i < nums.length; i++){
            hash.put(nums[i], i);
        }

        for(int i = 0; i < nums.length; i++){
            Integer correspondence = hash.get(target-nums[i]);
            if(correspondence != null && correspondence != i){
                index1 = i;
                index2 = correspondence;
                if (index1 > index2) {
                    temp = index1;
                    index1 = index2;
                    index2 = temp;
                }

                index1 += 1;
                index2 += 1;
                break;
            }
        }

        indexArr[0] = index1;
        indexArr[1] = index2;

        return indexArr;
    }



}
