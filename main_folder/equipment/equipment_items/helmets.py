from ..classes_equipment.class_helmet import Helmet


"Helmet"
no_helmet = Helmet(name="Nic", defence=0, stamina=0, price=0)
leather_helmet = Helmet(name="Skórzany hełm", defence=1, stamina=0, price=100)
iron_helmet = Helmet(name="żelazny hełm", defence=3, stamina=-1, price=200)
steel_helmet = Helmet(name="Stalowy hełm", defence=6, stamina=-1, price=300)
steel_helmet_covered = Helmet(name="Stalowy hełm obudowany", defence=10, stamina=-2, price=400)
master_helmet = Helmet(name="Mistrzowski hełm", defence=13, stamina=-2, price=500)

"Helmets list"
helmet_list = [
    leather_helmet,
    iron_helmet,
    steel_helmet,
    steel_helmet_covered,
    master_helmet
]
