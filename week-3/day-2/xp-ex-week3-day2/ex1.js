const h1 = getFirstElement("h1")
const h2 = getFirstElement("h2")
const h3 = getFirstElement("h3")


removeLastLine()

addButton()






h2?.addEventListener("click", changeBackground)
h3?.addEventListener("click", hideH3)


function makeParagraphsBold(){
    const paragraphs = document.querySele("p")
    for (const paragraph of paragraphs ){
        paragraph.classList.add("bold")
    }
}

function addButton(){
    const button = document.createElement("button")
    button.textContent = "Make Everything Bold"
    button.addEventListener("click", makeParagraphsBold)
    const article = getFirstElement("article")
    article.appendChild(button)
}

function hideH3(){
    h3.classList.add("hide")
}




function changeBackground(){
    h2?.classList.add("red")
}


function removeLastLine(){
    const article = document.querySelector("article")
    article?.lastElementChild.remove()
}





function getFirstElement(selector){
    return document.querySelector(selector)
}


function getFirstH2(){
    return document.querySelector("article > h2")
}