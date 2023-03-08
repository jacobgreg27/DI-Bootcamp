function isDivisible(){

    let sum = 0
  
  for (let i = 0; i < 500; i++){

    if(i % 23 === 0) {
      sum = sum + i

      console.log(i)
    }
    
  }
  console.log("the sum of numbers divisible by 23 is:", sum)
}

isDivisible()