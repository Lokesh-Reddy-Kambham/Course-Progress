//taking input from user
let a = prompt("Enter Something:")
console.log(a);
let num1 = Number(prompt("Enter a Number:"))
let num2 = Number(prompt("Enter a Number:"))
console.log(num1 + num2);

//conditinal statements
let age = Number(prompt("Enter Number"))
if (age >= 21) {
console.log("You are Eligible for marriage");
}
else if (age >=18) {
console.log("You are Eligible for voting & Driving");
}
else {
    console.log("You are Eligible for nothing , So wait and come");
}

//ternary operator
gender = prompt("Enter M for Male or F for Female").toLowerCase()
console.log(gender=="m" ? "Male" : "Female");
