# Вершина результата — сайт центра

Статический сайт: HTML, CSS, без JavaScript-фреймворков. Дизайн — шаблон из Claude Design
(`source-materials/original-draft.html`), наполнение — сведения заказчика.

- `site/` — готовый сайт, именно он загружается на хостинг.
  - `index.html`, `o-centre.html`, `uslugi.html`, `uslugi/*.html`, `specialisty.html`, `ceny.html`,
    `otzyvy.html`, `diplomy-i-razvitie.html`, `kontakty.html` — страницы (собираются скриптом).
  - `assets/style.css` — все стили, `assets/fonts/` — шрифты Montserrat, PT Sans, Marck Script.
  - `team/` — фото специалистов, `diplomas/` — документы и миниатюры.
- `build/build.py` — генератор страниц; `build/customer-content.json` — услуги, цены, команда,
  вопросы, документы.
- `source-materials/` — исходники: шаблон, прайсы, портреты, первая версия сайта заказчика.
- `CLAUDE-START.md` — описание сайта и правила для правок.

## Как менять сайт

Тексты и цены правятся в `build/customer-content.json` или `build/build.py`, стили — в
`site/assets/style.css`. После правок пересоберите страницы:

```bash
python3 build/build.py
```

HTML-файлы в `site/` руками не правьте: следующая сборка их перезапишет.

## Хостинг и деплой

Сайт размещён на виртуальном хостинге Timeweb (тариф Optimo), основной сайт аккаунта `cj110251`:
https://cj110251.tw1.ru — временный технический домен.

Файлы лежат в `~/public_html` на сервере `vh460.timeweb.ru`. Обновление — из корня репозитория:

```bash
./deploy.sh --dry-run   # показать, что изменится
./deploy.sh             # загрузить
```

Перед деплоем пересоберите страницы (`python3 build/build.py`). Скрипт синхронизирует `site/` с `public_html` через rsync по SSH-ключу: новые файлы загружаются, удалённые из `site/` удаляются на сервере, `cgi-bin` не трогается.

Картинки и PDF сервер отдаёт с кэшем на год. Заменённое фото кладите под новым именем, иначе посетители долго будут видеть старое.

Render не используем: он отдаёт сайты через Cloudflare, а Cloudflare в России ограничивают провайдеры.

## Локальный просмотр

```bash
python3 -m http.server 8765 --directory site
```
