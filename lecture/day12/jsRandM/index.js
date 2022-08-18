console.log('test')

const data = fetch("https://rickandmortyapi.com/api/character")
.then(res => res.json())
.then(data => console.log(data.results))
.catch(err => console.log(err))


console.log(res)