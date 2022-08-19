console.log('hi')

async function async_rick_morty(){
    let data = await fetch("https://rickandmortyapi.com/api/character")
    console.log(data)
    jsonData = await data.json()
    info = await jsonData
    console.log(info.results)
    info.results.forEach(element => {
        console.log(element)
        document.write(`<p>${element.name}</p>`)
    });

    return jsonData

}
async_rick_morty()