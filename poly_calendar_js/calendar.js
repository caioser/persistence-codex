let div = document.querySelector("#container");
let hoje = Date.now();
const options = { weekday: "long" };
let diaSemana = new Intl.DateTimeFormat("pt-BR", options).format(hoje);
div.innerHTML = diaSemana + "<br>" + hoje;
