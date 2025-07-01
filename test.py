
    # The input will be a list of integers, each separated by a newline character.
    # The first line of the input will be an integer N (1 <= N <= 100), indicating the number of test cases to follow.
    # Each of the test cases will consist of a line with an integer X (0 < X <= 100), followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).
    # For each test case, calculate the power of four of Yn, excluding when Yn is positive, and print the calculated sum in the output.
    # Note: There should be no output until all the input has been received.
    # Note 2: Do not put blank lines between test cases solutions.
    # Note 3: Take input from standard input, and output to standard output.
    # Note 4: The final output is guaranteed to be within the int32 range.
    # Note 5: It is possible that X and the number of integers Yn may not be equal. If that is the case, print -1 as the output.

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    N = int(data[0])
    index = 1
    results = []
    
    for _ in range(N):
        if index >= len(data):
            results.append("-1")
            continue
        
        X = int(data[index])
        index += 1
        
        if index >= len(data):
            results.append("-1")
            continue
        
        try:
            numbers = list(map(int, data[index].split()))
        except ValueError:
            results.append("-1")
            index += 1
            continue
        
        if len(numbers) != X:
            results.append("-1")
        else:
            total_sum = sum(y ** 4 for y in numbers if y < 0)
            results.append(str(total_sum))
        
        index += 1
    
    print("\n".join(results))
if __name__ == "__main__":
    main()