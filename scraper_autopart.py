import requests
from bs4 import BeautifulSoup

url = "https://autopart.tn/auto/iveco-55/daily-vi-camion-plate-forme-chassis-13059/35s15-35c15-40c15-50c15-65c15-70c15-72c15-119892.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print("=== TITRE DE LA PAGE ===")
    print(soup.title.string.strip())

    # Essai pour trouver le nom du produit
    nom_produit = soup.find("h1")
    if nom_produit:
        print("\n=== NOM DU PRODUIT ===")
        print(nom_produit.get_text(strip=True))
    else:
        print("\nNom du produit non trouvé")

    # Essai pour trouver le prix
    prix = soup.find("span", class_="price")
    if prix:
        print("\n=== PRIX ===")
        print(prix.get_text(strip=True))
    else:
        print("\nPrix non trouvé")

    # Essai pour trouver la référence
    reference = soup.find("span", class_="editable")
    if reference:
        print("\n=== RÉFÉRENCE ===")
        print(reference.get_text(strip=True))
    else:
        print("\nRéférence non trouvée")

    # Essai description courte
    description = soup.find("div", id="short_description_content")
    if description:
        print("\n=== DESCRIPTION COURTE ===")
        print(description.get_text(strip=True))
    else:
        print("\nDescription courte non trouvée")

    # Essai pour afficher le contenu complet de la section "Détails du produit"
    details = soup.find("section", id="idTab1")
    if details:
        print("\n=== DÉTAILS DU PRODUIT ===")
        print(details.get_text(strip=True)[:500] + "...")  # Affiche seulement les 500 premiers caractères
    else:
        print("\nDétails du produit non trouvés")

else:
    print("Erreur lors du chargement de la page:", response.status_code)
