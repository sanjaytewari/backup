function fibonacci(num) {
    if (num == 1)
        return 0;
    if (num == 2)
        return 1;
    return fibonacci(num - 1) + fibonacci(num - 2);
}

// let a= parseInt(
   a=  prompt('enter number: ')
   b =  fibonacci(a) 
console.log(b)
// );
// console.log('fibonacci(a)' + fibonacci(a));
// console.log("Fibonacci(1): " + fibonacci(1));
// console.log("Fibonacci(2): " + fibonacci(2));
// console.log("Fibonacci(3): " + fibonacci(3));
// console.log("Fibonacci(4): " + fibonacci(4));
// console.log("Fibonacci(5): " + fibonacci(5));

