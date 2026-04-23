function reverse_str(str){
    let reversed_str=""
    
    for (let i=str.length -1; i>=0; i--){
       reversed_str+=str[i]

    }
    return reversed_str

}

console.log(reverse_str("shammas"))