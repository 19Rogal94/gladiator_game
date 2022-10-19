from ..classes_equipment.class_shield import Shield


"Shield"
no_shield = Shield(name="Nic", defence=0, stamina=0, price=0)
wooden_shield = Shield(name="Drewniana tarcza", defence=2, stamina=-1, price=100)
reinforced_wooden_shield = Shield(name="Wzmocniona drewniana tarcza", defence=4, stamina=-1,
                                  price=200)
iron_shield = Shield(name="Żelazna tarcza", defence=8, stamina=-2, price=300)
steel_shield = Shield(name="Stalowa tarcza", defence=11, stamina=-2, price=400)
master_shield = Shield(name="Mistrzowska tarcza", defence=15, stamina=-3, price=500)

"Shields list"
shield_list = [
    wooden_shield,
    reinforced_wooden_shield,
    iron_shield,
    steel_shield,
    master_shield
]
