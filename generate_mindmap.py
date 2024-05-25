import re

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        content = fp.read()
    return content


mindmap = read_file("main.puml")
template  = read_file("_layout.puml")

# Функция для вычисления общей цены и массы и замены значений
def calculate_and_replace(mindmap):
    # Регулярные выражения для поиска price и mass
    price_pattern = re.compile(r'price=(\d+\.?\d*)')
    mass_pattern = re.compile(r'mass=(\d+\.?\d*)')
    
    total_price = 0
    total_mass = 0

    # Функции для замены price и mass
    def replace_price(match):
        return f"${match.group(1)}"

    def replace_mass(match):
        return f"{int(match.group(1))/1000}"

    # Обработка строк, содержащих #
    def process_line(line):
        nonlocal total_price, total_mass
        line_start = re.match(r'[\s\-+*_]*', line).group()  # Захватываем начальные символы (пробелы, дефисы, плюсы, звездочки)
        content = line[len(line_start):].strip()
        
        if '#' in content:
            content = content.split('#', 1)[1].strip()
            content = price_pattern.sub(replace_price, content)
            content = mass_pattern.sub(replace_mass, content)
            content = f"<s>{content}</s>"
            return f"{line_start}{content}"
        else:
            # Если строка не содержит #, считаем цену и массу
            prices = price_pattern.findall(content)
            masses = mass_pattern.findall(content)
            total_price += sum(float(price) for price in prices)
            total_mass += sum(float(mass) for mass in masses)
            content = price_pattern.sub(replace_price, content)
            content = mass_pattern.sub(replace_mass, content)
            return f"{line_start}{content}"

    # Разделить mindmap на строки и обработать каждую строку
    lines = mindmap.split('\n')
    processed_lines = [process_line(line) for line in lines]

    return total_price, total_mass, '\n'.join(processed_lines)

# Вычисление общей цены и массы и замена значений
total_price, total_mass, updated_mindmap = calculate_and_replace(mindmap)

# Форматирование и запись результата в файл с поддержкой UTF-8
with open("generated.puml", 'w', encoding='utf-8') as fp:
    fp.write(template.format(total_price, total_mass / 1000, updated_mindmap))

print(template.format(total_price, total_mass / 1000, updated_mindmap))