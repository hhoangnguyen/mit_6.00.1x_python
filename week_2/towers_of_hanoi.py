def print_move(fr, to):
    print('Move from ' + str(fr) + ' to ' + str(to))


def towers_of_hanoi(n, current_peg, target_peg, spare_peg):
    # base case: stack of size 1, just move to target_peg
    if n == 1:
        print_move(current_peg, target_peg)
    else:
        # move smaller, (n-1) stack from current_peg to spare_peg
        towers_of_hanoi(n-1, current_peg, spare_peg, target_peg)

        # move last item from current_peg to target_peg
        towers_of_hanoi(1, current_peg, target_peg, spare_peg)

        # move smaller, (n-1) stack from spare_peg to target_peg
        towers_of_hanoi(n-1, spare_peg, target_peg, current_peg)

print(towers_of_hanoi(3, 'P1', 'P2', 'P3'))
