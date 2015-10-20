public class Solution {
        
    public int climbStairs(int n) {
		int[] climbWays = new int[n+1];
		for (int i = 0; i < climbWays.length; i++) {
			climbWays[i] = 0;
		}

    	climbWays[0] = 1;
    	climbWays[1] = 1;
    	for (int i = 2; i <= n; i++) {
    		climbWays[i] = climbWays[i-1]+climbWays[i-2];
    	}
    	return climbWays[n];
        
    }


}