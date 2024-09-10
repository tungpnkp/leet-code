var createCounter = function(init) {
    let tmp = init;
    return {
            increment: () => {
                tmp = tmp +1;
                return tmp;
            },
            reset: () => {
                tmp = init
                return tmp;
            },
            decrement: () => {
                tmp = tmp - 1;
                return tmp;
            }

        }
};