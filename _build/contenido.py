# -*- coding: utf-8 -*-
"""
CONTENIDO DE LAS 6 MARCAS DE LICICON
====================================
Aquí se edita TODO el texto. Después corre:  python _build/build.py
y se regeneran las páginas de cada marca, sus blogs, el blog general,
el sitemap.xml y el robots.txt.

Para agregar un artículo: copia un bloque dentro de "posts" de la marca,
cambia slug / titulo / fecha / resumen / cuerpo, y vuelve a correr el build.
"""

SITIO = "https://www.licicon.com"
WHATSAPP = "5215521379039"
TELEFONO = "+52 55 2137 9039"
EMAIL = "contactolicicon@licicon.com"
AUTOR = "Roberto Amaral Ponce"
# Domicilio para el aviso de privacidad: escribe la dirección completa (calle, número, colonia, C.P., municipio).
DOMICILIO = "Toluca, Estado de México"
AVISO_FECHA = "29 de septiembre de 2026"
ZONA = ["Toluca", "Metepec", "Estado de México", "Ciudad de México"]

MARCAS = [
# ---------------------------------------------------------------- EJE LEGAL
{
 "slug": "eje-legal",
 "area": "Derecho",
 "resumen_home": "Asesoría legal personal y empresarial con enfoque preventivo: contratos, cumplimiento laboral REPSE, protección de datos personales y programas de compliance.",
 "nombre": "Eje Legal",
 "tema": "eje",
 "logo": "eje-legal.jpg",
 "logo_bg": "#fcf9f4",
 "fuente_titulos": "Playfair Display",
 "tipo_schema": "LegalService",
 "titulo_seo": "Eje Legal | Abogado en Toluca y Metepec · Asesoría legal y empresarial",
 "desc_seo": "Asesoría legal personal y empresarial en Toluca, Metepec y CDMX: contratos, cumplimiento REPSE, protección de datos personales y compliance. Explicaciones claras, enfoque preventivo.",
 "linea": "Asesoría legal personal y empresarial",
 "h1": "Asesoría legal clara, antes de que el problema llegue",
 "lead": "Contratos, cumplimiento laboral y fiscal, protección de datos y defensa de tu patrimonio. Te explicamos qué dice la ley y qué te conviene hacer, sin tecnicismos.",
 "servicios": [
   {"n": "Asesoría legal integral", "c": "Una consulta para entender tu situación y tus opciones.",
    "d": "Revisamos tu caso, te explicamos los riesgos reales y las rutas posibles con costos y tiempos estimados. Sirve para personas y para empresas que necesitan una segunda opinión antes de firmar o decidir.",
    "i": ["Diagnóstico por escrito", "Opciones con pros y contras", "Seguimiento por WhatsApp"]},
   {"n": "Contratos", "c": "Redacción y revisión de contratos que sí te protegen.",
    "d": "Arrendamiento, prestación de servicios, compraventa, confidencialidad, obra y sociedades. Cuidamos cláusulas de pago, penalizaciones, terminación y jurisdicción, que es donde se pierden los juicios.",
    "i": ["Revisión de contratos que te envían", "Contratos a la medida", "Plantillas para tu negocio"]},
   {"n": "Cumplimiento REPSE", "c": "Si subcontratas o prestas servicios especializados.",
    "d": "Registro y renovación ante la STPS, revisión de objeto social, contratos de servicios especializados y control documental de tus proveedores para no perder deducciones ni asumir responsabilidad solidaria.",
    "i": ["Registro y renovación REPSE", "Revisión de proveedores", "Contratos de servicios especializados"]},
   {"n": "Protección de datos personales", "c": "Avisos de privacidad y cumplimiento de la ley de datos.",
    "d": "Si tu negocio recaba nombres, teléfonos o correos, la ley te obliga a informar para qué los usas. Elaboramos tu aviso de privacidad, tus políticas internas y el procedimiento para atender solicitudes ARCO.",
    "i": ["Aviso de privacidad integral y simplificado", "Políticas internas", "Procedimiento ARCO"]},
   {"n": "Compliance empresarial", "c": "Orden legal para empresas que quieren crecer sin sustos.",
    "d": "Diagnóstico de obligaciones legales según tu giro, mapa de riesgos y programa de cumplimiento con referencia a ISO 37301 e ISO 31000. Puedes empezar con un diagnóstico inicial sin costo.",
    "i": ["Diagnóstico normativo", "Matriz de riesgos", "Programa de cumplimiento"]},
 ],
 "pasos": [
   ("Escuchamos", "Nos cuentas tu situación por WhatsApp o en una llamada breve."),
   ("Diagnosticamos", "Te decimos qué dice la ley, qué riesgo tienes y qué opciones hay."),
   ("Actuamos", "Redactamos, presentamos o negociamos con un costo acordado desde el inicio."),
   ("Prevenimos", "Te dejamos documentado lo necesario para que no vuelva a pasar."),
 ],
 "faq": [
   ("¿Atienden en línea o solo en Toluca?", "Atendemos en Toluca, Metepec y Ciudad de México, y la mayoría de asesorías y revisiones de contratos se resuelven en línea."),
   ("¿Cuánto cuesta una consulta?", "Depende del asunto. Antes de empezar te damos el costo por escrito, para que no haya sorpresas."),
   ("¿Mi pequeño negocio necesita aviso de privacidad?", "Sí, si recabas datos personales de clientes o empleados, aunque sea un nombre y un teléfono en WhatsApp."),
 ],
 "posts": [
  {"slug": "repse-que-exige-hoy-a-empresas-que-subcontratan",
   "titulo": "¿Tu empresa subcontrata? Lo que hoy exige el REPSE",
   "fecha": "2026-09-29",
   "resumen": "Desde la reforma de 2021 la subcontratación de personal está prohibida. Qué sí se permite, qué pide el REPSE y qué riesgos corre quien contrata.",
   "keywords": "REPSE, subcontratación, servicios especializados, STPS, responsabilidad solidaria",
   "cuerpo": """
<p>La reforma laboral de 2021 cambió la forma en que las empresas en México pueden apoyarse en terceros. Muchas siguen operando como antes, y el riesgo no recae solo en el proveedor: también en quien lo contrata.</p>
<h2>Qué quedó prohibido</h2>
<p>Está prohibido que una empresa ponga trabajadores a disposición de otra para que trabajen bajo su mando. Es decir, la subcontratación de personal. Lo que sí se permite es contratar <strong>servicios u obras especializadas</strong>, siempre que no formen parte del objeto social ni de la actividad económica preponderante de quien los recibe.</p>
<h2>Qué es el REPSE</h2>
<p>El Registro de Prestadoras de Servicios Especializados u Obras Especializadas lo lleva la Secretaría del Trabajo. Todo proveedor de servicios especializados debe estar inscrito, y el registro se renueva cada tres años.</p>
<h2>Por qué te importa si tú eres quien contrata</h2>
<ul>
<li><strong>Responsabilidad solidaria:</strong> si tu proveedor no paga salarios, IMSS o INFONAVIT de sus trabajadores, te pueden exigir a ti esas obligaciones.</li>
<li><strong>Deducciones fiscales:</strong> los pagos a un proveedor que no cumple pueden no ser deducibles, y el IVA puede no ser acreditable.</li>
<li><strong>Multas:</strong> la subcontratación de personal se sanciona con multas altas, calculadas en UMAs.</li>
</ul>
<h2>Revisión mínima de cada proveedor</h2>
<ol>
<li>Que tenga registro REPSE vigente y que el servicio que te presta esté dentro de lo registrado.</li>
<li>Que el contrato sea por escrito, describa el servicio especializado y el número estimado de trabajadores.</li>
<li>Que te entregue periódicamente sus comprobantes de cumplimiento ante IMSS, INFONAVIT y SAT.</li>
<li>Que el servicio no sea parte de tu actividad preponderante; si lo es, esos trabajadores deberían ser tuyos.</li>
</ol>
<h2>Si prestas servicios especializados</h2>
<p>Revisa que tu objeto social los contemple, que tu registro esté vigente y que presentes en tiempo los informes periódicos ante IMSS e INFONAVIT. Un registro vencido puede costarte clientes grandes, que ya lo piden como requisito.</p>
<p>En Eje Legal hacemos el registro, la renovación y la revisión de proveedores. Si no sabes si tu esquema cumple, escríbenos y lo revisamos contigo.</p>
"""},
 ],
},
# ---------------------------------------------------------------- INNOVA WEB
{
 "slug": "innova-web",
 "area": "Tecnología",
 "resumen_home": "Diseño y desarrollo de sitios, tiendas en línea y sistemas a la medida, con SEO técnico y cumplimiento legal integrados desde el primer día.",
 "nombre": "Innova Web Studio",
 "tema": "innova",
 "logo": "innova-web.jpg",
 "logo_bg": "#030406",
 "fuente_titulos": "Montserrat",
 "tipo_schema": "ProfessionalService",
 "titulo_seo": "Innova Web Studio | Diseño de páginas web en Toluca y Metepec",
 "desc_seo": "Diseño de páginas web, tiendas en línea y SEO en Toluca, Metepec y CDMX. Sitios rápidos, adaptados a celular y con aviso de privacidad incluido.",
 "linea": "Diseño y desarrollo web",
 "h1": "Páginas web rápidas, que se encuentran en Google y venden",
 "lead": "Diseñamos y programamos sitios, tiendas en línea y sistemas a la medida. Cada proyecto sale con su aviso de privacidad y lo básico de SEO resuelto desde el día uno.",
 "servicios": [
   {"n": "Diseño web", "c": "Un sitio con identidad propia, no una plantilla más.",
    "d": "Partimos de tu marca y de lo que tu cliente necesita encontrar para decidir. Diseñamos la estructura, los textos clave y la interfaz antes de programar.",
    "i": ["Estructura y textos", "Diseño visual a tu marca", "Dominio y correo profesional"]},
   {"n": "Páginas web responsivas", "c": "Que se vean y funcionen bien en cualquier celular.",
    "d": "La mayoría de tus visitas llegan desde el teléfono. Probamos cada página en pantallas chicas, con botones de WhatsApp y llamada al alcance del pulgar.",
    "i": ["Diseño mobile first", "Botón de WhatsApp", "Mapa y datos de contacto"]},
   {"n": "Tiendas online", "c": "Vende en línea con pagos, envíos e inventario.",
    "d": "Configuramos tu tienda en Shopify o a la medida, con catálogo, pasarela de pago, envíos y políticas de compra y devolución.",
    "i": ["Catálogo y variantes", "Pagos y envíos", "Políticas de tienda"]},
   {"n": "Velocidad y rendimiento", "c": "Un sitio lento pierde visitas y posiciones.",
    "d": "Optimizamos imágenes, carga de fuentes y código para que tu sitio abra rápido incluso con datos móviles. Medimos antes y después.",
    "i": ["Optimización de imágenes", "Medición de Core Web Vitals", "Hosting adecuado"]},
   {"n": "SEO y posicionamiento", "c": "Que te encuentren quienes ya te están buscando.",
    "d": "Configuramos títulos, descripciones, datos estructurados, sitemap y Google Search Console, y te ayudamos a planear contenido para búsquedas locales.",
    "i": ["SEO técnico", "Google Business Profile", "Plan de contenido"]},
   {"n": "Soporte y mantenimiento", "c": "Tu sitio actualizado, respaldado y funcionando.",
    "d": "Cambios de contenido, respaldos, renovación de dominio y atención a fallas con un pago mensual fijo.",
    "i": ["Cambios mensuales", "Respaldos", "Atención por WhatsApp"]},
 ],
 "pasos": [
   ("Brief", "Entendemos tu negocio, tu cliente y lo que el sitio debe lograr."),
   ("Diseño", "Te mostramos la propuesta visual y la ajustamos contigo."),
   ("Desarrollo", "Programamos, cargamos contenido y probamos en celular."),
   ("Publicación", "Conectamos dominio, Search Console y te entregamos accesos."),
 ],
 "faq": [
   ("¿Cuánto tarda una página web?", "Un sitio informativo suele quedar en dos a tres semanas si el contenido está listo. Tiendas y sistemas dependen del alcance."),
   ("¿El dominio queda a mi nombre?", "Sí. El dominio y los accesos son tuyos."),
   ("¿Por qué incluyen aviso de privacidad?", "Porque si tu sitio tiene formulario o WhatsApp estás recabando datos personales, y la ley te obliga a informarlo. Detrás del estudio hay un abogado."),
 ],
 "posts": [
  {"slug": "que-debe-tener-la-pagina-web-de-un-negocio",
   "titulo": "Qué debe tener la página web de un negocio (y qué le sobra)",
   "fecha": "2026-09-29",
   "resumen": "Siete elementos que hacen que una página web genere clientes, y los adornos que solo la hacen más lenta.",
   "keywords": "página web para negocio, diseño web Toluca, página web PyME",
   "cuerpo": """
<p>Una página web no es un folleto digital. Es el lugar donde alguien que ya te encontró decide si te escribe o se va con la competencia. Esto es lo que no puede faltar.</p>
<h2>Lo indispensable</h2>
<ol>
<li><strong>Qué haces y dónde, en la primera pantalla.</strong> “Taller mecánico en Metepec” funciona mejor que “Soluciones automotrices integrales”.</li>
<li><strong>Un botón de contacto visible.</strong> En México ese botón casi siempre es WhatsApp, con un mensaje ya escrito.</li>
<li><strong>Que cargue rápido en celular.</strong> Si tarda más de tres segundos, una parte importante de las visitas se va antes de ver algo.</li>
<li><strong>Pruebas de que eres real:</strong> fotos propias, dirección, horario, reseñas o casos.</li>
<li><strong>Una página por servicio importante.</strong> Google posiciona páginas, no sitios completos; una página sobre “remodelación de cocinas” tiene más posibilidades que un listado genérico.</li>
<li><strong>Aviso de privacidad.</strong> Si tienes formulario, chat o WhatsApp, recabas datos personales y la ley te obliga a informar cómo los usas.</li>
<li><strong>Google Search Console y Google Business Profile</strong> configurados, para saber cómo te encuentran y aparecer en el mapa.</li>
</ol>
<h2>Lo que suele sobrar</h2>
<ul>
<li>Pantallas de carga y animaciones largas: retrasan lo que el cliente vino a ver.</li>
<li>Carruseles automáticos que nadie mira más allá de la primera imagen.</li>
<li>Textos llenos de palabras que tu cliente no usa para buscarte.</li>
<li>Fotos de banco de imágenes que se ven en otros cien sitios.</li>
</ul>
<h2>Cómo saber si tu sitio actual funciona</h2>
<p>Ábrelo desde tu celular con datos móviles y cuenta cuánto tarda. Luego busca en Google tu servicio más tu ciudad. Si no apareces en la primera página, o si tu sitio tarda en abrir, hay trabajo por hacer.</p>
<p>En Innova Web Studio revisamos tu sitio sin costo y te decimos qué cambiar, aunque no trabajes con nosotros.</p>
"""},
 ],
},
# ---------------------------------------------------------------- BOSS STUDIO
{
 "slug": "boss-studio",
 "area": "Marketing",
 "resumen_home": "Gestión de redes sociales, contenido y publicidad digital para negocios que quieren ser la primera opción de su cliente.",
 "nombre": "Boss Studio",
 "tema": "boss",
 "logo": "boss-studio.jpg",
 "logo_bg": "#050608",
 "fuente_titulos": "Montserrat",
 "tipo_schema": "ProfessionalService",
 "titulo_seo": "Boss Studio | Manejo de redes sociales para negocios en Toluca y Metepec",
 "desc_seo": "Gestión de redes sociales, contenido, publicidad en Facebook e Instagram y WhatsApp Business para negocios en Toluca, Metepec y CDMX.",
 "linea": "Redes sociales y marketing para negocios",
 "h1": "Que te recuerden cuando te necesiten",
 "lead": "Manejamos las redes sociales de tu negocio: contenido, promociones, publicidad y WhatsApp Business, para que tus clientes piensen en ti primero.",
 "servicios": [
   {"n": "Gestión de redes sociales", "c": "Publicamos por ti con un calendario claro.",
    "d": "Planeamos el mes, diseñamos y publicamos en Facebook, Instagram y TikTok. Tú apruebas antes de que salga.",
    "i": ["Calendario mensual", "Diseño de publicaciones", "Publicación y programación"]},
   {"n": "Creación de contenido", "c": "Fotos, videos y reels de tu negocio real.",
    "d": "Hacemos sesiones en tu negocio para tener material propio: producto, equipo, proceso. El contenido real vende más que el de stock.",
    "i": ["Sesiones de foto y video", "Reels y videos cortos", "Tomas con dron"]},
   {"n": "Publicidad digital", "c": "Anuncios en Meta dirigidos a tu zona.",
    "d": "Campañas en Facebook e Instagram segmentadas por colonia, edad e intereses, con presupuesto controlado y reporte de lo que se gastó y lo que regresó.",
    "i": ["Campañas locales", "Promociones", "Reporte de resultados"]},
   {"n": "Estrategia de marca", "c": "Cómo quieres que te recuerden.",
    "d": "Definimos tono, mensajes clave, lema y estilo visual para que todo lo que publicas se sienta de la misma marca.",
    "i": ["Tono y mensajes", "Lema", "Guía visual básica"]},
   {"n": "Comunidad y WhatsApp Business", "c": "Responder rápido también es marketing.",
    "d": "Configuramos WhatsApp Business con catálogo, respuestas rápidas, etiquetas y listas de difusión, y te ayudamos a responder comentarios y mensajes.",
    "i": ["Catálogo y respuestas rápidas", "Listas de difusión", "Atención de comentarios"]},
   {"n": "Análisis y resultados", "c": "Qué funcionó y qué no, cada mes.",
    "d": "Un reporte sencillo con alcance, mensajes recibidos y promociones que generaron ventas, para decidir el siguiente mes con datos.",
    "i": ["Reporte mensual", "Recomendaciones", "Ajuste de estrategia"]},
 ],
 "pasos": [
   ("Conocemos tu negocio", "Visitamos, probamos tu producto y vemos quién te compra."),
   ("Planeamos el mes", "Calendario con temas, promociones y fechas clave."),
   ("Producimos y publicamos", "Fotos, video y publicaciones aprobadas por ti."),
   ("Medimos", "Revisamos resultados y ajustamos."),
 ],
 "faq": [
   ("¿Trabajan solo con restaurantes?", "No. Trabajamos con cualquier negocio local: comida, servicios, tiendas, consultorios y más."),
   ("¿El presupuesto de anuncios está incluido?", "No. El presupuesto de anuncios se paga directo a Meta y tú decides cuánto; nosotros lo administramos."),
   ("¿Tengo que firmar por un año?", "No. Trabajamos por mes para que te quedes por resultados."),
 ],
 "posts": [
  {"slug": "whatsapp-business-para-que-tus-clientes-regresen",
   "titulo": "Cómo usar WhatsApp Business para que tus clientes regresen",
   "fecha": "2026-09-29",
   "resumen": "Catálogo, respuestas rápidas, etiquetas y listas de difusión: cinco ajustes que convierten tu WhatsApp en una herramienta de ventas.",
   "keywords": "WhatsApp Business, marketing para negocios locales, listas de difusión, redes sociales Toluca",
   "cuerpo": """
<p>Para un negocio local en México, WhatsApp es el mostrador digital. Casi todas las redes sociales terminan ahí: el cliente ve la promoción en Facebook y escribe por WhatsApp. Si esa conversación no está bien atendida, la publicidad se desperdicia.</p>
<h2>1. Perfil completo</h2>
<p>Horario, dirección con ubicación en el mapa, descripción corta y enlace a tu página o redes. Un perfil vacío da desconfianza.</p>
<h2>2. Catálogo</h2>
<p>Sube tus productos o servicios con foto y precio. Ahorra preguntas repetidas y deja que el cliente elija antes de escribirte.</p>
<h2>3. Respuestas rápidas</h2>
<p>Crea atajos para lo que más te preguntan: horario, ubicación, formas de pago, costo de envío. Contestar en segundos cambia la venta.</p>
<h2>4. Etiquetas</h2>
<p>Marca a cada contacto como “nuevo cliente”, “pedido pendiente” o “cliente frecuente”. Así sabes a quién darle seguimiento y a quién mandarle qué promoción.</p>
<h2>5. Listas de difusión, con permiso</h2>
<p>Las listas de difusión solo llegan a quien tiene tu número guardado, por eso funcionan mejor con clientes que ya te conocen. Úsalas para promociones concretas, no para saturar: una o dos veces por semana es suficiente.</p>
<h2>Un detalle legal que casi nadie cuida</h2>
<p>Los números y nombres de tus clientes son datos personales. Si los usas para enviar promociones, tu negocio debería contar con un aviso de privacidad que lo explique. Es sencillo de resolver y te protege.</p>
<h2>Cómo medirlo</h2>
<p>Cuenta cada semana cuántos mensajes recibiste, cuántos se convirtieron en venta y cuántos clientes volvieron a comprar. Con eso sabes si tus redes están funcionando.</p>
<p>En Boss Studio configuramos tu WhatsApp Business junto con tus redes para que todo trabaje en la misma dirección.</p>
"""},
 ],
},
# ---------------------------------------------------------------- PUNTO INMUEBLES
{
 "slug": "punto-inmuebles",
 "area": "Inmobiliario",
 "resumen_home": "Compra, venta, renta y administración de inmuebles con revisión legal de cada operación y acompañamiento hasta la firma.",
 "nombre": "Punto Inmuebles",
 "tema": "inmuebles",
 "logo": "punto-inmuebles.jpg",
 "logo_bg": "#f7f4ef",
 "fuente_titulos": "Montserrat",
 "tipo_schema": "RealEstateAgent",
 "titulo_seo": "Punto Inmuebles | Venta y renta de casas en Toluca, Metepec y Edomex",
 "desc_seo": "Compra, venta y renta de inmuebles en Toluca, Metepec y el Estado de México, con asesoría personalizada y revisión legal de cada operación.",
 "linea": "Soluciones inmobiliarias",
 "h1": "Compra, vende o renta tu inmueble con respaldo legal",
 "lead": "Te acompañamos de principio a fin: precio, promoción, documentos y firma. Cada operación pasa por una revisión legal para que cierres sin sorpresas.",
 "servicios": [
   {"n": "Asesoría personalizada", "c": "Antes de vender o comprar, entiende tus números.",
    "d": "Analizamos el inmueble, la zona y tu objetivo para definir un precio realista y la mejor estrategia: vender, rentar o esperar.",
    "i": ["Opinión de valor", "Estrategia de venta o renta", "Estimación de gastos e impuestos"]},
   {"n": "Compra, venta y renta", "c": "Promoción, visitas y negociación.",
    "d": "Fotografía, publicación en portales, filtro de interesados, visitas y negociación. Te informamos de cada avance.",
    "i": ["Fotos y publicación", "Filtro de prospectos", "Negociación"]},
   {"n": "Gestión integral", "c": "Administración de inmuebles en renta.",
    "d": "Cobro de rentas, contratos, mantenimiento y atención a inquilinos para propietarios que no quieren ocuparse del día a día.",
    "i": ["Cobranza", "Mantenimiento", "Renovación de contratos"]},
   {"n": "Revisión legal de la operación", "c": "Documentos y contratos revisados por abogado.",
    "d": "Revisamos escrituras, gravámenes, contratos de promesa y arrendamiento, con apoyo de Eje Legal, para que el patrimonio quede protegido.",
    "i": ["Revisión de escrituras", "Contratos de promesa y arrendamiento", "Acompañamiento con notario"]},
   {"n": "Soluciones a tu medida", "c": "Herencias, copropiedad y casos especiales.",
    "d": "Inmuebles intestados, con varios dueños o con documentación incompleta. Te decimos qué hay que regularizar antes de venderlo.",
    "i": ["Diagnóstico documental", "Ruta de regularización", "Venta una vez regularizado"]},
 ],
 "pasos": [
   ("Diagnóstico", "Revisamos inmueble, documentos y objetivo."),
   ("Precio y estrategia", "Definimos precio, canales y tiempos."),
   ("Promoción", "Publicamos, filtramos y mostramos."),
   ("Cierre", "Negociación, contrato y firma ante notario."),
 ],
 "faq": [
   ("¿Cobran por publicar mi casa?", "Nuestra comisión se paga al cerrar la operación. Te la damos por escrito desde el inicio."),
   ("¿Qué pasa si mi casa tiene papeles incompletos?", "La revisamos y te decimos qué hay que regularizar antes de venderla."),
   ("¿Trabajan fuera de Toluca?", "Nos enfocamos en Toluca, Metepec y el Estado de México, y atendemos inmuebles en otros estados según el caso."),
 ],
 "posts": [
  {"slug": "documentos-para-vender-tu-casa-estado-de-mexico",
   "titulo": "Documentos para vender tu casa en el Estado de México",
   "fecha": "2026-09-29",
   "resumen": "La lista de papeles que te pedirá el notario y los que conviene tener antes de publicar, para no perder a un comprador por un trámite pendiente.",
   "keywords": "vender casa Estado de México, documentos venta casa, notario Toluca, IFREM",
   "cuerpo": """
<p>Muchas ventas se caen no por el precio, sino porque el vendedor tarda semanas en reunir documentos cuando el comprador ya está listo. Tenerlos antes de publicar acelera todo.</p>
<h2>Del inmueble</h2>
<ul>
<li><strong>Escritura</strong> inscrita en el Instituto de la Función Registral del Estado de México (IFREM).</li>
<li><strong>Boleta predial</strong> pagada al año en curso.</li>
<li><strong>Recibo de agua</strong> sin adeudo; el notario suele pedir constancia de no adeudo.</li>
<li><strong>Certificado de libertad de gravámenes</strong>, que confirma que no hay hipotecas ni embargos. Normalmente lo solicita el notario.</li>
<li>Si es departamento o condominio: constancia de no adeudo de cuotas de mantenimiento.</li>
</ul>
<h2>Del vendedor</h2>
<ul>
<li>Identificación oficial vigente, CURP y constancia de situación fiscal.</li>
<li>Acta de nacimiento y, si eres casado, acta de matrimonio: el régimen matrimonial define si tu cónyuge debe firmar.</li>
<li>Comprobante de domicilio, importante si buscas la exención de ISR por venta de casa habitación.</li>
</ul>
<h2>Si la casa está a crédito</h2>
<p>Pide a tu banco, INFONAVIT o FOVISSSTE el estado de adeudo. Se puede vender con crédito vigente, pero la deuda se liquida en la operación y el trámite de cancelación de hipoteca toma tiempo.</p>
<h2>Casos que requieren más tiempo</h2>
<ul>
<li>Casas heredadas sin juicio sucesorio terminado.</li>
<li>Construcciones que no aparecen en la escritura.</li>
<li>Inmuebles con varios dueños que no están de acuerdo.</li>
</ul>
<p>En esos casos conviene regularizar antes de publicar. El costo del trámite casi siempre es menor que lo que se pierde en precio vendiendo con problemas.</p>
<p>Esta guía es general; cada notaría puede pedir requisitos adicionales. En Punto Inmuebles revisamos tus documentos sin costo antes de poner tu casa en venta.</p>
"""},
 ],
},
# ---------------------------------------------------------------- PLANO Y OBRA
{
 "slug": "plano-y-obra",
 "area": "Construcción",
 "resumen_home": "Construcción residencial y comercial, remodelación integral y control digital de obra, con presupuesto por conceptos y bitácora con evidencia.",
 "nombre": "Plano y Obra",
 "tema": "plano",
 "logo": "plano-y-obra.jpg",
 "logo_bg": "#f5f4f1",
 "fuente_titulos": "Montserrat",
 "tipo_schema": "GeneralContractor",
 "titulo_seo": "Plano y Obra | Construcción y remodelación en Toluca y Metepec",
 "desc_seo": "Construcción residencial y comercial, remodelación integral y control de obra en Toluca, Metepec y el Estado de México. Del plano a la realidad, con presupuesto bajo control.",
 "linea": "Construcción y remodelación",
 "h1": "Del plano a la realidad, con el presupuesto bajo control",
 "lead": "Construimos y remodelamos espacios residenciales y comerciales con un proceso claro: catálogo de conceptos, avance medido y bitácora con evidencia.",
 "servicios": [
   {"n": "Construcción residencial", "c": "Tu casa desde cero o una ampliación.",
    "d": "Coordinamos proyecto, permisos y ejecución, con presupuesto por conceptos y calendario de obra desde el inicio.",
    "i": ["Casa nueva", "Ampliaciones y segundos niveles", "Permisos y licencias"]},
   {"n": "Construcción comercial", "c": "Locales, oficinas y naves.",
    "d": "Adecuación de locales y oficinas con tiempos cortos y coordinación con tu operación para no detener el negocio.",
    "i": ["Locales y oficinas", "Adecuaciones", "Obra por etapas"]},
   {"n": "Remodelación integral", "c": "Cocinas, baños, fachadas e interiores.",
    "d": "Diseño, demolición, instalaciones y acabados con un solo responsable, para que no tengas que coordinar cinco proveedores.",
    "i": ["Cocinas y baños", "Instalaciones", "Acabados"]},
   {"n": "Planeación y ejecución", "c": "Presupuesto, programa y supervisión.",
    "d": "Catálogo de conceptos, programa de obra y supervisión técnica. Útil también si ya tienes constructor y quieres a alguien de tu lado.",
    "i": ["Catálogo de conceptos", "Programa de obra", "Supervisión"]},
   {"n": "Control de obra digital", "c": "Ve el avance y el gasto de tu obra en tiempo real.",
    "d": "Nuestra plataforma propia registra el avance diario contra el catálogo, alerta desviaciones de costo y guarda la bitácora con fotos. Al final tienes un expediente completo.",
    "i": ["Avance diario", "Alertas de costo", "Bitácora con fotos"]},
 ],
 "pasos": [
   ("Levantamiento", "Visitamos, medimos y entendemos lo que necesitas."),
   ("Presupuesto por conceptos", "Cada partida con cantidad y precio, sin paquetes opacos."),
   ("Ejecución", "Obra con programa, supervisión y bitácora."),
   ("Entrega", "Recorrido final, garantía y expediente de obra."),
 ],
 "faq": [
   ("¿El presupuesto puede cambiar?", "Solo si cambia el alcance. Cualquier cambio se presupuesta y se aprueba por escrito antes de ejecutarlo."),
   ("¿Tramitan la licencia de construcción?", "Sí, te apoyamos con los trámites municipales cuando la obra los requiere."),
   ("¿Cómo pago?", "Por estimaciones contra avance real, no por adelantado completo."),
 ],
 "posts": [
  {"slug": "remodelar-sin-que-se-dispare-el-presupuesto",
   "titulo": "Remodelar tu casa sin que se dispare el presupuesto: 5 controles",
   "fecha": "2026-09-29",
   "resumen": "Por qué las remodelaciones casi siempre cuestan más de lo previsto y cinco controles simples para evitarlo.",
   "keywords": "remodelación casa Toluca, presupuesto de obra, control de obra, remodelación Metepec",
   "cuerpo": """
<p>“Íbamos a gastar la mitad” es la frase más común al terminar una remodelación. Casi nunca es mala fe: es falta de control desde el inicio. Estos son los cinco controles que usamos en cada obra.</p>
<h2>1. Presupuesto por conceptos, no por paquete</h2>
<p>Un presupuesto que dice “remodelación de cocina: $180,000” no te protege. Pide un catálogo con cada concepto, su unidad, cantidad y precio: demolición por metro cuadrado, azulejo colocado, salidas eléctricas. Así sabes exactamente qué pagas y puedes comparar.</p>
<h2>2. Alcance por escrito</h2>
<p>Define qué incluye y qué no: marca de materiales, retiro de escombro, instalaciones ocultas. Lo que no está escrito es lo que después se cobra como extra.</p>
<h2>3. Pagos contra avance</h2>
<p>Paga un anticipo razonable y después por estimaciones: el avance que realmente se ejecutó, medido. Nunca pagues el total por adelantado.</p>
<h2>4. Bitácora con fotos</h2>
<p>Registra cada día qué se hizo, con fotos, sobre todo de lo que quedará oculto: tuberías, cableado, impermeabilización. Si algo falla, la bitácora es tu evidencia.</p>
<h2>5. Reserva para imprevistos</h2>
<p>Al abrir muros o pisos aparecen sorpresas. Aparta un porcentaje del presupuesto para imprevistos y úsalo solo con cambios aprobados por escrito.</p>
<h2>Antes de empezar: permisos</h2>
<p>Si la obra toca estructura, fachada o amplía metros construidos, es probable que necesites licencia de construcción en tu municipio. Una obra sin permiso puede ser suspendida y complicar la venta futura del inmueble.</p>
<p>En Plano y Obra llevamos estos controles en nuestra plataforma de control de obra, y tú puedes ver el avance y el gasto desde tu celular.</p>
"""},
 ],
},
# ---------------------------------------------------------------- PUNTO CONTROL
{
 "slug": "punto-control",
 "area": "Administración",
 "resumen_home": "Administración, contabilidad y facturación para pequeñas y medianas empresas, con reportes mensuales para decidir con datos.",
 "nombre": "Punto Control",
 "tema": "control",
 "logo": "punto-control.jpg",
 "logo_bg": "#f9f9f9",
 "fuente_titulos": "Montserrat",
 "tipo_schema": "ProfessionalService",
 "titulo_seo": "Punto Control | Administración, contabilidad y facturación para PyMEs",
 "desc_seo": "Administración, contabilidad, facturación CFDI y control financiero para pequeñas y medianas empresas en Toluca, Metepec y CDMX.",
 "linea": "Administración y contabilidad",
 "h1": "Tu negocio en orden: cuentas claras, decisiones con datos",
 "lead": "Administración, contabilidad y facturación para pequeñas y medianas empresas. Sabes cuánto ganas, cuánto debes y cuánto te deben, cada mes.",
 "servicios": [
   {"n": "Administración", "c": "Procesos, cuentas por cobrar y por pagar.",
    "d": "Ordenamos cómo entra y sale el dinero de tu negocio: cobranza, pagos a proveedores, caja chica y calendario de obligaciones.",
    "i": ["Cuentas por cobrar y pagar", "Calendario de pagos", "Control de caja"]},
   {"n": "Contabilidad", "c": "Tu contabilidad al día y tus declaraciones a tiempo.",
    "d": "Registro contable mensual, conciliaciones bancarias y declaraciones, para que el SAT no sea una sorpresa.",
    "i": ["Contabilidad mensual", "Conciliación bancaria", "Declaraciones"]},
   {"n": "Facturación CFDI", "c": "Facturas correctas, sin cancelaciones ni rechazos.",
    "d": "Emisión de facturas, complementos de pago y notas de crédito, y revisión de lo que recibes para que sea deducible.",
    "i": ["Facturas y complementos de pago", "Revisión de facturas recibidas", "Cancelaciones"]},
   {"n": "Control y crecimiento", "c": "Números para decidir, no solo para cumplir.",
    "d": "Presupuesto, flujo de efectivo y márgenes por producto o servicio, para saber qué te deja dinero y qué no.",
    "i": ["Flujo de efectivo", "Presupuesto", "Márgenes"]},
   {"n": "Reportes de resultados", "c": "Un tablero mensual que sí entiendes.",
    "d": "Cada mes recibes un resumen con ventas, gastos, utilidad y pendientes, explicado en lenguaje sencillo.",
    "i": ["Reporte mensual", "Indicadores clave", "Reunión de revisión"]},
 ],
 "pasos": [
   ("Diagnóstico", "Revisamos tu situación fiscal y cómo llevas tus números hoy."),
   ("Orden", "Ponemos al día contabilidad, facturas y cuentas."),
   ("Operación mensual", "Registro, facturación y declaraciones cada mes."),
   ("Reporte", "Resultados y recomendaciones para decidir."),
 ],
 "faq": [
   ("¿Trabajan con personas físicas?", "Sí, con personas físicas con actividad empresarial, RESICO y personas morales."),
   ("Tengo meses atrasados, ¿me pueden ayudar?", "Sí. Primero regularizamos los periodos pendientes y después seguimos mes a mes."),
   ("¿Necesito cambiar de sistema?", "No necesariamente. Trabajamos con lo que ya usas y te proponemos cambios solo si te ahorran tiempo."),
 ],
 "posts": [
  {"slug": "errores-de-facturacion-y-control-que-cuestan-dinero",
   "titulo": "6 errores de facturación y control que le cuestan dinero a una PyME",
   "fecha": "2026-09-29",
   "resumen": "Facturas mal emitidas, cuentas personales mezcladas y cobranza sin seguimiento: los errores más comunes y cómo evitarlos.",
   "keywords": "facturación CFDI 4.0, contabilidad PyME, control financiero, contador Toluca",
   "cuerpo": """
<p>La mayoría de los problemas con el SAT y de las fugas de dinero en un negocio pequeño no vienen de fraudes, sino de hábitos. Estos son los seis que más vemos.</p>
<h2>1. Datos del cliente que no coinciden</h2>
<p>En CFDI 4.0 el nombre, RFC, código postal y régimen fiscal del receptor deben coincidir con su constancia de situación fiscal. Pide la constancia a cada cliente nuevo y guárdala; te ahorra cancelaciones.</p>
<h2>2. Olvidar los complementos de pago</h2>
<p>Si emites una factura con método de pago en parcialidades o diferido (PPD), cuando te pagan debes emitir el complemento de pago. Sin él, tu cliente puede tener problemas para deducir, y tú un pendiente con el SAT.</p>
<h2>3. Mezclar cuentas personales y del negocio</h2>
<p>Pagar gastos personales desde la cuenta del negocio, o al revés, hace imposible saber cuánto gana realmente tu empresa y complica justificar depósitos ante el SAT.</p>
<h2>4. No conciliar el banco cada mes</h2>
<p>Comparar tus movimientos bancarios contra tus facturas emitidas y recibidas detecta a tiempo cobros no facturados, pagos duplicados y gastos sin comprobante.</p>
<h2>5. Aceptar facturas sin revisar</h2>
<p>Una factura con uso de CFDI incorrecto o de un proveedor con problemas ante el SAT puede no ser deducible. Revísalas al recibirlas, no al cerrar el año.</p>
<h2>6. Cobrar sin seguimiento</h2>
<p>Vender mucho y cobrar tarde es una de las causas más comunes de falta de efectivo. Una lista semanal de cuentas por cobrar, con fechas y responsables, cambia el flujo del negocio.</p>
<h2>Por dónde empezar</h2>
<p>Separa cuentas, pide constancias fiscales a tus clientes y dedica una hora al mes a conciliar. Si no tienes tiempo, en Punto Control lo hacemos por ti y te entregamos un reporte que se entiende.</p>
"""},
 ],
},
]


# ------------------------------------------------------------------
# DESARROLLOS PROPIOS (se muestran en el inicio de licicon.com)
# Quita o edita los que no quieras hacer públicos.
# ------------------------------------------------------------------
PROYECTOS = [
  {"nombre": "Comanda", "tipo": "Punto de venta para restaurantes",
   "desc": "Toma de pedidos por mesero, pantalla de cocina en tiempo real y control de ventas. Se entrega como app operativa con su propia instancia por cliente.",
   "marca": "innova-web"},
  {"nombre": "Jun 順", "tipo": "Gestión de mesa para alta cocina",
   "desc": "Control de servicio por mesa con asignación de cada platillo a cada comensal, pensado para restaurantes de servicio fino y sommeliers.",
   "marca": "innova-web"},
  {"nombre": "Homoni", "tipo": "Plataforma de telemedicina",
   "desc": "Consulta médica por video, expediente y agenda en una sola plataforma, con tratamiento de datos de salud conforme a la ley.",
   "marca": "innova-web"},
  {"nombre": "Legal y Orden", "tipo": "Gestión de despachos jurídicos",
   "desc": "Expedientes, plazos, clientes y documentos de un despacho en un mismo sistema, con portal para el cliente en marca blanca.",
   "marca": "eje-legal"},
  {"nombre": "Contratto", "tipo": "Generación automatizada de contratos",
   "desc": "Contratos laborales y comerciales generados a partir de plantillas validadas, con datos capturados una sola vez y cero errores de transcripción.",
   "marca": "eje-legal"},
  {"nombre": "Control digital de obra", "tipo": "Supervisión de construcción",
   "desc": "Catálogo de conceptos, avance diario, alertas de desviación de costo y bitácora con evidencia fotográfica para cada obra.",
   "marca": "plano-y-obra"},
]

# ------------------------------------------------------------------
# CASOS (se muestran en el inicio). Confirma con cada cliente que
# acepta aparecer. No agregues cifras que no puedas comprobar.
# ------------------------------------------------------------------
CASOS = [
  {"cliente": "MARXION", "sector": "Agencia de branding y marketing", "lugar": "México",
   "firmas": ["innova-web", "eje-legal"],
   "reto": "Una agencia de marca necesitaba un sitio a la altura del trabajo que vende a sus clientes y una base legal sólida para su relación comercial con ellos.",
   "hicimos": "Diseñamos y desarrollamos su sitio, configuramos su dominio y lo publicamos en infraestructura de alto rendimiento. En paralelo, Eje Legal preparó su propuesta de iguala y el paquete documental para operar con clientes.",
   "entregables": ["Sitio web corporativo", "Dominio marxion.mx", "Paquete documental legal"],
   "url": "https://marxion.mx", "estado": ""},
  {"cliente": "iReanimación", "sector": "Capacitación en emergencias médicas", "lugar": "Ciudad de México",
   "firmas": ["innova-web"],
   "reto": "Una institución de capacitación clínica en urgencias y reanimación necesitaba mostrar su oferta de cursos y mantener su calendario al día sin depender de un programador para cada fecha nueva.",
   "hicimos": "Desarrollamos su sitio institucional e integramos su calendario de Google: cada curso que el equipo agenda aparece publicado automáticamente, organizado por mes y por tipo de capacitación.",
   "entregables": ["Sitio institucional", "Calendario de cursos automático", "Integración a medida con Google"],
   "url": "https://reanimacion.org", "estado": ""},
  {"cliente": "Medical Summit Cozumel", "sector": "Congreso médico internacional", "lugar": "Cozumel, Quintana Roo",
   "firmas": ["innova-web"],
   "reto": "Un congreso médico internacional requería un sitio capaz de presentar a sus ponentes, publicar el programa y recibir registros, y de crecer conforme se confirmaba la agenda.",
   "hicimos": "Construimos el sitio oficial del congreso con perfiles de ponentes, agenda, registro de asistentes y sección de patrocinadores, con actualizaciones continuas durante la preparación del evento.",
   "entregables": ["Sitio oficial del congreso", "Perfiles de ponentes y agenda", "Registro y patrocinadores"],
   "url": "https://ms-cozumel.org", "estado": ""},
  {"cliente": "Dúo Raíces", "sector": "Artesanía y cerámica mexicana", "lugar": "México",
   "firmas": ["innova-web"],
   "reto": "Una marca de cerámica y talavera vendía en Shopify con una plantilla genérica que no contaba la historia artesanal detrás de cada pieza.",
   "hicimos": "Diseñamos una portada propia para la marca y la integramos al tema de Shopify como secciones editables: historia, pilares, manifiesto, colección y valores, sin perder las funciones de la tienda.",
   "entregables": ["Diseño de portada de marca", "Secciones Shopify a la medida", "Tienda editable por la clienta"],
   "url": "", "estado": ""},
  {"cliente": "SPIMEX", "sector": "Mantenimiento, automatización y obra civil industrial", "lugar": "Tula de Allende, Hidalgo",
   "firmas": ["innova-web"],
   "reto": "Una empresa de servicios industriales necesitaba presentar con claridad sus capacidades técnicas ante clientes corporativos y licitaciones.",
   "hicimos": "Desarrollamos su sitio corporativo con la presentación de sus líneas de servicio, experiencia y canales de contacto directo para áreas de compras.",
   "entregables": ["Sitio corporativo", "Presentación de servicios industriales", "Contacto para compras"],
   "url": "", "estado": "En curso"},
]

# ------------------------------------------------------------------
# TESTIMONIOS — SOLO opiniones reales, con autorización por escrito.
# La sección del inicio aparece automáticamente cuando hay al menos uno.
# Ejemplo:
#   {"texto": "Lo que dijo la persona, tal cual.", "nombre": "Nombre A.",
#    "rol": "Dueña de negocio, Metepec", "firma": "boss-studio"},
# ------------------------------------------------------------------
TESTIMONIOS = [
]

# Contenido revisado y cartera completa.
MARCAS = [{'slug': 'eje-legal',
  'area': 'Derecho',
  'resumen_home': 'Asesoría legal personal y empresarial con enfoque preventivo: contratos, cumplimiento '
                  'laboral REPSE, protección de datos personales y programas de compliance.',
  'nombre': 'Eje Legal',
  'tema': 'eje',
  'logo': 'eje-legal.jpg',
  'logo_bg': '#fcf9f4',
  'fuente_titulos': 'Playfair Display',
  'tipo_schema': 'LegalService',
  'titulo_seo': 'Eje Legal | Abogado en Toluca y Metepec · Asesoría legal y empresarial',
  'desc_seo': 'Asesoría legal personal y empresarial en Toluca, Metepec y CDMX: contratos, cumplimiento '
              'REPSE, protección de datos personales y compliance. Explicaciones claras, enfoque preventivo.',
  'linea': 'Asesoría legal personal y empresarial',
  'h1': 'Asesoría legal clara, antes de que el problema llegue',
  'lead': 'Contratos, cumplimiento laboral y fiscal, protección de datos y defensa de tu patrimonio. Te '
          'explicamos qué dice la ley y qué te conviene hacer, sin tecnicismos.',
  'servicios': [{'n': 'Asesoría legal integral',
                 'c': 'Una consulta para entender tu situación y tus opciones.',
                 'd': 'Revisamos tu caso, te explicamos los riesgos reales y las rutas posibles con costos y '
                      'tiempos estimados. Sirve para personas y para empresas que necesitan una segunda '
                      'opinión antes de firmar o decidir.',
                 'i': ['Diagnóstico por escrito', 'Opciones con pros y contras', 'Seguimiento por WhatsApp']},
                {'n': 'Contratos',
                 'c': 'Redacción y revisión para precisar tus acuerdos.',
                 'd': 'Arrendamiento, prestación de servicios, compraventa, confidencialidad, obra y '
                      'sociedades. Cuidamos cláusulas de pago, penalizaciones, terminación y jurisdicción, '
                      'según el objeto y los riesgos del acuerdo.',
                 'i': ['Revisión de contratos que te envían',
                       'Contratos a la medida',
                       'Plantillas para tu negocio']},
                {'n': 'Cumplimiento REPSE',
                 'c': 'Si subcontratas o prestas servicios especializados.',
                 'd': 'Registro y renovación ante la STPS, revisión de objeto social, contratos de servicios '
                      'especializados y control documental de tus proveedores para identificar requisitos y '
                      'riesgos aplicables a cada contratación.',
                 'i': ['Registro y renovación REPSE',
                       'Revisión de proveedores',
                       'Contratos de servicios especializados']},
                {'n': 'Protección de datos personales',
                 'c': 'Avisos de privacidad y cumplimiento de la ley de datos.',
                 'd': 'Si tu negocio recaba nombres, teléfonos o correos, la ley te obliga a informar para '
                      'qué los usas. Elaboramos tu aviso de privacidad, tus políticas internas y el '
                      'procedimiento para atender solicitudes ARCO.',
                 'i': ['Aviso de privacidad integral y simplificado',
                       'Políticas internas',
                       'Procedimiento ARCO']},
                {'n': 'Compliance empresarial',
                 'c': 'Orden legal para empresas que quieren crecer sin sustos.',
                 'd': 'Diagnóstico de obligaciones legales según tu giro, mapa de riesgos y programa de '
                      'cumplimiento con referencia a ISO 37301 e ISO 31000. El alcance del diagnóstico se '
                      'acuerda antes de iniciar.',
                 'i': ['Diagnóstico normativo', 'Matriz de riesgos', 'Programa de cumplimiento']}],
  'pasos': [('Escuchamos', 'Nos cuentas tu situación por WhatsApp o en una llamada breve.'),
            ('Diagnosticamos', 'Te decimos qué dice la ley, qué riesgo tienes y qué opciones hay.'),
            ('Actuamos', 'Redactamos, presentamos o negociamos con un costo acordado desde el inicio.'),
            ('Prevenimos', 'Documentamos medidas preventivas y los pendientes que requieren seguimiento.')],
  'faq': [('¿Atienden en línea o solo en Toluca?',
           'Atendemos en Toluca, Metepec y Ciudad de México, y la mayoría de asesorías y revisiones de '
           'contratos se resuelven en línea.'),
          ('¿Cuánto cuesta una consulta?',
           'Depende del asunto. Antes de empezar te damos el costo por escrito, para que no haya sorpresas.'),
          ('¿Mi pequeño negocio necesita aviso de privacidad?',
           'Sí, si recabas datos personales de clientes o empleados, aunque sea un nombre y un teléfono en '
           'WhatsApp.')],
  'posts': [{'slug': 'repse-que-exige-hoy-a-empresas-que-subcontratan',
             'titulo': '¿Tu empresa subcontrata? Lo que hoy exige el REPSE',
             'fecha': '2026-09-29',
             'resumen': 'Desde la reforma de 2021 la subcontratación de personal está prohibida. Qué sí se '
                        'permite, qué pide el REPSE y qué riesgos corre quien contrata.',
             'keywords': 'REPSE, subcontratación, servicios especializados, STPS, responsabilidad solidaria',
             'cuerpo': '\n'
                       '<p>La reforma laboral de 2021 cambió la forma en que las empresas en México pueden '
                       'apoyarse en terceros. Muchas siguen operando como antes, y el riesgo no recae solo '
                       'en el proveedor: también en quien lo contrata.</p>\n'
                       '<h2>Qué quedó prohibido</h2>\n'
                       '<p>El artículo 12 de la Ley Federal del Trabajo prohíbe la subcontratación de '
                       'personal, entendida como proporcionar o poner a disposición trabajadores propios en '
                       'beneficio de otra persona. Es decir, la subcontratación de personal. Lo que sí se '
                       'permite es contratar <strong>servicios u obras especializadas</strong>, siempre que '
                       'no formen parte del objeto social ni de la actividad económica preponderante de '
                       'quien los recibe.</p>\n'
                       '<h2>Qué es el REPSE</h2>\n'
                       '<p>El Registro de Prestadoras de Servicios Especializados u Obras Especializadas lo '
                       'lleva la Secretaría del Trabajo. La obligación debe revisarse cuando se ponen '
                       'trabajadores propios a disposición de un tercero y en los demás supuestos '
                       'aplicables. El registro se renueva cada tres años.</p>\n'
                       '<h2>Por qué te importa si tú eres quien contrata</h2>\n'
                       '<ul>\n'
                       '<li><strong>Responsabilidad solidaria:</strong> si tu proveedor no paga salarios, '
                       'IMSS o INFONAVIT de sus trabajadores, te pueden exigir a ti esas obligaciones.</li>\n'
                       '<li><strong>Deducciones fiscales:</strong> los pagos a un proveedor que no cumple '
                       'pueden no ser deducibles, y el IVA puede no ser acreditable.</li>\n'
                       '<li><strong>Multas:</strong> la subcontratación de personal se sanciona con multas '
                       'altas, calculadas en UMAs.</li>\n'
                       '</ul>\n'
                       '<h2>Revisión mínima de cada proveedor</h2>\n'
                       '<ol>\n'
                       '<li>Que tenga registro REPSE vigente y que el servicio que te presta esté dentro de '
                       'lo registrado.</li>\n'
                       '<li>Que el contrato sea por escrito, describa el servicio especializado y el número '
                       'estimado de trabajadores.</li>\n'
                       '<li>Que te entregue periódicamente sus comprobantes de cumplimiento ante IMSS, '
                       'INFONAVIT y SAT.</li>\n'
                       '<li>Que el servicio no sea parte de tu actividad preponderante; revisa también el '
                       'objeto social de la beneficiaria y la naturaleza real de la contratación.</li>\n'
                       '</ol>\n'
                       '<h2>Si prestas servicios especializados</h2>\n'
                       '<p>Revisa que tu objeto social los contemple, que tu registro esté vigente y que '
                       'presentes en tiempo los informes periódicos ante IMSS e INFONAVIT. Un registro '
                       'vencido puede costarte clientes grandes, que ya lo piden como requisito.</p>\n'
                       '<p>En Eje Legal hacemos el registro, la renovación y la revisión de proveedores. Si '
                       'no sabes si tu esquema cumple, escríbenos y lo revisamos contigo.</p>\n'
                       '<p>Fuentes: <a href="https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf">Ley '
                       'Federal del Trabajo, artículos 12 a 15</a> y <a '
                       'href="https://repse.stps.gob.mx/">preguntas frecuentes oficiales del REPSE</a>. La '
                       'revisión de una contratación requiere analizar sus hechos y documentos.</p>'}]},
 {'slug': 'innova-web',
  'area': 'Tecnología',
  'resumen_home': 'Diseño y desarrollo de sitios, tiendas en línea y sistemas a la medida, con SEO técnico y '
                  'organización documental según el alcance del proyecto.',
  'nombre': 'Innova Web Studio',
  'tema': 'innova',
  'logo': 'innova-web.jpg',
  'logo_bg': '#030406',
  'fuente_titulos': 'Montserrat',
  'tipo_schema': 'ProfessionalService',
  'titulo_seo': 'Innova Web Studio | Diseño de páginas web en Toluca y Metepec',
  'desc_seo': 'Diseño de páginas web, tiendas en línea y SEO en Toluca, Metepec y CDMX. Sitios rápidos, '
              'adaptados a celular y con aviso de privacidad incluido.',
  'linea': 'Diseño y desarrollo web',
  'h1': 'Páginas web con identidad, claridad y una base técnica para crecer',
  'lead': 'Diseñamos y programamos sitios, tiendas en línea y sistemas a la medida. Cada proyecto sale con '
          'su aviso de privacidad y lo básico de SEO resuelto desde el día uno.',
  'servicios': [{'n': 'Diseño web',
                 'c': 'Un sitio con identidad propia, no una plantilla más.',
                 'd': 'Partimos de tu marca y de lo que tu cliente necesita encontrar para decidir. '
                      'Diseñamos la estructura, los textos clave y la interfaz antes de programar.',
                 'i': ['Estructura y textos', 'Diseño visual a tu marca', 'Dominio y correo profesional']},
                {'n': 'Páginas web responsivas',
                 'c': 'Que se vean y funcionen bien en cualquier celular.',
                 'd': 'La mayoría de tus visitas llegan desde el teléfono. Probamos cada página en pantallas '
                      'chicas, con botones de WhatsApp y llamada al alcance del pulgar.',
                 'i': ['Diseño mobile first', 'Botón de WhatsApp', 'Mapa y datos de contacto']},
                {'n': 'Tiendas online',
                 'c': 'Vende en línea con pagos, envíos e inventario.',
                 'd': 'Configuramos tu tienda en Shopify o a la medida, con catálogo, pasarela de pago, '
                      'envíos y políticas de compra y devolución.',
                 'i': ['Catálogo y variantes', 'Pagos y envíos', 'Políticas de tienda']},
                {'n': 'Velocidad y rendimiento',
                 'c': 'Un sitio lento pierde visitas y posiciones.',
                 'd': 'Optimizamos imágenes, carga de fuentes y código para que tu sitio abra rápido incluso '
                      'con datos móviles. Medimos antes y después.',
                 'i': ['Optimización de imágenes', 'Medición de Core Web Vitals', 'Hosting adecuado']},
                {'n': 'SEO y posicionamiento',
                 'c': 'Que te encuentren quienes ya te están buscando.',
                 'd': 'Configuramos títulos, descripciones, datos estructurados, sitemap y Google Search '
                      'Console, y te ayudamos a planear contenido para búsquedas locales.',
                 'i': ['SEO técnico', 'Google Business Profile', 'Plan de contenido']},
                {'n': 'Soporte y mantenimiento',
                 'c': 'Tu sitio actualizado, respaldado y funcionando.',
                 'd': 'Cambios de contenido, respaldos, renovación de dominio y atención a fallas con un '
                      'pago mensual fijo.',
                 'i': ['Cambios mensuales', 'Respaldos', 'Atención por WhatsApp']}],
  'pasos': [('Brief', 'Entendemos tu negocio, tu cliente y lo que el sitio debe lograr.'),
            ('Diseño', 'Te mostramos la propuesta visual y la ajustamos contigo.'),
            ('Desarrollo', 'Programamos, cargamos contenido y probamos en celular.'),
            ('Publicación', 'Conectamos dominio, Search Console y te entregamos accesos.')],
  'faq': [('¿Cuánto tarda una página web?',
           'Un sitio informativo suele quedar en dos a tres semanas si el contenido está listo. Tiendas y '
           'sistemas dependen del alcance.'),
          ('¿El dominio queda a mi nombre?', 'Sí. El dominio y los accesos son tuyos.'),
          ('¿Por qué incluyen aviso de privacidad?',
           'Porque si tu sitio tiene formulario o WhatsApp estás recabando datos personales, y la ley te '
           'obliga a informarlo. Detrás del estudio hay un abogado.')],
  'posts': [{'slug': 'que-debe-tener-la-pagina-web-de-un-negocio',
             'titulo': 'Qué debe tener la página web de un negocio (y qué le sobra)',
             'fecha': '2026-09-29',
             'resumen': 'Siete elementos que hacen que una página web genere clientes, y los adornos que '
                        'solo la hacen más lenta.',
             'keywords': 'página web para negocio, diseño web Toluca, página web PyME',
             'cuerpo': '\n'
                       '<p>Una página web no es un folleto digital. Es el lugar donde alguien que ya te '
                       'encontró decide si te escribe o se va con la competencia. Esto es lo que no puede '
                       'faltar.</p>\n'
                       '<h2>Lo indispensable</h2>\n'
                       '<ol>\n'
                       '<li><strong>Qué haces y dónde, en la primera pantalla.</strong> “Taller mecánico en '
                       'Metepec” funciona mejor que “Soluciones automotrices integrales”.</li>\n'
                       '<li><strong>Un botón de contacto visible.</strong> En México ese botón casi siempre '
                       'es WhatsApp, con un mensaje ya escrito.</li>\n'
                       '<li><strong>Que cargue rápido en celular.</strong> Una carga lenta puede dificultar '
                       'la consulta y aumentar el abandono.</li>\n'
                       '<li><strong>Pruebas de que eres real:</strong> fotos propias, dirección, horario, '
                       'reseñas o casos.</li>\n'
                       '<li><strong>Una página por servicio importante.</strong> Una página específica '
                       'permite explicar mejor cada servicio y atender búsquedas relacionadas; el '
                       'posicionamiento depende también de contenido, competencia y otros factores.</li>\n'
                       '<li><strong>Aviso de privacidad.</strong> Si mediante formularios, chat o WhatsApp '
                       'tratas datos personales, revisa las obligaciones de información y privacidad '
                       'aplicables.</li>\n'
                       '<li><strong>Google Search Console y Google Business Profile</strong> configurados, '
                       'para saber cómo te encuentran y aparecer en el mapa.</li>\n'
                       '</ol>\n'
                       '<h2>Lo que suele sobrar</h2>\n'
                       '<ul>\n'
                       '<li>Pantallas de carga y animaciones largas: retrasan lo que el cliente vino a '
                       'ver.</li>\n'
                       '<li>Carruseles automáticos que nadie mira más allá de la primera imagen.</li>\n'
                       '<li>Textos llenos de palabras que tu cliente no usa para buscarte.</li>\n'
                       '<li>Fotos de banco de imágenes que se ven en otros cien sitios.</li>\n'
                       '</ul>\n'
                       '<h2>Cómo saber si tu sitio actual funciona</h2>\n'
                       '<p>Ábrelo desde tu celular con datos móviles y cuenta cuánto tarda. Luego busca en '
                       'Google tu servicio más tu ciudad. Si no apareces en la primera página, o si tu sitio '
                       'tarda en abrir, hay trabajo por hacer.</p>\n'
                       '<p>En Innova Web Studio podemos revisar tu sitio y acordar contigo una propuesta de '
                       'mejora.</p>\n'}]},
 {'slug': 'boss-studio',
  'area': 'Marketing',
  'resumen_home': 'Gestión de redes sociales, contenido y publicidad digital para negocios que quieren ser '
                  'la primera opción de su cliente.',
  'nombre': 'Boss Social Studio',
  'tema': 'boss',
  'logo': 'boss-studio.jpg',
  'logo_bg': '#050608',
  'fuente_titulos': 'Montserrat',
  'tipo_schema': 'ProfessionalService',
  'titulo_seo': 'Boss Social Studio | Manejo de redes sociales para negocios en Toluca y Metepec',
  'desc_seo': 'Gestión de redes sociales, contenido, publicidad en Facebook e Instagram y WhatsApp Business '
              'para negocios en Toluca, Metepec y CDMX.',
  'linea': 'Redes sociales y marketing para negocios',
  'h1': 'Que te recuerden cuando te necesiten',
  'lead': 'Manejamos las redes sociales de tu negocio: contenido, promociones, publicidad y WhatsApp '
          'Business, para que tus clientes piensen en ti primero.',
  'servicios': [{'n': 'Gestión de redes sociales',
                 'c': 'Publicamos por ti con un calendario claro.',
                 'd': 'Planeamos el mes, diseñamos y publicamos en Facebook, Instagram y TikTok. Tú apruebas '
                      'antes de que salga.',
                 'i': ['Calendario mensual', 'Diseño de publicaciones', 'Publicación y programación']},
                {'n': 'Creación de contenido',
                 'c': 'Fotografía, video y reels según el alcance acordado.',
                 'd': 'Hacemos sesiones en tu negocio para tener material propio: producto, equipo, proceso. '
                      'El material propio ayuda a mostrar tu negocio de forma reconocible.',
                 'i': ['Sesiones de foto y video', 'Reels y videos cortos', 'Tomas con dron']},
                {'n': 'Publicidad digital',
                 'c': 'Anuncios en Meta dirigidos a tu zona.',
                 'd': 'Campañas en Facebook e Instagram segmentadas por colonia, edad e intereses, con '
                      'presupuesto controlado y reporte del gasto y de los resultados que puedan medirse.',
                 'i': ['Campañas locales', 'Promociones', 'Reporte de resultados']},
                {'n': 'Estrategia de marca',
                 'c': 'Cómo quieres que te recuerden.',
                 'd': 'Definimos tono, mensajes clave, lema y estilo visual para que todo lo que publicas se '
                      'sienta de la misma marca.',
                 'i': ['Tono y mensajes', 'Lema', 'Guía visual básica']},
                {'n': 'Comunidad y WhatsApp Business',
                 'c': 'Responder rápido también es marketing.',
                 'd': 'Configuramos WhatsApp Business con catálogo, respuestas rápidas, etiquetas y listas '
                      'de difusión, y te ayudamos a responder comentarios y mensajes.',
                 'i': ['Catálogo y respuestas rápidas', 'Listas de difusión', 'Atención de comentarios']},
                {'n': 'Análisis y resultados',
                 'c': 'Qué funcionó y qué no, cada mes.',
                 'd': 'Un reporte sencillo con alcance, mensajes recibidos y consultas y resultados '
                      'atribuibles cuando exista información para medirlos, para decidir el siguiente mes '
                      'con datos.',
                 'i': ['Reporte mensual', 'Recomendaciones', 'Ajuste de estrategia']}],
  'pasos': [('Conocemos tu negocio', 'Visitamos, probamos tu producto y vemos quién te compra.'),
            ('Planeamos el mes', 'Calendario con temas, promociones y fechas clave.'),
            ('Producimos y publicamos', 'Fotos, video y publicaciones aprobadas por ti.'),
            ('Medimos', 'Revisamos resultados y ajustamos.')],
  'faq': [('¿Trabajan solo con restaurantes?',
           'No. Trabajamos con cualquier negocio local: comida, servicios, tiendas, consultorios y más.'),
          ('¿El presupuesto de anuncios está incluido?',
           'No. El presupuesto de anuncios se paga directo a Meta y tú decides cuánto; nosotros lo '
           'administramos.'),
          ('¿Tengo que firmar por un año?',
           'No. La duración y las condiciones se acuerdan en la propuesta.')],
  'posts': [{'slug': 'whatsapp-business-para-que-tus-clientes-regresen',
             'titulo': 'Cómo usar WhatsApp Business para que tus clientes regresen',
             'fecha': '2026-09-29',
             'resumen': 'Catálogo, respuestas rápidas, etiquetas y listas de difusión: cinco ajustes que '
                        'convierten tu WhatsApp en una herramienta de ventas.',
             'keywords': 'WhatsApp Business, marketing para negocios locales, listas de difusión, redes '
                         'sociales Toluca',
             'cuerpo': '\n'
                       '<p>Para un negocio local en México, WhatsApp es el mostrador digital. Casi todas las '
                       'redes sociales terminan ahí: el cliente ve la promoción en Facebook y escribe por '
                       'WhatsApp. Si esa conversación no está bien atendida, la publicidad se '
                       'desperdicia.</p>\n'
                       '<h2>1. Perfil completo</h2>\n'
                       '<p>Horario, dirección con ubicación en el mapa, descripción corta y enlace a tu '
                       'página o redes. Un perfil vacío da desconfianza.</p>\n'
                       '<h2>2. Catálogo</h2>\n'
                       '<p>Sube tus productos o servicios con foto y precio. Ahorra preguntas repetidas y '
                       'deja que el cliente elija antes de escribirte.</p>\n'
                       '<h2>3. Respuestas rápidas</h2>\n'
                       '<p>Crea atajos para lo que más te preguntan: horario, ubicación, formas de pago, '
                       'costo de envío. Contestar en segundos cambia la venta.</p>\n'
                       '<h2>4. Etiquetas</h2>\n'
                       '<p>Marca a cada contacto como “nuevo cliente”, “pedido pendiente” o “cliente '
                       'frecuente”. Así sabes a quién darle seguimiento y a quién mandarle qué '
                       'promoción.</p>\n'
                       '<h2>5. Listas de difusión, con permiso</h2>\n'
                       '<p>Las listas de difusión solo llegan a quien tiene tu número guardado, por eso '
                       'funcionan mejor con clientes que ya te conocen. Úsalas para promociones concretas, '
                       'no para saturar: una o dos veces por semana es suficiente.</p>\n'
                       '<h2>Un detalle legal que casi nadie cuida</h2>\n'
                       '<p>Los números y nombres de tus clientes son datos personales. Si los usas para '
                       'enviar promociones, tu negocio debería contar con un aviso de privacidad que lo '
                       'explique. Es sencillo de resolver y te protege.</p>\n'
                       '<h2>Cómo medirlo</h2>\n'
                       '<p>Cuenta cada semana cuántos mensajes recibiste, cuántos se convirtieron en venta y '
                       'cuántos clientes volvieron a comprar. Con esa información puedes evaluar el '
                       'seguimiento y ajustar tu estrategia.</p>\n'
                       '<p>En Boss Social Studio configuramos tu WhatsApp Business junto con tus redes para '
                       'que todo trabaje en la misma dirección.</p>\n'}]},
 {'slug': 'punto-inmuebles',
  'area': 'Inmobiliario',
  'resumen_home': 'Compra, venta, renta y administración de inmuebles con revisión legal de cada operación y '
                  'acompañamiento hasta la firma.',
  'nombre': 'Punto Inmuebles',
  'tema': 'inmuebles',
  'logo': 'punto-inmuebles.jpg',
  'logo_bg': '#f7f4ef',
  'fuente_titulos': 'Montserrat',
  'tipo_schema': 'RealEstateAgent',
  'titulo_seo': 'Punto Inmuebles | Venta y renta de casas en Toluca, Metepec y Edomex',
  'desc_seo': 'Compra, venta y renta de inmuebles en Toluca, Metepec y el Estado de México, con asesoría '
              'personalizada y revisión legal de cada operación.',
  'linea': 'Soluciones inmobiliarias',
  'h1': 'Compra, vende o renta tu inmueble con respaldo legal',
  'lead': 'Te acompañamos de principio a fin: precio, promoción, documentos y firma. Cada operación pasa por '
          'una revisión legal para que cierres sin sorpresas.',
  'servicios': [{'n': 'Asesoría personalizada',
                 'c': 'Antes de vender o comprar, entiende tus números.',
                 'd': 'Analizamos el inmueble, la zona y tu objetivo para definir un precio realista y la '
                      'mejor estrategia: vender, rentar o esperar.',
                 'i': ['Opinión de valor',
                       'Estrategia de venta o renta',
                       'Estimación de gastos e impuestos']},
                {'n': 'Compra, venta y renta',
                 'c': 'Promoción, visitas y negociación.',
                 'd': 'Fotografía, publicación en portales, filtro de interesados, visitas y negociación. Te '
                      'informamos de cada avance.',
                 'i': ['Fotos y publicación', 'Filtro de prospectos', 'Negociación']},
                {'n': 'Gestión integral',
                 'c': 'Administración de inmuebles en renta.',
                 'd': 'Cobro de rentas, contratos, mantenimiento y atención a inquilinos para propietarios '
                      'que no quieren ocuparse del día a día.',
                 'i': ['Cobranza', 'Mantenimiento', 'Renovación de contratos']},
                {'n': 'Revisión legal de la operación',
                 'c': 'Documentos y contratos revisados por abogado.',
                 'd': 'Revisamos escrituras, gravámenes, contratos de promesa y arrendamiento, con apoyo de '
                      'Eje Legal, para que el patrimonio quede protegido.',
                 'i': ['Revisión de escrituras',
                       'Contratos de promesa y arrendamiento',
                       'Acompañamiento con notario']},
                {'n': 'Soluciones a tu medida',
                 'c': 'Herencias, copropiedad y casos especiales.',
                 'd': 'Inmuebles intestados, con varios dueños o con documentación incompleta. Te decimos '
                      'qué hay que regularizar antes de venderlo.',
                 'i': ['Diagnóstico documental', 'Ruta de regularización', 'Venta una vez regularizado']}],
  'pasos': [('Diagnóstico', 'Revisamos inmueble, documentos y objetivo.'),
            ('Precio y estrategia', 'Definimos precio, canales y tiempos.'),
            ('Promoción', 'Publicamos, filtramos y mostramos.'),
            ('Cierre', 'Negociación, contrato y firma ante notario.')],
  'faq': [('¿Cobran por publicar mi casa?',
           'Nuestra comisión se paga al cerrar la operación. Te la damos por escrito desde el inicio.'),
          ('¿Qué pasa si mi casa tiene papeles incompletos?',
           'La revisamos y te decimos qué hay que regularizar antes de venderla.'),
          ('¿Trabajan fuera de Toluca?',
           'Nos enfocamos en Toluca, Metepec y el Estado de México, y atendemos inmuebles en otros estados '
           'según el caso.')],
  'posts': [{'slug': 'documentos-para-vender-tu-casa-estado-de-mexico',
             'titulo': 'Documentos para vender tu casa en el Estado de México',
             'fecha': '2026-09-29',
             'resumen': 'La lista de papeles que te pedirá el notario y los que conviene tener antes de '
                        'publicar, para no perder a un comprador por un trámite pendiente.',
             'keywords': 'vender casa Estado de México, documentos venta casa, notario Toluca, IFREM',
             'cuerpo': '\n'
                       '<p>Muchas ventas se caen no por el precio, sino porque el vendedor tarda semanas en '
                       'reunir documentos cuando el comprador ya está listo. Tenerlos antes de publicar '
                       'acelera todo.</p>\n'
                       '<h2>Del inmueble</h2>\n'
                       '<ul>\n'
                       '<li><strong>Escritura</strong> inscrita en el Instituto de la Función Registral del '
                       'Estado de México (IFREM).</li>\n'
                       '<li><strong>Boleta predial</strong> pagada al año en curso.</li>\n'
                       '<li><strong>Recibo de agua</strong> sin adeudo; el notario suele pedir constancia de '
                       'no adeudo.</li>\n'
                       '<li><strong>Certificado de libertad de gravámenes</strong>, que informa sobre los '
                       'gravámenes inscritos a la fecha de su expedición. Normalmente lo solicita el '
                       'notario.</li>\n'
                       '<li>Si pertenece a un condominio: revisa si se requiere constancia de no adeudo de '
                       'cuotas de mantenimiento.</li>\n'
                       '</ul>\n'
                       '<h2>Del vendedor</h2>\n'
                       '<ul>\n'
                       '<li>Identificación oficial vigente, CURP y constancia de situación fiscal.</li>\n'
                       '<li>Acta de nacimiento y, si eres casado, acta de matrimonio: el régimen matrimonial '
                       'define si tu cónyuge debe firmar.</li>\n'
                       '<li>Comprobante de domicilio, importante si buscas la exención de ISR por venta de '
                       'casa habitación.</li>\n'
                       '</ul>\n'
                       '<h2>Si la casa está a crédito</h2>\n'
                       '<p>Pide a tu banco, INFONAVIT o FOVISSSTE el estado de adeudo. Se puede vender con '
                       'crédito vigente, pero la deuda se liquida en la operación y el trámite de '
                       'cancelación de hipoteca toma tiempo.</p>\n'
                       '<h2>Casos que requieren más tiempo</h2>\n'
                       '<ul>\n'
                       '<li>Casas heredadas sin juicio sucesorio terminado.</li>\n'
                       '<li>Construcciones que no aparecen en la escritura.</li>\n'
                       '<li>Inmuebles con varios dueños que no están de acuerdo.</li>\n'
                       '</ul>\n'
                       '<p>En esos casos conviene regularizar antes de publicar. Compara los costos y '
                       'tiempos de regularización antes de decidir cómo ofrecer el inmueble.</p>\n'
                       '<p>Esta guía es general; cada notaría puede pedir requisitos adicionales. En Punto '
                       'Inmuebles acordamos contigo una revisión documental antes de iniciar la '
                       'promoción.</p>\n'}]},
 {'slug': 'plano-y-obra',
  'area': 'Construcción',
  'resumen_home': 'Construcción residencial y comercial, remodelación integral y seguimiento de obra con '
                  'Certezza, con presupuesto por conceptos y bitácora con evidencia.',
  'nombre': 'Plano y Obra',
  'tema': 'plano',
  'logo': 'plano-y-obra.jpg',
  'logo_bg': '#f5f4f1',
  'fuente_titulos': 'Montserrat',
  'tipo_schema': 'GeneralContractor',
  'titulo_seo': 'Plano y Obra | Construcción y remodelación en Toluca y Metepec',
  'desc_seo': 'Construcción residencial y comercial, remodelación integral y control de obra en Toluca, '
              'Metepec y el Estado de México. Del plano a la realidad, con presupuesto bajo control.',
  'linea': 'Construcción y remodelación',
  'h1': 'Del plano a la realidad, con el presupuesto bajo control',
  'lead': 'Construimos y remodelamos espacios residenciales y comerciales con un proceso claro: catálogo de '
          'conceptos, avance medido y bitácora con evidencia.',
  'servicios': [{'n': 'Construcción residencial',
                 'c': 'Tu casa desde cero o una ampliación.',
                 'd': 'Coordinamos proyecto, permisos y ejecución, con presupuesto por conceptos y '
                      'calendario de obra desde el inicio.',
                 'i': ['Casa nueva', 'Ampliaciones y segundos niveles', 'Permisos y licencias']},
                {'n': 'Construcción comercial',
                 'c': 'Locales, oficinas y naves.',
                 'd': 'Adecuación de locales y oficinas con tiempos cortos y coordinación con tu operación '
                      'para no detener el negocio.',
                 'i': ['Locales y oficinas', 'Adecuaciones', 'Obra por etapas']},
                {'n': 'Remodelación integral',
                 'c': 'Cocinas, baños, fachadas e interiores.',
                 'd': 'Diseño, demolición, instalaciones y acabados con un solo responsable, para que no '
                      'tengas que coordinar cinco proveedores.',
                 'i': ['Cocinas y baños', 'Instalaciones', 'Acabados']},
                {'n': 'Planeación y ejecución',
                 'c': 'Presupuesto, programa y supervisión.',
                 'd': 'Catálogo de conceptos, programa de obra y supervisión técnica. Útil también si ya '
                      'tienes constructor y quieres a alguien de tu lado.',
                 'i': ['Catálogo de conceptos', 'Programa de obra', 'Supervisión']},
                {'n': 'Control de obra digital',
                 'c': 'Ve el avance y el gasto de tu obra en tiempo real.',
                 'd': 'Nuestra plataforma propia registra el avance diario contra el catálogo, alerta '
                      'desviaciones de costo y guarda la bitácora con fotos. Al final tienes un expediente '
                      'completo.',
                 'i': ['Avance diario', 'Alertas de costo', 'Bitácora con fotos']}],
  'pasos': [('Levantamiento', 'Visitamos, medimos y entendemos lo que necesitas.'),
            ('Presupuesto por conceptos', 'Cada partida con cantidad y precio, sin paquetes opacos.'),
            ('Ejecución', 'Obra con programa, supervisión y bitácora.'),
            ('Entrega', 'Recorrido final, expediente de obra y condiciones de entrega acordadas.')],
  'faq': [('¿El presupuesto puede cambiar?',
           'Solo si cambia el alcance. Cualquier cambio se presupuesta y se aprueba por escrito antes de '
           'ejecutarlo.'),
          ('¿Tramitan la licencia de construcción?',
           'Sí, te apoyamos con los trámites municipales cuando la obra los requiere.'),
          ('¿Cómo pago?', 'Por estimaciones contra avance real, no por adelantado completo.')],
  'posts': [{'slug': 'remodelar-sin-que-se-dispare-el-presupuesto',
             'titulo': 'Remodelar tu casa sin que se dispare el presupuesto: 5 controles',
             'fecha': '2026-09-29',
             'resumen': 'Por qué las remodelaciones casi siempre cuestan más de lo previsto y cinco '
                        'controles simples para evitarlo.',
             'keywords': 'remodelación casa Toluca, presupuesto de obra, control de obra, remodelación '
                         'Metepec',
             'cuerpo': '\n'
                       '<p>“Íbamos a gastar la mitad” es la frase más común al terminar una remodelación. '
                       'Casi nunca es mala fe: es falta de control desde el inicio. Estos son los cinco '
                       'controles que usamos en cada obra.</p>\n'
                       '<h2>1. Presupuesto por conceptos, no por paquete</h2>\n'
                       '<p>Un presupuesto que dice “remodelación de cocina: $180,000” no te protege. Pide un '
                       'catálogo con cada concepto, su unidad, cantidad y precio: demolición por metro '
                       'cuadrado, azulejo colocado, salidas eléctricas. Así sabes exactamente qué pagas y '
                       'puedes comparar.</p>\n'
                       '<h2>2. Alcance por escrito</h2>\n'
                       '<p>Define qué incluye y qué no: marca de materiales, retiro de escombro, '
                       'instalaciones ocultas. Lo que no está escrito es lo que después se cobra como '
                       'extra.</p>\n'
                       '<h2>3. Pagos contra avance</h2>\n'
                       '<p>Paga un anticipo razonable y después por estimaciones: el avance que realmente se '
                       'ejecutó, medido. Nunca pagues el total por adelantado.</p>\n'
                       '<h2>4. Bitácora con fotos</h2>\n'
                       '<p>Registra cada día qué se hizo, con fotos, sobre todo de lo que quedará oculto: '
                       'tuberías, cableado, impermeabilización. Si algo falla, la bitácora es tu '
                       'evidencia.</p>\n'
                       '<h2>5. Reserva para imprevistos</h2>\n'
                       '<p>Al abrir muros o pisos aparecen sorpresas. Aparta un porcentaje del presupuesto '
                       'para imprevistos y úsalo solo con cambios aprobados por escrito.</p>\n'
                       '<h2>Antes de empezar: permisos</h2>\n'
                       '<p>Si la obra toca estructura, fachada o amplía metros construidos, es probable que '
                       'necesites licencia de construcción en tu municipio. Una obra sin permiso puede ser '
                       'suspendida y complicar la venta futura del inmueble.</p>\n'
                       '<p>En Plano y Obra podemos apoyar el seguimiento con Certezza. El acceso, la '
                       'sincronización y los módulos se definen según la versión e implementación.</p>\n'}]},
 {'slug': 'punto-control',
  'area': 'Administración',
  'resumen_home': 'Administración, contabilidad y facturación para pequeñas y medianas empresas, con '
                  'reportes mensuales para decidir con datos.',
  'nombre': 'Punto Control',
  'tema': 'control',
  'logo': 'punto-control.jpg',
  'logo_bg': '#f9f9f9',
  'fuente_titulos': 'Montserrat',
  'tipo_schema': 'ProfessionalService',
  'titulo_seo': 'Punto Control | Administración, contabilidad y facturación para PyMEs',
  'desc_seo': 'Administración, contabilidad, facturación CFDI y control financiero para pequeñas y medianas '
              'empresas en Toluca, Metepec y CDMX.',
  'linea': 'Administración y contabilidad',
  'h1': 'Tu negocio en orden: cuentas claras, decisiones con datos',
  'lead': 'Administración, contabilidad y facturación para pequeñas y medianas empresas. Sabes cuánto ganas, '
          'cuánto debes y cuánto te deben, cada mes.',
  'servicios': [{'n': 'Administración',
                 'c': 'Procesos, cuentas por cobrar y por pagar.',
                 'd': 'Ordenamos cómo entra y sale el dinero de tu negocio: cobranza, pagos a proveedores, '
                      'caja chica y calendario de obligaciones.',
                 'i': ['Cuentas por cobrar y pagar', 'Calendario de pagos', 'Control de caja']},
                {'n': 'Contabilidad',
                 'c': 'Tu contabilidad al día y tus declaraciones a tiempo.',
                 'd': 'Organización de registros, conciliaciones y coordinación de obligaciones con el '
                      'profesional contable responsable.',
                 'i': ['Organización de información contable', 'Conciliación bancaria', 'Declaraciones']},
                {'n': 'Facturación CFDI',
                 'c': 'Emisión y revisión de comprobantes con seguimiento.',
                 'd': 'Emisión de facturas, complementos de pago y notas de crédito, y revisión documental; '
                      'la deducibilidad depende de requisitos fiscales y de cada operación.',
                 'i': ['Facturas y complementos de pago', 'Revisión de facturas recibidas', 'Cancelaciones']},
                {'n': 'Control y crecimiento',
                 'c': 'Números para decidir, no solo para cumplir.',
                 'd': 'Presupuesto, flujo de efectivo y márgenes por producto o servicio, para saber qué te '
                      'deja dinero y qué no.',
                 'i': ['Flujo de efectivo', 'Presupuesto', 'Márgenes']},
                {'n': 'Reportes de resultados',
                 'c': 'Un tablero mensual que sí entiendes.',
                 'd': 'Cada mes recibes un resumen con ventas, gastos, utilidad y pendientes, explicado en '
                      'lenguaje sencillo.',
                 'i': ['Reporte mensual', 'Indicadores clave', 'Reunión de revisión']}],
  'pasos': [('Diagnóstico', 'Revisamos tu situación fiscal y cómo llevas tus números hoy.'),
            ('Orden', 'Ponemos al día contabilidad, facturas y cuentas.'),
            ('Operación mensual',
             'Registros, facturación y coordinación contable según el servicio contratado.'),
            ('Reporte', 'Resultados y recomendaciones para decidir.')],
  'faq': [('¿Trabajan con personas físicas?',
           'Sí, con personas físicas con actividad empresarial, RESICO y personas morales.'),
          ('Tengo meses atrasados, ¿me pueden ayudar?',
           'Sí. Primero regularizamos los periodos pendientes y después seguimos mes a mes.'),
          ('¿Necesito cambiar de sistema?',
           'No necesariamente. Trabajamos con lo que ya usas y te proponemos cambios solo si te ahorran '
           'tiempo.')],
  'posts': [{'slug': 'errores-de-facturacion-y-control-que-cuestan-dinero',
             'titulo': '6 errores de facturación y control que le cuestan dinero a una PyME',
             'fecha': '2026-09-29',
             'resumen': 'Facturas mal emitidas, cuentas personales mezcladas y cobranza sin seguimiento: los '
                        'errores más comunes y cómo evitarlos.',
             'keywords': 'facturación CFDI 4.0, contabilidad PyME, control financiero, contador Toluca',
             'cuerpo': '\n'
                       '<p>La mayoría de los problemas con el SAT y de las fugas de dinero en un negocio '
                       'pequeño no vienen de fraudes, sino de hábitos. Estos son los seis que más '
                       'vemos.</p>\n'
                       '<h2>1. Datos del cliente que no coinciden</h2>\n'
                       '<p>En CFDI 4.0 el nombre, RFC, código postal y régimen fiscal del receptor deben '
                       'coincidir con su constancia de situación fiscal. Solicita los datos fiscales '
                       'necesarios al receptor; la entrega de una constancia de situación fiscal no es una '
                       'condición obligatoria para emitir la factura.</p>\n'
                       '<h2>2. Olvidar los complementos de pago</h2>\n'
                       '<p>Si emites una factura con método de pago en parcialidades o diferido (PPD), '
                       'cuando te pagan debes emitir el complemento de pago. Sin él, tu cliente puede tener '
                       'problemas para deducir, y tú un pendiente con el SAT.</p>\n'
                       '<h2>3. Mezclar cuentas personales y del negocio</h2>\n'
                       '<p>Pagar gastos personales desde la cuenta del negocio, o al revés, hace imposible '
                       'saber cuánto gana realmente tu empresa y complica justificar depósitos ante el '
                       'SAT.</p>\n'
                       '<h2>4. No conciliar el banco cada mes</h2>\n'
                       '<p>Comparar tus movimientos bancarios contra tus facturas emitidas y recibidas '
                       'detecta a tiempo cobros no facturados, pagos duplicados y gastos sin '
                       'comprobante.</p>\n'
                       '<h2>5. Aceptar facturas sin revisar</h2>\n'
                       '<p>Una factura con uso de CFDI incorrecto o de un proveedor con problemas ante el '
                       'SAT puede no ser deducible. Revísalas al recibirlas, no al cerrar el año.</p>\n'
                       '<h2>6. Cobrar sin seguimiento</h2>\n'
                       '<p>Vender mucho y cobrar tarde es una de las causas más comunes de falta de '
                       'efectivo. Una lista semanal de cuentas por cobrar, con fechas y responsables, cambia '
                       'el flujo del negocio.</p>\n'
                       '<h2>Por dónde empezar</h2>\n'
                       '<p>Separa cuentas, confirma los datos fiscales necesarios y programa revisiones '
                       'periódicas de conciliación. Si no tienes tiempo, en Punto Control lo hacemos por ti '
                       'y te entregamos un reporte que se entiende.</p>\n'
                       '<p>Fuente: <a '
                       'href="https://www.sat.gob.mx/minisitio/Factura/solicita_consideraciones.htm">SAT: '
                       'consideraciones para solicitar una factura</a>. El tratamiento fiscal concreto '
                       'depende de la operación y los requisitos aplicables.</p>'}]}]
PROYECTOS = [{'nombre': 'Certezza',
  'tipo': 'Control institucional de proyectos y obra',
  'desc': 'Levantamiento, catálogo, precios unitarios, programas, insumos, evidencia, bitácora, '
          'estimaciones, informes y portal del cliente. Módulos y sincronización según la versión '
          'implementada.',
  'marca': 'plano-y-obra'},
 {'nombre': 'Comanda',
  'tipo': 'Operación de restaurantes',
  'desc': 'Pedidos por mesero, QR por mesa, cocina, tickets y cuenta. La operación local o en internet se '
          'define por implementación.',
  'marca': 'innova-web'},
 {'nombre': 'Comanda Lite',
  'tipo': 'Operación ligera de restaurantes',
  'desc': 'Variante orientada al flujo de meseros, cocina y administración, con seguimiento de pedidos.',
  'marca': 'innova-web'},
 {'nombre': 'Jun 順',
  'tipo': 'Servicio de mesa para alta cocina',
  'desc': 'Proyecto de organización del servicio por mesa y comensal, dirigido a restaurantes de servicio '
          'fino.',
  'marca': 'innova-web'},
 {'nombre': 'Pasaporte del Sabor',
  'tipo': 'Fidelización digital y NFC',
  'desc': 'Sellos digitales y experiencias NFC para reconocer visitas y recompensas en cafeterías y negocios '
          'de alimentos.',
  'marca': 'innova-web'},
 {'nombre': 'Homoni',
  'tipo': 'Atención médica digital',
  'desc': 'Agenda, videoconsulta, expediente, recetas y seguimiento. La implementación requiere definir '
          'procesos y medidas para el tratamiento de datos de salud.',
  'marca': 'innova-web'},
 {'nombre': 'Homoni AI',
  'tipo': 'Asistencia para atención médica',
  'desc': 'Proyecto de asistentes, resúmenes y pendientes para acompañar al médico y al paciente. No '
          'sustituye el criterio clínico.',
  'marca': 'innova-web'},
 {'nombre': 'Homoni Pocket',
  'tipo': 'Seguimiento entre consultas',
  'desc': 'Proyecto de seguimiento médico sin depender de una videollamada.',
  'marca': 'innova-web'},
 {'nombre': 'Legal y Orden',
  'tipo': 'Gestión jurídica',
  'desc': 'Casos, clientes, calendario, documentos, videoconsulta y portal del cliente, según el alcance de '
          'la implementación.',
  'marca': 'eje-legal'},
 {'nombre': 'Contratto',
  'tipo': 'Automatización de documentos',
  'desc': 'Proyecto de generación de contratos desde plantillas, con menor recaptura y revisión jurídica '
          'antes de su uso.',
  'marca': 'eje-legal'},
 {'nombre': 'Catturare',
  'tipo': 'Gestión inmobiliaria',
  'desc': 'Inventario, fichas de propiedades, publicación y seguimiento de oportunidades inmobiliarias.',
  'marca': 'punto-inmuebles'},
 {'nombre': 'Boss Pro · Boss Engine · Boss Go',
  'tipo': 'Familia de seguimiento comercial',
  'desc': 'Proyectos CRM para organizar prospectos, etapas y resultados de la atención comercial.',
  'marca': 'boss-studio'},
 {'nombre': 'Conformità',
  'tipo': 'Diagnóstico de cumplimiento',
  'desc': 'Proyecto de diagnóstico y organización del cumplimiento institucional.',
  'marca': 'eje-legal'},
 {'nombre': '2Ride',
  'tipo': 'Movilidad vecinal',
  'desc': 'Piloto de viajes compartidos, recorridos por asientos y reservas para comunidades. Integraciones '
          'y disponibilidad sujetas a desarrollo.',
  'marca': 'innova-web'},
 {'nombre': '2iu',
  'tipo': 'Comercio y servicios locales',
  'desc': 'Proyecto para reunir negocios y servicios de una comunidad, con atención digital y seguimiento de '
          'consultas.',
  'marca': 'innova-web'},
 {'nombre': 'Plataforma escolar',
  'tipo': 'Comunicación y seguimiento escolar',
  'desc': 'Piloto de notificaciones, calendario y comunicación con familias, con una mascota colaborativa '
          'del plantel.',
  'marca': 'innova-web'},
 {'nombre': 'Bandeja unificada',
  'tipo': 'Atención digital de negocios',
  'desc': 'Proyecto para concentrar conversaciones de clientes y asistentes. Las conexiones de canales '
          'dependen de permisos e integraciones oficiales.',
  'marca': 'innova-web'},
 {'nombre': 'Herramientas PDF',
  'tipo': 'Productividad documental',
  'desc': 'Proyecto de extracción de información y conversión de documentos para facilitar su uso.',
  'marca': 'innova-web'},
 {'nombre': 'JARVIS personal',
  'tipo': 'Prototipo experimental',
  'desc': 'Asistente personal de voz con una interfaz tecnológica; iniciativa experimental.',
  'marca': 'innova-web'},
 {'nombre': 'Solid Eye',
  'tipo': 'Concepto experimental',
  'desc': 'Exploración de una interfaz monocular para información y notificaciones; concepto en '
          'investigación.',
  'marca': 'innova-web'}]
