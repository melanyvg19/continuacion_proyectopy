export function Dashboard(){    
    document.getElementById("dashboard").innerHTML = 
    `    
    <div id="encabezado">
        <h1>Dashboard</h1>
        <hr>
        <h2>Boletín Epidemiológico Medellín</h2>
    </div>
    <div class="dashboard-flex">  
        <div id="flexbox1"></div>
        <div id="flexbox2"></div>     
        <div id="flexbox3">
        <p>Aunque desde distintos sectores ambientalistas han reclamado que ante esta situación el Área Metropolitana del Valle de Aburrá tome algunas restricciones en cuanto al uso del carro o la práctica de actividades al aire libre, hasta el momento lo que ha dicho la entidad es que estos niveles de contaminación estaban pronosticados y le ha recomendado a la población disminuir el uso del carro particular y trabajar desde casa en caso de que sea posible, pero poco más.</p></div>
        <div id="flexbox4"></div>
        <cite>Tomado de <a href="https://www.medellin.gov.co/" target="_blank">www.medellin.gov.co</a></cite>
    </div>       
    `
}