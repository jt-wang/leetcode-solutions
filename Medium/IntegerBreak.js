/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {
   //7to10
   /*
    7 = 3*4 12
    8 = 3*3*2 = 18
    9 = 3*3*3 = 27
    10 = 3*3*4 = 36
    每个数比较大的情况下，数尽可能多
    11 = 3*3*3*2 = 54
    发现全都是 3 带上剩下的数
   */

  if (n === 1)
    return 1;
  if (n === 2)
    return 1;
  if (n === 3)
    return 2;
  if (n === 4)
    return 4;

  var result = 1;
  while (n > 4) {
    result *= 3;
    n -= 3;
  }

  result *= n;

  return result;



};