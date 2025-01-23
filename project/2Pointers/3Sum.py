sample = [-1,2,1,-4,5,-3]
target = -8

sortedsample = sorted(sample)

def threesummoreoptimized(sample, target):
    for i in range(0, len(sample)-2):
        left = i +1
        right = len(sample) -1
        while left < right:
            if sample[i] + sample[left] + sample[right] == target:
                print(True)
            if sample[i] + sample[left] + sample[right] < target:
                left += 1
            else:
                right -= 1
threesummoreoptimized(sortedsample, target)






