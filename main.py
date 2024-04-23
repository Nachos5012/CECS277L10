# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 04/16/2024
# Module 10 - Factory method
# Purpose - To create a factory method to create a hero object.
import check_input
import hero
import beg_factory
import exp_factory


def main():
  """Main function to run the Monster Trials game."""
  print("Monster Trials")
  player_name = input("What is your name? ").strip()
  h = hero.Hero(player_name)
  begfactory = beg_factory.BeginnerFactory()
  expfactory = exp_factory.ExpertFactory()
  monsters = []

  print(
      f"\nYou will face a series of 3 monsters, {player_name}. \nDefeat them all to win."
  )

  # Generating 2 beginner monsters and 1 expert monster
  for _ in range(2):
    monsters.append(begfactory.create_random_enemy())
  monsters.append(expfactory.create_random_enemy())

  while True:
    print("\nChoose an enemy to attack:")
    for i, monster in enumerate(monsters, start=1):
      print(f"{i}. {monster}")
    choice = check_input.get_int_range("Enter choice: ", 1, len(monsters))
    selected_enemy = monsters[choice - 1]

    print(f"\n{h}")
    print("1. Sword Attack")
    print("2. Arrow Attack")
    attack_choice = check_input.get_int_range("Enter choice: ", 1, 2)
    print()
    if attack_choice == 1:
      print(h.melee_attack(selected_enemy))
    else:
      print(h.ranged_attack(selected_enemy))

    if selected_enemy._hp <= 0:
      print(f"You have slain the {selected_enemy._name}")
      monsters.remove(selected_enemy)
      if not monsters:
        print("\nCongratulations! You defeated all three monsters!")
        break
    else:
      print(selected_enemy.melee_attack(h))
    if h._hp <= 0:
      print("\nYou have been defeated!")
      break

  print("Game Over")


main()
