const planets = [
    {name : "Mercury", moons : 0}, 
    {name :"Venus", moons : 0}, 
    { name :"Earth", moons : 1}, 
    {name : "Mars", moons : 0}, 
    {name :"Jupiter", moons : 2}]

for (const planet of planets) {
    
    const div = document.createElement("div")
    div.classList.add("planet")
    div.classList.add(planet.name.toLowerCase())

    for(let i = 0; i < planet.moons; i++){
        const moonDiv = document.createElement("div")
        moonDiv.classList.add("moon")
        moonDiv.style.left = i * 10 + "px"
        div.appendChild(moonDiv)
    }

    const section = document.querySelector(".listPlanets")
    section?.appendChild(div)
}