// Dmitry Dubrov

// Instructions
// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.

// Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).

// Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).

// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.
// Example:

//   Your string is : 'This dinner is not that bad ! You cook well', 
//   --> the result is : 'This dinner is good ! You cook well'

//   Your string is : 'This movie is not so bad !' 
//   --> the result is : 'This movie is good !'

//   Your string is : 'This dinner is bad !' 
//   --> the result is : 'This dinner is bad !'

function checkSentence(sentence) {
    
    let wordNot;
    wordNot = sentence.toLowerCase().indexOf('not');
    wordBad = sentence.toLowerCase().indexOf('bad');
    console.log(wordNot, wordBad);
    if (wordBad > wordNot && (wordBad != -1 && wordNot != -1)) {
        console.log('change');
        res = sentence.substring(0, wordNot) + 'good' + sentence.substring(wordBad + 3);
        return res
    }
    else {
        console.log('NO change');
        return sentence
    }
}

console.log(checkSentence('This dinner is not that bad ! You cook well !'))

console.log(checkSentence('This movie is not so bad !'))

console.log(checkSentence('This dinner is bad !'))

