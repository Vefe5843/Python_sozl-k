meme_dict = {
            "OBURİKS": "Çok yiyene verilen cevap",
            "SAKAR ŞAKİR": "Her zaman sakarlık yapana söylenen cevap",
            "ÇAKAL":"Biri beklenmedik bir şey yapınca söylenen cevap"
            }
print("BÜYÜK YAZIN")
word = input()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Elimizde yok elinize veriyim o zaman o yok bu yok")
