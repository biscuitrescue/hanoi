#!/usr/bin/env python3

# GITHUB: https://github.com/biscuitrescue/hanoi

import time

num_disks = int(input("Enter Number of Disks: "))
count = 0
towers = {"A": list(range(num_disks, 0, -1)), "B": [], "C": []}


def draw_towers():
    global count
    print("\nIteration:", count)
    count += 1

    for i in range(num_disks - 1, -1, -1):
        row_str = ""
        for name in ["A", "B", "C"]:
            tower = towers[name]
            if i < len(tower):
                row_str += f" [{tower[i]}]  "
            else:
                row_str += " | |  "
        print(row_str)
    print("===== ===== =====")
    print("  A     B     C  ")
    time.sleep(1)


def check_move(peg1, peg2):
    # if 1 peg is empty, move first disk of occupied peg to empty peg
    # if both pegs occupied, move smaller top disk to peg with larger top disk
    if not towers[peg1]:
        disk = towers[peg2].pop()
        towers[peg1].append(disk)
    elif not towers[peg2]:
        disk = towers[peg1].pop()
        towers[peg2].append(disk)
    elif towers[peg1][-1] < towers[peg2][-1]:
        disk = towers[peg1].pop()
        towers[peg2].append(disk)
    else:
        disk = towers[peg2].pop()
        towers[peg1].append(disk)


def hanoi():
    total_moves = (2**num_disks) - 1  # Runs 2^n - 1 times

    # determines rotation direction for odd and even number of disks
    if num_disks % 2 == 0:
        mv_pairs = [("A", "B"), ("A", "C"), ("B", "C")]
    else:
        mv_pairs = [("A", "C"), ("A", "B"), ("B", "C")]

    draw_towers()

    # loop drives all moves

    # I chose iteration over recursion to avoid the stack frame overhead and recursion depth limit
    for mv_num in range(1, total_moves + 1):
        pair_idx = (
            mv_num - 1
        ) % 3  # so that we always cycle pegs in the 3 towers. The number of pegs is inconsequential
        peg1, peg2 = mv_pairs[pair_idx]

        check_move(peg1, peg2)
        draw_towers()


if __name__ == "__main__":
    hanoi()
