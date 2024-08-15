import sys

def main():
    input = sys.stdin.readline
    test_cases = int(input())
    for _ in range(test_cases):
        rows, cols = map(int, input().split())
        grid = [input().strip() for _ in range(rows)]
        max_col_pos = 0
        max_row_pos = 0
        max_count = 0
        for row in range(1, rows + 1):
            hash_count = 0
            start_col = 0
            for col in range(1, cols + 1):
                if grid[row - 1][col - 1] == '#':
                    hash_count += 1
                    if start_col == 0:
                        start_col = col
            mid_col_pos = start_col + hash_count // 2
            if max_count < hash_count:
                max_col_pos = mid_col_pos
                max_count = hash_count
                max_row_pos = row
        print(max_row_pos, max_col_pos)

if __name__ == "__main__":
    main()
