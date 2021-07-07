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