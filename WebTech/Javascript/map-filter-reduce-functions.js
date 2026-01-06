//filter() function
let players = ["mike","Dustin","eleven","will","max","lucas","steve","nancy","jonathan","robin","hopper","joyce","karen","billy"]
let final_palyers = players.filter((player)=>{ return player.includes("i")})
console.log(final_palyers);

//map() function
let final_cast = players.map((x)=>{ return x.toUpperCase()})
console.log(final_cast);

//reduce() function
result = players.reduce((acc,x)=>{acc+x}," ")
console.log(result);