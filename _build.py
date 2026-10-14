"""Génère les pages HTML du site. Lancer : python3 _build.py
Pour ajouter un événement : compléter la liste EVENTS ci-dessous, puis relancer."""

EMAIL = "paul@thecuriouscrowd.fr"
FORM = f"https://formsubmit.co/ajax/{EMAIL}"  # 1er envoi : cliquer le lien d'activation reçu par email

EVENTS = [
    dict(day="11", month="Nov.", when="Mercredi 11 novembre · 19h45", tag="Grand reportage",
         title="Au cœur du conflit : récits d’une reporter", img="evt-conflit",
         desc="Dans les coulisses du reportage en terrain de guerre, avec Agathe Mahuet, reporter à France Info. Envoyée spéciale régulière à l’étranger, notamment en Ukraine et en Israël, lauréate du Grand Prix Varenne de la Radio 2024 pour un reportage en Ukraine. Elle répondra à toutes vos questions sur les difficultés du journalisme en zones de conflit.",
         url="https://buy.stripe.com/28E3cv5wF8QI3b1bRpdnW00"),
    dict(day="2", month="Déc.", when="Mercredi 2 décembre · 19h45", tag="L’envers du trône",
         title="Les coulisses de la famille royale britannique", img="evt-royales",
         desc="Rivalités, scandales, presse people… Margaret Macdonald (Elle, Paris Match, Gala), autrice de « Royales et Rebelles », raconte combien il est difficile d’être une femme au sein de la famille royale, anecdotes à l’appui. Venez lui poser toutes vos questions !",
         url="https://buy.stripe.com/bJe9AT8IRgjah1R3kTdnW02"),
]

def row(t, d): return f'<div class="row"><h4>{t}</h4><p>{d}</p></div>'

def page(file, title, desc, body):
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://www.thecuriouscrowd.fr/img/hero.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="favicon.svg?v=2" type="image/svg+xml">
<link rel="icon" href="favicon-32.png?v=2" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png?v=2">
<meta name="theme-color" content="#fff8ec">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="nav">
  <div class="wrap">
    <a class="logo" href="index.html">The <b>Curious</b> Crowd</a>
    <ul><li><a href="index.html#concept">Concept</a></li><li><a href="index.html#format">Format</a></li><li><a href="lieu-partenaire.html">Lieux partenaires</a></li></ul>
    <a class="btn" href="conferences.html">Réserver ma place</a>
    <button class="burger" aria-label="Ouvrir le menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
  <nav class="menu" aria-label="Menu mobile">
    <a class="m" href="conferences.html">Prochaines soirées</a>
    <a class="m" href="index.html#concept">Concept</a>
    <a class="m" href="index.html#format">Format</a>
    <a class="m" href="lieu-partenaire.html">Lieux partenaires</a>
    <a class="m" href="intervenant.html">Proposer un sujet</a>
    <img class="photo" src="img/concept1.jpg" alt="" style="height:180px;margin-top:24px">
    <a class="btn" href="conferences.html">Réserver ma place</a>
    <a class="link--muted" href="mailto:{EMAIL}">{EMAIL}</a>
  </nav>
</header>
<main>
{body}
</main>
<footer class="footer">
  <div class="wrap">
    <a class="logo" href="index.html">The <b>Curious</b> Crowd</a>
    <small>© 2026 The Curious Crowd · Rencontres en petit comité · Paris · <a href="mentions-legales.html">Mentions légales</a></small>
  </div>
</footer>
<script>
const b=document.querySelector('.burger'),m=document.querySelector('.menu');
b.addEventListener('click',()=>{{const o=m.classList.toggle('open');b.setAttribute('aria-expanded',o);document.body.style.overflow=o?'hidden':''}});
document.querySelectorAll('form').forEach(f=>f.addEventListener('submit',async e=>{{e.preventDefault();const btn=f.querySelector('button');btn.disabled=true;btn.textContent='Envoi…';try{{const r=await fetch(f.action,{{method:'POST',headers:{{Accept:'application/json'}},body:new FormData(f)}});if(!r.ok)throw 0;f.hidden=true;f.nextElementSibling.hidden=false}}catch(_){{btn.disabled=false;btn.textContent='Réessayer';alert('L’envoi a échoué. Écrivez-nous à {EMAIL}')}}}}));
m.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{{m.classList.remove('open');document.body.style.overflow=''}}));
</script>
</body>
</html>
"""
    open(file, "w", encoding="utf-8").write(html)

def head(label, a, b, sub=None):
    t = f'{a} ' if a else ''
    s = f'<p class="lead">{sub}</p>' if sub else ''
    return f'<div class="stack"><p class="label">{label}</p><h1 class="h1">{t}<span class="hl">{b}</span></h1>{s}</div>'

def field(name, label, ph, big=False, req=True, typ="text"):
    r = " required" if req else ""
    tag = f'<textarea name="{name}" placeholder="{ph}"{r}></textarea>' if big else f'<input type="{typ}" name="{name}" placeholder="{ph}"{r}>'
    return f'<label>{label}{tag}</label>'

def form(title, subject, fields, cta):
    return f"""<div class="card"><p class="label">Formulaire</p><h2 class="h3">{title}</h2>
<form action="{FORM}" method="POST">
<input type="hidden" name="_subject" value="{subject}"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table"><input type="text" name="_honey" style="display:none">
{''.join(fields)}
<div><button class="btn full-m" type="submit">{cta}</button><p class="note" style="margin-top:12px">On vous répond sous 48 h.</p></div>
</form><div class="sent" hidden><h3 class="h3"><span class="hl">Merci !</span></h3><p>Votre message est bien parti à l’équipe. On vous répond sous 48 h.</p></div></div>"""

# ---------- Accueil ----------
page("index.html", "The Curious Crowd — Les coulisses des métiers, racontées par ceux qui les font",
"Rencontres en petit comité dans des bars parisiens : un intervenant, 20 à 40 curieux, 1 verre offert.", f"""
<section class="hero"><div class="orb" style="width:300px;height:300px;right:28%;top:120px"></div><div class="wrap">
  <div class="hero-grid">
    <div>
      <h1 class="h1">Les <span class="blue">coulisses</span> des métiers et de l’actualité, racontées par <span class="hl">ceux qui les font.</span></h1>
      <p class="lead" style="margin-top:28px">Un verre avec un reporter de guerre, un médaillé olympique ou un DJ international. Ils racontent les coulisses de leur métier, vous posez vos questions.</p>
      <div class="ctas"><a class="btn" href="conferences.html">Voir nos prochaines soirées</a><a class="link" href="lieu-partenaire.html">Devenir lieu partenaire →</a></div>
    </div>
    <img class="photo" src="img/hero.jpg" alt="Une soirée The Curious Crowd dans un bar parisien">
  </div>
  <div class="infos"><span>1 soir de semaine</span><span>1 bar dans Paris</span><span>20 à 40 participants</span><span>20 € la soirée, 1 verre de votre choix offert</span><span>Paris</span></div>
</div></section>

<section id="concept" style="background:var(--ciel)"><div class="orb" style="width:450px;height:450px;right:-200px;bottom:-150px"></div><div class="wrap stack">
  <div class="cols cols-2" style="gap:48px 96px">
    <h2 class="h2">Des échanges de qualité dans des lieux qui ont du <span class="blue">caractère</span>.</h2>
    <div class="stack"><p>The Curious Crowd organise des échanges autour d’un verre en petit comité dans des bars ou des hôtels parisiens. Un intervenant partage ce qu’il sait d’un sujet précis, dans une ambiance où chacun peut poser ses questions quand il veut.</p><p>Le format a fait ses preuves aux Etats-Unis (Lectures on tap), et nous l’avons testé lors de plusieurs soirées privées d’une vingtaine de personnes.</p></div>
  </div>
  <div class="cols" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr));margin-top:56px">
    <img class="photo" src="img/concept1.jpg" alt="Un intervenant face au public" style="height:420px"><img class="photo" src="img/concept2.jpg" alt="Le comptoir d’un bar parisien" style="height:420px;grid-column:span 1">
  </div>
  <div class="cols cols-3" style="margin-top:56px">
    <div class="kpi"><strong>1</strong><span>soir de semaine</span></div><div class="kpi"><strong>20–40</strong><span>participants</span></div><div class="kpi"><strong>1</strong><span>verre de votre choix offert</span></div>
  </div>
</div></section>

<section id="format"><div class="wrap">
  <h2 class="h2">Une soirée, un intervenant, <span class="hl">des coulisses.</span></h2>
  <img class="photo" src="img/format.jpg" alt="Une rencontre dans un bar" style="height:340px;margin:56px 0">
  <div class="cols cols-3">
    <div class="step"><strong>19h45</strong><p>Accueil des participants autour d’un verre. Premier verre offert avec votre billet d’entrée.</p></div>
    <div class="step"><strong>20h15</strong><p>Début de l’échange avec l’intervenant.</p></div>
    <div class="step"><strong>21h30</strong><p>Prolongation de la soirée : rencontres, verres et discussions informelles.</p></div>
  </div>
</div></section>

<section style="background:var(--miel)"><div class="wrap">
  <h2 class="h2">Participants, intervenants ou propriétaires de lieux : à chacun son rendez-vous.</h2>
  <div class="cols cols-2" style="margin-top:56px">
    <div class="card"><img class="photo" src="img/participants.jpg" alt="" style="height:220px"><p class="label">Pour les participants</p><h3 class="h3">Venez avec votre curiosité, repartez avec une histoire à raconter.</h3>
      <div>{row("20 € la soirée","1 verre de votre choix offert.")}{row("20 à 40 personnes","Idéal pour faire des rencontres.")}{row("Des sujets concrets","Des échanges, jamais de cours magistral.")}</div>
      <div><a class="btn full-m" href="conferences.html">Réserver ma place</a></div></div>
    <div class="card card--dark"><img class="photo" src="img/concept2.jpg" alt="Le comptoir d’un bar parisien" style="height:220px"><p class="label">Pour les bars et les hôtels</p><h3 class="h3">Un soir calme ? Remplissez-le de curieux.</h3>
      <div>{row("Du monde un soir creux","Un public assuré sur un créneau de faible affluence.")}{row("Du chiffre assuré","Au moins une consommation par personne, bien souvent plusieurs verres et de la restauration annexe.")}{row("De l’image","Une communauté fidèle et un positionnement culturel.")}{row("Du clé en main","Invités, contenu, animation et communication : nous nous chargeons de tout.")}</div>
      <div><a class="btn btn--light full-m" href="lieu-partenaire.html">Devenir lieu partenaire</a></div></div>
  </div>
  <div class="card" style="margin-top:24px;flex-direction:row;flex-wrap:wrap;align-items:center;justify-content:space-between">
    <div class="stack"><p class="label">Pour les intervenants</p><h3 class="h3">Vous êtes spécialiste d’un sujet ?<br>Une histoire à raconter ?<br>Un livre à promouvoir ?</h3></div>
    <a class="btn full-m" href="intervenant.html">Contactez-nous</a>
  </div>
</div></section>

<section style="background:#fff"><div class="wrap">
  <h2 class="h2">Construire une communauté autour des idées.</h2>
  <div class="cols cols-2" style="margin:56px 0"><img class="photo" src="img/ambition1.jpg" alt="" style="height:300px"><img class="photo" src="img/ambition2.jpg" alt="" style="height:300px;object-position:center 75%"></div>
  <div class="cols cols-2" style="gap:48px">
    <div><h3 style="font-size:22px;margin-bottom:8px">Court terme</h3><div class="goal"><span>01</span>Lancer une programmation régulière à Paris</div><div class="goal"><span>02</span>Bâtir une communauté fidèle</div><div class="goal"><span>03</span>Installer une identité forte avec des partenaires locaux</div></div>
    <div><h3 style="font-size:22px;margin-bottom:8px">Moyen terme</h3><div class="goal"><span>01</span>Développer des formats récurrents</div><div class="goal"><span>02</span>Nouer des partenariats culturels et médias</div><div class="goal"><span>03</span>Étendre le concept à d’autres villes</div></div>
  </div>
</div></section>

<section class="contact"><div class="orb" style="width:400px;height:400px;right:-120px;top:-80px;opacity:.6"></div><div class="wrap">
  <h2 class="h1" style="max-width:860px">Rencontrons-nous vite.</h2>
  <div class="ctas"><a class="btn btn--light" href="mailto:{EMAIL}">Écrire à l’équipe</a><a class="link" style="font-size:20px;text-decoration:none" href="mailto:{EMAIL}">{EMAIL}</a></div>
</div></section>
""")

# ---------- Prochaines soirées ----------
cards = "".join(f"""<article class="card event">
  <div class="date"><strong>{e['day']}</strong><span class="hl">{e['month']}</span></div>
  <div class="stack">
    <p class="label">{e['when']} · {e['tag']}</p><h2 class="h3">{e['title']}</h2><p>{e['desc']}</p>
    <div class="cols cols-2">{row("Café Lino","81 bd de Charonne, 75011 Paris")}{row("20 € l’entrée","1 verre de votre choix offert")}</div>
    <div class="actions"><a class="btn full-m" href="{e['url']}">Réserver ma place</a><span class="note">Paiement sécurisé via Stripe</span></div>
  </div>
  <img class="photo" src="img/{e['img']}.jpg" alt="{e['title']}">
</article>""" for e in EVENTS)
page("conferences.html", "Prochaines soirées — The Curious Crowd", "Choisissez votre soirée et réservez votre place.", f"""
<section><div class="wrap stack">{head("Agenda","Les prochaines","soirées.","Choisissez votre soirée, réservez votre place, et venez avec vos questions. Places limitées.")}
<div class="stack" style="margin-top:56px">{cards}</div></div></section>""")

# ---------- Lieu partenaire ----------
page("lieu-partenaire.html", "Devenir lieu partenaire — The Curious Crowd", "Accueillez nos soirées : 20 à 40 curieux un soir de semaine, on s’occupe de tout.", f"""
<section><div class="wrap stack">{head("Lieux partenaires","Votre lieu,","notre scène.","Un soir de semaine, 20 à 40 curieux viennent écouter un intervenant… et consomment chez vous. Vous ouvrez vos portes, on s’occupe de tout le reste.")}
<img class="photo banner" src="img/participants.jpg" alt="Un bar partenaire en soirée" style="margin-top:56px">
<div class="cols cols-2" style="align-items:start">
  <div class="card"><p class="label">Pourquoi nous accueillir</p><h2 class="h3">Un soir creux qui devient un soir plein.</h2><div>{row("Du monde un soir creux","20 à 40 personnes en semaine, à partir de 19h45.")}{row("Du chiffre assuré","Au moins une consommation par personne, bien souvent plusieurs verres et de la restauration annexe.")}{row("Une nouvelle clientèle","Des curieux qui découvrent votre lieu… et y reviennent.")}{row("Du clé en main","Intervenant, billetterie, animation et communication : on gère tout.")}</div></div>
  {form("Parlez-nous de votre lieu.","Nouveau lieu partenaire",[field("lieu","Nom du lieu","Ex. Café Lino"),field("adresse","Adresse","Rue et arrondissement"),field("capacite","Capacité assise","Ex. 40 places"),field("nom","Prénom et nom","Ex. Camille Martin"),field("email","Email","vous@exemple.fr",typ="email"),field("message","Un mot sur votre lieu (facultatif)","Ambiance, soirs calmes, disponibilités…",big=True,req=False)],"Proposer mon lieu")}
</div></div></section>""")

# ---------- Intervenant ----------
page("intervenant.html", "Proposer un sujet — The Curious Crowd", "Racontez votre métier à 20 à 40 curieux, autour d’un verre.", f"""
<section><div class="wrap stack">{head("Intervenants","Votre métier,","notre sujet du soir.","Reporter, sportive, chef, chercheur… Votre quotidien fascine ceux qui ne le vivent pas. Venez le raconter à 20 à 40 curieux, autour d’un verre.")}
<img class="photo banner" src="img/format.jpg" alt="Soirée en petit comité" style="margin-top:56px">
<div class="cols cols-2" style="align-items:start">
  <div class="card"><p class="label">Comment se déroule une soirée</p><h2 class="h3">Vous racontez, ils vous questionnent.</h2><div>{row("Une rencontre, pas un cours magistral","Votre métier, vos coulisses, vos anecdotes. Pas besoin de slides.")}{row("Des questions au fil de l’eau","Le public intervient quand il veut, dans une ambiance détendue.")}{row("Un public curieux","20 à 40 personnes, dans un bar ou un hôtel parisien.")}{row("Du clé en main","Lieu, billetterie, animation et communication : on gère tout.")}</div></div>
  {form("Parlez-nous de votre sujet.","Nouvelle proposition d’intervenant",[field("nom","Prénom et nom","Ex. Camille Martin"),field("metier","Votre métier","Ex. reporter, autrice, DJ"),field("sujet","Le sujet que vous aimeriez raconter","Ex. Couvrir une guerre en direct"),field("email","Email","vous@exemple.fr",typ="email"),field("liens","Liens (facultatif)","Site, articles, podcast, réseaux…",req=False),field("message","Un mot de plus (facultatif)","Anecdotes, disponibilités, questions…",big=True,req=False)],"Proposer mon sujet")}
</div></div></section>""")

# ---------- Merci (paiement) & merci (formulaire) ----------
page("merci.html", "Réservation confirmée — The Curious Crowd", "Merci pour votre réservation.", f"""
<section><div class="wrap stack">{head("Réservation confirmée","C’est","réservé !","Merci ! Votre reçu vous a été envoyé par email. On a hâte de vous voir.")}
<img class="photo banner" src="img/concept2.jpg" alt="" style="margin-top:56px">
<div class="card"><p class="label">Votre soirée</p><h2 class="h3">Le mercredi, à partir de 19h45.</h2><div>{row("Café Lino","81 bd de Charonne, 75011 Paris · Métro Alexandre Dumas")}{row("Votre billet","20 € · 1 verre de votre choix offert")}{row("Arrivée","Accueil dès 19h45 autour d’un verre, début de l’échange à 20h15.")}</div>
<div class="ctas" style="margin-top:0"><a class="btn" href="conferences.html">Voir les autres soirées</a></div></div>
</div></section>""")
# ---------- Mentions légales ----------
legal = "".join(f'<h3 style="font-size:20px;margin-top:8px">{h}</h3><p>{t}</p>' for h, t in [
 ("Éditeur", f"The Curious Crowd — [forme juridique, capital, SIRET], [adresse], Paris. Directeur de la publication : [nom]. Contact : {EMAIL}"),
 ("Hébergement", "GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis."),
 ("Paiements", "Les paiements sont traités de façon sécurisée par Stripe. Aucune donnée bancaire n’est conservée par The Curious Crowd."),
 ("Données personnelles", "Les données collectées via les formulaires servent uniquement à vous recontacter. Vous pouvez demander leur suppression à tout moment par email.")])
page("mentions-legales.html", "Mentions légales — The Curious Crowd", "Mentions légales du site The Curious Crowd.", f"""
<section><div class="wrap stack">{head("Informations","","Mentions légales.")}
<img class="photo banner" src="img/ambition1.jpg" alt="" style="margin-top:56px">
<div class="card" style="max-width:860px">{legal}</div>
</div></section>""")
print("ok")
