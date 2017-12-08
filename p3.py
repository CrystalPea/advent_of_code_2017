def create_spiral(number):
    spiral = [[]]
    i = 1
    while i <= number:
        if i < 3:
            spiral[0].append(i)
        else:
            for arr in spiral:
                if (i - 1) in arr:
                    cursor_index = arr.index(i - 1)
                    cursor_arr = spiral.index(arr)
            if cursor_index is 0:
                if cursor_arr == len(spiral) - 1 and len(spiral[-1]) == 1:
                    spiral[cursor_arr].append(i)
                else:
                    if cursor_arr + 1 >= len(spiral):
                        spiral.append([])
                    if len(spiral[cursor_arr]) <= len(spiral[cursor_arr + 1]):
                        spiral[0].insert(0,i)
                    else:
                        spiral[cursor_arr + 1].insert(0,i)

            else:
                if cursor_arr == 0:
                    spiral.insert(0,[i])
                elif len(spiral[cursor_arr]) <= len(spiral[cursor_arr - 1]):
                    spiral[cursor_arr].append(i)
                else:
                    spiral[cursor_arr - 1].append(i)
        i+= 1
    return spiral
