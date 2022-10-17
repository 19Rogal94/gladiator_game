from ..classes_equipment.class_shield import Shield


"Shield"
brak_tarczy = Shield(name="Nic", defence=0, stamina=0, price=0)
drewniana_tarcza = Shield(name="Drewniana tarcza", defence=2, stamina=-1, price=100)
wzmocniona_drewniana_tarcza = Shield(name="Wzmocniona drewniana tarcza", defence=4, stamina=-1,
                                     price=200)
zelazna_tarcza = Shield(name="Żelazna tarcza", defence=8, stamina=-2, price=300)
stalowa_tarcza = Shield(name="Stalowa tarcza", defence=11, stamina=-2, price=400)
mistrzowska_tarcza = Shield(name="Mistrzowska tarcza", defence=15, stamina=-3, price=500)

"Shields list"
shield_list = [
    drewniana_tarcza,
    wzmocniona_drewniana_tarcza,
    zelazna_tarcza,
    stalowa_tarcza,
    mistrzowska_tarcza
]
