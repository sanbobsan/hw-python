def group_roles(roles, textLines):
    role_lines = {}

    for i, line in enumerate(textLines, 1):
        if ":" not in line:
            continue
        role, text = line.split(":", 1)
        text = text.lstrip()
        if role not in role_lines:
            role_lines[role] = []
        role_lines[role].append((i, text))

    result = []
    for idx, role in enumerate(roles):
        result.append(role + ":")
        if role in role_lines:
            for num, txt in role_lines[role]:
                result.append(f"{num}) {txt}")
        if idx < len(roles) - 1:
            result.append("")

    return "\n".join(result)


def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines if line.strip()]  # Игнорируем пустые строки
    roles_start = None
    textLines_start = None
    for idx, line in enumerate(lines):
        if line == "roles:":
            roles_start = idx + 1
        elif line == "textLines:":
            textLines_start = idx + 1
            break

    roles = []
    if roles_start is not None and textLines_start is not None:
        for i in range(roles_start, textLines_start - 1):
            roles.append(lines[i])

    textLines = []
    if textLines_start is not None:
        textLines = lines[textLines_start:]

    output = group_roles(roles, textLines)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(output)

    print("Файл output.txt записан")


if __name__ == "__main__":
    main()
