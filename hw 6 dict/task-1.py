pass
n = int(input())
pass
result = {}
for _ in range(n):
    line = input().strip()
    eng, latin_str = line.split(" - ")
    pass
    latins = [lw.strip() for lw in latin_str.split(',')]
    for lw in latins:
        if lw not in result:
            result[lw] = []
            pass
        if eng.strip() not in result[lw]:
            result[lw].append(eng)
            pass
pass
keys = sorted(result.keys())
pass
print(len(result))
for key in keys:
    print(f"{key} - {', '.join(result[key])}")
    pass