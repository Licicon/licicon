# -*- coding: utf-8 -*-
"""Textos del aviso de privacidad y la política de cookies de licicon.com y sus firmas."""
from contenido import MARCAS, EMAIL, TELEFONO, AUTOR, DOMICILIO, AVISO_FECHA

def aviso():
    firmas = ", ".join(m["nombre"] for m in MARCAS[:-1]) + " y " + MARCAS[-1]["nombre"]
    return f"""
<p class="intro">Este aviso explica qué datos personales recabamos, para qué los usamos y cómo puede ejercer sus derechos. Aplica a licicon.com, a las secciones de cada firma del grupo ({firmas}) y a los servicios que contrate con cualquiera de ellas.</p>

<h2>1. Responsable</h2>
<p><strong>{AUTOR}</strong>, persona física con actividad empresarial, que opera bajo el nombre comercial LICICON y las marcas {firmas}, con domicilio en {DOMICILIO}, es responsable del tratamiento de sus datos personales.</p>
<p>Contacto para cualquier asunto de privacidad: <a href="mailto:{EMAIL}">{EMAIL}</a> · {TELEFONO}.</p>

<h2>2. Datos que recabamos</h2>
<p><strong>Al contactarnos</strong> por el formulario, WhatsApp, correo o teléfono: nombre, correo electrónico, número telefónico, empresa y la información que usted decida compartir en su mensaje.</p>
<p><strong>Al contratar un servicio</strong>, según la firma y el servicio: datos de identificación (identificación oficial, CURP, RFC), datos de contacto y domicilio, datos fiscales (constancia de situación fiscal, régimen), datos patrimoniales relacionados con el servicio (por ejemplo, documentos de un inmueble o información contable del negocio) y datos laborales cuando el servicio lo requiera.</p>
<p><strong>Datos sensibles.</strong> Algunos asuntos legales pueden requerir información sensible (por ejemplo, de salud o de carácter familiar). Solo la trataremos cuando sea indispensable para atender su asunto y con su consentimiento expreso y por escrito.</p>
<p><strong>Datos de terceros.</strong> Si nos proporciona datos de otras personas (por ejemplo, empleados, copropietarios o contrapartes), usted declara contar con su autorización para compartirlos.</p>

<h2>3. Finalidades</h2>
<p><strong>Finalidades necesarias</strong> para la relación con usted:</p>
<ul>
<li>Responder solicitudes de información, cotizaciones y mensajes.</li>
<li>Prestar los servicios contratados: asesoría legal, desarrollo web, marketing, intermediación inmobiliaria, construcción, administración y contabilidad.</li>
<li>Elaborar contratos, facturar y cobrar.</li>
<li>Cumplir obligaciones legales, fiscales y requerimientos de autoridad.</li>
</ul>
<p><strong>Finalidades adicionales</strong>, que no son necesarias para el servicio:</p>
<ul>
<li>Enviarle información sobre servicios del grupo, publicaciones y eventos.</li>
<li>Solicitarle su opinión sobre nuestro servicio y, solo con su autorización expresa, publicarla con su nombre.</li>
</ul>
<p>Si no desea que usemos sus datos para las finalidades adicionales, escríbanos a <a href="mailto:{EMAIL}">{EMAIL}</a> con el asunto «Finalidades adicionales». Su negativa no afecta los servicios que contrate.</p>

<h2>4. Con quién compartimos sus datos</h2>
<p>No vendemos ni rentamos sus datos personales. Los compartimos únicamente cuando es necesario para prestar el servicio o cumplir la ley:</p>
<ul>
<li><strong>Proveedores tecnológicos</strong> que procesan datos por nuestra cuenta: alojamiento del sitio (GitHub Pages), procesamiento del formulario (Formspree), mensajería (WhatsApp de Meta) y correo electrónico. Actúan bajo nuestras instrucciones y sus propias políticas de privacidad.</li>
<li><strong>Notarios, instituciones financieras y autoridades</strong>, cuando su operación o trámite lo requiera (por ejemplo, en una compraventa de inmueble o un registro ante autoridad).</li>
<li><strong>Otras firmas del Grupo LICICON</strong>, solo cuando su proyecto involucre a más de una y para la misma finalidad para la que nos dio sus datos.</li>
</ul>
<p>Estas comunicaciones no requieren su consentimiento cuando son necesarias para cumplir la relación jurídica con usted o una obligación legal, conforme a la ley.</p>

<h2>5. Derechos ARCO y revocación del consentimiento</h2>
<p>Usted puede <strong>acceder</strong> a sus datos, <strong>rectificarlos</strong>, <strong>cancelarlos</strong> u <strong>oponerse</strong> a su tratamiento, así como revocar el consentimiento que nos haya otorgado.</p>
<p>Envíe su solicitud a <a href="mailto:{EMAIL}">{EMAIL}</a> con:</p>
<ul>
<li>Su nombre y un medio para responderle.</li>
<li>Copia de su identificación o, en su caso, la de su representante legal y el documento que lo acredite.</li>
<li>La descripción clara de los datos y del derecho que desea ejercer.</li>
<li>Cualquier documento que facilite la localización de sus datos.</li>
</ul>
<p>Le responderemos en un plazo máximo de 20 días hábiles y, si procede, haremos efectiva la solicitud dentro de los 15 días hábiles siguientes. Algunos datos deberán conservarse por el tiempo que exijan las leyes fiscales y mercantiles.</p>

<h2>6. Limitar el uso de sus datos</h2>
<p>Puede pedirnos en cualquier momento que dejemos de enviarle comunicaciones informativas o promocionales por correo o WhatsApp, respondiendo «Baja» al mensaje o escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>7. Cookies y tecnologías similares</h2>
<p>Este sitio usa almacenamiento técnico e integra Google Tag Manager para gestionar etiquetas de medición. Las etiquetas de Analytics, cuando estén configuradas y publicadas, pueden tratar datos de navegación. Consulte el detalle en nuestra <a href="/politica-de-cookies/">política de cookies</a>.</p>

<h2>8. Seguridad</h2>
<p>Aplicamos medidas administrativas, técnicas y físicas para proteger sus datos contra daño, pérdida, alteración o acceso no autorizado, con referencia a buenas prácticas de seguridad de la información como ISO/IEC 27001.</p>

<h2>9. Cambios a este aviso</h2>
<p>Podemos actualizar este aviso por cambios legales o en nuestros servicios. Publicaremos la versión vigente en esta página, con su fecha de actualización.</p>

<h2>10. Autoridad</h2>
<p>Si considera que su derecho a la protección de datos personales ha sido vulnerado, puede acudir a la Secretaría Anticorrupción y Buen Gobierno, autoridad competente conforme a la Ley Federal de Protección de Datos Personales en Posesión de los Particulares publicada en marzo de 2025.</p>
"""

def cookies():
    return f"""
<p class="intro">Esta política explica qué tecnologías de almacenamiento usa licicon.com y las páginas de sus firmas, y cómo puede controlarlas.</p>

<h2>Qué usamos</h2>
<p>Usamos Google Tag Manager (contenedor GTM-5PW4C5LB) para gestionar etiquetas. Cuando Google Analytics esté configurado y publicado, podrá medir visitas, páginas consultadas, interacciones y datos técnicos del dispositivo y navegador. La medición efectiva depende de las etiquetas publicadas en el contenedor. Además, guardamos los siguientes datos técnicos en su navegador:</p>
<div class="tbl"><table>
<thead><tr><th>Nombre</th><th>Tipo</th><th>Para qué sirve</th><th>Duración</th></tr></thead>
<tbody>
<tr><td>cookiesAccepted</td><td>Almacenamiento local</td><td>Recordar que ya leyó este aviso para no mostrarlo otra vez.</td><td>Hasta que borre los datos del navegador</td></tr>
<tr><td>introVisto</td><td>Almacenamiento de sesión</td><td>Mostrar la animación de entrada una sola vez por visita.</td><td>Se borra al cerrar la pestaña</td></tr>
</tbody></table></div>

<h2>Servicios de terceros</h2>
<p>El navegador se conecta a Google para cargar Tag Manager. Las etiquetas publicadas en el contenedor pueden enviar datos de navegación a Google Analytics y usar cookies como _ga para distinguir visitas. Consulte <a href="https://policies.google.com/privacy">la política de privacidad de Google</a> y <a href="https://tools.google.com/dlpage/gaoptout">su complemento de inhabilitación de Analytics</a>.</p>
<p>Para mostrar las tipografías, el sitio carga fuentes desde Google Fonts, lo que implica que su navegador se conecte a servidores de Google, que pueden registrar datos técnicos como su dirección IP. Los botones de WhatsApp y los enlaces externos solo se conectan con esos servicios cuando usted los usa.</p>

<h2>Cómo controlarlas</h2>
<p>Puede borrar o bloquear el almacenamiento desde la configuración de su navegador. El sitio seguirá funcionando; solo volverá a ver el aviso y la animación de entrada.</p>

<h2>Cambios</h2>
<p>Si en el futuro incorporamos herramientas de medición o publicidad, actualizaremos esta política y le pediremos su consentimiento antes de activarlas.</p>
<p>Para más información sobre el tratamiento de sus datos consulte nuestro <a href="/aviso-de-privacidad/">aviso de privacidad</a> o escríbanos a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
"""
