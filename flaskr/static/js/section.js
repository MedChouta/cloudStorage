class Section{
    
    constructor(title, text, img){
        this.title = title
        this.text = text
        this.img = img
    }

    build(){
        let sectionElt = document.createElement("section")
        let articleElt = document.createElement("article")
        let titleElt = document.createElement("h1")
        let divElt = document.createElement("div")
        let textElt = document.createElement("p")
        let aside = document.createElement("aside")
        let asideImg = document.createElement("img")



        //element class initialisation
        articleElt.classList.add("m-auto", "mt-4", "p-12", "w-5/6", "shadow-lg", "rounded-lg")
        divElt.classList.add("flex", "items-center", "justify-around")
        textElt.classList.add("w-1/3")
        asideImg.classList.add("rounded-lg")

        titleElt.textContent = this.title
        textElt.innerHTML = this.text
        
        asideImg.src = this.img.src
        asideImg.alt = this.img.alt

        sectionElt.setAttribute("data-aos","fade-right")
        sectionElt.classList.add("bg-white")

        aside.appendChild(asideImg)
        divElt.appendChild(textElt)
        divElt.appendChild(aside)
        articleElt.appendChild(titleElt)
        articleElt.appendChild(divElt)
        sectionElt.appendChild(articleElt)
        


        document.getElementById('presentation').appendChild(sectionElt)
    }
}

let text1 = `

File Encryption made easy with Crypto</br>
A file encryption utility using the secure AES-128 algorithm</br>
Available for: </br>

<img class="p-2" src="https://img.icons8.com/ios-glyphs/60/000000/linux.png" alt="Linux">
<img class="p-2" src="https://img.icons8.com/ios/50/000000/windows8-filled.png" alt="Windows">
<img class="p-2" src="https://img.icons8.com/ios-glyphs/50/000000/mac-client.png" alt="Mac">

`

let section = new Section("Keep your files secret", text1, {src: "/static/img/screenshot.png", alt: "Utility screenshot"})
section.build()

let text2 = `

With CryptonCloud,store you files and access them wherever and whenever you want for free.</br>
You can also combine Crypton with CryptonCloud to store your files directly from the utility

`

let section2 = new Section("Never lose your files", text2, {src: "/static/img/secure.png", alt: "illustration"})
section2.build()