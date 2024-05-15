export function Faq(){    
    document.getElementById("faq").innerHTML = 
    `   
    <link rel="stylesheet" href="./Assets/faq.css"> 
    <div class="accordion">
        <div class="img-box">
            <img src="./Assets/img/preguntas.jpg" alt="preguntas">
        </div>
    
    
    <div class="accordion-text">
        <div class="titulo">Preguntas Frecuentes</div>   

    <ul class="faq-text">
        <li>
            <div class="preguntas">
                <span class="texto">¿Cómo puedo contribuir a la sostenibilidad ambiental en Medellín?</span>
                <i class="bx bxs-chevron-down arrow"></i>
            </div>
            <p>Puedes contribuir adoptando prácticas sostenibles en tu vida diaria, como reducir el consumo de agua y energía, reciclar adecuadamente, utilizar el transporte público o bicicleta, y participar en actividades de voluntariado ambiental.</p>
            <span class="line"></span>
        </li>
        <li>
            <div class="preguntas">
                <span class="texto">¿Existen programas de educación ambiental disponibles para la comunidad en Medellín?</span>
                <i class="bx bxs-chevron-down arrow"></i>
            </div>
            <p>Sí, en Medellín se ofrecen programas de educación ambiental para todas las edades, que incluyen charlas, talleres, visitas guiadas a reservas naturales y actividades prácticas para fomentar la conciencia y el cuidado del medio ambiente.</p>
            <span class="line"></span>
        </li>
        <li>
            <div class="preguntas">
                <span class="texto">¿Qué tipo de análisis se utilizan para comprender y abordar los problemas ambientales?</span>
                <i class="bx bxs-chevron-down arrow"></i>
            </div>
            <p>Se recopilan datos sobre calidad del aire, niveles de contaminantes, consumo de recursos naturales y biodiversidad. Estos datos se analizan para identificar tendencias, evaluar impactos y diseñar estrategias efectivas para la protección del medio ambiente.</p>
            <span class="line"></span>
        </li>
        <li>
            <div class="preguntas">
                <span class="texto">¿Cuáles son los principales desafíos ambientales que enfrenta Medellín y cómo se abordan?</span>
                <i class="bx bxs-chevron-down arrow"></i>
            </div>
            <p>Medellín enfrenta desafíos como la contaminación del aire, la gestión de residuos y la deforestación. Estos problemas se abordan mediante la implementación de políticas ambientales integrales, proyectos de conservación de la biodiversidad y programas de educación ambiental para la comunidad.</p>
            <span class="line"></span>
        </li>
        <li>
            <div class="preguntas">
                <span class="texto">¿Cómo puedo obtener más información sobre proyectos y actividades relacionadas con la sostenibilidad ambiental en Medellín?</span>
                <i class="bx bxs-chevron-down arrow"></i>
            </div>
            <p>Puedes obtener más información a través de organizaciones ambientales locales, sitios web gubernamentales, redes sociales y eventos comunitarios. Además, puedes suscribirte a boletines informativos o participar en grupos de discusión en línea para mantenerte actualizado sobre iniciativas ambientales en la ciudad.</p>
            <span class="line"></span>
        </li>
    </ul> 
    </div>       
</div>
`
}