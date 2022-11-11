 
var Elemento_escolhido = ""

var folha_elemento = document.getElementsByClassName("folha")[0]
var trevo_elemento = document.getElementsByClassName("trevo")[0]
var espiga_elemento = document.getElementsByClassName("espiga")[0]
 
 

 document.getElementById("espiga").addEventListener("click",()=>{

    if(Elemento_escolhido != "espiga" )
    {
        //Mudar o objeto Css colocando ou removendo a Classe
        espiga_elemento.classList.add("pill-02")
        trevo_elemento.classList.remove("pill-02")
        folha_elemento.classList.remove("pill-02")
        Elemento_escolhido = "espiga"
    }
    else
    {
            Elemento_escolhido = ""
            espiga_elemento.classList.remove("pill-02")

    }
 },false)

 document.getElementById("trevo").addEventListener("click",()=>{
    if(Elemento_escolhido != "trevo")
    {
        trevo_elemento.classList.add("pill-02")
        folha_elemento.classList.remove("pill-02")
        espiga_elemento.classList.remove("pill-02")
        Elemento_escolhido = "trevo"
    }
    else
    {
            Elemento_escolhido = ""
            trevo_elemento.classList.remove("pill-02")
    }


},false)

document.getElementById("folha").addEventListener("click",()=>{
    if(Elemento_escolhido != "folha")
    {
        folha_elemento.classList.add("pill-02")
        trevo_elemento.classList.remove("pill-02")
        espiga_elemento.classList.remove("pill-02")
        Elemento_escolhido = "folha"
    }
    else
    {
            Elemento_escolhido = ""
            folha_elemento.classList.remove("pill-02")
    }

    
},false)