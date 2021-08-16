function acronymize(str) {
    var newAcry = ''
    var wordsArr = str.split(" ")
    for(var i=0; i<wordsArr.length; i++){
        newAcry += wordsArr[i][0]
    }
    return newAcry
}

acronymize('hello world, this is just a base message')


function reverseString(str) {
    var revStr = ""
    for(var i=str.length-1; i>=0; i--) {
        revStr += str[i]
    }
    return revStr
}

reverseString('topdog')


/* 
  Parens Valid
    Given an str that has parenthesis in it
    return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the underlined ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing

function parensValid(str) {
    var check =[]
    for (var i = 0; i < str.length; i++) {
        if(str[i] === '(' || str[i] === '[' || str[i] '{') {
            check.push(str[i])
        }
    }
}

/*****************************************************************************/

/* 
  Braces Valid
  Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

function bracesValid(str) {}


const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

function isPalindrome(str) {
  for (var i = 0; i <= (str.length / 2); i++) {
    if (str[i] != str[str.length -1 - i]) return false;
}
return true;
}
// OTHER METHOD
function isPalindromeOneLine(str) {
    return str === str.split("").reverse().joing("");
}

console.log(isPalindrome(str1))
console.log(isPalindrome(str2))
console.log(isPalindrome(str3))
console.log(isPalindrome(str4))

/* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
*/

const str1 = "what up, daddy-o?";
const expected1 = "dad";

const str2 = "uh, not much";
const expected2 = "u";

const str3 = "Yikes! my favorite racecar erupted!";
const expected3 = "e racecar e";

function longestPalindromicSubstring(str) {
  var checkPalen = ""
  var longPalen = False

  //For loop through string
  for(i = 0; i < str.length; i++){
    //Set a starting point to check for long palindrome
    checkPalen = checkPalen + str[i];

    //loop through characters after i
    for(x = i + 1; x < str.length; x++){
      checkPalen = checkPalen + str[x];

      if (str[i] == str[x]){
        longPalen = isPalindrome(checkPalen);

        if(longPalen == true){
          return checkPalen;
        }

      }

      checkPalen = "";

    }

  }

  return str[0]
}

console.log(longestPalindromicSubstring(str1))
console.log(longestPalindromicSubstring(str2))
console.log(longestPalindromicSubstring(str3))



//----------------------------------------------------
//endoded string
//----------------------------------------------------
const str4 = "bbcc";
const expected4 = "bbcc";

function encodeStr(str){
  newstring = ''
  count = 0
  for (var i = 0; i <= str.length; i++); {
    newstring += str[i]
    for (var j = i + 1; j < str.length; j++); {
      if (str[i] == str[j]) { // if (str[i] == str[i-1])
        count++
      } else {
        newstring += count
        count = 0
        i = j - 1
      }
    }
  }
  return newstring;
}

console.log(encodeStr(str4))

// --------------------------------------------
// frequency table builder
// --------------------------------------------

const arr1 = ['a','a','a']
// expected output:
  // a: 3,

function frequencyTableBuilder(arr) {
  if(Array.length > 1){
    return {};
  }
  newArr = {};
  for (var i=0; i<arr.length; i++) {
    index = arr[i];
    if(newArr.hasOwnPorperty(index)){
      newArr[index]++;
    } else {
      newArr[index] = 1
    }
  }
  return newArr;
}

// --------------------------------------------
// reverse string
// --------------------------------------------
const str1 = "This is a test"

// better solution
function reverseWordOrder(wordStr) {
  const myArr = wordStr.split(" ");
  newArr = ''
  for(var i = myArr.length-1; i>-1; i--) {
    newArr += myArr[i]+ ' ';
  }
  return newArr
}

//one line solution

function reverseOptimized(wordStr) {
  return wordstr.split(" ").reverse(" ").join
}


//frequency counter, when frequency is > 1 move to next part of loop
/* 
  Given a string,
  return a new string with the duplicates excluded
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "parallel"
const expected3 = "parle"

function stringDedupe(str) {
  deduped = str[0]
  for(var i= 1; i < str.length; i++) {
    if(str[i] != str[i-1]){
      deduped += (str[i])
    }
  }
  return deduped
}

console.log(stringDedupe(str2))




/*****************************************************************************/
// split by " " seperate words, reverse worse, join together

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

// function reverseWords(str) {
//   preSpaceText = []
//   reverseWordsString = []
//   for(var i = 0; i < str.length; i++){
//     if(str[i] == " " || i == str.length-1){
//       if(i == str.length-1){
//         preSpaceText.push(str[i])
//       }
//       preSpaceText.reverse().join()
//       reverseWordsString.push(preSpaceText)
//       reverseWordsString.push("")
//       preSpaceText = []
//     }
//     else{
//       preSpaceText.push(str[i])
//     }
//   }
//   return reverseWordsString.join(" ")
// }
// console.log(reverseWords(str2))


// --------------------------------
// BELOW IS AN INCOMPLETE FUNCTION
// --------------------------------
function splitReverse(str) {
  var reverseText = str.split(" ")
  newOrder = ''
  for (var i = 0; i < str.length; i++) {
    newOrder += reverseText[i] + ' '
  }
  return newOrder
}

console.log(splitReverse(str2))


// String: Rotate String
  // Create a standalone function that accepts a string and an integer, 
  // and rotates the characters in the string to the right by that given integer amount.

const str1 = "Hello World";
const rotateAmnt1 = 0;
const expected1 = "Hello World";

const str2 = "Hello World";
const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const str3 = "Hello World";
const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const str4 = "Hello World";
const rotateAmnt4 = 4;
const expected4 = "orldHello W";

function rotateStr(str, n) {
  arr = str.split("");
  for(let i = str.length-1; i>=str.length-n; i--){ //start at end of array and go for n times
    arr.unshift(arr.pop());     // pop from end of array and unshift to beginning

  }
  let answer = arr.join("");
  return answer;

}

//Better Effiancy O(constant)
function rotateStr2(str,n){
  let answer = "";
  for(let i = str.length-1; i>= str.length-n;i--){  //goes from the end of the string n(rotation) time
      answer = str[i]+answer;                         //and add its to the new variable
  }
  answer += str.substring(0,str.length-n);  //adding a subtring to var answer starting at the beginning
  return answer;                              //of the string
}

console.log(rotateStr2(str3,2));

//console.log(rotateStr(str1,4));

// Create the function isRotation(str1,str2) that
// returns whether the second string is a rotation of the first.

const strA1 = "ABCD";
const strB1 = "CDAB";
const expected1 = true;
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated

const strA2 = "ABCD";
const strB2 = "CDBA";
const expected2 = false;
// Explanation: all same letters in 2nd string, but out of order

function isRotation(s1, s2) {
  for(var i = 0; i < s1.length; i++){
    let str = rotateStr(s1, i);
    if (str == s2){
     return true;
    }  
  } 
  return false;
}

console.log(isRotation(strA1,strB1))

//every possible rotation of a string is contained in the string added to its self
//   return (s1 + s1).includes(s2)
//"ABCDABCD" CHECK FOR "CDBA"


/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.
  Is there a quick way to determine if they aren't an anagram before spending more time?
  Given two strings
  return whether or not they are anagrams
*/

const strA1 = "yes";
const strB1 = "eys";
const expected1 = true;

const strA2 = "yes";
const strB2 = "eYs";
const expected2 = true;

const strA3 = "no";
const strB3 = "noo";
const expected3 = false;

const strA4 = "silent";
const strB4 = "listen";
const expected4 = true;


function isAnagram(s1, s2) {
  if (s1.length !== s2.length) {
    return false;
  }

  let arr = s2.toLowerCase()//.split("")
  let arr2 = s1.toLowerCase()
  for (var i = 0; i < arr2.length; i++) {
    if (arr.includes(arr2[i])) {
      return true;
    } else {
      return false
    }
  }
}


//another version, not complete

// function isAnotherAnogram(s1,s2) {
//   if (s1.length !== s2.length) {
//     return false;
//   }

//   const s1CharFreq = {};
//   const s2CharFreq = {};

//   for (var i = 0; i < s1.length; i++) {
//     const s1CharUpper = s1[i].toUpperCase();
//     const s2CharFreq = s2[i].toUpperCase();

//     if(s1CHarFreq.hasOwnPorperty(s1CharUpper)) {
//       s1CharFreq[s1CharUpper]++;
//     } else {
//       s1CharFreq[s1CharUpper] = 1
//     }

//     if(s2CHarFreq.hasOwnPorperty(s2CharUpper)) {
//       s2CharFreq[s2CharUpper]++;
//     } else {
//       s2CharFreq[s2CharUpper] = 1
//     }

//     for (const char in s1CharFreq) {
//       if(!s2.hasOwnPorperty(char)) reutrn false;

//       if(s1CharFreq[char] !== s2CharFreq)
//     }

//   }

// }

console.log(isAnagram(strA1,strB1))

/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

function trim(str) {
  let start
  let end

  for (let i = 0; i < str.length; i++){
    if (str[i] != " "){
      start = i;
    }
  }
  for (let y = str.length - 1; y >= 0; y--){
    if (str[y] != " "){
      end = y;
    }
  }

  return str.substring(i, y)
}


/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

// still cant get this one running
function balancePoint(nums) {
  var left = 0
  var right = 0

  for (var i=0; i<nums.length; i++) {
    // check left side
    for (var j = 0; j < i; j++) {
      left += nums[j];
    }
    // check right side
    for (var j = i + 1; j < nums.length; j++) {
      right += nums[j];
    }
    // if true reutrn the index i
    if (left == right) {
      return i;
    } else {
      return false
    }
    
  }
}

console.log(balancePoint(nums1))




/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
*/


const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

function binarySearch(sortedNums, searchNum) {
    
    
    if (sortedNums[sortedNums.length/2] == searchNum){
      return true
    }
    else if (sortedNums[sortedNums.length/2] > searchNum){
      // iterate to the left (lower numbers)
      for (let j = sortedNums.length/2; j = sortedNums.length/2; j--){
        if (j == searchNum){
          return true
        }
      }
    }
    else if (sortedNums[sortedNums.length/2] < searchNum){
      // iterate to larger numbers
      for (let j = sortedNums.length/2; j = sortedNums.length/2; j++){
        if (j == searchNum){
          return true
        }

      }
    }
    return false
}

console.log(binarySearch(nums1, searchNum1))
console.log(binarySearch(nums2, searchNum2))
console.log(binarySearch(nums3, searchNum3))



/* 
  Given a SORTED array of integers, dedupe the array 
  Because array elements are already in order, all duplicate values will be grouped together.
  Ok to use a new array
  Bonus: do it in O(n) time (no nested loops, new array ok)
*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

function dedupeSorted(nums) {
  let output = []

  for(var i = 0; i < nums.length; i++) {
    output.push(nums[i]) ///////
    for(var j = i+1; j < nums.length; j++) {
      if(nums[j] !== nums[i]) {
        output.push(nums[j])
        i = j
      } else {
        i = j
      }
    }
  }
  return output
}

//first way of doing it
// function dedupeSorted(nums) {
//   newArray = []

//   for (let i = 0; i < nums.length; i++){
//     if (!newArray.includes(nums[i])){
//       newArray.push(nums[i])
//     }
//   }
//   return newArray
// }

console.log(dedupeSorted(nums1))
console.log(dedupeSorted(nums2))
console.log(dedupeSorted(nums3))


/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

function fewestCoinChange(cents) {
  //gets the max num of coins first
  let coinNum = {}
  while(cents) {
    if (cents % 25 == 0) {
      coinNum["quarter"] = cents / 25
      cents %= 25
    } else if (cents % 10 == 0) {
      coinNum["dime"] = cents / 10
      cents %= 10
    } else if (cents % 5 == 0) {
      coinNum["nickle"] = cents / 5
      cents %= 5
    } else {
      coinNum["pennie"] = cents / 1
      cents %= 1
    }
  }
  return coinNum
}

console.log(fewestCoinChange(cents1))
console.log(fewestCoinChange(cents2))
console.log(fewestCoinChange(cents3))
console.log(fewestCoinChange(cents4))


/* 
  Recursive Factorial
  Input: integer
  Output: integer, product of ints from 1 up to given integer
  
  If less than zero, treat as zero.
  Bonus: If not integer, truncate (remove decimals).
  
  Experts tell us 0! is 1.
  
  rFact(3) = 6 (1*2*3)
  rFact(6.8) = 720 (1*2*3*4*5*6)
*/

const num1 = 3;
const expected1 = 6;
// Explanation: 1*2*3 = 6

const num2 = 6.8;
const expected2 = 720;
// Explanation: 1*2*3*4*5*6 = 720

const num3 = 0;
const expected3 = 1;

function factorial(n) {
  n = Math.floor(n)
  //exeption
  if(n <= 0) {
    return 1
  }

  //Base case
  if(n > 1) {
    return n * factorial(n-1)
  } else {
    return 1;
  }
}

console.log(factorial(num1))
console.log(factorial(num2))
console.log(factorial(num3))

/*****************************************************************************/

/* 
  Return the fibonacci number at the nth position, recursively.
  
  Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
  The next number is found by adding up the two numbers before it,
  starting with 0 and 1 as the first two numbers of the sequence.
*/

const num1 = 0;
const expected1 = 0;

const num2 = 1;
const expected2 = 1;

const num3 = 2;
const expected3 = 1;

const num4 = 3;
const expected4 = 2;

const num5 = 4;
const expected5 = 3;

const num6 = 8;
const expected6 = 21;

function fibonacci(num) {
  //Base case
  if(num <= 1) {
    return num;
  }

  return fibonacci(num - 1) + fibonacci(num - 2);
}

console.log(fibonacci(num1))
console.log(fibonacci(num2))
console.log(fibonacci(num3))
console.log(fibonacci(num4))
console.log(fibonacci(num5))
console.log(fibonacci(num6))



/*
  Recursive Binary Search
  Input: SORTED array of ints, int value
  Output: bool representing if value is found
  Recursively search to find if the value exists, do not loop over every element.
  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

function binarySearch(sortedNums, searchNum) {
  //Base Case
  let found = false 
  if(sortedNums.length == 0) {    //if the array is 0 than the searchnum isnt in there
    return false
  }
  if(sortedNums.length == 1) {       //if the arr length is 1 check to see if searchnum in the there
    if(searchNum == sortedNums[0]) {    //if it is, return true
      return true                       //if not, return false
    } else {
      return false
    }
  }

  let middleIndex = Math.floor(sortedNums.length/2);     //set  variable that is the middle of the array to start

  if(searchNum == sortedNums[middleIndex]) {           //if the searchnum == the middle start point, return  true
    return true;
  } else if (searchNum > sortedNums[middleIndex]) {    //if its greater than the search number, re-run the function with the new range
    binarySearch(sortedNums.slice(middleIndex+1), searchNum)    //on the greater half of the arr
  } else {
    found = binarySearch(sortedNums.slice(0, middleIndex), searchNum) //if not than re-run the function with the lower half of the arr
  }                                                             //.slice() is making a new range of the arr, that we will run the new function from
  return found
}

console.log(binarySearch(nums1, searchNum1))
console.log(binarySearch(nums2, searchNum2))
console.log(binarySearch(nums3, searchNum3))


// start recursion at end of string ans go backwords, str.length-1

function reverseStr(str) {
  if(str == "") {
    return false
  }

  return reverseStr(str.substring(1))
}






function sumToOneDigit(num) {
  string_num = num.toString()
  sum = 0

  if (sum < 2 ) {
    sum = parseInt(string_num)
    return sum
  }
  sum += sumToOneDigit(parsInt(string_num.substring(0, string_num.length - 1)))
}






/*
  Given an array nested with unknown amount of arrays,
  return the integers all under ONE array.
*/

const arr1 = [1, 2, 3, 4, 5, 6];
const expected1 = [1, 2, 3, 4, 5, 6];

const arr2 = [1, 2, [4, 5], 6];
const expected2 = [1, 2, 4, 5, 6];

const arr3 = [1, 2, [3, 4, [5]], 6];
const expected3 = [1, 2, 3, 4, 5, 6];

/* 
  Two useful built in functions:
  Array.isArray() : returns true if argument is an array
    - Array.isArray([1, 2, 3]) => true
    - Array.isArray([4, 5, 6]) => true
    - Array.isArray(1) => false
  
  Array.concat() : concatenates two arrays together
    - arr1.concat(arr2) => [1, 2, 3, 4, 5, 6, 1, 2, [4, 5], 6]
*/

// function recursiveFlatten(arr) {
//   let result = []
//   if (arr && arr.length > 0) {
//     arr.forEach(function(value) {       //looping throught the array
//       if(Array.isArray(value)) {
//         result = result.concat(recursiveFlatten(value))      //if its an array it concats it 
//       } else {
//         result.push(value)
//       }
//     })
//   }
//   return result
// }

function newRecursiveFlatten(arr) {
  let result = []
  for (let i = 0; i < arr.length; i ++) {  //loop through the array for each index
    if(Array.isArray(arr[i])) {
      result = result.concat(newRecursiveFlatten(arr[i]))     //if the index is an array, concat the new array with the function 
    } else {
      result.push(arr[i])   //if the index is not an array, push it to the variable result(which in an empty array)
    }
  }
  return result
}


console.log(newRecursiveFlatten(arr1))
console.log(newRecursiveFlatten(arr2))
console.log(newRecursiveFlatten(arr3))
