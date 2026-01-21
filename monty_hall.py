# Paradoja de Monty Hall (c) 2025 Baltasar MIT License <baltasarq@gmail.com>


import random as rnd
import sys
import argparse
import matplotlib.pyplot as plt


def generate_random_list_door_pairs(max, num_doors=3):
    """Generates a random list of pairs, from 1 to num_doors,
        being the first value the door with the prize,
        and the second value the door chosen.
        :param max: the maximum number of pairs.
        :num_doors: number of doors, normally 3.
        :return: a random list of pairs (prize, chosen).
    """
    toret = []
    for _ in range(max):
        toret.append(
                tuple([rnd.randint(1, num_doors),
                        rnd.randint(1, num_doors)]))
    ...

    return toret
...


def extract_coincidences(l_pairs):
    """Extracts from a list of pairs, those with equal values.
        :param l_pairs: a list of pairs.
        :return: a list of pairs with equal both values.
    """
    return [pair for pair in l_pairs if pair[0] == pair[1]]
...


def create_selection_changed(num_doors=3):
    """Creates one pair (prize, chosen), after changing the initial choice.
        :param ndoors: the number of doors.
    """
    # Initial choice
    doors = list(range(1, num_doors + 1))
    treasure_door = rnd.choice(doors)
    chosen_door = rnd.choice(doors)
    
    # One door not containing the treasure is revealed
    # Also it won't be the selected door
    door_revealed = set(doors)
    door_revealed.discard(treasure_door)
    door_revealed.discard(chosen_door)
    revealed_door = rnd.choice(list(door_revealed))
    
    # Change your chosen door
    available_doors = set(doors)
    available_doors.discard(chosen_door)
    available_doors.discard(revealed_door)
    chosen_door2 = available_doors.pop()
    
    return tuple([treasure_door, chosen_door2])
...


def generate_random_list_door_pairs_after_change(max, num_doors=3):
    """Creates a list of pairs (prize, chosen) of max elements.
        This takes into account the choice change strategy.
        :param max: the number of elements in the list.
        :param num_doors: the number of doors.
    """
    selections_changed = []
    
    for _ in range(max):
        selections_changed.append(create_selection_changed(num_doors))
    ...
    
    return selections_changed
...


def print_to(f, l_pairs):
    """Textually shows the pairs (prize, chosen) generated.
        :param f: the file to dump the text to.
        :l_pairs: a list of pairs.
    """
    print("0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1", file=f)
    print("1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0", file=f)
    print("-------------------------------------")
    print(
            str.join(" | ", [str(x) for x in
                                [pair[0] for pair in l_pairs]]),
            file=f)
    print(
            str.join(" | ", [str(x) for x in
                                [pair[1] for pair in l_pairs]]),
            file=f)
    print("-------------------------------------", file=f)
    num_correct = len(extract_coincidences(l_pairs))
    total = len(l_pairs)
    percentage = (num_correct / total) * 100
    print(f"Correct: {num_correct}/{total} ({percentage:5.2f}%)\n", file=f)
...


def show_graph(percentage_correct, msg_explain):
    """Shows a graph using pyplot.
        :param percentage_correct: a percentage between 0 and 100,
                            or a list of percentages.
        :param msg_explain: an explaining message, or a list of messages.
    """
    if not isinstance(percentage_correct, list):
        percentage_correct = [percentage_correct]
    ...
    
    if not isinstance(msg_explain, list):
        msg_explain = [msg_explain]
    ...
    
    plt.bar(
        msg_explain,
        percentage_correct,
        color=["blue", "green"])

    plt.yticks(range(0, 101, 10))
    plt.title("Monty Hall paradox")
    plt.ylabel("Percentage (0-100%)")
    plt.show()
...


if __name__ == "__main__":
    rnd.seed()

    parser = argparse.ArgumentParser(
                    prog='pyhall',
                    description='The Monty Hall Paradox')
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-enoc", "--evaluate-no-change", action="store_true")
    parser.add_argument("-ec", "--evaluate-change", action="store_true")
    args = vars(parser.parse_args())
    max = 100000

    if args.get("verbose"):
        max = 10
    ...
    
    generated_pairs = []
    generated_pairs1 = []
    msg = ""
    msg1 = ""
    
    if args.get("evaluate_no_change"):
        generated_pairs1 = generate_random_list_door_pairs(max)
        msg1 = "correct selections (no door change)"
    ...
    
    if args.get("evaluate_change"):
        generated_pairs = generate_random_list_door_pairs_after_change(max)
        msg = "correct selections (door changed)"
    else:
        generated_pairs = generated_pairs1
        generated_pairs1 = []
        msg = msg1
    ...
    
    if (generated_pairs1 != []
    and generated_pairs != []):
        correct_pairs1 = extract_coincidences(generated_pairs1)
        correct_pairs2 = extract_coincidences(generated_pairs)
        num_correct1 = len(correct_pairs1)
        num_correct2 = len(correct_pairs2)
        percentage1 = (num_correct1 / max) * 100
        percentage2 = (num_correct2 / max) * 100
        
        if max < 40:
            print_to(sys.stdout, generated_pairs1)
            print_to(sys.stdout, generated_pairs)
        ...
        
        show_graph([percentage1, percentage2],
                   [f"{msg1}: {percentage1: 5.2f}%",
                    f"{msg}: {percentage2: 5.2f}%"])
    elif generated_pairs != []:
        correct_pairs = extract_coincidences(generated_pairs)
        num_correct = len(correct_pairs)
        percentage = (num_correct / max) * 100
        
        if max < 40:
            print_to(sys.stdout, generated_pairs)
        ...
        
        show_graph(percentage,
                    f"{msg}: {percentage: 5.2f}%")
    else:
        parser.print_help()
    ...
...
