def average(array):
    # your code goes here
    plant_heights = set(array)
    if len(plant_heights) > 0 and len(plant_heights) < 101:
        return sum(plant_heights) / len(plant_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)