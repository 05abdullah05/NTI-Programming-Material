function factorial(n)
{
    if(n==1 || n==0)
     return 1;
    else
     return n* factorial(n-1)
}

console.log(factorial(4))

// the factorial function says to multiply all the whole numbers from the chosen number down to one.
// factorial (4)
//     4 * factorila(3)
//         3 * factorila(2)
//             2 * factorila(1)  

// facotorial of 1 is 1 as our if statement  so 2 * 1 = 2 
// Now 2 is the value of factorial 2 so 3 * factorial(2) becomes 3 * 2= 6
// Now 6 is the value of factorial 3 so 4 * factorial(3) becomes 4 * 6= 24
// And at last right under factorial call is 24 so factorial of 4 is 24


// var printNumTwo;
// for (var i = 0; i < 3; i++) {
//   if (i === 2) {
//     printNumTwo = function() {
//       return i;
//     };
//   }
// }
// console.log(printNumTwo());