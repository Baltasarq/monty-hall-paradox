# Paradoja de Monty Hall (c) 2023 Baltasar MIT License <baltasarq@gmail.com>


import pandas as pd
import random as rnd
import matplotlib.pyplot as plt


def build_episode(ndoors):
    # Initial choice
    doors = list(range(1, ndoors + 1))
    treasure_door = rnd.choice(doors)
    chosen_door = rnd.choice(doors)

    # One door not containing the treasure is revealed
    doors_without_treasure = list(doors)
    doors_without_treasure.remove(treasure_door)
    revealed_door = rnd.choice(doors_without_treasure)

    # Change your chosen door
    doors_without_revealed = list(doors)
    doors_without_revealed.remove(revealed_door)

    if chosen_door != revealed_door:
        doors_without_revealed.remove(chosen_door)

    chosen_door2 = rnd.choice(doors_without_revealed)

    return {
                "num_doors": ndoors,
                "treasure_door": treasure_door,
                "chosen_door": chosen_door,
                "revealed_door": revealed_door,
                "chosen_door2": chosen_door2
    }


def build_episodes(nepisodes, ndoors):
    toret = []

    for _ in range(nepisodes):
        toret.append(build_episode(ndoors))

    return toret


def print_episodes(episodes):
    for episode in episodes:
        print(f"doors: {episode['num_doors']}, treasure at #{episode['treasure_door']}"
                + f" chosen_door #{episode['chosen_door']} revealed_door #{episode['revealed_door']}"
                + f" 2nd. chosen door #{episode['chosen_door2']}")


if __name__ == "__main__":
    rnd.seed()
    num_doors = 3
    num_episodes = 1000
    data = build_episodes(num_episodes, num_doors)
    df = pd.DataFrame(data)

    # Find the number of items when changing the choice was wrong
    bad_snd_choice_df = df.apply(lambda r: r.chosen_door == r.treasure_door and r.chosen_door2 != r.treasure_door, axis=1)
    num_bad_snd_choice_df = len(bad_snd_choice_df[bad_snd_choice_df == True].index)
    percent_bad_snd = num_bad_snd_choice_df / num_episodes * 100
    print(f"Times when changing choice was wrong: {num_bad_snd_choice_df} - {percent_bad_snd: 5.2f}%")

    # Find the number of items when changing the choice was correct
    good_snd_choice_df = df.apply(lambda r: r.chosen_door != r.treasure_door and r.chosen_door2 == r.treasure_door, axis=1)
    num_good_snd_choice_df = len(good_snd_choice_df[good_snd_choice_df == True].index)
    percent_good_snd = num_good_snd_choice_df / num_episodes * 100
    print(f"Times when changing choice was correct: {num_good_snd_choice_df} - {percent_good_snd:5.2f}%")

    print(f"Improvement: {percent_bad_snd / percent_good_snd * 100: 5.2f}%")

    plt.bar(
        ["aciertos sin cambiar de puerta",
         "aciertos cambiando de puerta"],
        [percent_bad_snd,
         percent_good_snd],
        color=["green", "red"])

    plt.yticks(range(0, 101, 10))
    plt.title("Monty Hall paradox")
    plt.ylabel("Percentage (0-100%)")
    plt.show()
