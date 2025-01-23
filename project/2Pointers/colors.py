colors = [2,1,1,0,0]


def swap(colors, i , j):
    temp = colors[i]
    colors[i] = colors[j]
    colors[j] = temp


def sortcolors(colors):
    i, j, k = 0, 0, len(colors) - 1  # Initialize pointers
    while j <= k:
        if colors[j] == 0:
            swap(colors, i, j)
            i += 1
            j += 1
        elif colors[j] == 1:
            j += 1
        else:  # colors[j] == 2
            swap(colors, j, k)
            k -= 1
    print(colors)

sortcolors(colors)


