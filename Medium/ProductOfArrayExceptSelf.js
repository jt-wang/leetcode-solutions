var productExceptSelf = function(nums) {
    var hash = {};
    hash[0] = {};
    hash[0][0] = nums[0];
    hash[nums.length-1] = {};
    hash[nums.length-1][nums.length-1] = nums[nums.length-1];

    for (var i = 1; i <= nums.length-1; i++) {

        hash[0][i] = hash[0][i-1] * nums[i];
    }
    for (var j = nums.length-2; j >= 0; j--) {
        hash[nums.length-1][j] = hash[nums.length-1][j+1] * nums[j];
    }

    var output = [];
    output[0] = hash[nums.length-1][1];
    output[nums.length-1] = hash[0][nums.length-2];

    for (var k = 1; k <= nums.length-2; k++) {
    	output[k] = hash[0][k-1] * hash[nums.length-1][k+1];
    }
    return output;
};
console.log( productExceptSelf([1,2,3,4]));
