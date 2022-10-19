from ..classes_equipment.class_weapon import Weapon


"Long distance weapon"
stones = Weapon(name="Kamienie", strength=0, strenght_long=0, stamina=0, price=0, weapon_type="long_distance")
slingshot = Weapon(name="Proca", strength=0, strenght_long=2, stamina=0, price=100, weapon_type="long_distance")
shuriken = Weapon(name="Shurikeny", strength=0, strenght_long=5, stamina=0, price=200, weapon_type="long_distance")
wooden_arch = Weapon(name="Łuk drewniany", strength=0, strenght_long=8, stamina=0, price=300,
                     weapon_type="long_distance")
steel_arch = Weapon(name="Łuk drewniany", strength=0, strenght_long=11, stamina=0, price=400,
                    weapon_type="long_distance")
master_arch = Weapon(name="Łuk mistrzowski", strength=0, strenght_long=15, stamina=0, price=500,
                     weapon_type="long_distance")

"Long distance weapons list"
weapon_long_distance_list = [
    slingshot,
    shuriken,
    wooden_arch,
    steel_arch,
    master_arch
]
