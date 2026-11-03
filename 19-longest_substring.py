
text = input("Enter a string: ")

seen = set()
left = 0
longest = ""

for right in range(len(text)):
    while text[right] in seen:
        seen.remove(text[left])
        left += 1

    seen.add(text[right])

    if right - left + 1 > len(longest):
        longest = text[left:right + 1]

print("Longest substring:", longest)
print("Length:", len(longest))
