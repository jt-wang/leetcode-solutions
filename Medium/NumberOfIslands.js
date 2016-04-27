var arr = [
  [0,1,1,1,0,1,0],
  [0,0,1,0,1,0,1],
  [1,1,0,0,1,1,0],
  [0,0,0,0,0,0,0]
];

//problem 1
function is_land (map, i, j) {
  if (map === null) 
    return false;
  if (map.length === 0)
    return false;
  if (map[0].length === 0)
    return false;
  if ( (i >=0 && i < map.length) && (j >= 0 && j < map[0].length) ) {
    // console.log(0<=i);
    // console.log('i=' + i + ' '+ 'j=' +j);
    if (map[i][j] === 1) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}

function dfs (map,i, j) {
  if (is_land(map, i, j)) {
    map[i][j] = 2;
    dfs(map, i, j+1);
    dfs(map, i, j-1);
    dfs(map, i+1, j);
    dfs(map, i-1, j);
  } else {
    return;
  }
}




/**
 * 计算该点所处小岛面积
 * @param  {number} x 横坐标, 即列号
 * @param  {number} y 纵坐标, 即行号
 * @return {number}   面积
 */
function get_area (map, i, j) {
  var area = 0;
  if (is_land(map, i, j)) {

    function dfs (map,i, j) {
      if (is_land(map, i, j)) {
        map[i][j] = 2;
        area += 1;
        dfs(map, i, j+1);
        dfs(map, i, j-1);
        dfs(map, i+1, j);
        dfs(map, i-1, j);  
      } else {
        return;
      }
    }
  dfs(map, i, j);
  }
  return area;
}

function get_island_count(map) {
  var count = 0;

  for (var i = 0; i < map.length; i++) {
    for (var j = 0; j < map[0].length; j++) {
      if (map[i][j] === 1) {
        count += 1;
        dfs(map, i, j);
      }
    }
  }
  return count;
}

console.log(get_island_count(arr));
// console.log(get_area(arr, 2, 1));

