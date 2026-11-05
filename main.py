from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemies = [
        Character("Goblin", 20, 3),
        Character("Orc", 20, 3),
    ]

    print(hero)
    for enemy in enemies:
        print(enemy)
    print()

    while hero.is_alive() and (
        enemies[0].is_alive() or enemies[1].is_alive()
    ):
        for enemy in enemies:
            if not enemy.is_alive():
                continue
            hero.attack(enemy)
            if enemy.is_alive():
                enemy.attack(hero)
            if not hero.is_alive():
                break
        print(hero)
        for enemy in enemies:
            print(enemy)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("Enemies win!")

if __name__ == "__main__":
    main()
