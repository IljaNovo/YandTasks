def move_list(not_shifted_list, shift):
    if shift == 0: return not_shifted_list.copy()
    if shift < 0:  return move_left(not_shifted_list, abs(shift))
    if shift > 0:  return move_right(not_shifted_list, shift)
        
def move_right(not_shifted_list, shift):
    shifted_list = []
    shifted_list.extend(not_shifted_list)
    for i in range(shift):
        temp = shifted_list.pop()
        shifted_list.insert(0, temp)
    return shifted_list

def move_left(not_shifted_list, shift):
    shifted_list = []
    shifted_list.extend(not_shifted_list)
    for i in range(shift):
        temp = shifted_list.pop(0)
        shifted_list.append(temp)
    return shifted_list

shift = -1
initList = [1, 2, 5, 4, 5, 6, 7, 8, 9, 10, 67]
shiftedList = move_list(initList, shift)

if shift == 0:
    print(shiftedList[-1])
if shift < 0:
    print(shiftedList[(len(shiftedList) - 1) - (abs(shift) % len(shiftedList))])
if shift > 0:
    print(shiftedList[(shift + len(shiftedList) - 1) % len(shiftedList)])
