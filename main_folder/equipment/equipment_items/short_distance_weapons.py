from ..classes_equipment.class_weapon import Weapon


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

"Short distance weapons list"
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
