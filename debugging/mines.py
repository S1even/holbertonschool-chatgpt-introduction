#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_cells = width * height - mines
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.non_mine_cells_revealed = 0

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        if not self.revealed[y][x]:
            self.revealed[y][x] = True
            self.non_mine_cells_revealed += 1
            if self.non_mine_cells_revealed == self.total_cells:
                return True
            if self.count_mines_nearby(x, y) == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Entrez la coordonnée x : "))
                y = int(input("Entrez la coordonnée y : "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! Vous avez touché une mine.")
                    break
                elif self.non_mine_cells_revealed == self.total_cells:
                    self.print_board(reveal=True)
                    print("Félicitations! Vous avez gagné!")
                    break
            except ValueError:
                print("Entrée invalide. Veuillez entrer des nombres uniquement.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
