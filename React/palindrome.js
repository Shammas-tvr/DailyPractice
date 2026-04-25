function palindrome(word){
    if (word.length <= 1){
        return true;
    }
    let right =0;
    let left = word.length-1;
    while (right < left){
        if (word[right] != word[left]){
            return false
        }
        right ++;
        left --;
    }
    return true
}

console.log(palindrome("malayalam"))