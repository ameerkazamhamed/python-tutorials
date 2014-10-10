class Grid():
    '''Three dimensional game grid matrix for use in text or graphic games
    (chess, battleship, connect4, etc.)'''

    col_labels = list('123456789')
    x_labels = col_labels
    row_labels = list('abcdefghijklmnopqrstuvwxyz'.upper())
    y_labels = row_labels

    def __init__(self,cols=10,rows=10,depth=10,char='~',size=None):
        self.coord = [[[]]]
        if size:
            rows = size
            cols = size
            depth = size
        self.size_x = cols
        self.size_y = rows
        self.size_z = depth
        self._build_yxz()

    def _build_yxz(self):
        for y in range(self.size_y+1):
            for x in range(self.size_y+1):

        


    def print(self,labels=True,rlabels=False,clabels=False,space=' ',depth=-1):
        '''Prints the grid in 2D showing the top-most item at that location.'''

        # TODO change these to detect the longest label length
        row_label_size = len(self.row_labels[0])
        col_labels_size = len(self.col_labels[0])


        '''
        # print the column labels, if any, account for size of row labels
        if labels or clabels:
            if labels or rlabels:
                print(' ' * row_label_size, end=space)
            for index in range(len(self.cols[0])):
                if index >= len(self.col_labels): break
                col_label = self.col_labels[index]
                print(col_label, end=space)
            print()
        '''

class Tile():
    pass

if __name__ == '__main__':
    grid = Grid(size=2)
    '''
    grid.rows[3][5][2] = '*'
    print(grid.rows[3][5][2])
    print(grid.cols[3][5][2])
    print(grid.coord[5][3][2])
    '''

