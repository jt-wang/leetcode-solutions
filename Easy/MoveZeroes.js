var moveZeroes = function(nums) {
    var number_of_zero = 0;
    nums.forEach( function (num, index) {
       if (num !== 0) {
           for (var i = index-1; i >= 0; i--) {
               if ( nums[i] !== 0) {
                   nums[i+1] = num;
                   if (index != (i+1)) {
                     nums[index] = 0;  
                   }
                   break;
               } else if (i === 0) {
                nums[i] = num;
                nums[index] = 0;
                break;
               }
           }
       } 
    });
};
