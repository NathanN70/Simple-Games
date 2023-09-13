# monopoly board to use.
# each tile is 1 append to the board.
# components of each tile are, in order: id, name, buy price, prices, and house prices. As needed
# location id based on code system. Letter, then Number. Normal props, Letters A-H each represent a district. The number (1-3) represents different props in the district
# for free spaces, letter X, number system same
# for rails and utility, letters R and U (rails number 1-4)
# for chest and chance, letters Y and Z
board = [
    ["X1", "Go"],
    ["A1", "Mediterranean Avenue", 60, [2, 10, 30, 90, 160, 250], 50],
    ["Y1", "Community Chest"],
    ["A2", "Baltic Avenue", 60, [4, 20, 60, 180, 320, 450], 50],
    # add more
]