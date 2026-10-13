#!/usr/bin/env python3
"""Собирает страницы сайта в site/ по шаблону из Claude Design.

Данные заказчика (услуги, цены, команда, вопросы, документы) лежат в
customer-content.json; тексты, которые связывают их в страницы, — здесь.
Запуск: python3 build/build.py
"""
import json
import pathlib
from html import escape

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DATA = json.loads((ROOT / "build" / "customer-content.json").read_text(encoding="utf-8"))

PHONE_1, PHONE_1_TEL = "8 (495) 198-05-17", "+74951980517"
PHONE_2, PHONE_2_TEL = "8 (958) 558-02-33", "+79585580233"
ADDRESS = "Москва, ул.\u00a0Адмирала Лазарева, д.\u00a052к3"
ADDRESS_FULL = "117041, г.\u00a0Москва, ул.\u00a0Адмирала Лазарева, д.\u00a052к3"
HOURS = "Пн–Сб · 9:00–20:00"
TELEGRAM, TELEGRAM_NAME = "https://t.me/rezultat02", "@rezultat02"
VK = "https://vk.com/rezultat_logoped"
YOUTUBE = "https://youtube.com/@ns_tumanova"
MAP_LINK = "https://yandex.ru/maps/?text=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%90%D0%B4%D0%BC%D0%B8%D1%80%D0%B0%D0%BB%D0%B0%20%D0%9B%D0%B0%D0%B7%D0%B0%D1%80%D0%B5%D0%B2%D0%B0%2C%2052%D0%BA3"
MAP_WIDGET = "https://yandex.ru/map-widget/v1/?ll=37.515927%2C55.544394&z=16&pt=37.515927%2C55.544394%2Cpm2rdm"
LICENSE = "№ Л035-01298-77/00643373 от 13.03.2023 г."
LICENSE_BY = "Выдана бессрочно Департаментом образования и науки г. Москвы."
INN, OGRN = "774300416875", "318774600530861"
VIDEOS = ["CceLc5ONOPU", "cF_ZE5bkTUo", "f0HQLnpyubc"]

ICON = {
    "phone": '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/>',
    "send": '<path d="M21.4 3.6 2.9 10.8c-1 .4-1 1.8.1 2.1l4.7 1.5 1.8 5.6c.3.9 1.4 1.1 2 .5l2.6-2.5 4.9 3.6c.7.5 1.7.1 1.9-.8L23 4.9c.2-1-.7-1.7-1.6-1.3zM9.6 14.6l8.7-6.9-7.2 8 -.3 3.1z"/>',
    "pin": '<path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/>',
    "clock": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.6 3.5 2.1-.8 1.3L11 13.2V7h2z"/>',
    "home": '<path d="M12 3 2 11h3v9h5v-6h4v6h5v-9h3z"/>',
}


def icon(name):
    return f'<span class="contact-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor">{ICON[name]}</svg></span>'

LOGO_PATHS = (
    '<line x1="10" y1="50" x2="30" y2="43" stroke="{a}" stroke-width="5" stroke-linecap="round"/>'
    '<line x1="30" y1="43" x2="53" y2="29" stroke="{b}" stroke-width="5.5" stroke-linecap="round"/>'
    '<circle cx="10" cy="50" r="5.5" fill="none" stroke="{c}" stroke-width="4.5"/>'
    '<circle cx="30" cy="43" r="7" fill="none" stroke="{d}" stroke-width="5.5"/>'
    '<circle cx="53" cy="29" r="9" fill="none" stroke="{e}" stroke-width="6.5"/>'
    '<line x1="53" y1="20" x2="53" y2="6" stroke="{e}" stroke-width="4" stroke-linecap="round"/>'
    '<path d="M53 4 L71 7.5 L64.5 10.5 L71 14 L53 14 Z" fill="#F5B52C"/>'
)
LOGO_LIGHT = LOGO_PATHS.format(a="#6DAF47", b="#2E8B8B", c="#86C24A", d="#5FA33F", e="#2E7C86")
LOGO_DARK = LOGO_PATHS.format(a="#7FC241", b="#3BB0AB", c="#7FC241", d="#A9D96B", e="#3BB0AB")
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230E6D70'/%3E"
           "%3Cpath d='M12 46L28 39L45 27' stroke='%23BCE27C' stroke-width='5' fill='none' stroke-linecap='round'/%3E"
           "%3Ccircle cx='12' cy='46' r='5' fill='none' stroke='%23BCE27C' stroke-width='4'/%3E%3Ccircle cx='28' cy='39' r='6' fill='none' stroke='%23BCE27C' stroke-width='4.5'/%3E"
           "%3Ccircle cx='45' cy='27' r='7.5' fill='none' stroke='%23fff' stroke-width='5'/%3E%3Cpath d='M45 19V8' stroke='%23fff' stroke-width='3.5'/%3E%3Cpath d='M45 6L58 9L53 11L58 14H45Z' fill='%23F5B52C'/%3E%3C/svg%3E")

E = escape


def ext(href, text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{href}" target="_blank" rel="noopener noreferrer">{text}</a>'


# ---------------------------------------------------------------- данные услуг
SVC = {s["id"]: s for s in DATA["services"]}
ADD = {a["id"]: a for a in DATA["additional"]}
PG = {g["id"]: g for g in DATA["priceGroups"]}


def prices(group, *idx):
    return [(group, PG[group]["items"][i]) for i in idx]


SERVICES = [
    dict(slug="logoped", src="speech", abbr="Л", prices=prices("price-speech", 0, 2, 3, 6), price_link="price-speech"),
    dict(slug="neiropsiholog", src="neuro", abbr="НП", prices=prices("price-psych", 2, 4) + prices("price-tumanova", 2), price_link="price-psych"),
    dict(slug="defektolog", src="defectologist", abbr="ДФ", prices=prices("price-speech", 0), price_link="price-speech",
         price_extra="Стоимость регулярных занятий уточняйте при записи."),
    dict(slug="afk", src="afk", abbr="АФК", prices=[], price_link=None,
         price_extra="Стоимость занятий АФК, сенсорной интеграции и мозжечковой стимуляции уточняйте при записи."),
    dict(slug="miologoped", src="mio", abbr="МЛ", prices=prices("price-speech", 7) + prices("price-tumanova", 5, 6), price_link="price-speech"),
    dict(slug="pedagog-ovz", src="special-teacher", abbr="ПД", prices=[], price_link=None,
         price_extra="Стоимость занятий уточняйте при записи."),
    dict(slug="psiholog", src="psychologist", abbr="ПС", prices=prices("price-psych", 0, 1, 5, 6), price_link="price-psych"),
    dict(slug="neiroprofil", src="profile", abbr="НФ", prices=prices("price-tumanova", 0), price_link="price-tumanova"),
    dict(slug="teipirovanie", src="taping", abbr="Т", prices=prices("price-speech", 4), price_link="price-speech",
         price_extra="Отдельная стоимость тейпирования не указана — уточняйте при записи."),
    dict(slug="dens", src="dens", abbr="ДЭ", prices=prices("price-speech", 4), price_link="price-speech",
         price_extra="Отдельная стоимость ДЭНС не указана — уточняйте при записи."),
    dict(slug="apparatnye", src="equipment", abbr="БОС", prices=prices("price-bos", 6, 0, 2), price_link="price-bos",
         price_extra="Все цены — за полный курс. Перед курсом нужна предварительная консультация, она проводится отдельно."),
]
for s in SERVICES:
    if s["src"] in SVC:
        c = SVC[s["src"]]
        s.update(title=c["title"], short=c["short"], paras=c["paras"], bullets=c["bullets"], cta=c["cta"].replace("↗", "").strip())
    elif s["src"] in ADD:
        a = ADD[s["src"]]
        s.update(title=a["title"], paras=a["intro"], sections=a["sections"], bullets=[])
    s["url"] = f"uslugi/{s['slug']}.html"

S = {s["slug"]: s for s in SERVICES}
S["teipirovanie"].update(short="Эластичные тейпы как дополнительный инструмент логопедической и миофункциональной работы", cta="Обсудить тейпирование")
S["dens"].update(short="Динамическая электронейростимуляция — по индивидуальным показаниям", cta="Обсудить ДЭНС")
S["apparatnye"].update(
    title="БОС и аппаратные методы", short="БОС-тренировки, стабилотренажёр, ритмограф и другие технологии в помощь специалисту",
    paras=["Аппаратные занятия подбираются индивидуально. Перед началом важно обсудить цель, ограничения и способ оценки результата."],
    bullets=[], cta="Обсудить аппаратные программы", tech=DATA["tech"])

NOTE_EXTRA = ("<strong>Единая цель — индивидуальное сочетание методов.</strong> Не каждому ребёнку нужны тейпирование или ДЭНС. "
              "Сначала определяем задачи, затем согласуем подходящие методы, нагрузку и критерии оценки динамики.")
NOTE_TECH = ("Оборудование — часть программы, а не обещание результата само по себе. Выбор метода зависит от запроса, особенностей ребёнка "
             "и ограничений. Занятия в центре не заменяют необходимую медицинскую помощь.")
SOURCES = {
    "teipirovanie": "О методе: " + ext("https://www.royalberkshire.nhs.uk/media/ao0ealui/kinesiology-tape-for-hand-therapy_mar26.pdf", "информация NHS о тейпировании") + ".",
    "dens": "О методе: " + ext("https://denas.faberlic.com/uploads/filemanager/manuals/maual_denas_complex.pdf", "инструкция производителя ДЭНАС") + ".",
    "apparatnye": "О понятии биологической обратной связи: " + ext("https://www.nccih.nih.gov/health/providers/terms-related-to-complementary-and-integrative-health", "NCCIH")
                  + ". О нейрообратной связи: " + ext("https://www.cancer.gov/publications/dictionaries/cancer-terms/def/neurofeedback", "NCI") + ".",
}
HOME_SERVICES = ["logoped", "neiropsiholog", "defektolog", "afk", "miologoped", "psiholog"]
NEED_LINKS = {"speech": "logoped", "neuro": "neiropsiholog", "afk": "afk"}

# ---------------------------------------------------------------- команда
TEAM_EXTRA = {
    "Сысоев Георгий Юрьевич": ["АФК", "Адаптация детей с РАС", "Проект AUTMIND"],
    "Реутова Аяна Юрьевна": ["Нейрологопедия", "Миологопедия"],
    "Долгова Юлия Николаевна": ["Психология", "Нейропсихология"],
    "Еремкина Елена Сергеевна": ["Логопедия", "Дефектология", "Миологопедия"],
    "Чаусов Владислав Андреевич": ["АФК", "Сенсорная интеграция", "Мозжечковая стимуляция"],
    "Юхано Елена Игоревна": ["Логопедия", "Дефектология"],
    "Каверзнева Елена Сергеевна": ["Работа с детьми с ОВЗ", "Нейроподход"],
}
TEAM_DOCS = {"Еремкина Елена Сергеевна": "eremkina-docs", "Каверзнева Елена Сергеевна": "kaverzneva-docs"}
TEAM_PHOTO_SIZE = {"nina-tumanova": (1000, 1202), "ayana-reutova": (720, 900), "yulia-dolgova": (720, 900), "elena-eremkina": (720, 865)}

# ---------------------------------------------------------------- общие части


def head(title, desc, rel):
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#0B2F4A">
<meta property="og:type" content="website">
<meta property="og:locale" content="ru_RU">
<meta property="og:site_name" content="Вершина результата">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="{rel}assets/fonts/montserrat-cyrillic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{rel}assets/fonts/pt-sans-400-cyrillic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{rel}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Перейти к содержанию</a>
"""


NAV = [("o-centre.html", "О центре"), ("uslugi.html", "Услуги"), ("specialisty.html", "Специалисты"), ("ceny.html", "Цены"),
       ("otzyvy.html", "Отзывы"), ("diplomy-i-razvitie.html", "Дипломы"), ("kontakty.html", "Контакты")]


def header(rel, active):
    def cur(href):
        return ' aria-current="page"' if href == active else ""
    items = []
    for href, label in NAV:
        if href == "uslugi.html":
            menu = "".join(f'<a href="{rel}{s["url"]}">{E(s["title"])}</a>' for s in SERVICES)
            items.append(f'<div class="nav-drop"><a href="{rel}{href}"{cur(href)}>{label} <span class="nav-caret" aria-hidden="true">▼</span></a>'
                         f'<div class="nav-menu"><div class="nav-menu-panel">{menu}</div></div></div>')
        else:
            items.append(f'<a href="{rel}{href}"{cur(href)}>{label}</a>')
    return f"""<div class="topbar"><div class="wrap">
<span class="topbar-dot topbar-addr">{ADDRESS}</span>
<a class="topbar-phone" href="tel:{PHONE_1_TEL}">{PHONE_1}</a>
<a href="tel:{PHONE_2_TEL}">{PHONE_2}</a>
<span class="topbar-hours">{HOURS.replace(' · ', ' ')}</span>
<div class="topbar-social">{ext(TELEGRAM, 'Telegram')}{ext(VK, 'VK')}{ext(YOUTUBE, 'YouTube')}</div>
</div></div>
<header class="site-header"><div class="wrap">
<a class="brand" href="{rel}index.html" aria-label="Вершина результата — на главную">
<svg viewBox="0 0 74 58" fill="none" aria-hidden="true">{LOGO_LIGHT}</svg>
<span><span class="brand-name">ВЕРШИНА<br>РЕЗУЛЬТАТА</span><span class="brand-sub">Центр нейрокоррекции и развития детей</span></span>
</a>
<nav class="nav" aria-label="Основное меню">{''.join(items)}</nav>
<a class="btn btn-yellow btn-sm header-cta" href="{rel}kontakty.html">Записаться</a>
</div></header>
<main id="main">
"""


def footer(rel):
    return f"""</main>
<footer class="site-footer">
<div class="wrap footer-grid">
<div>
<div class="footer-brand"><svg viewBox="0 0 74 58" fill="none" aria-hidden="true">{LOGO_DARK}</svg><span>ВЕРШИНА<br>РЕЗУЛЬТАТА</span></div>
<p class="footer-about">Центр нейрокоррекции и развития детей. От диагностики — к результату.</p>
<div class="footer-social">{ext(TELEGRAM, 'TG')}{ext(VK, 'VK')}{ext(YOUTUBE, 'YT')}</div>
</div>
<div>
<div class="footer-title">Разделы</div>
<a class="f-link" href="{rel}index.html">Главная</a>
<a class="f-link" href="{rel}o-centre.html">О центре</a>
<a class="f-link" href="{rel}uslugi.html">Услуги</a>
<a class="f-link" href="{rel}specialisty.html">Специалисты</a>
<a class="f-link" href="{rel}diplomy-i-razvitie.html">Дипломы и развитие</a>
</div>
<div>
<div class="footer-title">Клиентам</div>
<a class="f-link" href="{rel}ceny.html">Цены</a>
<a class="f-link" href="{rel}otzyvy.html">Отзывы</a>
<a class="f-link" href="{rel}index.html#faq">Вопросы родителей</a>
<a class="f-link" href="{rel}kontakty.html">Контакты</a>
</div>
<div>
<div class="footer-title">Контакты</div>
<a class="f-link footer-strong" href="tel:{PHONE_1_TEL}">{PHONE_1}</a>
<a class="f-link" href="tel:{PHONE_2_TEL}">{PHONE_2}</a>
<p>{ADDRESS}</p>
<p>{HOURS}</p>
</div>
</div>
<div class="footer-bottom"><div class="wrap">
<span>© 2026 Центр нейрокоррекции и развития детей «Вершина результата»</span>
<span>Образовательная лицензия {LICENSE.split(' от ')[0]} · ИНН {INN} · ОГРН {OGRN}</span>
</div></div>
</footer>
</body>
</html>
"""


def page_head(crumb, title, sub=None, script=None, rel=""):
    s = f'<p class="script">{E(script)}</p>' if script else ""
    p = f"<p>{E(sub)}</p>" if sub else ""
    return (f'<section class="page-head"><div class="wrap"><div class="crumbs"><a href="{rel}index.html">Главная</a> / {E(crumb)}</div>'
            f"<h1>{E(title)}</h1>{s}{p}</div></section>")


def license_strip():
    return (f'<aside class="license" aria-label="Образовательная лицензия">'
            f'<span class="license-head"><span class="license-check" aria-hidden="true">✓</span>Центр имеет образовательную лицензию</span>'
            f'<span><strong>Лицензия {LICENSE}</strong> · бессрочно</span></aside>')


def license_card():
    return (f'<div class="license-card"><div class="license-head"><span class="license-check" aria-hidden="true">✓</span>Центр имеет образовательную лицензию</div>'
            f'<p><strong>Государственная лицензия {LICENSE}</strong><br>{LICENSE_BY}</p>'
            f'<p><strong>{ADDRESS_FULL}</strong><br>ИНН {INN} · ОГРН {OGRN}</p></div>')


def svc_card(s, rel):
    return (f'<a class="card svc-card" href="{rel}{s["url"]}"><div class="svc-abbr">{s["abbr"]}</div>'
            f'<h3>{E(s["title"])}</h3><p>{E(s["short"])}</p><span class="more">Подробнее →</span></a>')


def video_cards():
    return "".join(
        f'<a class="video-card" href="https://www.youtube.com/watch?v={v}" target="_blank" rel="noopener noreferrer">'
        f'<span class="video-play" aria-hidden="true">▶</span><span><b>Видеоотзыв родителей {i}</b><br><span>Смотреть на YouTube ↗</span></span></a>'
        for i, v in enumerate(VIDEOS, 1))


def founder_creds():
    return ('<div class="cred-group"><h3>Образование</h3><p>Медицинское образование. Завершила обучение в институте Сеченова по направлению '
            '«Биохакинг для оздоровления современного поколения».</p></div>'
            '<div class="cred-group"><h3>Специализации</h3><p class="strong">Логопед-дефектолог высшей категории</p>'
            '<p>Специальный психолог, нейропсихолог, миологопед, специалист по нейробиоуправлению.</p></div>')


EXPERTISE = "Психология • Нейропсихология • Миология речи • Нейробиоуправление • Медицинская база"


def faq_block():
    return "".join(f"<details><summary>{E(f['q'])}</summary><p>{E(f['a'])}</p></details>" for f in DATA["faq"])


def cta_band(rel):
    return (f'<section class="cta"><div class="wrap"><h2>Начните путь к результату</h2>'
            f'<p>Назовите возраст ребёнка и коротко опишите, что вас беспокоит. Обсудим подходящего специалиста, стоимость и доступное время.</p>'
            f'<div class="cta-actions"><a class="btn btn-navy" href="{rel}kontakty.html">Записаться на консультацию</a></div></div></section>')


def write(path, html):
    out = SITE / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("  ", path)


# ---------------------------------------------------------------- страницы

def page_index():
    rel = ""
    needs = "".join(
        f'<a class="card-soft need-card" href="{S[NEED_LINKS[n["href"]]]["url"]}"><div class="mark">{n["num"][:2]}</div>'
        f'<span class="tech-tag" style="margin-top:16px">{E(n["num"].split("/", 1)[1].strip())}</span>'
        f'<h3 style="margin-top:6px">{E(n["title"])}</h3><p>{E(n["text"])}</p><span class="more">{E(n["link"].replace("↗", "→"))}</span></a>'
        for n in DATA["needs"])
    steps = "".join(
        f'<div class="step-card"><div class="step-num">{i}</div><div><span class="tech-tag">{E(st["label"].split("/", 1)[1].strip())}</span>'
        f'<h3 style="margin-top:4px">{E(st["title"])}</h3><p>{E(st["text"])}</p></div></div>'
        for i, st in enumerate(DATA["steps"], 1))
    route = "".join(
        f'<div class="route-row"><div class="route-num">0{i}</div><div><h3>{t}</h3><p>{p}</p></div></div>'
        for i, (t, p) in enumerate([
            ("Услышим ваш запрос", "Что беспокоит сейчас и что хотелось бы изменить в повседневной жизни."),
            ("Разберёмся в трудностях", "Подберём специалиста и подходящий формат первичной оценки."),
            ("Обсудим план занятий", "Понятные задачи, посильная нагрузка и ориентиры для оценки динамики.")], 1))
    body = f"""<section class="hero"><div class="wrap">
{license_strip()}
<div class="hero-grid" style="padding-top:36px">
<div class="hero-copy">
<span class="pill pill-white">У КАЖДОГО СВОЯ ВЕРШИНА</span>
<h1>Маленькие шаги.<br><span>Важные перемены.</span></h1>
<p class="script hero-script">От диагностики к результату</p>
<p class="hero-lead">Помогаем детям развивать речь, внимание, движение и навыки общения. А родителям — понять, с чего начать и как поддержать ребёнка.</p>
<div class="hero-actions"><a class="btn btn-yellow" href="kontakty.html">Подобрать первый шаг</a><a class="btn btn-outline" href="uslugi.html">Наши услуги</a></div>
<p class="hero-note">Не нужно заранее знать, какой специалист вам нужен.</p>
</div>
<div class="hero-aside"><div class="hero-bubble" aria-hidden="true"></div>
<div class="route-card"><span class="label">Как начать занятия</span><h2>Начнём с вашего ребёнка</h2>{route}
<p class="route-foot">В своём темпе. С вниманием к особенностям.</p></div></div>
</div></div>
<svg class="mountains" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true"><path d="M0 90 L360 30 L520 60 L760 12 L1000 55 L1230 22 L1440 60 L1440 90 Z" fill="#0E6D70" opacity="0.12"/><path d="M0 90 L300 55 L560 78 L820 40 L1080 72 L1300 48 L1440 78 L1440 90 Z" fill="#0E6D70" opacity="0.2"/></svg>
</section>

<section class="facts" aria-label="Коротко о центре"><div class="wrap">
<div><div class="fact-num">Лицензия</div><div class="fact-label">образовательная, бессрочно</div></div>
<div><div class="fact-num">8</div><div class="fact-label">специалистов в одной команде</div></div>
<div><div class="fact-num">Онлайн</div><div class="fact-label">занятия с логопедом</div></div>
<div><div class="fact-num">Пн–Сб</div><div class="fact-label">с 9:00 до 20:00</div></div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2 class="h2 title-up">Что сейчас важно для вашей семьи?</h2>
<p class="script" style="font-size:30px;color:var(--yellow);margin-top:6px">Поможем сориентироваться</p>
<p>Опишите ситуацию своими словами. Мы поможем сориентироваться в направлениях и выбрать, с кем обсудить ваш запрос.</p></div>
<div class="grid g3">{needs}</div>
<p class="center" style="font-size:19px;max-width:760px;margin:34px auto 0;color:var(--text)">Не уверены, какое направление выбрать? <a class="link-under" href="kontakty.html">Расскажите, что беспокоит →</a></p>
</div></section>

<section class="method"><div class="wrap section">
<div class="section-head"><span class="pill pill-teal">КАК УСТРОЕН ПУТЬ</span><h2 class="h2 title-up">От первого обращения к работе над навыками</h2>
<p>Вам важно понимать, что происходит на занятиях и зачем. Поэтому начинаем с обсуждения запроса и возвращаемся к нему при оценке динамики.</p></div>
<div class="grid g4">{steps}</div>
<p class="script method-script">Не просто список занятий — понятный план действий.</p>
</div></section>

<section class="section"><div class="wrap">
<div class="row-head"><div><h2 class="h2 title-up">Наши услуги</h2><p>От отдельных занятий до сочетания нескольких направлений.</p></div><a class="link-under" href="uslugi.html">Все услуги →</a></div>
<div class="grid g3">{''.join(svc_card(S[x], rel) for x in HOME_SERVICES)}</div>
</div></section>

<section class="dark"><div class="wrap founder-grid">
<div class="photo-frame founder-photo"><img src="team/nina-tumanova-styled.jpg" width="1000" height="1202" loading="lazy" alt="Туманова Нина Сергеевна — руководитель и основатель центра"></div>
<div>
<span class="label">Руководитель и основатель центра</span>
<h2 class="founder-name">Нина Сергеевна Туманова</h2>
<p class="founder-text">Логопед-дефектолог высшей категории, специальный психолог, нейропсихолог, миологопед, специалист по нейробиоуправлению. Медицинское образование.</p>
<div class="founder-facts">
<div class="founder-fact"><b>Высшая категория</b><span>логопед-дефектолог</span></div>
<div class="founder-fact"><b>«Голос-ОК»</b><span>автор и методолог приложения — помощника логопеда</span></div>
<div class="founder-fact"><b>Автор и наставник</b><span>собственные пособия и курсы для специалистов</span></div>
</div>
<p class="founder-quote">{EXPERTISE}</p>
<a class="btn btn-yellow" style="margin-top:22px" href="o-centre.html#rukovoditel">О руководителе и центре</a>
</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head" style="margin-bottom:38px"><h2 class="h2 title-up">Родители говорят о нас</h2><p class="script" style="font-size:28px;color:var(--teal-2);margin-top:4px">Видеоотзывы на канале Нины Тумановой</p></div>
<div class="grid g3">{video_cards()}</div>
<p class="center" style="margin-top:30px"><a class="link-under" href="otzyvy.html">Все отзывы →</a></p>
</div></section>

<section class="method" id="faq"><div class="wrap section">
<div class="section-head"><span class="pill pill-teal">ВОПРОСЫ РОДИТЕЛЕЙ</span><h2 class="h2 title-up">Перед первой встречей</h2></div>
<div class="faq">{faq_block()}</div>
</div></section>

{cta_band(rel)}
"""
    write("index.html", head("Вершина результата — центр нейрокоррекции и развития детей в Москве",
                             "Логопед, нейропсихолог, дефектолог, АФК и поддержка детей с особенностями развития. Поможем выбрать первый шаг. Москва, ул. Адмирала Лазарева, 52к3.",
                             rel) + header(rel, "index.html") + body + footer(rel))


def page_services():
    rel = ""
    body = (page_head("Услуги", "Услуги центра", "От отдельных занятий до сочетания нескольких направлений. Откройте услугу, чтобы узнать, над чем работает специалист и сколько это стоит.")
            + f'<div class="wrap page-body"><div class="grid g3">{"".join(svc_card(s, rel) for s in SERVICES)}</div>'
            + '<div class="dark-box"><h2>Не уверены, какое направление выбрать?</h2><p>Расскажите, что беспокоит, — поможем сориентироваться и выбрать, с кем обсудить ваш запрос.</p>'
            + '<a class="btn btn-yellow" href="kontakty.html">Подобрать первый шаг</a></div></div>')
    write("uslugi.html", head("Услуги — Вершина результата", "Логопед, нейропсихолог, дефектолог, АФК, миологопед, психолог, нейропрофиль, тейпирование, ДЭНС и аппаратные методы.", rel)
          + header(rel, "uslugi.html") + body + footer(rel))


def page_service(s):
    rel = "../"
    bullets = "".join(f'<div class="check">{E(b)}</div>' for b in s.get("bullets", []))
    main = "".join(f"<p>{E(p)}</p>" for p in s["paras"])
    if bullets:
        main += f'<h3>Над чем работаем</h3><div class="checks">{bullets}</div>'
    for sec in s.get("sections", []):
        main += f'<h3>{E(sec["h"])}</h3>' + "".join(f"<p>{E(p)}</p>" for p in sec["ps"])
    if s.get("tech"):
        main += '<h3>Технологии</h3><div class="grid g2">' + "".join(
            f'<div class="card-soft"><span class="tech-tag">{E(t["tag"])}</span><h3 style="text-transform:none;color:var(--navy);margin-top:10px">{E(t["title"])}</h3><p>{E(t["text"])}</p></div>'
            for t in s["tech"]) + "</div>"
        main += f'<div class="note-box">{NOTE_TECH}</div>'
    if s["slug"] in ("teipirovanie", "dens"):
        main += f'<div class="note-box">{NOTE_EXTRA}</div>'
    if s["slug"] in SOURCES:
        main += f'<p class="source">{SOURCES[s["slug"]]}</p>'
    rows = "".join(
        f'<div class="aside-row"><span>{E(it["name"])}</span><b>{E(it["price"])}</b><small>{E(it["unit"])} · {E(it["meta"].split(" · ")[0])}</small></div>'
        for _, it in s["prices"])
    extra = f'<p class="aside-empty">{E(s["price_extra"])}</p>' if s.get("price_extra") else ""
    all_prices = f'<a class="aside-link" href="{rel}ceny.html#{s["price_link"]}">Все цены направления →</a>' if s.get("price_link") else f'<a class="aside-link" href="{rel}ceny.html">Все цены →</a>'
    body = f"""<section class="page-head-dark"><div class="wrap wrap-1100"><div class="crumbs"><a href="{rel}index.html">Главная</a> / <a href="{rel}uslugi.html">Услуги</a></div>
<div class="svc-hero"><div class="svc-abbr">{s['abbr']}</div><div><h1>{E(s['title'])}</h1><p>{E(s['short'])}</p></div></div></div></section>
<div class="wrap wrap-1100 page-body"><div class="detail-grid">
<div class="prose">{main}</div>
<aside class="price-aside"><div class="label">Стоимость</div>{rows}{extra}
<a class="btn btn-yellow" href="{rel}kontakty.html">{E(s['cta'])}</a>{all_prices}
<div class="aside-call">Есть вопросы? Позвоните:<br><a href="tel:{PHONE_1_TEL}">{PHONE_1}</a></div></aside>
</div></div>
"""
    write(s["url"], head(f"{s['title']} — Вершина результата", s["short"], rel) + header(rel, "uslugi.html") + body + footer(rel))


def page_about():
    rel = ""
    values = [
        ("Несколько направлений в одном центре", "Речь, обучение, движение и общение — от отдельных занятий до сочетания нескольких направлений."),
        ("Поддержка детей с особенностями развития", "Понятные задачи, посильная нагрузка и ориентиры для оценки динамики. В своём темпе, с вниманием к особенностям."),
        ("Родители — участники процесса", "Обсуждаем наблюдения и динамику, согласуем рекомендации для дома и при необходимости корректируем программу вместе с родителями."),
        ("Комплексно, но без лишнего", "Комплексный подход — это нужное ребёнку сочетание направлений, а не обязательное посещение всех специалистов."),
    ]
    vals = "".join(f'<div class="value-card"><h3>{E(t)}</h3><p>{E(p)}</p></div>' for t, p in values)
    assess = ["Какие навыки требуют внимания сейчас", "На какие сильные стороны можно опереться", "С какого специалиста и направления начать", "По каким изменениям отслеживать динамику"]
    asteps = "".join(f'<div class="step-card"><div class="step-num">{i}</div><div><h3 class="plain">{E(a)}</h3></div></div>' for i, a in enumerate(assess, 1))
    work = [
        ("Автор пособий, курсов и наставник", ["Автор собственных пособий и курсов для специалистов. Наставник."]),
        ("Социальное предпринимательство", ["Участник и партнёр форумов по социальному предпринимательству."]),
        ("Профессиональные конференции", ["Участник всероссийских и международных конференций, посвящённых проблемам развития детей."]),
        ("Приложение «Голос-ОК»", ["Автор и методолог первого в России приложения — помощника логопеда «Голос-ОК».",
                                   "«Голос-ОК» — разработка для распознавания детской речи с помощью искусственного интеллекта. Она распознаёт нарушенную речь и предлагает упражнения в процессе коррекции, помогая закреплять отрабатываемые навыки в самостоятельной речи."]),
    ]
    works = "".join(f'<div><h3>{E(t)}</h3>' + "".join(f"<p>{E(p)}</p>" for p in ps) + "</div>" for t, ps in work)
    docs = DATA["docGroups"][0]["cards"]
    thumbs = "".join(f'<a class="doc-thumb" href="diplomy-i-razvitie.html#tumanova-docs" aria-label="{E(c["title"])}"><img src="{c["img"]}" loading="lazy" alt="{E(c["alt"])}"></a>'
                     for c in (docs[0], docs[2], docs[9], docs[14]))
    body = page_head("О центре", "О центре", script="У каждого своя вершина") + f"""
<section class="wrap wrap-1000 page-body">
<p style="font-size:18px;line-height:1.7">«Вершина результата» — центр нейрокоррекции и развития детей в Москве. Помогаем детям развивать речь, внимание, движение и навыки общения. А родителям — понять, с чего начать и как поддержать ребёнка.</p>
<p style="font-size:18px;line-height:1.7;margin-top:14px">В центре работают логопеды, нейропсихологи, психологи, миологопеды и специалисты по АФК. Если ребёнку нужна помощь нескольких специалистов, команда объединяет их работу вокруг приоритетных задач.</p>
<div class="grid g2" style="gap:16px;margin-top:30px">{vals}</div>
</section>

<section class="method"><div class="wrap section">
<div class="section-head"><span class="pill pill-teal">СНАЧАЛА — ПОНЯТЬ РЕБЁНКА</span><h2 class="h2 title-up">Не просто список занятий. Понятный план действий.</h2>
<p>Важны и трудности, и то, что уже получается. На первой встрече обсудим ваш запрос, а по итогам оценки — задачи дальнейшей работы.</p></div>
<div class="grid g4">{asteps}</div>
<p class="center lead-muted" style="margin-top:26px">Объём обследования и стоимость согласуем до записи. Не все направления нужны каждому ребёнку.</p>
</div></section>

<section class="dark" id="rukovoditel"><div class="wrap founder-grid" style="align-items:start">
<div class="photo-frame founder-photo" style="height:520px"><img src="team/nina-tumanova-styled.jpg" width="1000" height="1202" loading="lazy" alt="Туманова Нина Сергеевна — руководитель и основатель центра"></div>
<div>
<span class="label">Руководитель и основатель центра</span>
<h2 class="founder-name">Туманова Нина Сергеевна</h2>
<p class="founder-quote" style="margin:6px 0 24px">{EXPERTISE}</p>
{founder_creds()}
<div class="chips" style="margin-top:24px"><span class="chip-dark">Логопед-дефектолог высшей категории</span><span class="chip-dark">Нейропсихолог</span><span class="chip-dark">Автор «Голос-ОК»</span></div>
<a class="btn btn-yellow" style="margin-top:26px" href="kontakty.html">Записаться к Нине Сергеевне</a>
</div>
</div>
<div class="wrap founder-work">{works}</div>
</section>

<section class="wrap wrap-1100 section">
<div class="section-head" style="margin-bottom:30px"><h2 class="h2 title-up">Лицензия и документы</h2><p>Документы об обучении специалистов собраны на отдельной странице: можно открыть и скачать оригиналы.</p></div>
{license_card()}
<div class="grid g4" style="gap:14px;margin-top:24px">{thumbs}</div>
<p class="center" style="margin-top:26px"><a class="link-under" href="diplomy-i-razvitie.html">Все дипломы и сертификаты →</a></p>
</section>
{cta_band(rel)}
"""
    write("o-centre.html", head("О центре — Вершина результата", "Центр нейрокоррекции и развития детей «Вершина результата»: подход, образовательная лицензия, руководитель центра Нина Сергеевна Туманова.", rel)
          + header(rel, "o-centre.html") + body + footer(rel))


def spec_card(p):
    tags = "".join(f'<span class="chip">{E(t)}</span>' for t in TEAM_EXTRA.get(p["name"], []))
    if p["img"]:
        key = p["img"].split("/")[-1].replace("-styled.png", "").replace("-styled.jpg", "")
        w, h = TEAM_PHOTO_SIZE.get(key, (720, 864))
        img = p["img"].replace(".png", ".jpg")
        photo = f'<div class="spec-photo"><img src="{img}" width="{w}" height="{h}" loading="lazy" alt="{E(p["alt"])}"></div>'
    else:
        parts = p["name"].split()
        photo = f'<div class="spec-mono" aria-hidden="true"><span>{parts[1][0]}{parts[0][0]}</span></div>'
    docs = f' · <a class="more" style="margin-top:0" href="diplomy-i-razvitie.html#{TEAM_DOCS[p["name"]]}">Документы</a>' if p["name"] in TEAM_DOCS else ""
    text = " ".join(p["details"])
    return (f'<article class="spec-card"{(" id=" + chr(34) + p["id"] + chr(34)) if p["id"] else ""}>{photo}<div class="spec-body"><h3>{E(p["name"])}</h3>'
            f'<p class="spec-role">{E(p["role"])}</p><p class="spec-text">{E(text)}</p><div class="chips">{tags}</div>'
            f'<span class="more"><a href="kontakty.html">Записаться →</a>{docs}</span></div></article>')


def page_specialists():
    rel = ""
    cards = "".join(spec_card(p) for p in DATA["team"])
    body = page_head("Специалисты", "Наши специалисты", "Все специалисты центра работают в едином комплексном подходе: учитывают речь, движение, обучение, общение и эмоциональное состояние ребёнка. Каждый отвечает за свою профессиональную область.") + f"""
<div class="wrap page-body">
<div class="team-note" id="team-coordination"><h2>Разные специалисты — общий план помощи</h2>
<p>Логопеды, нейропсихологи, психологи, миологопеды и специалисты по АФК согласуют цели занятий и нагрузку. Если ребёнку нужна помощь нескольких специалистов, команда объединяет их работу вокруг приоритетных задач.</p>
<p>Обсуждаем наблюдения и динамику, согласуем рекомендации для дома и при необходимости корректируем программу вместе с родителями. Комплексный подход — это нужное ребёнку сочетание направлений, а не обязательное посещение всех специалистов.</p></div>
<article class="lead-card" id="nina-tumanova">
<div class="photo-frame"><img src="team/nina-tumanova-styled.jpg" width="1000" height="1202" loading="lazy" alt="Туманова Нина Сергеевна — руководитель и основатель центра"></div>
<div class="lead-body"><span class="label">Руководитель и основатель центра</span><h2>Туманова Нина Сергеевна</h2>
<p class="founder-quote">{EXPERTISE}</p>{founder_creds()}
<a class="btn btn-yellow" href="kontakty.html">Записаться к Нине Сергеевне</a>
<a class="aside-link" style="text-align:left;color:var(--lime)" href="o-centre.html#rukovoditel">Подробнее о руководителе →</a></div>
</article>
<div class="grid g3" style="gap:24px">{cards}</div>
<div class="dark-box"><h2>Не знаете, к кому обратиться?</h2><p>Расскажите о возрасте ребёнка и вашей задаче — поможем выбрать специалиста.</p><a class="btn btn-yellow" href="kontakty.html">Подобрать специалиста</a></div>
</div>
"""
    write("specialisty.html", head("Специалисты — Вершина результата", "Команда центра «Вершина результата»: логопеды-дефектологи, нейропсихологи, психологи, миологопеды, специалисты по АФК.", rel)
          + header(rel, "specialisty.html") + body + footer(rel))


def page_prices():
    rel = ""
    cards = ""
    for g in DATA["priceGroups"]:
        rows = "".join(f'<div class="price-row"><div><h3>{E(i["name"])}</h3><p>{E(i["meta"])}</p></div>'
                       f'<div class="price-cost"><b>{E(i["price"])}</b><small>{E(i["unit"])}</small></div></div>' for i in g["items"])
        notes = ("<ul class=\"price-notes\">" + "".join(f"<li>{E(n)}</li>" for n in g["notes"]) + "</ul>") if g["notes"] else ""
        cards += (f'<section class="price-card" id="{g["id"]}"><div class="price-card-head"><h2>{E(g["title"])}</h2><p>{E(g["subtitle"])}</p></div>'
                  f'<div class="price-list">{rows}{notes}</div></section>')
    body = page_head("Цены", "Цены", "Для каждой услуги указаны длительность и формат оплаты: консультация, абонемент или полный курс.") + f"""
<div class="wrap page-body">
<div class="grid g2" style="gap:24px;align-items:start">{cards}</div>
<p class="lead-muted" style="font-size:15px;margin-top:26px">{E(DATA['priceNote'])}</p>
<div class="dark-box"><h2>Не знаете, что подойдёт?</h2><p>Расскажите о ребёнке — поможем выбрать услугу и формат занятий.</p><a class="btn btn-yellow" href="kontakty.html">Помогите выбрать услугу</a></div>
</div>
"""
    write("ceny.html", head("Цены — Вершина результата", "Стоимость услуг центра: логопедия и миокоррекция, нейрокоррекция и психология, БОС и аппаратные программы, приём Н. С. Тумановой.", rel)
          + header(rel, "ceny.html") + body + footer(rel))


def page_reviews():
    rel = ""
    body = page_head("Отзывы", "Отзывы", "Видеоотзывы родителей опубликованы на YouTube-канале Нины Тумановой.", script="Родители говорят о нас") + f"""
<div class="wrap page-body">
<div class="grid g3">{video_cards()}</div>
<div class="grid g2" style="margin-top:28px">
<div class="card-soft"><h3>YouTube-канал</h3><p>Видеоотзывы и материалы Нины Сергеевны Тумановой.</p><p style="margin-top:14px">{ext(YOUTUBE, 'Открыть канал ↗', 'link-under')}</p></div>
<div class="card-soft"><h3>Сообщество ВКонтакте</h3><p>Новости центра и общение с родителями.</p><p style="margin-top:14px">{ext(VK, 'Открыть сообщество ↗', 'link-under')}</p></div>
</div>
</div>
{cta_band(rel)}
"""
    write("otzyvy.html", head("Отзывы — Вершина результата", "Видеоотзывы родителей о центре «Вершина результата» на YouTube-канале Нины Тумановой.", rel)
          + header(rel, "otzyvy.html") + body + footer(rel))


def page_diplomas():
    rel = ""
    tl = "".join(f'<div class="step-card"><div class="step-num">{E(t["year"])}</div><p>{E(t["text"])}</p></div>' for t in DATA["timeline"])
    labels = {"tumanova-docs": "Нина Туманова", "kaverzneva-docs": "Елена Каверзнева", "eremkina-docs": "Елена Еремкина", "archive-docs": "Архив"}
    nav = "".join(f'<a class="btn btn-ghost" href="#{g["id"]}">{labels[g["id"]]}</a>' for g in DATA["docGroups"])
    groups = ""
    for g in DATA["docGroups"]:
        cards = ""
        for c in g["cards"]:
            cid = f' id="{c["id"]}"' if c["id"] else ""
            cards += (f'<article class="doc-card"{cid}><a class="doc-preview" href="{c["href"]}" target="_blank" rel="noopener" aria-label="Открыть: {E(c["title"])}">'
                      f'<img src="{c["img"]}" loading="lazy" alt="{E(c["alt"])}"></a><div class="doc-body"><small>{E(c["kind"])}</small><h3>{E(c["title"])}</h3><p>{E(c["desc"])}</p>'
                      f'<div class="doc-actions"><a href="{c["href"]}" target="_blank" rel="noopener">Открыть<span class="sr-only">: {E(c["title"])}</span></a>'
                      f'<a href="{c["href"]}" download="{c["download"]}">Скачать<span class="sr-only">: {E(c["title"])}</span></a></div></div></article>')
        groups += f'<section class="doc-group" id="{g["id"]}"><h2>{E(g["title"])}</h2><div class="grid g3">{cards}</div></section>'
    intro = "".join(f"<p>{E(p)}</p>" for p in DATA["docIntro"])
    body = f"""<section class="page-head"><div class="wrap"><div class="crumbs"><a href="index.html">Главная</a> / Дипломы и развитие</div>
<h1>Наши дипломы и путь развития</h1>{intro}
<div class="hero-actions" style="margin-top:22px"><a class="btn btn-yellow" href="#documents">Смотреть документы ↓</a><a class="btn btn-outline" href="specialisty.html">Познакомиться с командой</a></div></div></section>
<section class="method"><div class="wrap section">
<div class="section-head"><span class="pill pill-teal">ЭТАПЫ ОБУЧЕНИЯ КОМАНДЫ</span><h2 class="h2 title-up">Расширяем знания. Развиваем практику.</h2></div>
<div class="timeline">{tl}</div>
<p class="center lead-muted" style="font-size:15px;margin-top:22px">Хронология составлена по представленным документам об обучении специалистов.</p>
</div></section>
<div class="wrap page-body" id="documents">
<div class="row-head" style="margin-bottom:18px"><div><h2 class="h2 title-up">Обучение в деталях</h2><p>Сертификаты, удостоверения и справка о зачислении подписаны по типу документа.</p></div></div>
<nav class="doc-nav" aria-label="Документы по специалистам">{nav}</nav>
{groups}
</div>
{cta_band(rel)}
"""
    write("diplomy-i-razvitie.html", head("Наши дипломы и путь развития — Вершина результата",
                                          "Сертификаты и удостоверения специалистов центра «Вершина результата». Этапы профессионального развития и оригиналы документов.", rel)
          + header(rel, "diplomy-i-razvitie.html") + body + footer(rel))


def page_contacts():
    rel = ""
    body = page_head("Контакты", "Контакты", "Позвоните или напишите — поможем выбрать специалиста, формат и время.") + f"""
<div class="wrap wrap-1100 page-body">
<div class="contact-dark">
<div>
<span class="label">Начнём с разговора</span>
<h2>Расскажите о ребёнке. Поможем выбрать следующий шаг.</h2>
<p>Назовите возраст и коротко опишите, что вас беспокоит. Обсудим подходящего специалиста, стоимость и доступное время.</p>
<div class="contact-actions">{ext(TELEGRAM, 'Написать в Telegram ↗', 'btn btn-yellow')}<a class="btn btn-outline" href="tel:{PHONE_1_TEL}">Позвонить в центр</a></div>
<small>Запись подтверждается после согласования с центром.</small>
</div>
<div class="contact-list">
<div class="contact-item">{icon("phone")}<div><b>Телефоны</b><a class="big" href="tel:{PHONE_1_TEL}">{PHONE_1}</a><a href="tel:{PHONE_2_TEL}">{PHONE_2}</a></div></div>
<div class="contact-item">{icon("send")}<div><b>Telegram</b>{ext(TELEGRAM, TELEGRAM_NAME)}</div></div>
<div class="contact-item">{icon("pin")}<div><b>Адрес</b><span>{ADDRESS_FULL}</span>{ext(MAP_LINK, 'Посмотреть на Яндекс Картах ↗', 'lime')}</div></div>
<div class="contact-item">{icon("clock")}<div><b>Часы работы</b><span>{HOURS}</span></div></div>
<div class="contact-item">{icon("home")}<div><b>Центр нейрокоррекции и развития детей</b><span>«Вершина результата»</span></div></div>
</div>
</div>
<div class="map"><iframe src="{MAP_WIDGET}" title="Карта: {ADDRESS}" loading="lazy" allowfullscreen></iframe></div>
<div class="socials">{ext(TELEGRAM, 'Telegram', 'btn btn-ghost')}{ext(VK, 'ВКонтакте', 'btn btn-ghost')}{ext(YOUTUBE, 'YouTube', 'btn btn-ghost')}</div>
<div style="margin-top:28px">{license_card()}</div>
</div>
"""
    write("kontakty.html", head("Контакты — Вершина результата", f"Запись и консультации: {PHONE_1}, {PHONE_2}, Telegram {TELEGRAM_NAME}. {ADDRESS}. {HOURS}.", rel)
          + header(rel, "kontakty.html") + body + footer(rel))


if __name__ == "__main__":
    print("Сборка в", SITE)
    page_index()
    page_about()
    page_services()
    for s in SERVICES:
        page_service(s)
    page_specialists()
    page_prices()
    page_reviews()
    page_diplomas()
    page_contacts()
