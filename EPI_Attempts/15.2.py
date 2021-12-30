def n_queens(n: int):
    def solve_n_queens(row):
        if row == n:
            result.append(list(col_placement))
            print("??????????????????????????????????????????????????")
            print("Append!!!!!!!!!!!!")
            print("??????????????????????????????????????????????????")
            return
        for col in range(n):
            for i, c in enumerate(col_placement[:row]):
                print("c: ",c)
                print("col: ",col)
                print("abs(c-col): ",abs(c-col))
                print("i: ",i)
                print("row: ",row)
                print("row-i: ",row-i)
                print("enumerate(col_placement[:row]) : ",list(enumerate(col_placement[:row])))
                print("abs(c-col) not in (0,row-i): " ,abs(c-col) not in (0,row-i))
                print("-----------------------------------------------------")
            if all(
                abs(c-col) not in (0,row-i)
                for i, c in enumerate(col_placement[:row])):
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("row: ",row)
                    print("col: ",col)
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    col_placement[row] = col
                    solve_n_queens(row + 1)

    result, col_placement = [],[0]*n
    solve_n_queens(0)
    return result

print(n_queens(4))

a = [1,2,3,4]

def n_queens(n: int):
    def solve_n_queens(row):
        if row == n:
            result.append(list(col_placement))
            return
        for col in range(n):
            if all(
                ##for next line the 0 is for same column and row-i is same diagonal
                abs(c-col) not in (0,row-i)
                for i, c in enumerate(col_placement[:row])):
                    col_placement[row] = col
                    solve_n_queens(row + 1)

    result, col_placement = [],[0]*n
    solve_n_queens(0)
    return result