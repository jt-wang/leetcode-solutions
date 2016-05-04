import java.util.*;
public class TopKFrequentElements {
    public Map topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsValue(nums[i])) {
                map.replace(nums[i], map.get(nums[i])+1);
            } else {
                map.put(nums[i], 1);
            }
        }

        return map;

    }

    public static void main(String[] args) {
        TopKFrequentElements t = new TopKFrequentElements();
        int[] a = {1,1,1,2,2};
        Map<Integer, Integer> c = t.topKFrequent(a, 1);
        for (Map.Entry<Integer, Integer> entry : c.entrySet()) {  
            System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());  
        }  

    }
}