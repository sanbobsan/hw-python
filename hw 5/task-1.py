with open("INPUT.txt", "r") as f:
    n = int(f.readline().strip())
    lines = [f.readline().strip() for _ in range(n)]

phrase = "the quick brown fox jumps over the lazy dog"
lengths = [3, 5, 5, 3, 5, 4, 3, 4, 3]
success = False

for line in lines:
    # skip by len
    if len(line) != 43:
        continue

    # skip by amount of words
    words = line.split()
    if len(words) != 9:
        continue

    # skip by len of words
    invalid = False
    for i in range(9):
        if len(words[i]) != lengths[i]:
            invalid = True
            break
    if invalid:
        continue

    # creating cypher
    cypher = {}
    invalid = False

    for i in range(43):
        if line[i] == " ":
            continue

        encrypted_letter = line[i]
        letter = phrase[i]

        if encrypted_letter in cypher:
            if cypher[encrypted_letter] != letter:
                invalid = False
                break
        else:
            cypher[encrypted_letter] = letter

    if not invalid and len(cypher) == 26:
        success = True
        break


if success:
    with open("OUTPUT.TXT", "w") as f:
        for line in lines:
            decrypted = []
            for letter in line:
                if letter == " ":
                    decrypted.append(" ")
                else:
                    decrypted.append(cypher[letter])
            f.write("".join(decrypted) + "\n")

else:
    with open("OUTPUT.TXT", "w") as f:
        f.write("No solution")
