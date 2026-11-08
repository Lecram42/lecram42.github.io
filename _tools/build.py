"""Génère index.html, une page par app, sitemap.xml et 404.html.

Usage :  python _tools/build.py      (depuis la racine du dépôt)
Pour ajouter une app : ajouter une entrée dans APPS ci-dessous (et ses
images dans images/), puis relancer le script.
"""
import datetime, html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://lecram42.github.io"
AUTHOR = "Florian Marcel"
TODAY = datetime.date.today().isoformat()
ASSETS = json.load(open(os.path.join(ROOT, "_tools", "assets.json"), encoding="utf-8"))

# ---------------------------------------------------------------------------
# Contenu. `features` = puces, `about` = paragraphes, `faq` = (question, réponse).
# ---------------------------------------------------------------------------
APPS = [
    {
        "slug": "souffly", "name": "Souffly", "id": "6804810131",
        "subtitle": "Bougies & cotillons de fête",
        "title": "Souffly — Souffle sur des bougies d'anniversaire virtuelles (iPhone)",
        "description": "Souffly : souffle dans le micro de ton iPhone pour éteindre des bougies d'anniversaire, dérouler un sifflet de fête ou faire tourner un moulin à vent. Gratuit, sans compte.",
        "category": "EntertainmentApplication", "store_cat": "Divertissement",
        "card": "Souffle sur des bougies d'anniversaire",
        "lead": "Des bougies d'anniversaire, un sifflet de fête et un moulin à vent qui réagissent à ton souffle, en temps réel, grâce au micro de ton iPhone.",
        "about": [
            "Pas de gâteau sous la main, un anniversaire à distance, ou juste envie d'amuser les enfants ? Souffly transforme ton téléphone en accessoire de fête : allume les bougies, souffle fort… et regarde-les s'éteindre une à une.",
            "Choisis le nombre de bougies, ajoute une photo, puis partage le moment sur Messages, WhatsApp ou Instagram. Le sifflet de fête (la « langue de belle-mère ») se déroule quand tu souffles, et le moulin à vent tourne avec une vraie inertie.",
        ],
        "features": [
            "Bougies d'anniversaire virtuelles : nombre réglable, photo personnalisée",
            "Sifflet de fête qui se déroule à chaque souffle",
            "Moulin à vent à six pales avec inertie réaliste",
            "Détection du souffle en temps réel via le micro",
            "Partage en un tap sur Messages, WhatsApp, Instagram",
            "Aucun compte, rien n'est envoyé sur un serveur",
        ],
        "faq": [
            ("Comment éteindre les bougies dans Souffly ?", "Il suffit de souffler vers le micro de l'iPhone, comme sur un vrai gâteau. Plus le souffle est fort, plus les flammes vacillent et s'éteignent vite."),
            ("Souffly est-il gratuit ?", "Oui. L'app est gratuite ; le sifflet et le moulin se débloquent définitivement après une courte publicité."),
            ("Le son du micro est-il enregistré ?", "Non. Le micro sert uniquement à mesurer l'intensité du souffle sur l'appareil ; aucun son n'est enregistré ni envoyé."),
        ],
        "keywords": "bougies d'anniversaire virtuelles, souffler bougie application, gâteau d'anniversaire iPhone, sifflet de fête, langue de belle-mère, moulin à vent",
        "legal": "Souffly-legal",
    },
    {
        "slug": "meuhbox", "name": "MeuhBox", "id": "6820679499",
        "subtitle": "Retourne ton tél, il meugle !",
        "title": "MeuhBox — La boîte à meuh dans ton iPhone : retourne-le, il meugle",
        "description": "MeuhBox transforme ton iPhone en boîte à meuh : retourne-le et il meugle. 16 boîtes à collectionner, de la vache de Paris au mouton des alpages. Gratuit.",
        "category": "EntertainmentApplication", "store_cat": "Divertissement",
        "card": "Retourne ton téléphone, il meugle",
        "lead": "Le jouet de notre enfance, version iPhone : retourne ton téléphone comme une boîte à meuh… et il meugle.",
        "about": [
            "MeuhBox reproduit le geste de la boîte à meuh : retourne ton iPhone… et il meugle. Le capteur de mouvement fait tout, il n'y a aucun bouton à presser.",
            "Collectionne 16 boîtes illustrées venues du monde entier, de la vache de Paris au bêlement des alpages, chacune avec son animal, son décor et son « accent ». Certains sons sont de vrais enregistrements.",
        ],
        "features": [
            "Retourne le téléphone pour faire meugler la boîte",
            "16 boîtes illustrées à collectionner",
            "Sons réels pour certains animaux",
            "Fonctionne même en mode silencieux, avec vibration",
            "Sensibilité du retournement réglable",
            "La boîte de Paris est offerte, les autres se débloquent avec une vidéo",
        ],
        "faq": [
            ("Comment fonctionne MeuhBox ?", "Retourne ton iPhone comme une vraie boîte à meuh : l'accéléromètre détecte le mouvement et la boîte meugle."),
            ("MeuhBox est-elle gratuite ?", "Oui. La boîte de Paris est disponible immédiatement, les autres se débloquent en regardant une courte vidéo."),
            ("Faut-il créer un compte ?", "Non, aucun compte n'est nécessaire."),
        ],
        "keywords": "boîte à meuh, boite a meuh application, meuh iPhone, jouet vache, son de vache, retourner téléphone",
        "legal": "meuhbox-legal",
    },
    {
        "slug": "phoneopener", "name": "PhoneOpener", "id": "6807761733",
        "subtitle": "Fais sauter des capsules !",
        "title": "PhoneOpener — Décapsuleur virtuel : fais sauter des capsules (iPhone)",
        "description": "PhoneOpener : tire le décapsuleur, fais sauter des capsules et complète ta collection de 24 modèles. Jeu gratuit pour iPhone, sans achat ni abonnement.",
        "category": "GameApplication", "store_cat": "Divertissement",
        "card": "Décapsule et collectionne",
        "lead": "Tire le décapsuleur, fais sauter la capsule… et complète ta collection de 24 modèles.",
        "about": [
            "PhoneOpener est un petit jeu de décapsulage : glisse le doigt pour tirer le décapsuleur et fais sauter des capsules de bouteille. Chaque capsule rejoint ta collection, des plus courantes aux plus rares.",
            "Monte dans les six rangs, consulte tes statistiques et partage tes trouvailles sur WhatsApp ou par SMS. Sept décapsuleurs différents sont à débloquer.",
            "Les bouteilles et capsules sont virtuelles : n'utilise jamais ton téléphone pour ouvrir une vraie bouteille.",
        ],
        "features": [
            "24 capsules à collectionner, dont des rares",
            "6 rangs à gravir",
            "7 décapsuleurs à débloquer",
            "Écran de collection avec statistiques",
            "Partage sur WhatsApp ou par SMS",
            "Aucun achat, aucun abonnement",
        ],
        "faq": [
            ("PhoneOpener ouvre-t-il de vraies bouteilles ?", "Non. Tout est virtuel : c'est un jeu de collection. N'utilise jamais ton téléphone comme décapsuleur."),
            ("Combien y a-t-il de capsules ?", "24 capsules, réparties de la plus commune à la plus rare."),
        ],
        "keywords": "décapsuleur, capsule de bouteille, jeu de collection, décapsuleur virtuel, collection de capsules",
        "legal": "PhoneOpener-legal",
    },
    {
        "slug": "tiltboat", "name": "TiltBoat", "id": "6796813347",
        "subtitle": "Ton bateau qui tangue au tilt",
        "title": "TiltBoat — Incline ton iPhone et fais tanguer ton bateau",
        "description": "TiltBoat, jouet relaxant pour iPhone et iPad : incline le téléphone pour faire tanguer ton bateau. Débloque voiliers, équipage, baleines et tempêtes. Gratuit.",
        "category": "GameApplication", "store_cat": "Simulation",
        "card": "Ton bateau qui tangue au tilt",
        "lead": "Incline ton téléphone et regarde ton bateau tanguer sur la mer, comme une maquette que tu tiendrais entre tes mains.",
        "about": [
            "TiltBoat est un petit jouet numérique pour se détendre. Grâce aux capteurs de mouvement, chaque inclinaison fait vraiment bouger le bateau : pas de bouton, pas d'objectif, juste toi et la mer. Un pavé tactile permet aussi de simuler l'inclinaison du bout du doigt.",
            "Du petit radeau au paquebot, en passant par le voilier, la barque ou le sous-marin : débloque ta flotte, ajoute un équipage (matelot, bouée canard, sirène…), de la faune (tortue, baleine, requin) et change la météo (tempête, neige, arc-en-ciel).",
        ],
        "features": [
            "Contrôle par inclinaison (gyroscope) ou pavé tactile",
            "Une flotte de bateaux à débloquer",
            "Équipage, faune marine et météo personnalisables",
            "Bonus quotidien de pièces, sans pression",
            "iPhone et iPad, en français, anglais et espagnol",
            "Aucun compte, aucune donnée envoyée",
        ],
        "faq": [
            ("TiltBoat est-il un jeu ?", "C'est plutôt un jouet relaxant : il n'y a ni score ni objectif, on incline le téléphone et on regarde le bateau réagir."),
            ("Faut-il payer pour débloquer les bateaux ?", "Non : les pièces se gagnent avec le bonus quotidien ou en regardant une publicité facultative."),
        ],
        "keywords": "jeu bateau, jouet relaxant, inclinaison téléphone, gyroscope, voilier, mer, tempête, application anti-stress",
        "legal": "tiltboat-legal",
    },
    {
        "slug": "weave", "name": "Weave", "id": "6807174206",
        "subtitle": "Esquive le trafic à moto",
        "title": "Weave — Jeu de moto arcade : esquive le trafic (iPhone)",
        "description": "Weave, jeu d'arcade gratuit pour iPhone : ta moto file sur une route à deux voies, esquive voitures, nids-de-poule et flaques d'huile. Un seul geste, vitesse croissante.",
        "category": "GameApplication", "store_cat": "Jeux · Action",
        "card": "Esquive le trafic à moto",
        "lead": "Ta moto avance toute seule : à toi de basculer à gauche ou à droite pour esquiver le trafic, de plus en plus vite.",
        "about": [
            "Weave est un jeu d'arcade en vue du dessus. Sur une route à deux voies, esquive voitures, nids-de-poule et flaques d'huile d'un simple tap ou swipe. La vitesse ne fait qu'augmenter : combien de mètres tiendras-tu ?",
            "Style flat design coloré, prise en main immédiate, une seconde chance par partie, et de l'équipement cosmétique à débloquer gratuitement : moto, blouson, casque, traînée de vitesse.",
        ],
        "features": [
            "Un seul geste : gauche ou droite",
            "Difficulté et vitesse qui augmentent avec la distance",
            "Record affiché sur l'écran d'accueil et partageable",
            "Une seconde chance par partie",
            "Motos, blousons et casques à débloquer gratuitement",
            "Aucun compte, aucune donnée collectée",
        ],
        "faq": [
            ("Weave est-il gratuit ?", "Oui, entièrement. Les éléments cosmétiques se débloquent en regardant des publicités facultatives."),
            ("Peut-on jouer hors connexion ?", "Oui, la partie fonctionne sans connexion."),
        ],
        "keywords": "jeu de moto, jeu arcade, esquiver voitures, jeu de course, jeu simple, endless runner",
        "legal": "Weave-legal",
    },
    {
        "slug": "cornall", "name": "CornAll", "id": "6805999212",
        "subtitle": "Comptage cornhole & tournois",
        "title": "CornAll — Compteur de points cornhole et tournois (iPhone)",
        "description": "CornAll compte les points de cornhole en solo, duo ou mêlée et gère des tournois de 3 à 8 joueurs sur plusieurs planches. Historique, stats, hors ligne. Gratuit.",
        "category": "SportsApplication", "store_cat": "Sports",
        "card": "Compteur de points cornhole & tournois",
        "lead": "Le compteur de points pour le cornhole : solo, duo ou mêlée, et un vrai mode tournoi sur plusieurs planches.",
        "about": [
            "Fini le calcul de tête et les disputes sur le score : CornAll applique les règles du cornhole (sac sur la planche, sac dans le trou, annulation des points) et affiche le score de chaque manche.",
            "Organise un tournoi de 3 à 8 joueurs sur plusieurs planches en parallèle, retrouve l'historique de tes parties et tes statistiques, puis partage la carte de résultat avec les joueurs.",
        ],
        "features": [
            "Six formats de partie : solo, duo, mêlée…",
            "Mode tournoi de 3 à 8 joueurs, multi-planches",
            "Historique des parties et statistiques",
            "Export et import de l'historique",
            "Carte de résultat à partager",
            "Hors ligne, sans compte, thème clair ou sombre",
        ],
        "faq": [
            ("Comment compter les points au cornhole ?", "Un sac sur la planche vaut 1 point, un sac dans le trou vaut 3 points, et les points des deux équipes s'annulent à chaque manche. CornAll fait ce calcul pour toi."),
            ("CornAll gère-t-il les tournois ?", "Oui, de 3 à 8 joueurs, avec plusieurs planches en parallèle."),
            ("Faut-il une connexion Internet ?", "Non, l'app fonctionne entièrement hors ligne."),
        ],
        "keywords": "cornhole, compteur de points cornhole, règles cornhole, tournoi cornhole, score cornhole, jeu de sacs",
        "legal": "Cornall-legal",
    },
    {
        "slug": "bonnedatemeteo", "name": "BonneDateMétéo", "id": "6809931304",
        "subtitle": "Météo historique événements",
        "title": "BonneDateMétéo — Choisir la date de son mariage selon la météo historique",
        "description": "Mariage, anniversaire, festival en extérieur : BonneDateMétéo analyse 20 ans de météo réelle pour trouver le jour le plus sûr, même un an à l'avance. Gratuit, sans compte.",
        "category": "WeatherApplication", "store_cat": "Météo",
        "card": "Choisir sa date selon la météo historique",
        "lead": "Mariage, anniversaire, fête en plein air : choisis la date qui a le plus de chances d'être ensoleillée, grâce à 20 ans d'historique météo.",
        "about": [
            "Personne ne peut prévoir la météo d'un 15 juin un an à l'avance. Mais on peut savoir que, ces quinze dernières années, il a fait beau ce jour-là 12 fois sur 15 à cet endroit. C'est exactement ce que montre BonneDateMétéo.",
            "Indique un lieu et une période : l'app consulte 20 ans de données réelles (pluie, température, vent) et colore chaque jour en vert, orange ou rouge selon la proportion d'années où tes critères ont été respectés. À l'approche de la date, la vraie prévision prend le relais.",
        ],
        "features": [
            "20 ans de données météo réelles par lieu",
            "Calendrier vert / orange / rouge jour par jour",
            "Profils Standard, Tolérant, Exigeant ou critères sur mesure",
            "Prévision réelle affichée à moins de 15 jours",
            "Rappels automatiques avant l'événement",
            "Rapport partageable avec le wedding planner ou les invités",
        ],
        "faq": [
            ("Comment choisir la date d'un mariage en fonction de la météo ?", "Les prévisions ne vont pas au-delà de 15 jours. Pour une date lointaine, le plus fiable est de regarder la météo réelle de ce jour sur les années passées : c'est ce que calcule BonneDateMétéo sur 20 ans."),
            ("BonneDateMétéo prédit-elle la météo ?", "Non. Elle affiche des statistiques historiques, puis la vraie prévision quand la date est à moins de 15 jours."),
            ("Mes données sont-elles envoyées ?", "Non, aucun compte n'est nécessaire et tes événements restent sur ton téléphone."),
        ],
        "keywords": "météo mariage, choisir date mariage, météo historique, statistiques météo, quel jour fera beau, fête en extérieur",
        "legal": "bonnedatemeteo-legal",
    },
    {
        "slug": "countit", "name": "CountIt", "id": "6790743817",
        "play": "app.countit.mobile",
        "subtitle": "Carnet intime & prévention",
        "title": "CountIt — Carnet intime privé et chiffré, santé sexuelle et prévention",
        "description": "CountIt, carnet intime 100 % local et chiffré : note tes rencontres sans jugement, suis tes statistiques et garde les bons réflexes de prévention IST/VIH. iPhone et Android.",
        "category": "LifestyleApplication", "store_cat": "Style de vie",
        "card": "Carnet intime privé & prévention",
        "lead": "Le carnet privé et chiffré pour garder une trace de tes rencontres, sans jugement, sans cloud, avec la prévention intégrée.",
        "about": [
            "CountIt n'est pas un réseau social : pas de profil, pas de fil, pas de swipe. Juste un carnet où noter chaque rencontre en quelques secondes, avec ton ressenti, la protection utilisée et une note libre.",
            "Toutes les données restent sur ton téléphone, chiffrées avec une clé dérivée de ton mot de passe, et se déverrouillent avec Face ID ou l'empreinte digitale. Un onglet prévention rappelle les bons réflexes (dépistage IST/VIH, PEP) et des ressources fiables.",
        ],
        "features": [
            "Données 100 % locales et chiffrées, sans cloud",
            "Déverrouillage Face ID / empreinte digitale",
            "Statistiques et graphique d'activité",
            "Badges qui récompensent la régularité et la prévention",
            "Onglet prévention IST/VIH avec ressources fiables",
            "Export, import et suppression complète en un geste",
        ],
        "faq": [
            ("Mes données sont-elles envoyées sur un serveur ?", "Non. Tout est stocké et chiffré sur ton téléphone ; même le développeur n'y a pas accès."),
            ("CountIt est-il gratuit ?", "Le carnet est gratuit ; les statistiques se débloquent par un achat unique à vie, sans abonnement."),
            ("À qui s'adresse CountIt ?", "Aux personnes de 18 ans et plus. Ce n'est pas un service médical : en cas de doute, consulte un professionnel de santé."),
        ],
        "keywords": "carnet intime, journal intime privé, santé sexuelle, prévention IST, dépistage VIH, application chiffrée",
        "legal": "countit-legal",
    },
]

OS_LABEL = {"countit": "iPhone & Android", "tiltboat": "iPhone & iPad", "bonnedatemeteo": "iPhone & iPad"}

e = html.escape


def store_url(a):
    return f"https://apps.apple.com/fr/app/id{a['id']}"


def lum(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


CSS = """
:root{--bg:#f6f7f9;--card:#fff;--text:#1a1d23;--muted:#5d636e;--border:#e3e6ea;--accent:#3a6df0;--on-accent:#fff;--radius:16px}
@media (prefers-color-scheme:dark){:root{--bg:#121417;--card:#1c1f24;--text:#f0f1f3;--muted:#9ba1ab;--border:#2b2f36;--accent:#6c93ff}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent)}
.wrap{max-width:860px;margin:0 auto;padding:0 20px}
.top{padding-top:18px;padding-bottom:18px;font-size:.92rem}
.top a{color:var(--muted);text-decoration:none}
.top a:hover{color:var(--text)}
h1,h2{line-height:1.2;text-wrap:balance}
h2{font-size:1.3rem;margin:44px 0 12px}
.hero{display:flex;gap:22px;align-items:center;padding:28px 0 8px}
.hero img{width:112px;height:112px;border-radius:26px;flex-shrink:0;box-shadow:0 6px 24px -8px rgba(0,0,0,.35)}
.hero h1{font-size:2.1rem;margin:0 0 4px}
.hero .sub{margin:0;color:var(--muted);font-size:1.05rem}
.lead{font-size:1.15rem;margin:22px 0}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 22px;padding:0;list-style:none}
.meta li{font-size:.82rem;padding:4px 10px;border:1px solid var(--border);border-radius:99px;color:var(--muted)}
.cta{display:inline-flex;align-items:center;gap:10px;background:var(--app,var(--accent));color:var(--on-app,var(--on-accent));text-decoration:none;font-weight:650;padding:13px 22px;border-radius:12px}
.cta:hover{filter:brightness(1.08)}
.cta svg{width:20px;height:20px;fill:currentColor}
.cta.alt{background:transparent;color:var(--text);border:1px solid var(--border);margin-left:8px}
.shots{display:flex;gap:14px;overflow-x:auto;padding:6px 2px 14px;margin:30px 0 0;scroll-snap-type:x mandatory}
.shots img{height:420px;width:auto;border-radius:18px;border:1px solid var(--border);scroll-snap-align:start;flex-shrink:0}
.shots.land img{height:260px}
.shots.square img{height:240px;border:0}
ul.feat{padding-left:1.2em}
ul.feat li{margin:4px 0}
details{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px 16px;margin:8px 0}
summary{font-weight:600;cursor:pointer}
details p{margin:10px 0 0;color:var(--muted)}
.grid{display:grid;grid-template-columns:1fr;gap:12px;padding:0;margin:0;list-style:none}
@media (min-width:560px){.grid{grid-template-columns:1fr 1fr}}
.card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:16px;display:flex;align-items:center;gap:14px;text-decoration:none;color:inherit;height:100%;transition:border-color .15s,transform .15s}
.card:hover{border-color:var(--accent);transform:translateY(-1px)}
.card img{width:56px;height:56px;border-radius:13px;flex-shrink:0}
.card h3{font-size:1.05rem;margin:0 0 2px}
.card p{font-size:.86rem;color:var(--muted);margin:0;line-height:1.4}
.intro{text-align:center;padding:56px 0 28px}
.intro h1{font-size:2rem;margin:0 0 10px}
.intro p{color:var(--muted);margin:0 auto;max-width:560px}
.about{color:var(--muted)}
footer{padding-top:48px;padding-bottom:48px;color:var(--muted);font-size:.85rem;text-align:center}
footer a{color:var(--muted)}
@media (max-width:520px){.hero{flex-direction:column;align-items:flex-start}.hero h1{font-size:1.8rem}.shots img{height:360px}.cta.alt{margin:10px 0 0}}
"""

APPLE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.37 12.62c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.78-3.32-1.8-1.41-.14-2.76.83-3.48.83-.72 0-1.82-.81-3-.79-1.54.02-2.96.9-3.76 2.27-1.6 2.78-.41 6.9 1.15 9.16.76 1.1 1.67 2.34 2.86 2.3 1.15-.05 1.58-.74 2.97-.74 1.38 0 1.78.74 2.99.72 1.24-.02 2.02-1.12 2.77-2.23.87-1.28 1.23-2.52 1.25-2.58-.03-.01-2.4-.92-2.42-3.66zM14.1 5.88c.63-.77 1.06-1.83.94-2.9-.91.04-2.02.61-2.67 1.37-.58.67-1.1 1.76-.96 2.8 1.02.08 2.06-.52 2.69-1.27z"/></svg>'


def head(title, desc, path, og_image, extra=""):
    url = SITE + path
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="{AUTHOR}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#f6f7f9" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121417" media="(prefers-color-scheme: dark)">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{AUTHOR} — Applications">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/{og_image}">
{extra}<style>{CSS}</style>
</head>
"""


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>\n"


PERSON = {"@type": "Person", "@id": SITE + "/#florian", "name": AUTHOR, "url": SITE + "/",
          "jobTitle": "Développeur indépendant d'applications mobiles",
          "sameAs": ["https://apps.apple.com/fr/developer/florian-marcel/id6790743819", "https://github.com/Lecram42"]}


def card(a, prefix=""):
    return (f'<li><a class="card" href="{prefix}{a["slug"]}/">'
            f'<img src="{prefix}images/{a["slug"]}-160.webp" alt="Icône de {e(a["name"])}" width="56" height="56" loading="lazy" decoding="async">'
            f'<div><h3>{e(a["name"])}</h3><p>{e(a["card"])}</p></div></a></li>')


FOOTER = f"""<footer class="wrap"><p>© {datetime.date.today().year} {AUTHOR} · Applications conçues et développées en France<br>
<a href="/">Toutes les applications</a> · <a href="https://apps.apple.com/fr/developer/florian-marcel/id6790743819">Page développeur App Store</a></p></footer>
"""


def app_page(a):
    meta = ASSETS[a["slug"]]
    accent = meta["accent"]
    on = "#111" if lum(accent) > 0.55 else "#fff"
    path = f"/{a['slug']}/"
    shots = meta["shots"]
    shape = "land" if shots[0]["w"] > shots[0]["h"] else ("square" if shots[0]["w"] == shots[0]["h"] else "")
    app_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "MobileApplication", "name": a["name"], "alternateName": f"{a['name']} — {a['subtitle']}",
             "description": a["description"], "url": SITE + path, "installUrl": store_url(a),
             "operatingSystem": "iOS" + (", Android" if a.get("play") else ""),
             "applicationCategory": a["category"], "image": f"{SITE}/images/{a['slug']}-512.png",
             "screenshot": [SITE + "/" + s["src"] for s in shots],
             "inLanguage": "fr", "author": {"@id": PERSON["@id"]},
             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in a["faq"]]},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Applications", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": a["name"], "item": SITE + path}]},
            PERSON,
        ],
    }
    extra = (f'<meta name="keywords" content="{e(a["keywords"])}">\n'
             f'<meta name="apple-itunes-app" content="app-id={a["id"]}">\n' + ld(app_ld))
    others = "".join(card(o, "../") for o in APPS if o is not a)
    play = (f'<a class="cta alt" href="https://play.google.com/store/apps/details?id={a["play"]}&amp;hl=fr">Google Play</a>'
            if a.get("play") else "")
    legal = (f'<p class="about">Liens utiles : <a href="/{a["legal"]}/support.html">Support</a> · '
             f'<a href="/{a["legal"]}/privacy-policy.html">Politique de confidentialité</a></p>') if a.get("legal") else ""
    return head(a["title"], a["description"], path, f"images/og/{a['slug']}.png", extra) + f"""<body style="--app:{accent};--on-app:{on}">
<nav class="wrap top" aria-label="Fil d'Ariane"><a href="/">← Toutes les applications de {AUTHOR}</a></nav>
<main class="wrap">
<header class="hero">
<img src="../images/{a['slug']}-512.png" alt="Icône de l'application {e(a['name'])}" width="112" height="112">
<div><h1>{e(a['name'])}</h1><p class="sub">{e(a['subtitle'])}</p></div>
</header>
<p class="lead">{e(a['lead'])}</p>
<ul class="meta"><li>Gratuit</li><li>{OS_LABEL.get(a['slug'], 'iPhone')}</li><li>{e(a['store_cat'])}</li><li>Sans compte</li></ul>
<a class="cta" href="{store_url(a)}">{APPLE_SVG}Télécharger sur l'App Store</a>{play}
<div class="shots {shape}">{''.join(f'<img src="../{s["src"]}" alt="Capture d’écran {i} de {e(a["name"])}" width="{s["w"]}" height="{s["h"]}" loading="lazy" decoding="async">' for i, s in enumerate(shots, 1))}</div>
<h2>Qu'est-ce que {e(a['name'])} ?</h2>
{''.join(f'<p>{e(p)}</p>' for p in a['about'])}
<h2>Fonctionnalités</h2>
<ul class="feat">{''.join(f'<li>{e(f)}</li>' for f in a['features'])}</ul>
<p><a class="cta" href="{store_url(a)}">{APPLE_SVG}Obtenir {e(a['name'])} gratuitement</a></p>
<h2>Questions fréquentes</h2>
{''.join(f'<details><summary>{e(q)}</summary><p>{e(r)}</p></details>' for q, r in a['faq'])}
{legal}
<h2>Autres applications</h2>
<ul class="grid">{others}</ul>
</main>
{FOOTER}</body>
</html>
"""


def index_page():
    title = f"{AUTHOR} — Applications iPhone gratuites : jeux, jouets et outils"
    desc = ("Applications iPhone gratuites créées par Florian Marcel, développeur indépendant : bougies d'anniversaire à souffler, "
            "boîte à meuh, compteur de cornhole, météo pour choisir la date d'un mariage, jeux de moto et de bateau.")
    data = {"@context": "https://schema.org", "@graph": [
        dict(PERSON, description=desc),
        {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": f"{AUTHOR} — Applications", "inLanguage": "fr",
         "publisher": {"@id": PERSON["@id"]}},
        {"@type": "ItemList", "name": "Applications de Florian Marcel", "itemListElement": [
            {"@type": "ListItem", "position": i, "url": f"{SITE}/{a['slug']}/", "name": a["name"]} for i, a in enumerate(APPS, 1)]},
    ]}
    return head(title, desc, "/", "images/og/site.png", ld(data)) + f"""<body>
<main class="wrap">
<header class="intro">
<h1>{AUTHOR}</h1>
<p>Développeur indépendant, je crée des applications iPhone simples et gratuites : petits jeux, jouets qui réagissent au souffle ou au mouvement, et outils pratiques. Sans compte, sans collecte de données.</p>
</header>
<ul class="grid">{''.join(card(a) for a in APPS)}</ul>
<section class="about">
<h2>Des apps qui jouent avec ton téléphone</h2>
<p>Chaque application exploite un capteur de l'iPhone d'une façon inattendue : le micro pour éteindre des <a href="souffly/">bougies d'anniversaire virtuelles</a>, l'accéléromètre pour faire meugler une <a href="meuhbox/">boîte à meuh</a> ou tanguer un <a href="tiltboat/">petit bateau</a>. À côté des jouets, des outils du quotidien : <a href="cornall/">compter les points au cornhole</a>, <a href="bonnedatemeteo/">choisir la date d'un mariage selon la météo historique</a> ou tenir un <a href="countit/">carnet intime chiffré</a>.</p>
<p>Toutes les apps sont gratuites, fonctionnent sans inscription et gardent tes données sur ton téléphone.</p>
</section>
</main>
{FOOTER}</body>
</html>
"""


def not_found():
    return head("Page introuvable — Florian Marcel", "Cette page n'existe pas.", "/404.html", "images/og/site.png",
                '<meta name="robots" content="noindex">\n') + f"""<body><main class="wrap"><header class="intro"><h1>Page introuvable</h1>
<p>Cette page n'existe pas (ou plus). Voici les applications disponibles :</p></header>
<ul class="grid">{''.join(card(a, "/") for a in APPS)}</ul></main>{FOOTER}</body></html>
"""


def sitemap():
    urls = [("/", "1.0")] + [(f"/{a['slug']}/", "0.8") for a in APPS]
    body = "".join(f"<url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>\n" for u, p in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'


def write(rel, text):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


write("index.html", index_page())
for a in APPS:
    write(f"{a['slug']}/index.html", app_page(a))
write("404.html", not_found())
write("sitemap.xml", sitemap())
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("ok:", len(APPS), "apps")
