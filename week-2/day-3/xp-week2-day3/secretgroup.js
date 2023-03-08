const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let themNames = ""

const sortin = names.sort()


for (const names of sortin) {
    console.log(names)
    themNames = themNames + names[0] 

}
console.log(themNames) 