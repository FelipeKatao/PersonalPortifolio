var seguraAlgo = ""
MelanciaVerifica()
document.getElementById("btmelanc").addEventListener("click",()=>{
    if(seguraAlgo == "melancia")
    {
        seguraAlgo = ""
    }
    else
    {
        seguraAlgo = "melancia"
    }
    MelanciaVerifica()
})

function MelanciaVerifica(){
    if(seguraAlgo == "melancia")
    {
        document.getElementById("logica").innerHTML = "<h1> Melancias é bom </h1>"
    }
    else{
        document.getElementById("logica").innerHTML = "<h1> Não tem melancia </h1>"
    }
}
