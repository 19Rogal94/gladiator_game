def verification_equipment_in_list(equipment_list: list, action: str) -> bool:
    new_list = [arg.name for arg in equipment_list]
    return action.capitalize() in new_list
