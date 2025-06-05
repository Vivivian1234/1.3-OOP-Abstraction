
from weapons import Weapon, Sword, Bow, list

inventory = []

def main():
    while True:
        action = input("\nThis is the weapon recording system. What would you like to do? \n- 1. Add weapon \n- 2. View inventory \n- 3. Search inventory \n- 4. Change stats\n- 5. Exit\n")

        if action == "1":
            name = input("Enter name of weapon (give it a nice name :D like Guoba, Mehrak, *Sinner's Final Notice* hehe): ")
            damage = int(input("Enter damage: "))

            weapon_choice = input("Choose type: \n- 1. Sword \n- 2. Bow\n")
            
            if weapon_choice == "1":
                category = "Sword"
                melee_type = input("Enter damage type (e.g., slashing, piercing, etc.): ")
                new_weapon = Sword(name, category, damage, melee_type)
            elif weapon_choice == "2":
                category = "Bow"
                user_range_input = input("Choose range type: \n- 1. Piercing\n- 2. Explosive)\n")
                if user_range_input == "1":
                    range_type = "Piercing"
                    new_weapon = Bow(name, category, damage, range_type)
                elif user_range_input == "2":
                    range_type = "Explosive"
                    new_weapon = Bow(name, category, damage, range_type)
                else:
                    print("\nInvalid input. Please try again.\n")
                    continue

            else:
                print("\nInvalid input. Please try again.\n")
                continue

            inventory.append(new_weapon)
            print("\nWeapon added successfully!\n")

        elif action == "2":
            for weapon in inventory:
                weapon.get_stats()
                print("-" * 20)
        
        elif action == "3":
            search_term = input("Enter weapon name to search: ")
            found = [weapon for weapon in inventory if weapon.name.lower() == search_term.lower()]
            print()
            if found:
                for weapon in found:
                    weapon.get_stats()
            else:
                print("\nWeapon not found.\n")

        elif action == "4":
            print("---Changing stats---")
            search = input("Enter weapon name to change stats: ")
            if search in inventory if weapon.name.lower() == search.lower()
                weapon.get_stats()
                if weapon == Sword:
                    stat_change = input("Enter stat you want to change: \n- 1. Name\n- 2. \n- 3. Melee Type\n- 4. Damage\n")
                    if stat_change == "1":
                        new_stat = input("Enter new name: ")
                        weapon.name = new_stat
                        print(weapon.get_stats)

        elif action == "4":
            print("---Changing stats---")
            found = [weapon for weapon in inventory if weapon.name.lower() == search_term.lower()]
            print()
            if found:
                for weapon in found:
                    weapon.get_stats()
                    search = input("Enter weapon name to change stats: ")
                    if weapon == Sword:
                        stat_change = input("Enter stat you want to change: \n- 1. Name\n- 2. \n- 3. Melee Type\n- 4. Damage\n")
                        if stat_change == "1":
                            new_stat = input("Enter new name: ")
                            weapon.name = new_stat
                            print(weapon.get_stats) 
                        if stat_change == "2":
                            new_stat = input("Enter new damage type (e.g., slashing, piercing, etc.): ")
            

        elif action == "5":
            print("\nThank you for using this program.\n")
            break
        else:
            print("\nInvalid input. Please try again.\n")

if __name__ == "__main__":
    main()