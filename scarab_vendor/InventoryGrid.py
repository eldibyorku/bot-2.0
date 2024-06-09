import numpy as np

class InventoryGrid:
    def __init__(self, top_left, bottom_right, rows, columns, empty_cell_color):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.rows = rows
        self.columns = columns
        self.empty_cell_color = empty_cell_color
        self.cell_width = (bottom_right[0] - top_left[0]) / columns
        self.cell_height = (bottom_right[1] - top_left[1]) / rows
        self.cells = np.full((rows, columns), True)  # Assuming all cells are empty initially

    def is_cell_empty(self, row, col, img_data):
        center_x = self.top_left[0] + (col + 0.5) * self.cell_width
        center_y = self.top_left[1] + (row + 0.5) * self.cell_height
        return img_data[int(center_y), int(center_x)] == self.empty_cell_color

    def get_cell_center(self, row, col):
        center_x = self.top_left[0] + (col + 0.5) * self.cell_width
        center_y = self.top_left[1] + (row + 0.5) * self.cell_height
        return (int(center_x), int(center_y))
