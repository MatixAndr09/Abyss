from rich import console

cmd = console.Console()

while True:
    cli = cmd.input("Abyss $> ")
    if cli == "help":
        cmd.print("Commands:\n\n[magenta bold]help[/] - Shows this message\n[magenta bold]exit[/] - Exits the program")
    elif cli == "exit":
        break
    else:
        cmd.print("[red bold](ERR)[/]  Command not found!")