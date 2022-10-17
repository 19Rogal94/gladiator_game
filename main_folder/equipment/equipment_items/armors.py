from ..classes_equipment.class_armor import Armor


"Armor"
brak_zbroi = Armor(name="Nic", defence=0, stamina=0, price=0)
materialowa_zbroja = Armor(name="Materiałowa zbroja", defence=1, stamina=0, price=100)
skorzana_zbroja = Armor(name="Skórzana zbroja", defence=3, stamina=-1, price=200)
zelazna_zbroja = Armor(name="Żelazna zbroja", defence=6, stamina=-2, price=300)
stalowa_zbroja = Armor(name="Stalowa zbroja", defence=10, stamina=-2, price=400)
mistrzowska_zbroja = Armor(name="Mistrzowska zbroja", defence=13, stamina=-2, price=500)


"Armors list"
armor_list = [
    materialowa_zbroja,
    skorzana_zbroja,
    zelazna_zbroja,
    stalowa_zbroja,
    mistrzowska_zbroja
]
