function changeEnough(itemPrice, amountOfChange){
    console.log("the item price", itemPrice)
    const sum = calculateSum(amountOfChange)
    if(sum > itemPrice){
        console.log("you can afford it")
        return true

    } else{
        console.log("you cannot afford it")
        return false
    }

}

function calculateSum(arr){
    let sum = 0

    for(let i = 0; i < arr.length; i++){
        let coinValue
        const numberOfCoins = arr[i]
       if(i === 0){ coinValue = 0.25}
       if(i === 1){ coinValue = 0.10}
       if(i === 2){ coinValue = 0.05}
       if(i === 3){ coinValue = 0.01}

       console.log("we have ", numberOfCoins, "coins that have a value of ", coinValue)
      
       sum = sum + numberOfCoins * coinValue

    }
     console.log("the total sum is", sum)

    return sum
}
changeEnough(4.25, [25, 20, 5, 0])