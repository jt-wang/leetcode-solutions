/** @params 
*/
Array.prototype.swap = function(i, j) {
  if (i !== j) {
  var temp = this[i];
  this[i] = this[j];
  this[j] = temp;
}
} 

