var topk = function(nums, k) {
    if (nums === null)
        return [];

    if (nums.length === 0)
        return [];

    if (k > nums.length)
        return [];

    if (k <= 0)
        return [];

    var map = new Map();
    for (var i = 0; i < nums.length; i++) {
        if (map.has(nums[i])) {
            map.set(nums[i], map.get(nums[i])+1);
        } else {
            map.set(nums[i], 1);
        }
    }

    var nums = [];

    map.forEach( function(value, key) {
        nums.push({ key: key, value:value});
    });
    nums.sort(function(a, b) {
        return b.value - a.value;
    });

    var result = [];
    for (var j = 0; j < k; j++) {
        result.push(nums[j].key);
    }
    return result;

}

var m = topk([1,1,1,5,7,9,9,9,9,9, 2,2], 2);
console.log(m);