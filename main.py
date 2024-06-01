import os
from rich import console

cmd = console.Console()


def print_gradient(text, start_color, end_color, steps=10):
    for i in range(len(text)):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / (len(text) - 1))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / (len(text) - 1))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / (len(text) - 1))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(f"{color_code}{text[i]}\033[0m", end="")


print("\n")
print_gradient("Abyss [Version 0.2]\n(C) MatixAndr09. All rights reserved.\n", (84, 0, 84), (191, 65, 147))
print("\n")
while True:
    working_dir = os.getcwd()
    cli = cmd.input(f"[white dim]{working_dir}[/] >>> ")
    if cli == "help":
        cmd.print("Commands:\n\n[magenta bold]help[/] - Shows this message\n[magenta bold]exit[/] - Exits the program")
    elif cli == "exit":
        break
    else:
        cmd.print("[red bold](ERR)[/]  Command not found!")
