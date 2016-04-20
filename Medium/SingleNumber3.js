/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    //hashMap is o(1)
    var map = {};
    var result_list = [];
    nums.forEach( function (num) {
        if (num in map) {
            map[num] = 2;
        } else {
            map[num] = 1;
        }
    } );
    nums.forEach(function (num) {
       if (map[num] == 1) {
           result_list.push(num);
       }
    });
    return result_list;
};
