const people = ["Greg", "Mary", "Devon", "James"];

people.shift(0);

console.log(people);

people.splice(2, 1, "Jason");

console.log(people);

people.push("Jacob");

console.log(people);

console.log(people.indexOf("Mary"));


people.slice(1);

console.log(people);

console.log(people.indexOf("Foo"));

// It is negative because the index of Foo does not exist in this array. 

const last = people[people.length - 1]

console.log(`last:`, last)

console.log(people)

for (let i = 0; i < people.length; i++){
     
    console.log(i,people[i])

    if(people[i] === "Jason") { break }
    
        
}

