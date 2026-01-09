//object which is in the form of key & value pair,In two ways we can declare objects
//1. using Curly Braces { }
let user_data = {
    name : "Vasco De Gama",
    age  : 23,
    email : "obscure@gmail.com",
    address : {
        city : "Bangalore",
        state : "Karnataka"
    }
}
//2.object constructor 
let employee = new Object(
    {id : 1,
    name : "Lokesh",
    role : "Full Stack",
    skills : {
        languages : ["Python","JavaScript","Java" ] ,
        database : ["MYSQL","SQL"] ,
        frontend : ["HTML","CSS"]
    }
    }
)
// key - value pair is called as property of an object
// Fetch properties of an object in two ways

//1. Dot Notation
console.log(user_data.address.city);
console.log(employee.name);

//2. Square Brackets 
console.log(employee["role"]);
console.log(employee["skills"]["languages"]);

//object methods 
console.log(Object.keys(user_data));
console.log(Object.values(employee));
console.log(Object.entries(employee));

