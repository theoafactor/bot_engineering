"""shirts
    - colors: green, yellow, red
    - sizes: l, m, s
    """

colors = ["green", "yellow", "red"]

sizes = ["l", "m", "s"]

#products = [(color, size) for color in colors for size in sizes]

#print(products)

products = []

for color in colors:
    for size in sizes:
        products.append((color, size))


print(products)