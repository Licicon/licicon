# -*- coding: utf-8 -*-
"""
Generador estático de las páginas de marca de licicon.com
Uso (desde la raíz del repo):   python _build/build.py
Genera:  /<marca>/index.html, /<marca>/blog/..., /blog/index.html,
         sitemap.xml y robots.txt.  No toca index.html principal.
La carpeta _build no se publica en GitHub Pages (Jekyll ignora carpetas con "_").
"""
import json, os, html, sys, re
from datetime import date
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(__file__))
from contenido import MARCAS, SITIO, WHATSAPP, TELEFONO, EMAIL, AUTOR, ZONA

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape
MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

def fecha_larga(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} de {MESES[int(m)-1]} de {y}"

def wa(msg):
    return f"https://wa.me/{WHATSAPP}?text={quote(msg)}"

GTM_HEAD = "<!-- Google Tag Manager -->\n<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':\nnew Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],\nj=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=\n'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);\n})(window,document,'script','dataLayer','GTM-5PW4C5LB');</script>\n<!-- End Google Tag Manager -->"
GTM_BODY = '<!-- Google Tag Manager (noscript) -->\n<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5PW4C5LB"\nheight="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\n<!-- End Google Tag Manager (noscript) -->'

def write(rel, content):
    if rel.endswith(".html") and "<!-- Google Tag Manager -->" not in content:
        content = re.sub(r"<head\b[^>]*>", lambda m: m.group(0) + "\n" + GTM_HEAD, content, count=1)
        content = re.sub(r"<body\b[^>]*>", lambda m: m.group(0) + "\n" + GTM_BODY, content, count=1)
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C9 3 3.3 8.6 3.3 15.6c0 2.4.7 4.7 1.9 6.7L3 29l6.9-2.1c1.9 1 4 1.6 6.1 1.6 7 0 12.7-5.7 12.7-12.7C28.7 8.6 23 3 16 3zm0 23.2c-1.9 0-3.8-.5-5.4-1.5l-.4-.2-4.1 1.2 1.3-4-.3-.4a10.5 10.5 0 1 1 8.9 4.9zm5.8-7.8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.3-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.5c.2.2 2.4 3.7 5.8 5.1 2.9 1.1 3.4.9 4.1.8.6-.1 1.9-.8 2.2-1.5.3-.8.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>'

def fonts(m):
    fam = "family=Montserrat:wght@400;600;700;800"
    if m["fuente_titulos"] == "Playfair Display":
        fam = "family=Playfair+Display:wght@500;600;700&" + fam
    return (
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        f'<link href="https://fonts.googleapis.com/css2?{fam}&display=swap" rel="stylesheet">'
    )

def head(m, title, desc, url, img, jsonld, kind="website"):
    return f"""<!DOCTYPE html>
<html lang="es-MX">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{kind}">
<meta property="og:site_name" content="{e(m['nombre'])} · Grupo LICICON">
<meta property="og:locale" content="es_MX">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITIO}/assets/og/{m['slug']}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(m['nombre'])}, una firma del Grupo LICICON">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITIO}/assets/og/{m['slug']}.jpg">
<meta name="theme-color" content="{m['logo_bg']}">
<link rel="icon" href="/assets/licicon-emblema.png">
{fonts(m)}
<link rel="stylesheet" href="/assets/marcas.css">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body class="t-{m['tema']}">
"""

def topbar(m, actual):
    def item(href, txt, key):
        cur = ' aria-current="page"' if key == actual else ""
        return f'<a href="{href}"{cur}>{txt}</a>'
    base = f"/{m['slug']}/"
    return f"""<header class="top"><div class="wrap">
  <a class="back" href="/#firmas"><img src="/assets/licicon-emblema.png" alt="" width="30" height="30"><span>LICICON</span></a>
  <nav class="menu" aria-label="{e(m['nombre'])}">
    {item(base, 'Inicio', 'inicio')}{item(base + '#servicios', 'Servicios', 'serv')}{item(base + 'blog/', 'Blog', 'blog')}{item(base + '#contacto', 'Contacto', 'cont')}
  </nav>
</div></header>
"""

def family(actual_slug):
    lis = []
    for o in MARCAS:
        cur = ' aria-current="page"' if o["slug"] == actual_slug else ""
        lis.append(f'<li><a href="/{o["slug"]}/"{cur} style="background:{o["logo_bg"]}" title="{e(o["nombre"])}"><img src="/assets/marcas/{o["logo"]}" alt="{e(o["nombre"])}" loading="lazy"></a></li>')
    return f"""<section class="family" aria-labelledby="fam"><div class="wrap">
  <h2 id="fam">Otras marcas del Grupo LICICON</h2>
  <ul>{''.join(lis)}</ul>
</div></section>
"""

def cta_band(m):
    msg = f"Hola, vengo de la página de {m['nombre']} y me gustaría más información."
    return f"""<section class="cta" id="contacto"><div class="wrap">
  <div><h2 class="h">¿Platicamos tu caso?</h2><p>Cuéntanos qué necesitas y acordemos el siguiente paso.</p></div>
  <div class="actions">
    <a class="btn btn-p" href="{wa(msg)}" target="_blank" rel="noopener">WhatsApp {TELEFONO}</a>
    <a class="btn btn-s" href="mailto:{EMAIL}?subject={quote(m['nombre'])}">{EMAIL}</a>
  </div>
</div></section>
"""

def footer(m):
    msg = f"Hola, vengo de la página de {m['nombre']}."
    return f"""<footer class="foot"><div class="wrap">
  <span>© {date.today().year} {e(m['nombre'])} · una marca de <a href="/">LICICON</a></span>
  <span><a href="/aviso-de-privacidad/">Aviso de privacidad</a> · <a href="/politica-de-cookies/">Cookies</a> · {' · '.join(ZONA[:2])}</span>
</div></footer>
<a class="wa" href="{wa(msg)}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">{WA_SVG}</a>
<script>
(function(){{var d=document.documentElement;d.classList.add('js');
requestAnimationFrame(function(){{setTimeout(function(){{d.classList.add('loaded')}},60)}});
var red=matchMedia('(prefers-reduced-motion: reduce)').matches;
var sel='.sec-head,.svc details,.steps li,.post-row,.faq details,.cta .wrap>*,.family li,.prose>*,.art header,.blog-head';
var els=document.querySelectorAll(sel);
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{rootMargin:'0px 0px -6% 0px'}});
els.forEach(function(el){{var sib=el.parentNode?[].indexOf.call(el.parentNode.children,el):0;el.classList.add('rv');el.style.setProperty('--d',Math.min(sib,6)*0.07+'s');io.observe(el)}});
var top=document.querySelector('.top');addEventListener('scroll',function(){{top.classList.toggle('solid',scrollY>10)}},{{passive:true}});
document.querySelectorAll('.svc details').forEach(function(dt){{var sm=dt.querySelector('summary'),b=dt.querySelector('.body');
 sm.addEventListener('click',function(ev){{if(red)return;ev.preventDefault();
  if(dt.open){{var h=b.scrollHeight;b.animate([{{height:h+'px',opacity:1}},{{height:'0px',opacity:0}}],{{duration:450,easing:'cubic-bezier(.65,0,.35,1)'}}).onfinish=function(){{dt.open=false}};}}
  else{{dt.open=true;var h2=b.scrollHeight;b.animate([{{height:'0px',opacity:0}},{{height:h2+'px',opacity:1}}],{{duration:650,easing:'cubic-bezier(.19,1,.22,1)'}});}}
 }});}});
}})();
</script>
</body></html>
"""

def org_schema(m):
    url = f"{SITIO}/{m['slug']}/"
    return {
        "@type": m["tipo_schema"],
        "@id": url + "#org",
        "name": m["nombre"],
        "description": m["desc_seo"],
        "url": url,
        "logo": f"{SITIO}/assets/marcas/{m['logo']}",
        "image": f"{SITIO}/assets/marcas/{m['logo']}",
        "telephone": TELEFONO,
        "email": EMAIL,
        "areaServed": [{"@type": "Place", "name": z} for z in ZONA],
        "address": {"@type": "PostalAddress", "addressLocality": "Toluca", "addressRegion": "Estado de México", "addressCountry": "MX"},
        "parentOrganization": {"@type": "Organization", "name": "LICICON", "url": SITIO + "/"},
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Servicios de " + m["nombre"],
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["n"], "description": s["d"]}} for s in m["servicios"]]},
    }

def post_rows(m, posts):
    out = []
    for p in posts:
        out.append(f"""<a class="post-row" href="/{m['slug']}/blog/{p['slug']}/">
  <time datetime="{p['fecha']}">{fecha_larga(p['fecha'])}</time>
  <h3>{e(p['titulo'])}</h3><p>{e(p['resumen'])}</p></a>""")
    return "\n".join(out)

def ordenar(posts):
    return sorted(posts, key=lambda p: p["fecha"], reverse=True)

# ------------------------------------------------------------------ páginas
def pagina_marca(m):
    url = f"{SITIO}/{m['slug']}/"
    img = f"{SITIO}/assets/marcas/{m['logo']}"
    faq_schema = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in m["faq"]]}
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "LICICON", "item": SITIO + "/"},
        {"@type": "ListItem", "position": 2, "name": m["nombre"], "item": url}]}
    ld = {"@context": "https://schema.org", "@graph": [org_schema(m), faq_schema, crumbs]}

    servicios = []
    for i, s in enumerate(m["servicios"]):
        items = "".join(f"<li>{e(x)}</li>" for x in s["i"])
        ask = wa(f"Hola, me interesa el servicio de {s['n']} de {m['nombre']}.")
        servicios.append(f"""<details id="s-{i+1}">
  <summary><h3>{e(s['n'])}</h3><span class="c">{e(s['c'])}</span><span class="pm" aria-hidden="true">+</span></summary>
  <div class="body"><p>{e(s['d'])}</p><ul>{items}</ul>
  <a class="ask" href="{ask}" target="_blank" rel="noopener">Cotizar {e(s['n'].lower())} por WhatsApp</a></div>
</details>""")

    pasos = "".join(f"<li><strong>{e(t)}</strong><span>{e(d)}</span></li>" for t, d in m["pasos"])
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in m["faq"])
    extra = ""
    if m.get("cta_extra"):
        extra = f'<a class="btn btn-s" href="{m["cta_extra"]["url"]}" target="_blank" rel="noopener">{e(m["cta_extra"]["texto"])}</a>'
    posts = ordenar(m["posts"])

    body = f"""{topbar(m, 'inicio')}
<main>
<section class="hero"><div class="wrap">
  <div>
    <p class="kicker">{e(m['linea'])} en {e(', '.join(ZONA[:2]))} y {e(ZONA[3])}</p>
    <h1 class="h">{e(m['h1'])}</h1>
    <p class="lead">{e(m['lead'])}</p>
    <div class="actions">
      <a class="btn btn-p" href="#servicios">Ver servicios</a>
      {extra}
    </div>
  </div>
  <div class="logo-tile" style="background:{m['logo_bg']}"><img src="/assets/marcas/{m['logo']}" alt="Logotipo de {e(m['nombre'])}" width="720" height="480"></div>
</div></section>

<figure class="studio-brand-photo"><img src="/assets/studio/{m['slug']}.jpg" alt="Imagen ilustrativa de {e(m['nombre'])}" loading="lazy"><figcaption>{e(m['linea'])}</figcaption></figure>
<section class="sec" id="servicios"><div class="wrap">
  <div class="sec-head"><h2 class="h">Servicios</h2><p>Toca cada servicio para ver qué incluye y cotizarlo directo por WhatsApp.</p></div>
  <div class="svc">
{chr(10).join(servicios)}
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head"><h2 class="h">Cómo trabajamos</h2><p>Un proceso corto y claro, con costos acordados antes de empezar.</p></div>
  <ol class="steps">{pasos}</ol>
</div></section>

<section class="sec" id="blog"><div class="wrap">
  <div class="sec-head"><h2 class="h">Blog</h2><p>Guías prácticas para tomar mejores decisiones.</p></div>
  <div class="posts">{post_rows(m, posts[:3])}</div>
  <a class="more" href="/{m['slug']}/blog/">Todos los artículos de {e(m['nombre'])}</a>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head"><h2 class="h">Preguntas frecuentes</h2><p>Lo que más nos preguntan antes de empezar.</p></div>
  <div class="faq">{faqs}</div>
</div></section>
</main>
{cta_band(m)}
{family(m['slug'])}
{footer(m)}"""
    write(f"{m['slug']}/index.html", head(m, m["titulo_seo"], m["desc_seo"], url, img, ld) + body)
    return url

def pagina_blog_marca(m):
    url = f"{SITIO}/{m['slug']}/blog/"
    posts = ordenar(m["posts"])
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "name": f"Blog de {m['nombre']}", "url": url, "publisher": {"@id": f"{SITIO}/{m['slug']}/#org"},
         "blogPost": [{"@type": "BlogPosting", "headline": p["titulo"], "url": f"{url}{p['slug']}/", "datePublished": p["fecha"]} for p in posts]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "LICICON", "item": SITIO + "/"},
            {"@type": "ListItem", "position": 2, "name": m["nombre"], "item": f"{SITIO}/{m['slug']}/"},
            {"@type": "ListItem", "position": 3, "name": "Blog", "item": url}]}]}
    title = f"Blog de {m['nombre']} | {m['linea']}"
    desc = f"Artículos y guías de {m['nombre']} sobre {m['linea'].lower()} para personas y negocios en {ZONA[0]}, {ZONA[1]} y el {ZONA[2]}."
    body = f"""{topbar(m, 'blog')}
<main class="wrap">
  <nav class="crumbs" aria-label="Ruta"><a href="/">LICICON</a> / <a href="/{m['slug']}/">{e(m['nombre'])}</a> / Blog</nav>
  <header class="blog-head"><h1 class="h">Blog de {e(m['nombre'])}</h1><p>{e(desc)}</p></header>
  <div class="posts" style="padding-bottom:64px">{post_rows(m, posts)}</div>
</main>
{cta_band(m)}
{family(m['slug'])}
{footer(m)}"""
    write(f"{m['slug']}/blog/index.html", head(m, title, desc, url, f"{SITIO}/assets/marcas/{m['logo']}", ld) + body)
    return url

def pagina_post(m, p):
    url = f"{SITIO}/{m['slug']}/blog/{p['slug']}/"
    img = f"{SITIO}/assets/marcas/{m['logo']}"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "headline": p["titulo"], "description": p["resumen"], "datePublished": p["fecha"],
         "dateModified": p.get("modificado", p["fecha"]), "inLanguage": "es-MX", "mainEntityOfPage": url, "image": img,
         "keywords": p.get("keywords", ""),
         "author": {"@type": "Person", "name": AUTOR},
         "publisher": {"@type": "Organization", "name": m["nombre"], "logo": {"@type": "ImageObject", "url": img}}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "LICICON", "item": SITIO + "/"},
            {"@type": "ListItem", "position": 2, "name": m["nombre"], "item": f"{SITIO}/{m['slug']}/"},
            {"@type": "ListItem", "position": 3, "name": "Blog", "item": f"{SITIO}/{m['slug']}/blog/"},
            {"@type": "ListItem", "position": 4, "name": p["titulo"], "item": url}]}]}
    otros = [x for x in ordenar(m["posts"]) if x["slug"] != p["slug"]][:2]
    rel = f"""<section class="sec" style="padding-top:40px"><h2 class="h" style="font-size:26px;margin-bottom:10px">Sigue leyendo</h2><div class="posts">{post_rows(m, otros)}</div></section>""" if otros else ""
    msg = f"Hola, leí el artículo \"{p['titulo']}\" y quiero asesoría."
    body = f"""{topbar(m, 'blog')}
<main class="wrap">
  <nav class="crumbs" aria-label="Ruta"><a href="/">LICICON</a> / <a href="/{m['slug']}/">{e(m['nombre'])}</a> / <a href="/{m['slug']}/blog/">Blog</a></nav>
  <article class="art">
    <header><h1 class="h">{e(p['titulo'])}</h1>
    <p class="meta">Por {e(AUTOR)} · <time datetime="{p['fecha']}">{fecha_larga(p['fecha'])}</time></p></header>
    <div class="prose">{p['cuerpo']}</div>
    <aside class="art-cta"><p><strong>¿Te sirvió?</strong> Si quieres que revisemos tu caso en particular, escríbenos.</p>
      <a class="btn btn-p" href="{wa(msg)}" target="_blank" rel="noopener">Hablar con {e(m['nombre'])}</a></aside>
  </article>
  {rel}
</main>
{family(m['slug'])}
{footer(m)}"""
    write(f"{m['slug']}/blog/{p['slug']}/index.html", head(m, f"{p['titulo']} | {m['nombre']}", p["resumen"], url, img, ld, "article") + body)
    return url, p.get("modificado", p["fecha"])

def blog_general():
    todos = sorted([(m, p) for m in MARCAS for p in m["posts"]], key=lambda x: x[1]["fecha"], reverse=True)
    rows = "".join(f"""<a class="row" href="/{m['slug']}/blog/{p['slug']}/">
  <span class="tag" style="background:{m['logo_bg']}"><img src="/assets/marcas/{m['logo']}" alt="{e(m['nombre'])}" loading="lazy"></span>
  <span class="txt"><time datetime="{p['fecha']}">{fecha_larga(p['fecha'])} · {e(m['nombre'])}</time><strong>{e(p['titulo'])}</strong><em>{e(p['resumen'])}</em></span></a>""" for m, p in todos)
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": "Blog del Grupo LICICON", "url": f"{SITIO}/blog/",
          "publisher": {"@type": "Organization", "name": "LICICON", "url": SITIO + "/"}}
    page = f"""<!DOCTYPE html>
<html lang="es-MX"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Blog | Grupo LICICON: legal, web, marketing, inmuebles, construcción y administración</title>
<meta name="description" content="Guías prácticas de las marcas del Grupo LICICON: Eje Legal, Innova Web Studio, Boss Studio, Punto Inmuebles, Plano y Obra y Punto Control.">
<link rel="canonical" href="{SITIO}/blog/"><meta property="og:image" content="{SITIO}/assets/og/licicon.jpg"><meta property="og:title" content="Publicaciones del Grupo LICICON"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/licicon-emblema.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#05070a;color:#e8e4da;font-family:Montserrat,system-ui,sans-serif;line-height:1.6}}
a{{color:inherit}}.wrap{{width:min(960px,100% - 40px);margin:auto}}
.top{{border-bottom:1px solid rgba(212,175,55,.2);padding:18px 0}}.top a{{display:flex;gap:10px;align-items:center;text-decoration:none;font-family:Cinzel,serif;color:#d4af37;letter-spacing:.08em}}
h1{{font-family:Cinzel,serif;font-size:clamp(32px,5vw,52px);color:#d4af37;margin:56px 0 8px;font-weight:600}}
.sub{{color:#9a968c;max-width:60ch;margin:0 0 40px}}
.row{{display:grid;grid-template-columns:120px 1fr;gap:22px;padding:22px 0;border-top:1px solid rgba(212,175,55,.15);text-decoration:none;align-items:center}}
.tag{{overflow:hidden;display:grid;grid-template:minmax(0,1fr)/minmax(0,1fr);aspect-ratio:3/2;border-radius:4px;padding:8px}}.tag img{{width:100%;height:100%;object-fit:contain}}
.txt time{{font-size:13px;color:#8d897f;display:block}}.txt strong{{display:block;font-size:20px;margin:4px 0}}.txt em{{font-style:normal;color:#9a968c;font-size:15px}}
.row:hover strong{{color:#d4af37}}footer{{padding:48px 0;color:#6d6a62;font-size:13px}}
@media(max-width:560px){{.row{{grid-template-columns:84px 1fr;gap:14px}}.txt strong{{font-size:17px}}}}
</style></head><body>
<header class="top"><div class="wrap"><a href="/"><img src="/assets/licicon-emblema.png" alt="" width="30" height="30">LICICON</a></div></header>
<main class="wrap"><h1>Blog del grupo</h1><p class="sub">Artículos de nuestras seis marcas. Cada uno vive en la sección de su marca.</p>
{rows}</main>
<footer class="wrap">© {date.today().year} LICICON · <a href="/aviso-de-privacidad/">Aviso de privacidad</a> · <a href="/politica-de-cookies/">Cookies</a></footer>
</body></html>"""
    write("blog/index.html", page)

def casos_html(por_slug):
    from contenido import CASOS
    out = []
    for i, c in enumerate(CASOS):
        firmas = " y ".join(f'<a href="/{f}/">{e(por_slug[f]["nombre"])}</a>' for f in c["firmas"] if f in por_slug)
        st = f'<span class="st">{e(c["estado"])}</span>' if c.get("estado") else ""
        lis = "".join(f"<li>{e(x)}</li>" for x in c["entregables"])
        visit = f'<a class="visit" href="{c["url"]}" target="_blank" rel="noopener">Ver proyecto <svg viewBox="0 0 12 12"><path d="M2 10L10 2M4 2h6v6"/></svg></a>' if c.get("url") else ""
        out.append(f"""<article class="case" data-r>
  <div class="who"><span class="label">{e(c['sector'])}</span><h3>{e(c['cliente'])}{st}</h3><span class="where">{e(c['lugar'])}</span></div>
  <div class="story"><h4>El reto</h4><p>{e(c['reto'])}</p><h4>Lo que hicimos</h4><p>{e(c['hicimos'])}</p></div>
  <div class="meta"><ul>{lis}</ul><p class="by">Con {firmas}</p>{visit}</div>
</article>""")
    return "\n".join(out)

def testimonios_html(por_slug):
    from contenido import TESTIMONIOS
    if not TESTIMONIOS:
        return ""
    qs = []
    for i, t in enumerate(TESTIMONIOS):
        f = por_slug.get(t.get("firma"))
        extra = f' · <a href="/{f["slug"]}/" style="color:var(--gold-2)">{e(f["nombre"])}</a>' if f else ""
        qs.append(f'<blockquote class="quote" data-r style="--d:{i*120}"><p>{e(t["texto"])}</p><footer><b>{e(t["nombre"])}</b>{e(t["rol"])}{extra}</footer></blockquote>')
    return f"""<section class="sec" id="opiniones" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><div><span class="label" data-r>Opiniones</span><h2 data-r style="--d:100">Lo que dicen nuestros clientes.</h2></div><p></p></div>
  <div class="quotes">{''.join(qs)}</div>
</div></section>"""

def paginas_legales():
    import legal
    from contenido import AVISO_FECHA
    for slug, titulo, desc, cuerpo in [
        ("aviso-de-privacidad", "Aviso de privacidad", "Aviso de privacidad integral de LICICON y sus firmas: datos que recabamos, finalidades, transferencias y cómo ejercer sus derechos ARCO.", legal.aviso()),
        ("politica-de-cookies", "Política de cookies", "Qué tecnologías de almacenamiento usa licicon.com y cómo controlarlas.", legal.cookies())]:
        page = f"""<!DOCTYPE html>
<html lang="es-MX"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo} | LICICON</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITIO}/{slug}/"><link rel="icon" href="/assets/licicon-emblema.png">
<meta property="og:title" content="{titulo} | LICICON"><meta property="og:image" content="{SITIO}/assets/og/licicon.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#08090b;color:#ebe7de;font-family:Montserrat,system-ui,sans-serif;font-weight:300;line-height:1.8;-webkit-font-smoothing:antialiased}}
a{{color:#d4af37}}.wrap{{width:min(820px,100%);margin:auto;padding:0 clamp(20px,5vw,40px)}}
.top{{border-bottom:1px solid rgba(212,175,55,.16);padding:18px 0}}.top a{{display:inline-flex;gap:12px;align-items:center;text-decoration:none;font-family:'Cormorant Garamond',Georgia,serif;color:#ebe7de;letter-spacing:.34em;font-size:20px}}
.lbl{{display:block;font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:#b8995a;margin:72px 0 14px}}
h1{{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(42px,6vw,68px);line-height:1;margin:0 0 16px}}
.upd{{color:#5e5b55;font-size:13px;margin:0 0 48px;padding-bottom:40px;border-bottom:1px solid rgba(212,175,55,.16)}}
.intro{{font-size:18px;color:#ebe7de}}
h2{{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:28px;margin:48px 0 10px}}
p,li{{color:#a5a198;font-size:15.5px}}strong{{color:#ebe7de;font-weight:500}}ul{{padding-left:20px}}li{{margin:6px 0}}li::marker{{color:#b8995a}}
.tbl{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;font-size:14px;min-width:560px}}th,td{{text-align:left;padding:12px 14px 12px 0;border-bottom:1px solid rgba(212,175,55,.16);vertical-align:top}}th{{font-weight:500;color:#b8995a;font-size:11px;letter-spacing:.18em;text-transform:uppercase}}td{{color:#a5a198}}td:first-child{{color:#ebe7de;font-family:monospace;font-size:13px}}
footer{{margin-top:80px;padding:32px 0 calc(40px + env(safe-area-inset-bottom,0px));border-top:1px solid rgba(212,175,55,.16);font-size:13px;color:#5e5b55;display:flex;flex-wrap:wrap;gap:12px 24px;justify-content:space-between}}footer a{{color:#8f8b82}}
</style></head><body>
<header class="top"><div class="wrap"><a href="/"><img src="/assets/licicon-emblema.png" alt="" width="30" height="30">LICICON</a></div></header>
<main class="wrap"><span class="lbl">Legal</span><h1>{titulo}</h1><p class="upd">Última actualización: {AVISO_FECHA}</p>{cuerpo}
<footer><span>© {date.today().year} LICICON</span><span><a href="/aviso-de-privacidad/">Aviso de privacidad</a> · <a href="/politica-de-cookies/">Política de cookies</a> · <a href="/">Inicio</a></span></footer></main>
</body></html>"""
        write(f"{slug}/index.html", page)
    return [f"{SITIO}/aviso-de-privacidad/", f"{SITIO}/politica-de-cookies/"]

ARROW = '<svg viewBox="0 0 16 16"><path d="M1 8h13M9 3l5 5-5 5"/></svg>'

def seccion_home():
    """Genera /index.html a partir de _build/home_template.html y del contenido."""
    from contenido import PROYECTOS
    B = os.path.dirname(os.path.abspath(__file__))
    tpl = open(os.path.join(B, "home_template.html"), encoding="utf-8").read()
    por_slug = {m["slug"]: m for m in MARCAS}

    hero = "".join(f'<a href="/{m["slug"]}/" style="--i:{i}" title="{e(m["nombre"])}"><img src="/assets/marcas/mark/{m["slug"]}.png" alt="{e(m["nombre"])}"></a>' for i, m in enumerate(MARCAS))

    firmas = []
    for i, m in enumerate(MARCAS):
        firmas.append(f"""<a class="firm" href="/{m['slug']}/" data-r style="--d:{i*70}">
  <span class="mk"><span class="bg" style="background:{m['logo_bg']}"></span><img class="m" src="/assets/marcas/mark/{m['slug']}.png" alt="" loading="lazy"><img class="c" src="/assets/marcas/mark/{m['slug']}-color.jpg" alt="" loading="lazy"></span>
  <span class="nm"><span class="label">{e(m['area'])}</span><h3>{e(m['nombre'])}</h3></span>
  <p class="ds">{e(m['resumen_home'])}</p>
  <span class="go" aria-hidden="true">{ARROW}</span>
</a>""")

    tabs, panels = [], []
    for i, m in enumerate(MARCAS):
        on = i == 0
        tabs.append(f'<button class="tab" role="tab" id="t-{m["slug"]}" aria-controls="p-{m["slug"]}" aria-selected="{str(on).lower()}" tabindex="{0 if on else -1}">{e(m["nombre"])}</button>')
        items = []
        for j, sv in enumerate(m["servicios"]):
            lis = "".join(f"<li>{e(x)}</li>" for x in sv["i"])
            items.append(f'<div class="svc-item" style="--i:{j}"><h4>{e(sv["n"])}</h4><p>{e(sv["d"])}</p><ul>{lis}</ul></div>')
        panels.append(f"""<div class="panel{' on' if on else ''}" role="tabpanel" id="p-{m['slug']}" aria-labelledby="t-{m['slug']}">
  <figure class="service-panorama"><img src="/assets/studio/{m['slug']}.jpg" alt="Imagen ilustrativa de {e(m['nombre'])}" loading="lazy"></figure>
  <aside><span class="label">{e(m['area'])}</span><h3>{e(m['nombre'])}</h3><p>{e(m['lead'])}</p>
    <div class="lk"><a href="/{m['slug']}/">Visitar {e(m['nombre'])} {ARROW}</a><a href="/{m['slug']}/blog/">Publicaciones {ARROW}</a></div></aside>
  <div class="svc-list">{''.join(items)}</div>
</div>""")

    proys = []
    for i, p in enumerate(PROYECTOS):
        mm = por_slug.get(p.get("marca"))
        by = f'Desarrollado por <a href="/{mm["slug"]}/">{e(mm["nombre"])}</a>' if mm else "Desarrollo LICICON"
        proys.append(f'<article class="dev" data-r style="--d:{(i%3)*100}"><span class="label">{e(p["tipo"])}</span><h3>{e(p["nombre"])}</h3><p>{e(p["desc"])}</p><span class="by">{by}</span></article>')

    ops = "".join(f'\n        <option value="{m["slug"]}">{e(m["nombre"])} · {e(m["linea"])}</option>' for m in MARCAS)
    foot = "".join(f'<li><a href="/{m["slug"]}/">{e(m["nombre"])}</a></li>' for m in MARCAS)

    tipos = {m["slug"]: m["tipo_schema"] for m in MARCAS}
    ld = {"@context": "https://schema.org", "@type": "Organization", "name": "LICICON", "url": SITIO + "/",
          "logo": SITIO + "/assets/licicon-emblema.png", "email": EMAIL, "telephone": TELEFONO,
          "subOrganization": [{"@type": tipos[m["slug"]], "name": m["nombre"], "url": f"{SITIO}/{m['slug']}/"} for m in MARCAS]}

    word = "".join(f'<span style="--i:{i}">{c}</span>' for i, c in enumerate("LICICON"))
    imarks = "".join(f'<img src="/assets/marcas/mark/{m["slug"]}.png" alt="" style="--i:{i}">' for i, m in enumerate(MARCAS))
    tpl = tpl.replace("{{INTRO_WORD}}", word).replace("{{INTRO_MARKS}}", imarks)
    out = (tpl.replace("{{HERO_MARKS}}", hero).replace("{{FIRMAS}}", "\n".join(firmas))
              .replace("{{TABS}}", "\n".join(tabs)).replace("{{PANELS}}", "\n".join(panels))
              .replace("{{PROYECTOS}}", "\n".join(proys)).replace("{{OPCIONES}}", ops)
              .replace("{{FIRMAS_FOOTER}}", foot).replace("{{CASOS}}", casos_html(por_slug)).replace("{{TESTIMONIOS}}", testimonios_html(por_slug))
              .replace("{{YEAR}}", str(date.today().year))
              .replace("{{JSONLD}}", json.dumps(ld, ensure_ascii=False)))
    write("index.html", out)

def main():
    urls = [(SITIO + "/", date.today().isoformat(), "1.0"), (SITIO + "/blog/", date.today().isoformat(), "0.6")]
    for m in MARCAS:
        urls.append((pagina_marca(m), date.today().isoformat(), "0.9"))
        urls.append((pagina_blog_marca(m), date.today().isoformat(), "0.6"))
        for p in m["posts"]:
            u, mod = pagina_post(m, p)
            urls.append((u, mod, "0.7"))
    blog_general()
    seccion_home()
    for u in paginas_legales():
        urls.append((u, date.today().isoformat(), "0.3"))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, mod, pr in urls:
        sm.append(f"  <url><loc>{u}</loc><lastmod>{mod}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITIO}/sitemap.xml\n")
    print(f"OK · {len(urls)} URLs en sitemap")

if __name__ == "__main__":
    main()
