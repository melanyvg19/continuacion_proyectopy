export function Header(){    
    document.getElementById("navbar").innerHTML = 
    `
  <nav>
   <ul class="menu-horizontal">
    <li>
        <a href="#">Menú</a>
        <ul class="menu-vertical">
            <li><a href="/index.html">Home</a></li>
            <li><a href="#dashboard">Dashboard</a></li>
            <li><a href="/components/quienesSomos.html">Acerca de</a></li>
        </ul>
    </li>
    <li>
        <a href="#">Servicios</a>
        <ul class="menu-vertical">
            <li><a href="#service">Informes de análisis</a></li>
            <li><a href="#service">Herramientas predictivas</a></li>            
        </ul>
    </li>
    <li>
        <a href="#">Datos</a>
        <ul class="menu-vertical">
            <li><a href="#datos">Origen</a></li>
            <li><a href="#datos">Importancia</a></li>
            <li><a href="#datos">Actualizaciones</a></li>
        </ul>
    </li>
    <li>
        <a href="#">Adicionales</a>
        <ul class="menu-vertical">
            <li><a href="#testimonios">Testimonio</a></li>
            <li><a href="#noticias">Noticias</a></li>
            <li><a href="#faq">FAQ</a></li>
            <li><a href="#recursos">Recursos educativos</a></li>
        </ul>
    </li>
   </ul>
    
     
  </nav>           
               
    `
}
    


