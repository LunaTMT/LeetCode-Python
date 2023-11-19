function getPINs(str) {
   const AL = {
       '0': ['0', '8'],
       '1': ['1', '2', '4'],
       '2': ['1', '2', '3', '5'],
       '3': ['2', '3', '6'],
       '4': ['1', '4', '5', '7'],
       '5': ['2', '4', '5', '6', '8'],
       '6': ['3', '5', '6', '9'],
       '7': ['4', '7', '8'],
       '8': ['0', '5', '7', '8', '9'],
       '9': ['6', '8', '9']
   };
 
   let combinations = AL[str[0]]
   getCombinations(1)
   return combinations
   
   function getCombinations(i) {
     if (i === str.length) {
       return;
     }
 
     var newCombinations = [];
     for (var password of combinations) {
       for (var e of AL[str[i]]) {
         newCombinations.push(password + e);
       }
     }
     combinations = newCombinations; 
 
     return getCombinations(i + 1);
   }
 }