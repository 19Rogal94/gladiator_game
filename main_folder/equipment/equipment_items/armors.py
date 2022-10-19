from ..classes_equipment.class_armor import Armor


"Armor"
no_armor = Armor(name="Nic", defence=0, stamina=0, price=0)
cloth_armor = Armor(name="Materiałowa zbroja", defence=1, stamina=0, price=100)
leather_armor = Armor(name="Skórzana zbroja", defence=3, stamina=-1, price=200)
iron_armor = Armor(name="Żelazna zbroja", defence=6, stamina=-2, price=300)
steel_armor = Armor(name="Stalowa zbroja", defence=10, stamina=-2, price=400)
master_armor = Armor(name="Mistrzowska zbroja", defence=13, stamina=-2, price=500)


"Armors list"
armor_list = [
    cloth_armor,
    leather_armor,
    iron_armor,
    steel_armor,
    master_armor
]
