let z = 6

let string = "";

for (let i = 1; i <= z; i++) {
    for (let j = 0; j < i; j++){
        string +="*";
    }
    string += "\n";
}

console.log(string);

