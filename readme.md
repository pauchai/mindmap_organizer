This project is aimed at helping to organize a backpack for travels
Just edit main.puml to create mindmap 
To generate mindmap run: 
```
python generate_mindmap.py
```
main.puml
```
- <&home>Поход
-- <&rain>Снаряжение
---_ Спальник price=30 mass=1100
---_ Гaмак price=15 mass=120
---_ Тент price=15 mass=120
---_ Тент-пончо price=15 mass=120
---_ #Каримат обычный price=15 mass=120
---_ Коврик надувной price=15 mass=120
---_ Фонарь наголовный price=15 mass=300
---_ #Палатка price=80 mass=2500
---_ Веревка
++ <&book>Гаджеты
+++_ #Камера price=100 mass=300
+++_ Смартфон mass=300
+++_ Ноутбук mass=1000
+++_ #Мобильный штатив price=20
+++_ #Портативная солнечная панель price=100 mass=1000
+++_ #удлинитель
+++_ #powerbank price=200 mass=200

-- <&cloudy>Одежда
---_ Обувь price=20 mass=100
---_ Панама
---_ #Дождевик-тент price=20 mass=100
---_ #Шапка price=10 mass=100

-- посуды средство для огня price=30 mass=500
---_ Огниво
---_ Фильтр для воды price=20 mass=120
---_ Комплект посуды price=20 mass=120
-- Сумки
---_ Сумка на пояс price=40 mass=300
---_ Рюкзак price=100 mass=1000

++ #Провиант mass=3000


++ <&wrench>Инструмент
+++_ Лопата соперская price=30 mass=500
+++_ Топор price=30 mass=1000
+++_ Пила price=30 mass=1000
+++_ Нож price=40 mass=400
+++_ сверло price=50 mass=500
+++_ #стамеска price=50 mass=400
+++_ multitool price=20 mass=150

++ <&list>прочее
```

![пример сгенерированнной карты mindmap](./generated.png)
