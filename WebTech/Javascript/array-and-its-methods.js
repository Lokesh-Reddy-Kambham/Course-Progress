let players = ["Dhoni","virat","Smirti","Rahul","Nehra","GG"]

//pop() is used to remove last element by default
players.pop()
console.log(players);

//push is used to add element from last index
players.push("Bhuvi")
console.log(players);

//unshift() is used to add element from first index
players.unshift("Rahul Dravid")
console.log(players);

//shift is used to remove first element
players.shift()
console.log(players);

//splice is used to Remove sequence of elements , to Add , to Replace
players.splice(2,1) // Removed 
console.log(players);

players.splice(2,0,"Rohit Sharma","Travis Head") // Added
console.log(players);

players.splice(5,1,"jaiswal") // Replaced
console.log(players);