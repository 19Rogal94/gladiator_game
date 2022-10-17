from ..classes_equipment.class_helmet import Helmet


"Helmet"
brak_helmu = Helmet(name="Nic", defence=0, stamina=0, price=0)
skorzany_helmet = Helmet(name="Skórzany hełm", defence=1, stamina=0, price=100)
zelazny_helmet = Helmet(name="żelazny hełm", defence=3, stamina=-1, price=200)
stalowy_helmet = Helmet(name="Stalowy hełm", defence=6, stamina=-1, price=300)
stalowy_helmet_obudowany = Helmet(name="Stalowy hełm obudowany", defence=10, stamina=-2, price=400)
mistrzowski_helmet = Helmet(name="Mistrzowski hełm", defence=13, stamina=-2, price=500)

"Helmets list"
helmet_list = [
    skorzany_helmet,
    zelazny_helmet,
    stalowy_helmet,
    stalowy_helmet_obudowany,
    mistrzowski_helmet
]
