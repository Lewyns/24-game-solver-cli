from fractions import Fraction
from rich.console import Console
from rich.panel import Panel

console = Console()


def solve_24(numbers):
    items = [(Fraction(n), str(n)) for n in numbers]

    def search(items):
        if len(items) == 1:
            value, expr = items[0]
            if value == 24:
                return expr
            return None

        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                a_value, a_expr = items[i]
                b_value, b_expr = items[j]

                rest = [
                    items[k]
                    for k in range(len(items))
                    if k != i and k != j
                ]

                candidates = [
                    (a_value + b_value, f"({a_expr} + {b_expr})"),
                    (a_value - b_value, f"({a_expr} - {b_expr})"),
                    (b_value - a_value, f"({b_expr} - {a_expr})"),
                    (a_value * b_value, f"({a_expr} * {b_expr})"),
                ]

                if b_value != 0:
                    candidates.append(
                        (a_value / b_value, f"({a_expr} / {b_expr})")
                    )

                if a_value != 0:
                    candidates.append(
                        (b_value / a_value, f"({b_expr} / {a_expr})")
                    )

                for new_value, new_expr in candidates:
                    result = search(rest + [(new_value, new_expr)])
                    if result:
                        return result

        return None

    return search(items)


def main():
    console.print(
        Panel.fit(
            "[bold yellow]24 Game Solver[/bold yellow]\n"
            "[cyan]Enter 4 numbers and I will find a solution![/cyan]",
            border_style="bright_magenta"
        )
    )

    while True:
        user_input = console.input(
            "\n[bold cyan]Enter your number here! ⭐ : [/bold cyan]"
        )

        if user_input.lower() in ["exit", "quit"]:
            console.print("[bold red]Goodbye![/bold red]")
            break

        try:
            numbers = list(map(int, user_input.split()))

            if len(numbers) != 4:
                console.print("[bold red]Please enter exactly 4 numbers.[/bold red]")
                continue

            solution = solve_24(numbers)

            if solution:
                console.print(
                    f"\n[bold green]Your solution is[/bold green] "
                    f"[bold yellow]{solution} = 24[/bold yellow]"
                )
            else:
                console.print(
                    "\n[bold red]No solution found for these numbers.[/bold red]"
                )

        except ValueError:
            console.print("[bold red]Please enter numbers only.[/bold red]")


if __name__ == "__main__":
    main()