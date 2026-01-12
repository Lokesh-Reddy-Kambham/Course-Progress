function login(){
            let users = JSON.parse(localStorage.getItem("users")) || []
             let username = document.getElementById("usr").value
             let password = document.getElementById("pwd").value

        let exists = users.some((x)=>{
            return x.username === username
        })
        if (exists){
            alert("username already exists")
            return 
        }
        let a = {
            username:username,
            password:password
        }
        users.push(a)
        localStorage.setItem("users",JSON.stringify(users))
        alert("user registered");
    }