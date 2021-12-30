# NUM_PEGS=3  

# def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
#     returnable = [[] for i in range(NUM_PEGS)]
#     returnable[0] = [i for i in reversed(range(num_rings))]
#     if(num_rings == 1):
#         returnable[0] = 0
#         returnable[1] = 1
#     compute_tower_hanoi(num_rings-1)


# pegs = [list(reversed(range(1,7)))] + [[] for _ in range(1,3)]

# print(pegs)