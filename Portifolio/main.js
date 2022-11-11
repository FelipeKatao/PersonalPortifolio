import { Articles } from "./components/Arrticle.js"

document.getElementById("nameBt").addEventListener('click',()=>{
    let name = prompt("Say My name")
    if(name == 'Heisenberg')
    {
        var elemento = document.getElementsByClassName('dark')[0]
        elemento.style.opacity = 1
        var a =setInterval(()=>{
            elemento.style.opacity = 0.4
            document.getElementById("walterWhite").src = 'https://th.bing.com/th/id/R.7e57fa0234b42154813fe950fd184948?rik=cLm1yXlfB3UZ9w&pid=ImgRaw&r=0'
            document.getElementsByClassName("article-banner")[0].innerHTML = "<h1>Heisenberg</h1>"
            document.getElementsByClassName("article-banner")[0].innerHTML += "O Homem mais brabo do cartel de drogas de toda a albuquerque,matou gustavo,Tuco salamanca e entre outros, criador do cristal azul"
            clearInterval(a)
        },2000)
    }
    else
    {
        alert("Você errou")
    }

},false)

Articles("articles_base","Professor de Quimica","Sou professor de quimica a mais de 20 anos na escola secundaria de alburquerque    ","Professor graduado")
Articles("articles_base","CEO da Empresa Gray Matter","Criei a formula quimica que proprocionou para a empresa crescer bastante em menos de 3 anos","CEO")
Articles("articles_base","Fabricante de cristal","Criador do cristal usado na Gray Matter","Produtor")
Articles("articles_base","CEO de Lava jato","Responsavel por cuidar do Lava Jato Car Wash Class A1 no centro de Alburquerque.","CEO Lavajato")
