import math
def generate_power_set(S: [int]) -> [[int]]:
    power_set = []
    for i in range(1 << len(S)):
        bit_array = i
        subset = []
        while bit_array:
            subset.append(int(math.log2(bit_array & ~(bit_array - 1))))
            print(i,bit_array,power_set)
            bit_array &= bit_array - 1
            print(bit_array)

        power_set.append(subset)
    return power_set

print(generate_power_set([1,2,8]))