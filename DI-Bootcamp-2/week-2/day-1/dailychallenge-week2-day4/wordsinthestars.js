const answer = prompt("Type a few words separated by commas");

const words = answer.split(",");





const lengthOfLongestWord = getLengthOfLongestWord();


displayRows();


function displayRows(){
    const delimiterRow = createFirstRow();
    
    console.log(delimiterRow);

    for(const word of words){
        displayWord(word);
    }

    console.log(delimiterRow);
}




function displayWord(word){
    const numberOfSpacesToAdd = lengthOfLongestWord - word.length + 1;
    const emptySpaces = " ".repeat(numberOfSpacesToAdd)
    console.log("* " + word + emptySpaces + "*");
}










function getLengthOfLongestWord(){

    let lengthOfLongestWord = 0;
    
    for(const word of words){
        console.log(word);
    
        const wordLength = word.length;
    
        if (wordLength > lengthOfLongestWord) {
            lengthOfLongestWord = wordLength;
        }
      } 
      return lengthOfLongestWord;
    }



    function createFirstRow(){

        const numberOfStarOnFirstRow = lengthOfLongestWord + 4;

        let row = ""
    
        for (let i=0; i < numberOfStarOnFirstRow; i++) {
    
            row = row + "*";
        }
    
        return row
    }