def create_spiral(number):
    spiral = [[]]
    numbers = list(range(1,(number + 1)))
    cursor_index = 0
    cursor_arr = 0
    for i in numbers:
        if i < 3:
            spiral[0].append(i)
            cursor_index += 1
        else:
            if cursor_index is 0:
                if cursor_arr == len(spiral) - 1 and len(spiral[-1]) == 1:
                    spiral[cursor_arr].append(i)
                    cursor_index += 1
                else:
                    if cursor_arr + 1 >= len(spiral):
                        spiral.append([])
                    if len(spiral[cursor_arr]) <= len(spiral[cursor_arr + 1]):
                        spiral[0].insert(0,i)
                        cursor_arr = 0
                    else:
                        spiral[cursor_arr + 1].insert(0,i)
                        cursor_arr += 1

            else:
                if cursor_arr == 0:
                    spiral.insert(0,[i])
                    cursor_index = 0
                elif len(spiral[cursor_arr]) <= len(spiral[cursor_arr - 1]):
                    spiral[cursor_arr].append(i)
                    cursor_index += 1
                else:
                    spiral[cursor_arr - 1].append(i)
                    cursor_arr -= 1
    return spiral

def walk_spiral(number):
    spiral = create_spiral(number)
    for arr in spiral:
        if number in arr:
            y = spiral.index(arr)
            x = arr.index(number)
        if 1 in arr:
            goal_y = spiral.index(arr)
            goal_x = arr.index(1)

    return (abs(x - goal_x) + abs(y - goal_y))


def create_mod_spiral(number, should_break=False):
    spiral = [[]]
    numbers = list(range(1,(number + 1)))
    cursor_index = 0
    cursor_arr = 0
    for i in numbers:
        if i < 3:
            mod = 1
            spiral[0].append(mod)
            cursor_index += 1
        else:
            if cursor_index is 0:
                if cursor_arr == len(spiral) - 1 and len(spiral[-1]) == 1:
                    mod = spiral[cursor_arr][0] + spiral[cursor_arr - 1][0] + spiral[cursor_arr - 1][1] + spiral[cursor_arr - 1][2]
                    spiral[cursor_arr].append(mod)
                    cursor_index += 1
                else:
                    if cursor_arr + 1 >= len(spiral):
                        spiral.append([])
                    if len(spiral[cursor_arr]) <= len(spiral[cursor_arr + 1]):
                        num = len(spiral[0])
                        mod = spiral[1][-(num)] + spiral[0][cursor_index]
                        if len(spiral[1]) > num:
                            mod += spiral[1][-(num + 1)]
                        if len(spiral[1]) > num + 1:
                            mod += spiral[1][-(num + 2)]
                        spiral[0].insert(0,mod)
                        cursor_arr = 0
                    else:
                        mod = spiral[cursor_arr][0] + spiral[cursor_arr][1]
                        if len(spiral) > cursor_arr + 1 and spiral[cursor_arr + 1]:
                            mod += spiral[cursor_arr + 1][0]
                        if len(spiral) > cursor_arr + 2 and spiral[cursor_arr + 2]:
                            mod += spiral[cursor_arr + 2][0]
                        spiral[cursor_arr + 1].insert(0,mod)
                        cursor_arr += 1

            else:
                if cursor_arr == 0:
                    mod = spiral[cursor_arr][-1] + spiral[cursor_arr][-2]
                    spiral.insert(0,[mod])
                    cursor_index = 0
                elif len(spiral[cursor_arr]) <= len(spiral[cursor_arr - 1]):
                    mod = spiral[cursor_arr][cursor_index] + spiral[cursor_arr - 1][cursor_index]
                    if len(spiral[cursor_arr - 1]) > cursor_index + 1:
                        mod += spiral[cursor_arr - 1][cursor_index + 1]
                    if len(spiral[cursor_arr - 1]) > cursor_index + 2:
                        mod+= spiral[cursor_arr - 1][cursor_index + 2]
                    spiral[cursor_arr].append(mod)
                    cursor_index += 1
                else:
                    if cursor_arr > 1:
                        mod = spiral[cursor_arr][-1] + spiral[cursor_arr][-2] + spiral[cursor_arr - 1][-1] + spiral[cursor_arr - 2][-1]
                    else:
                        mod = spiral[cursor_arr][-1] + spiral[cursor_arr][-2] + spiral[cursor_arr - 1][-1]
                    spiral[cursor_arr - 1].append(mod)
                    cursor_arr -= 1
        if should_break and mod > number:
            return mod
    return spiral
