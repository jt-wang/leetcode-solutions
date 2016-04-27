'use strict';
/**
 * @param  {number} i
 * @param  {number} j
 */
Array.prototype.swap = function(i, j) {
  if ( 0 <= i < this.length && 0 <= j < this.length && i !== j) {
    var temp = this[i];
    this[i] = this[j];
    this[j] = temp;
  }
}
 
/** @param {String} str 
 */
function perm(str) { 
  var result = new Set();
  var arr = str.split('');
  function fn(n) { //为第n个位置选择元素 
     for(var i=n;i<arr.length;i++) { 
         arr.swap(i, n);
         if(arr.length-1 - n > 1) {
          //判断数组中剩余的待全排列的元素是否大于1个 
            fn(n+1); //从第n+1个下标进行全排列 
          }
          else {
            result.add(arr.join('')); //显示一组结果 
            }
          arr.swap(i, n); 
         } 
     } 

  fn(0);
  for(var o of result) {
    console.log(o);
  }
}

perm('abc');