class Solution:
    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        rows = len(is_water)
        columns = len(is_water[0])
        INF = rows * columns  # Large value to represent uninitialized heights

        # Initialize the cellHeights matrix with INF (unprocessed cells)
        cell_heights = [[INF] * columns for _ in range(rows)]

        # Set the height of water cells to 0
        for row in range(rows):
            for col in range(columns):
                if is_water[row][col] == 1:
                    cell_heights[row][col] = 0  # Water cells have height 0

        # Forward pass: updating heights based on top and left neighbors
        for row in range(rows):
            for col in range(columns):
                # Initialize minimum neighbor distance
                min_neighbor_distance = INF

                # Check the cell above
                neighbor_row = row - 1
                neighbor_col = col
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                # Check the cell to the left
                neighbor_row = row
                neighbor_col = col - 1
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                # Set the current cell's height as the minimum of its neighbors + 1
                cell_heights[row][col] = min(
                    cell_heights[row][col], min_neighbor_distance + 1
                )

        # Backward pass: updating heights based on bottom and right neighbors
        for row in range(rows - 1, -1, -1):
            for col in range(columns - 1, -1, -1):
                # Initialize minimum neighbor distance
                min_neighbor_distance = INF

                # Check the cell below
                neighbor_row = row + 1
                neighbor_col = col
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                # Check the cell to the right
                neighbor_row = row
                neighbor_col = col + 1
                if self.is_valid_cell(
                    neighbor_row, neighbor_col, rows, columns
                ):
                    min_neighbor_distance = min(
                        min_neighbor_distance,
                        cell_heights[neighbor_row][neighbor_col],
                    )

                # Set the current cell's height as the minimum of its neighbors + 1
                cell_heights[row][col] = min(
                    cell_heights[row][col], min_neighbor_distance + 1
                )

        return cell_heights  # Return the calculated cell heights

    # Function to check if a cell is within grid bounds
    def is_valid_cell(
        self, row: int, col: int, rows: int, columns: int
    ) -> bool:
        return 0 <= row < rows and 0 <= col < columns 