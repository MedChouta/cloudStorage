class Form{

    constructor(title){
        this.title = title
        this.form = this.build()
    }

    build(){
        let formElt = document.createElement("form")
        let title = document.createElement("h1")
        let auth = document.getElementById("auth")
        
        formElt.method = "post"
        title.textContent = this.title
        //CSS
        formElt.classList.add("flex", "flex-col", "border", "shadow-lg", "p-2")
        formElt.setAttribute("data-aos", "flip-left")

        formElt.appendChild(title)
        auth.appendChild(formElt)

        return formElt
    }

    addInput(input){
        
        let pElt = document.createElement("p")
        let inputElt = document.createElement("input")
        inputElt.type = input.type
        inputElt.name = input.name
        inputElt.id = input.id
        inputElt.placeholder = input.placeholder
        inputElt.value = input.value

        if(inputElt.id === ""){
            inputElt.removeAttribute("id")
        }
        
        //CSS
        inputElt.classList.add("border", "rounded", "p-1", "bg-white")

        this.form.appendChild(inputElt)
        
        return inputElt 
    }

}

let login = new Form("Login")
login.addInput({type: "hidden", name: "login", id: "", placeholder:"", value:""})
login.addInput({type: "email", name: "email", id: "email", placeholder:"Email", value:""})
login.addInput({type: "password", name: "password", id: "", placeholder:"Password", value:""})

loginButton = login.addInput({type: "submit", name: "", id: "", placeholder:"", value:"Login"})

let register = new Form("Register")
register.addInput({type: "hidden", name: "register", id: "", placeholder:"", value:""})
register.addInput({type: "text", name: "firstName", id: "name", placeholder:"Your first name", value:""})
register.addInput({type: "text", name: "lastName", id: "", placeholder:"Your last name", value:""})
register.addInput({type: "email", name: "email", id: "", placeholder:"Your email address", value:""})
register.addInput({type: "password", name: "password", id: "", placeholder:"Choose a password", value:""})

registerButton = register.addInput({type: "submit", name: "", id: "", placeholder:"", value:"Register"})


loginButton.classList.add("button")
registerButton.classList.add("button")