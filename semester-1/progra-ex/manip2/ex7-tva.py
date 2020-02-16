prix_article_htva = int(input("Entrez le prix de l'article htva: "))
categorie = input("Entrez une catégorie ('normal', 'important', 'nécessaire')")

if categorie == "normal":
    print(f"Le prix de l'article avec tva est de {prix_article_htva + prix_article_htva*6/100}")

elif categorie == "important":
    print(f"Le prix de l'article avec tva est de {prix_article_htva + prix_article_htva*12/100}")

else:
    print(f"Le prix de l'article avec tva est de {prix_article_htva + prix_article_htva*21/100}")

