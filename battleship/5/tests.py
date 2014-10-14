import unittest
import battleship

class BattleShipTests(unittest.TestCase):

    def setUp(self):
        self.grid = battleship.Grid()

    def test_is_empty_at(self):
        self.assertTrue(self.grid.is_empty_at())
        self.grid.squares[1][1] = '*'
        self.assertFalse(self.grid.is_empty_at())

if __name__ == '__main__':
    unittest.main()
