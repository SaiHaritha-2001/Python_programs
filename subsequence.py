string = input()
subsequence = input()
subsequence_index = 0
subsequence_length = len(subsequence)

for char in string:
    if subsequence_index < subsequence_length and char == subsequence[subsequence_index]:
        subsequence_index += 1
    if subsequence_index == subsequence_length:
        break

if subsequence_index == subsequence_length:
    print("yes")
else:
    print("no")

        
