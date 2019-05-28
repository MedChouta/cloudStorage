var fileElt = document.getElementsByClassName('file')
var imgExtensions = ['jpg', 'png', 'bitmap', 'jpeg', 'tiff']
var Extensions = []

for(let i = 0; i < imgExtensions.length; i++){
    Extensions.push(imgExtensions[i].toUpperCase())
    Extensions.push(imgExtensions[i])
}

for(let i = 0; i < fileElt.length; i++){
    
    let files = fileElt[i].id.split('.')
    let extension = files[this.length + 1]

    if(Extensions.includes(extension)){
        fileElt[i].src = "static/img/icons/img.png"
    }
    else{
        fileElt[i].src = "static/img/icons/" + extension + ".png"
    }

    fileElt[i].onerror = function(){ fileElt[i].src = "static/img/icons/unknown.png" }
}

/***************************/

var forms = document.getElementsByClassName('form')
var inputs = document.getElementsByClassName('input')

for(let i = 0; i < forms.length; i++)
    inputs[i].onchange = () => {
    forms[i].submit()
}


/***************************/

var optionsExt = document.getElementById('ext')

for(let i = 0; i < imgExtensions.length; i++){
    let option = document.createElement('option')
    option.value = imgExtensions[i]
    option.text = imgExtensions[i]
    optionsExt.appendChild(option)

    console.log(optionsExt)
}