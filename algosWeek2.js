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