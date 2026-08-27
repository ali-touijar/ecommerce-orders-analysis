import pandas as pd

#telecharger le fichier CSV dans pandas sous forme de dataframe
df = pd.read_csv("data/orders.csv")

#afficher les 5 premières lignes du dataframe
df.head()
#afficher les informations sur le dataframe
df.info()
#afficher les statistiques descriptives du dataframe
df.describe()

#Combien de commandes ont été reçues ?
c=df['order_date'].count()
#Combien de commandes viennent de Fès ?
len(df[df['city'] == 'Fes'])
#Quels sont les différents produits vendus ?
df['product'].unique()
#Quel est le prix unitaire maximum ?
df['unit_price'].max()
#Quel est le prix unitaire moyen ?
df['unit_price'].mean()

#le montant total de chaque commande
df["total_price"] = (df["quantity"] * df["unit_price"])

#Valeur moyenne des ordres
avg_ord=df["total_price"].mean()
#Quel est le chiffre d'affaires total ?
total_revenue = df["total_price"].sum()
#Quel est le CA réalisé à Fès ?
CA_Fes=df[df['city']=='Fes']["total_price"].sum()
#Quelles sont les commandes dont le montant dépasse 5 000 DH ?
df[df['total_price']>5000]
#Quel est la commande avec le plus haut prix total ?
df[df['total_price'] == df['total_price'].max()]

#Quel est le produit de la commande avec le plus haut prix total ?
df.loc[df['total_price'].idxmax(), 'product']
#ou bien :
df.loc[df["total_price"] == df["total_price"].max(), ["order_id", "product"]]

#Toutes les commandes de Fès ont été enregistrées avec une remise de 5 % qui n'aurait pas dû être appliquée.
#Je corrige les données en augmentant de 5 % le total_price des commandes de Fès.
df.loc[df['city']=='Fes', 'total_price']*=1.05

#Valeur moyenne des ordres
avg_ord=df["total_price"].mean()
#Quel est le chiffre d'affaires total ?
total_revenue = df["total_price"].sum()
#Quel est le CA réalisé à Fès ?
CA_Fes=df[df['city']=='Fes']["total_price"].sum()

#export du fichier netoyé
df.to_csv("data/clean_orders.csv", index=False)

# Génération du rapport
with open("output/sales_report.txt", "w") as f:
    f.write("===== SALES REPORT =====\n\n")
    f.write(f"total orders: {c}\n")
    f.write(f"Total revenue: {total_revenue} DH\n")
    f.write(f"Revenue in Fes: {CA_Fes} DH\n")
    f.write(f"Average order value: {avg_ord} DH\n")