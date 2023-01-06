lista = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

sklepy = []
produkty = []

for keys in lista.keys():
  sklepy.append(keys.title())

for keys, values in lista.items():
  produkty.append(values)
