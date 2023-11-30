from forex_python.converter import CurrencyRates
import json
from datetime import datetime

def convertir_devise(montant, devise_source, devise_cible):
    c = CurrencyRates()

    try:
        taux = c.get_rate(devise_source, devise_cible)
        resultat = montant * taux
        return resultat
    except:
        return None

def enregistrer_conversion(historique, montant, devise_source, devise_cible, resultat):
    conversion = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Montant": montant,
        "Devise Source": devise_source,
        "Devise Cible": devise_cible,
        "Résultat": resultat
    }

    historique.append(conversion)

    with open("historique_conversions.json", "w") as fichier:
        json.dump(historique, fichier, indent=4)

def afficher_historique(historique):
    if not historique:
        print("Aucune conversion enregistrée dans l'historique.")
        return

    print("Historique des conversions :")
    for conversion in historique:
        print(f"{conversion['Date']} - Converti {conversion['Montant']} {conversion['Devise Source']} en {conversion['Résultat']} {conversion['Devise Cible']}")

def main():
    historique = []

    while True:
        try:
            montant = float(input("Entrez le montant à convertir : "))
            devise_source = input("Entrez la devise source (ex: USD) : ").upper()
            devise_cible = input("Entrez la devise cible (ex: EUR) : ").upper()

            resultat = convertir_devise(montant, devise_source, devise_cible)

            if resultat is not None:
                print(f"{montant} {devise_source} équivaut à {resultat} {devise_cible}")
                enregistrer_conversion(historique, montant, devise_source, devise_cible, resultat)
            else:
                print("Conversion impossible. Vérifiez les devises fournies.")
        
        except ValueError:
            print("Veuillez entrer un montant numérique.")
        
        continuer = input("Voulez-vous effectuer une autre conversion ? (oui/non) : ").lower()
        if continuer != 'oui':
            break

    afficher_historique(historique)

if __name__ == "__main__":
    main()
