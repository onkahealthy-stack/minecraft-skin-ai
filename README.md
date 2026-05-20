# 🎨 Minecraft Skin AI Generator

**Профессиональный искусственный интеллект для создания уникальных скинов Minecraft**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)

## ✨ Возможности

- 🤖 **AI Генерация** - создание скинов по текстовому описанию
- 🎨 **8+ Стилей** - фэнтези, киберпанк, пиксель-арт, минимализм и другие
- 🖼️ **Редактор** - редактирование и улучшение существующих скинов
- 🌍 **Web Interface** - красивый веб-интерфейс
- ⚡ **REST API** - полнофункциональное API для интеграции
- 📱 **Адаптивный дизайн** - работает на всех устройствах
- 💾 **История** - сохранение и управление всеми созданными скинами
- 🎲 **Случайная генерация** - вдохновение нажатием кнопки

## 🚀 Быстрый старт

### Требования
- Python 3.10+
- 8GB+ RAM (для моделей ИИ)
- GPU (рекомендуется, но опционально)

### Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/onkahealthy-stack/minecraft-skin-ai.git
cd minecraft-skin-ai

# Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# Установите зависимости
pip install -r requirements.txt

# Загрузите модели ИИ (первый запуск)
python -c "from core.generator import SkinGenerator; SkinGenerator()"
```

## 💻 Использование

### Web Интерфейс (рекомендуется)

```bash
python main.py
```

Откройте http://localhost:8000 в браузере 🌐

### REST API

```bash
# Генерация нового скина
curl -X POST "http://localhost:8000/api/generate" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "красный рыцарь с мечом", "style": "fantasy"}'

# Редактирование скина
curl -X POST "http://localhost:8000/api/edit/skin_1" \
  -H "Content-Type: application/json" \
  -d '{"modification": "добавить крылья"}'

# Получить список всех скинов
curl "http://localhost:8000/api/skins"

# Получить доступные стили
curl "http://localhost:8000/api/styles"
```

### CLI (Командная строка)

```bash
# Генерация скина
python cli.py generate "зеленый ниндзя" --style cyberpunk

# Случайная генерация
python cli.py random --count 5

# Редактирование
python cli.py edit "skin_1" --modification "добавить шляпу"

# Список стилей
python cli.py styles
```

## 📡 API Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| POST | `/api/generate` | Генерация скина по описанию |
| POST | `/api/edit/{id}` | Редактирование существующего скина |
| GET | `/api/skins` | Получить список всех скинов |
| GET | `/api/skins/{id}` | Получить конкретный скин |
| POST | `/api/random` | Генерировать случайный скин |
| GET | `/api/styles` | Список доступных стилей |
| DELETE | `/api/skins/{id}` | Удалить скин |

## 🎨 Доступные стили

- **fantasy** - Фэнтези (драконы, маги, рыцари)
- **cyberpunk** - Киберпанк (неон, робото, будущее)
- **pixel** - Пиксель-арт (ретро, классический Minecraft)
- **minimalist** - Минимализм (простые формы, ясные линии)
- **steampunk** - Стимпанк (гайки, паровые механизмы)
- **anime** - Аниме (японский стиль, большие глаза)
- **horror** - Ужас (темный, мрачный, жуткий)
- **nature** - Природа (животные, растения, лес)

## 📁 Структура проекта

```
minecraft-skin-ai/
├── core/
│   ├── __init__.py
│   ├── generator.py          # Ядро генератора
│   ├── models.py             # Модели ИИ
│   └── config.py             # Конфигурация
├── web/
│   ├── __init__.py
│   ├── app.py                # FastAPI приложение
│   ├── routes.py             # API маршруты
│   └── static/
│       ├── index.html        # Веб-интерфейс
│       ├── style.css
│       └── script.js
├── cli.py                     # CLI интерфейс
├── main.py                    # Точка входа
├── requirements.txt           # Зависимости
├── .gitignore
├── LICENSE
└── README.md
```

## ⚙️ Конфигурация

Отредактируйте `core/config.py` для настройки:

```python
# Модель ИИ
MODEL_NAME = "runwayml/stable-diffusion-v1-5"

# Параметры генерации
INFERENCE_STEPS = 50  # Больше = качественнее, но медленнее
GUIDENCE_SCALE = 7.5  # Соответствие промпту

# Качество вывода
OUTPUT_SIZE = (512, 512)  # Размер изображения
SKIN_SIZE = (64, 64)      # Размер скина Minecraft
```

## 🎯 Примеры использования

### Пример 1: Создание эпического босса
```python
from core.generator import SkinGenerator

generator = SkinGenerator()
skin = generator.generate(
    prompt="эпический демон с огненными крыльями и мрачной аурой",
    style="horror"
)
skin.save("demon_boss.png")
```

### Пример 2: Пакетная генерация
```python
for i in range(10):
    skin = generator.random_generate()
    skin.save(f"random_skin_{i}.png")
```

### Пример 3: Улучшение существующего скина
```python
from core.generator import SkinGenerator, load_image

generator = SkinGenerator()
original = load_image("my_skin.png")
improved = generator.enhance(original, "добавить больше деталей")
improved.save("improved_skin.png")
```

## 🚨 Решение проблем

### "CUDA out of memory"
```bash
# Уменьшите параметры в config.py
INFERENCE_STEPS = 25
OUTPUT_SIZE = (256, 256)
```

### Медленная генерация
- Используйте GPU (установите `torch` с CUDA поддержко��)
- Уменьшите `INFERENCE_STEPS`
- Включите режим "half precision": `USE_FP16 = True`

### Скины не сохраняются
- Проверьте права на папку `skins/`
- Используйте абсолютные пути: `/full/path/to/skin.png`

## 📊 Производительность

| Оборудование | Время генерации | Качество |
|--------------|-----------------|----------|
| GPU (RTX 3080) | 5-10 сек | Максимальное |
| GPU (RTX 2060) | 15-25 сек | Высокое |
| CPU (Intel i7) | 2-5 минут | Среднее |

## 🤝 Вклад в проект

Мы приветствуем вклады! Пожалуйста:

1. Создайте fork проекта
2. Создайте ветку (`git checkout -b feature/AmazingFeature`)
3. Commit изменения (`git commit -m 'Add AmazingFeature'`)
4. Push на ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📝 Лицензия

Этот проект лицензирован под MIT License - см. [LICENSE](LICENSE) файл для деталей.

## 🙏 Благодарности

- [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5) - модель ИИ
- [FastAPI](https://fastapi.tiangolo.com/) - веб-фреймворк
- [PyTorch](https://pytorch.org/) - библиотека машинного обучения
- Сообщество Minecraft

## 📧 Контакты

Вопросы? Создавайте Issues на GitHub!

---

**Создано с ❤️ для сообщества Minecraft**
