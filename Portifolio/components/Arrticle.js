export function Articles(targetId,Titulo,Conteudo,subtitle){
    let Get_targtet = document.getElementById(targetId)
    Get_targtet.innerHTML += ""+
   "<div class='card' style='width: 18rem;'>"
    +"<div class='card-body'>"
    +"<h5 class='card-title'>"+Titulo+"</h5>"
    +"<h6 class='card-subtitle mb-2 text-muted'>"+subtitle+"</h6>"
    +"<p class='card-text'>"+Conteudo+"</p>"
 +"</div>"
+"</div>"
}