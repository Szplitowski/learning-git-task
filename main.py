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

print("Lista zakupów:")

for i in range (0,2):
  print(f"Idę do {sklepy[i]}, kupuję tu następujące rzeczy:{produkty[i]}")

print(f"W sumie kupuję {len(produkty[0])+len(produkty[1])} produktów")
#final