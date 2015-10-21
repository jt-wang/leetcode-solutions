public class Solution {
    public int addDigits(int num) {
    	/*
    	对于一个多位数，比如 abcd
    	abcd = a * 10^3 + b * 10^2 + c*10 + d
    	所以, a + b + c + d = abcd - 999a - 99b - 9c
    	所以	  a+b+c+d % 9 = abcd % 9
    	所以 一直做下去, 会一直同余。因为最后得到的是一位数，所以直接mod 9即可。
    	对0,和 9的倍数特殊判断下。	
    	*/
        if (num == 0) {
    	    return 0;
        }else if( num % 9 == 0){
    	    return 9;
        }else {
    	return num % 9;
        }
    }
}