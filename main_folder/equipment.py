import class_equipment

"Long distance weapon"
kamienie = class_equipment.Weapon(name="Kamienie", strenght=0, strenght_long=0, stamina=0, price=0,
                                  weapon_type="long_distance")
proca = class_equipment.Weapon(name="Proca", strenght=0, strenght_long=2, stamina=0, price=100,
                               weapon_type="long_distance")
shuriken = class_equipment.Weapon(name="Shurikeny", strenght=0, strenght_long=5, stamina=0, price=200,
                                  weapon_type="long_distance")
luk_drewniany = class_equipment.Weapon(name="Łuk drewniany", strenght=0, strenght_long=8, stamina=0, price=300,
                                       weapon_type="long_distance")
luk_stalowy = class_equipment.Weapon(name="Łuk drewniany", strenght=0, strenght_long=11, stamina=0, price=400,
                                     weapon_type="long_distance")
mistrzowski_luk = class_equipment.Weapon(name="Łuk mistrzowski", strenght=0, strenght_long=15, stamina=0, price=500,
                                         weapon_type="long_distance")

"Short distance weapon - primary"
piesci = class_equipment.Weapon(name="Pięści", strenght=0, strenght_long=0, stamina=0, price=0,
                                weapon_type="short_distance")

"Short distance weapon - mace"
drewniana_maczuga = class_equipment.Weapon(name="Drewniana maczuga", strenght=4, strenght_long=0, stamina=-2, price=100,
                                           weapon_type="short_distance")
kamienna_maczuga = class_equipment.Weapon(name="Kamienna maczuga", strenght=8, strenght_long=0, stamina=-3, price=200,
                                          weapon_type="short_distance")
zelazna_maczuga = class_equipment.Weapon(name="Żelazna maczuga", strenght=12, strenght_long=0, stamina=-4, price=300,
                                         weapon_type="short_distance")
stalowa_maczuga = class_equipment.Weapon(name="Stalowa maczuga", strenght=16, strenght_long=0, stamina=-5, price=400,
                                         weapon_type="short_distance")
mistrzowska_maczuga = class_equipment.Weapon(name="Mistrzowska maczuga", strenght=21, strenght_long=0, stamina=-6,
                                             price=500, weapon_type="short_distance")

"Short distance weapon - sword"
krotki_miecz = class_equipment.Weapon(name="Krótki miecz", strenght=2, strenght_long=0, stamina=0, price=100,
                                      weapon_type="short_distance")
zelazny_miecz = class_equipment.Weapon(name="Żelazny miecz", strenght=5, strenght_long=0, stamina=0, price=200,
                                       weapon_type="short_distance")
stalowy_miecz = class_equipment.Weapon(name="Stalowy miecz", strenght=8, strenght_long=0, stamina=0, price=300,
                                       weapon_type="short_distance")
dlugi_stalowy_miecz = class_equipment.Weapon(name="Długi stalowy miecz", strenght=11, strenght_long=0, stamina=0,
                                             price=400, weapon_type="short_distance")
mistrzowski_miecz = class_equipment.Weapon(name="Mistrzowski miecz", strenght=15, strenght_long=0, stamina=0, price=500,
                                           weapon_type="short_distance")

"Short distance weapon - axe"
kamienny_topor = class_equipment.Weapon(name="Krótki topór", strenght=3, strenght_long=0, stamina=-1, price=100,
                                        weapon_type="short_distance")
zelazny_topor = class_equipment.Weapon(name="Żelazny topór", strenght=7, strenght_long=0, stamina=-2, price=200,
                                       weapon_type="short_distance")
stalowy_topor = class_equipment.Weapon(name="Stalowy topór", strenght=11, strenght_long=0, stamina=-3, price=300,
                                       weapon_type="short_distance")
stalowy_topor_obustronny = class_equipment.Weapon(name="Stalowy topór obustronny", strenght=15, strenght_long=0,
                                                  stamina=-4, price=400, weapon_type="short_distance")
mistrzowski_topor = class_equipment.Weapon(name="Mistrzowski topór", strenght=20, strenght_long=0, stamina=-5,
                                           price=500, weapon_type="short_distance")

"Helmet"
brak_helmu = class_equipment.Helmet(name="Nic", defence=0, stamina=0, price=0)
skorzany_helmet = class_equipment.Helmet(name="Skórzany hełm", defence=1, stamina=0, price=100)
zelazny_helmet = class_equipment.Helmet(name="żelazny hełm", defence=3, stamina=-1, price=200)
stalowy_helmet = class_equipment.Helmet(name="Stalowy hełm", defence=6, stamina=-1, price=300)
stalowy_helmet_obudowany = class_equipment.Helmet(name="Stalowy hełm obudowany", defence=10, stamina=-2, price=400)
mistrzowski_helmet = class_equipment.Helmet(name="Mistrzowski hełm", defence=13, stamina=-2, price=500)

"Armor"
brak_zbroi = class_equipment.Armor(name="Nic", defence=0, stamina=0, price=0)
materialowa_zbroja = class_equipment.Armor(name="Materiałowa zbroja", defence=1, stamina=0, price=100)
skorzana_zbroja = class_equipment.Armor(name="Skórzana zbroja", defence=3, stamina=-1, price=200)
zelazna_zbroja = class_equipment.Armor(name="Żelazna zbroja", defence=6, stamina=-2, price=300)
stalowa_zbroja = class_equipment.Armor(name="Stalowa zbroja", defence=10, stamina=-2, price=400)
mistrzowska_zbroja = class_equipment.Armor(name="Mistrzowska zbroja", defence=13, stamina=-2, price=500)

"Shield"
brak_tarczy = class_equipment.Helmet(name="Nic", defence=0, stamina=0, price=0)
drewniana_tarcza = class_equipment.Shield(name="Drewniana tarcza", defence=2, stamina=-1, price=100)
wzmocniona_drewniana_tarcza = class_equipment.Shield(name="Wzmocniona drewniana tarcza", defence=4, stamina=-1,
                                                     price=200)
zelazna_tarcza = class_equipment.Shield(name="Żelazna tarcza", defence=8, stamina=-2, price=300)
stalowa_tarcza = class_equipment.Shield(name="Stalowa tarcza", defence=11, stamina=-2, price=400)
mistrzowska_tarcza = class_equipment.Shield(name="Mistrzowska tarcza", defence=15, stamina=-3, price=500)

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
