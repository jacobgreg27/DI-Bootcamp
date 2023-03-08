const button = getButton()

const shuffleButton = document.getElementById("shuffle")



button?.addEventListener("click", handleClick)

shuffleButton?.addEventListener("click", shuffleStories)


function getFormValues (){
    const noun = document.getElementById("noun").value

    const adjective = document.getElementById("adjective").value

    const person = document.getElementById("person").value

    const verb = document.getElementById("verb").value

    const place = document.getElementById("place").value

    return{
        noun : noun,
        adjective : adjective,
        person : person,
        verb : verb,
        place : place
    }
}







function handleClick(e) {
    e.preventDefault()
    const formValues = getFormValues()

    const noun = formValues.noun
    const adjective = formValues.adjective
    const person = formValues.person
    const verb = formValues.verb
    const place = formValues.place




    if (noun == "" || adjective == "" || person == "" || verb == "" || place == "")
    return

     const story = writeStory(noun, adjective, person, verb, place)
     console.log("story:", story)

     appendStoryToPage(story)
    
}

function shuffleStories(){
    const formValues = getFormValues()

    const noun = formValues.noun
    const adjective = formValues.adjective
    const person = formValues.person
    const verb = formValues.verb
    const place = formValues.place
   

    let story
    const randomNumber = generateRandomNumber()
    if(randomNumber === 1){
        story = writeStory(noun, adjective, person, verb, place)
    } else if (randomNumber === 2){
        story = writeStory2(noun, adjective, person, verb, place)
    } else {
        story = writeStory3(noun, adjective, person, verb, place)
    }
    appendStoryToPage(story)
}

function generateRandomNumber(){
    return Math.floor(Math.random() * 2) + 1
}


function appendStoryToPage(story){
    const paragraph = document.getElementById("story")
    const span = document.createElement("span")
    span.innerText = story
    paragraph.innerText = ""
    paragraph.appendChild(span)
}

function writeStory(noun, adjective, person, verb, place){
    return `I like to look at ${noun}s, I think that they are ${adjective}. My favorite person is ${person}. We often ${verb} together when we are in ${place}`
}

function writeStory2(noun, adjective, person, verb, place){
    return `I hate ${noun}s, I think that they are ${adjective}. My least favorite person is ${person}. We rarely ${verb} together when we are in ${place}`
}

function writeStory3(noun, adjective, person, verb, place){
    `I like to look at ${noun}s, I think that they are ${adjective}. My favorite place is ${place}. I like to ${verb} together with him. `
}


function getButton(){
    return document.getElementById("lib-button")
}