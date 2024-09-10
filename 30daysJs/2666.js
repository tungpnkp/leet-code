/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    var hasCall = false;
    return function(...args){
        if(!hasCall) {
            hasCall = true;
            return fn(...args);
        }
        else {
            return undefined;
        }
    }
};


