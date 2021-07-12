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


