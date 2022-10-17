from ..classes_equipment.class_weapon import Weapon


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

"Long distance weapons list"
weapon_long_distance_list = [
    proca,
    shuriken,
    luk_drewniany,
    luk_stalowy,
    mistrzowski_luk
]
