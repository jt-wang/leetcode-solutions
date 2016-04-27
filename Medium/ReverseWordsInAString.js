/**
 * @param {string} str
 * @returns {string}
 */
var reverseWords = function(str) {
    if (str === null) {
        return '';
    }
    
    if (str.length === 0) {
        return '';
    }
    str = str.replace(/\s+/g, ' ').trim();
    if (str.length === 0) {
        return '';
    }
    
    var arr = str.split(' ');
    return arr.reverse().join(' ');
};

console.log(reverseWords('  a  b'));