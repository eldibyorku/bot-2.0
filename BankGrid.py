import numpy as np
import pytesseract
from PIL import Image
import time
import csv

class BankGrid:
    def __init__(self, top_left, bottom_right, rows, columns):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.rows = rows
        self.columns = columns
        self.grid = np.zeros((rows, columns), dtype=int)  # Assuming default item count is 0
        self.cell_width = (bottom_right[0] - top_left[0]) / columns
        self.cell_height = (bottom_right[1] - top_left[1]) / rows

    def set_item_count(self, row, col, count):
        self.grid[row, col] = count

    def get_item_count(self, row, col):
        return self.grid[row, col]

    def get_cell_center(self, row, col):
        center_x = self.top_left[0] + (col + 0.5) * self.cell_width
        center_y = self.top_left[1] + (row + 0.5) * self.cell_height
        return (int(center_x), int(center_y))



    def display_grid(self):
        for row in range(self.rows):
            for col in range(self.columns):
                # Get the item count for the current cell
                count = self.get_item_count(row, col)
                # Print the item count, formatted to be right-aligned within 5 spaces
                print(f"{count:>5}", end=" ")
            # After printing all columns in a row, print a newline character to move to the next line
            print()

    def load_from_csv(self, file_name):
        with open(file_name, 'r', newline='') as csvfile:
            grid_reader = csv.reader(csvfile)
            for row_idx, row in enumerate(grid_reader):
                for col_idx, count in enumerate(row):
                    self.set_item_count(row_idx, col_idx, int(count))

    def withdraw(self, row, col, stack_size=20):
        avail = self.get_item_count(row, col)
        if avail >= 20:
            avail = avail -20
            self.set_item_count(row, col, avail)
            return 20
        elif avail > 0:
            self.set_item_count(row,col, 0)
            return avail
        else:
            return 0