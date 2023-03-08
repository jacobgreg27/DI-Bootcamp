hotelCost()

function hotelCost(numberOfNights){
  const costPerNight = 140
  const totalPrice = Number(numberOfNights) * costPerNight
  return totalPrice
}


function isOnlyNumbers(str){
    const regex = new RegExp(/^[0-9]*$/)
    return regex.test(str)
}

function includesNumbers(str){
    const regex = new RegExp(/\d/)
    return regex.test(str)
}


function plainRideCost(destination){
    if (destination === "London") return 183
    if (destination === "Paris") return 220
    return 300
}





function rentalCarCost(carAnswer){
    const dailyPrice = 40

    const numberOfDays = Number(carAnswer)

    let discount = 0

    if(numberOfDays >= 10) discount = 0.05

    const totalPrice = dailyPrice * numberOfDays * (1 - discount)

    return totalPrice
}















function totalVacationCost(){
    let hotelAnswer
    let carAnswer
    let destination = ""

    while(!isOnlyNumbers(hotelAnswer)){
        hotelAnswer = prompt("How many nights would you like to stay?")
    }

    while(!isOnlyNumbers(carAnswer)){
        carAnswer = prompt("How many nights would you like to stay?")
    }

    while(destination == "" || includesNumbers(destination)){
        destination = prompt("where are you going?")
    }

    const carPrice = rentalCarCost(carAnswer)
    const hotelPrice = hotelCost(hotelAnswer)
    const planePrice = plainRideCost(destination)

    console.log('hotelPrice:', hotelPrice)
    console.log('carPrice:', carPrice)
    console.log('planePrice:', planePrice)

    const totalPrice = carPrice + hotelPrice + planePrice
    console.log("total Price:", totalPrice)

   

}
totalVacationCost()