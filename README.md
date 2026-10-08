# Вершина результата — сайт центра

Статический сайт без сборки: HTML, CSS и немного JavaScript.

- `site/` — то, что публикуется: `index.html` (главная), `diplomy-i-razvitie.html`, фото команды и документы.
- `source-materials/` — исходники (прайсы, портреты, черновик). На сайт не попадают.
- `CLAUDE-START.md` — описание сайта и правила для дальнейших правок.
- `pered-publikatsiey.md` — рабочие замечания перед запуском.

## Деплой на Render (Static Site)

| Поле | Значение |
|---|---|
| Branch | `main` |
| Root Directory | пусто |
| Build Command | пусто |
| Publish Directory | `site` |

Каждый push в `main` обновляет сайт автоматически.

## Локальный просмотр

```bash
python3 -m http.server 8765 --directory site
```
