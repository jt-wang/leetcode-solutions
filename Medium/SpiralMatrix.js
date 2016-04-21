/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  var result = [];
  if (matrix === null) {
    return [];
  }

  if (matrix.length === 0) {
    return [];
  }

  if (matrix[0].length === 0) {
    return [];
  }

  var top = 0;
  var bottom = matrix.length-1;
  var left = 0;
  var right = matrix[0].length-1;
  var horizonal = left;
  var vertical = top;


function p() {
  console.log(result);
}
  /*
   * horizonal: left -> right
   * vertical: top -> bottom
   * top += 1
   * horizonal: right -> left
   * right -= 1
   * vertical: bottom -> top
   * left += 1
   * bottom -= 1
   * */

  //重点: 在每次while 内部，也需要判断边界，随时退出

  while (left <= right && top <= bottom) {



  if (left > right)
    break;
  for (horizonal = left; horizonal <= right; horizonal++){
    result.push(matrix[vertical][horizonal]);
  }
  horizonal--;
  top++;


  if (top > bottom)
    break;

  for (vertical = top; vertical <= bottom; vertical++){
    result.push(matrix[vertical][horizonal]);

  }
  vertical--;
  right--;

  if (left > right)
    break;
  for (horizonal = right; horizonal >= left; horizonal--){
    result.push(matrix[vertical][horizonal]);
  }
  horizonal++;
  bottom--;

  if (top > bottom)
    break;
    for (vertical = bottom; vertical >= top; vertical--){
    result.push(matrix[vertical][horizonal]);
  }
  vertical++;



  left += 1;
  }

  return result;
}

function betterSpiralOrder (matrix) {
    var result = [];
  if (matrix === null) {
    return [];
  }

  if (matrix.length === 0) {
    return [];
  }

  if (matrix[0].length === 0) {
    return [];
  }

  var top = 0;
  var bottom = matrix.length-1;
  var left = 0;
  var right = matrix[0].length-1;
  var horizonal = left;
  var vertical = top;



  var i = 1;
  var j = 0;
  while (left <= right && top <= down) {
    
  }
}





