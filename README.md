# 24 Game Solver CLI

A simple Python command-line application that solves the classic 24 Game.  
The program takes 4 numbers as input and finds a mathematical expression that equals 24.

## Features

- Solve the 24 Game using 4 input numbers
- Supports addition, subtraction, multiplication, and division
- Uses exact fraction calculation to avoid floating-point errors
- Colorful terminal interface using Rich
- Allows repeated input until the user exits

## Example

### Input

```bash
Enter your number here! ⭐ : 4 4 6 0
```

### Output

```bash
Your solution is (4 * (6 + 0)) = 24
```

If no solution is found, the program will display:

```bash
No solution found for these numbers.
```

## Installation

Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/24-game-solver-cli.git
cd 24-game-solver-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python main.py
```

Then enter 4 numbers separated by spaces:

```bash
4 4 6 0
```

To exit the program, type:

```bash
exit
```

or

```bash
quit
```

## How It Works

The program tries every possible combination of the 4 numbers with basic arithmetic operators:

- Addition
- Subtraction
- Multiplication
- Division

It recursively combines numbers until only one result remains.  
If the result equals 24, the program returns the expression.

## Requirements

- Python 3.8+
- Rich

## Project Structure

```text
24-game-solver-cli/
│
├── main.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## License

This project is licensed under the MIT License.
