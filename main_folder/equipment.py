# import main_folder.class_equipment
from main_folder.class_equipment import Weapon, Helmet, Armor, Shield

"Long distance weapon"
kamienie = Weapon(name="Kamienie", strenght=0, strenght_long=0, stamina=0, price=0, weapon_type="long_distance")
proca = Weapon(name="Proca", strenght=0, strenght_long=2, stamina=0, price=100, weapon_type="long_distance")
shuriken = Weapon(name="Shurikeny", strenght=0, strenght_long=5, stamina=0, price=200, weapon_type="long_distance")
luk_drewniany = Weapon(name="Łuk drewniany", strenght=0, strenght_long=8, stamina=0, price=300,
                       weapon_type="long_distance")
luk_stalowy = Weapon(name="Łuk drewniany", strenght=0, strenght_long=11, stamina=0, price=400,
                     weapon_type="long_distance")
mistrzowski_luk = Weapon(name="Łuk mistrzowski", strenght=0, strenght_long=15, stamina=0, price=500,
                         weapon_type="long_distance")

"Short distance weapon - primary"
piesci = Weapon(name="Pięści", strenght=0, strenght_long=0, stamina=0, price=0, weapon_type="short_distance")

"Short distance weapon - mace"
drewniana_maczuga = Weapon(name="Drewniana maczuga", strenght=4, strenght_long=0, stamina=-2, price=100,
                           weapon_type="short_distance")
kamienna_maczuga = Weapon(name="Kamienna maczuga", strenght=8, strenght_long=0, stamina=-3, price=200,
                          weapon_type="short_distance")
zelazna_maczuga = Weapon(name="Żelazna maczuga", strenght=12, strenght_long=0, stamina=-4, price=300,
                         weapon_type="short_distance")
stalowa_maczuga = Weapon(name="Stalowa maczuga", strenght=16, strenght_long=0, stamina=-5, price=400,
                         weapon_type="short_distance")
mistrzowska_maczuga = Weapon(name="Mistrzowska maczuga", strenght=21, strenght_long=0, stamina=-6, price=500,
                             weapon_type="short_distance")

"Short distance weapon - sword"
krotki_miecz = Weapon(name="Krótki miecz", strenght=2, strenght_long=0, stamina=0, price=100,
                      weapon_type="short_distance")
zelazny_miecz = Weapon(name="Żelazny miecz", strenght=5, strenght_long=0, stamina=0, price=200,
                       weapon_type="short_distance")
stalowy_miecz = Weapon(name="Stalowy miecz", strenght=8, strenght_long=0, stamina=0, price=300,
                       weapon_type="short_distance")
dlugi_stalowy_miecz = Weapon(name="Długi stalowy miecz", strenght=11, strenght_long=0, stamina=0, price=400,
                             weapon_type="short_distance")
mistrzowski_miecz = Weapon(name="Mistrzowski miecz", strenght=15, strenght_long=0, stamina=0, price=500,
                           weapon_type="short_distance")

"Short distance weapon - axe"
kamienny_topor = Weapon(name="Krótki topór", strenght=3, strenght_long=0, stamina=-1, price=100,
                        weapon_type="short_distance")
zelazny_topor = Weapon(name="Żelazny topór", strenght=7, strenght_long=0, stamina=-2, price=200,
                       weapon_type="short_distance")
stalowy_topor = Weapon(name="Stalowy topór", strenght=11, strenght_long=0, stamina=-3, price=300,
                       weapon_type="short_distance")
stalowy_topor_obustronny = Weapon(name="Stalowy topór obustronny", strenght=15, strenght_long=0, stamina=-4,
                                  price=400, weapon_type="short_distance")
mistrzowski_topor = Weapon(name="Mistrzowski topór", strenght=20, strenght_long=0, stamina=-5, price=500,
                           weapon_type="short_distance")

"Helmet"
brak_helmu = Helmet(name="Nic", defence=0, stamina=0, price=0)
skorzany_helmet = Helmet(name="Skórzany hełm", defence=1, stamina=0, price=100)
zelazny_helmet = Helmet(name="żelazny hełm", defence=3, stamina=-1, price=200)
stalowy_helmet = Helmet(name="Stalowy hełm", defence=6, stamina=-1, price=300)
stalowy_helmet_obudowany = Helmet(name="Stalowy hełm obudowany", defence=10, stamina=-2, price=400)
mistrzowski_helmet = Helmet(name="Mistrzowski hełm", defence=13, stamina=-2, price=500)

"Armor"
brak_zbroi = Armor(name="Nic", defence=0, stamina=0, price=0)
materialowa_zbroja = Armor(name="Materiałowa zbroja", defence=1, stamina=0, price=100)
skorzana_zbroja = Armor(name="Skórzana zbroja", defence=3, stamina=-1, price=200)
zelazna_zbroja = Armor(name="Żelazna zbroja", defence=6, stamina=-2, price=300)
stalowa_zbroja = Armor(name="Stalowa zbroja", defence=10, stamina=-2, price=400)
mistrzowska_zbroja = Armor(name="Mistrzowska zbroja", defence=13, stamina=-2, price=500)

"Shield"
brak_tarczy = Helmet(name="Nic", defence=0, stamina=0, price=0)
drewniana_tarcza = Shield(name="Drewniana tarcza", defence=2, stamina=-1, price=100)
wzmocniona_drewniana_tarcza = Shield(name="Wzmocniona drewniana tarcza", defence=4, stamina=-1,
                                     price=200)
zelazna_tarcza = Shield(name="Żelazna tarcza", defence=8, stamina=-2, price=300)
stalowa_tarcza = Shield(name="Stalowa tarcza", defence=11, stamina=-2, price=400)
mistrzowska_tarcza = Shield(name="Mistrzowska tarcza", defence=15, stamina=-3, price=500)

"Equipment list"
weapon_short_distance_list = [
    drewniana_maczuga,
    krotki_miecz,
    kamienny_topor,
    kamienna_maczuga,
    zelazny_miecz,
    zelazny_topor,
    zelazna_maczuga,
    stalowy_miecz,
    stalowy_topor,
    stalowa_maczuga,
    dlugi_stalowy_miecz,
    stalowy_topor_obustronny,
    mistrzowska_maczuga,
    mistrzowski_miecz,
    mistrzowski_topor
]

weapon_long_distance_list = [
    proca,
    shuriken,
    luk_drewniany,
    luk_stalowy,
    mistrzowski_luk
]

helmet_list = [
    skorzany_helmet,
    zelazny_helmet,
    stalowy_helmet,
    stalowy_helmet_obudowany,
    mistrzowski_helmet
]

armor_list = [
    materialowa_zbroja,
    skorzana_zbroja,
    zelazna_zbroja,
    stalowa_zbroja,
    mistrzowska_zbroja
]

shield_list = [
    drewniana_tarcza,
    wzmocniona_drewniana_tarcza,
    zelazna_tarcza,
    stalowa_tarcza,
    mistrzowska_tarcza
]
