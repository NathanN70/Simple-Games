# monopoly board to use.
# each tile is 1 append to the board.
# components of each tile are, in order: id, name, buy price, prices, and house prices. As needed
# location id based on code system. Letter, then Number. Normal props, Letters A-H each represent a district. The number (1-3) represents different props in the district
# for free spaces, letter X, number system same
# for rails and utility, letters R and U (rails number 1-4)
# for chest and chance, letters Y and Z
# for tax, letter T
# for go to jail, letter J
board = [
    ["X1", "Go"],
    ["A1", "Mediterranean Avenue", 60, [2, 10, 30, 90, 160, 250], 50],
    ["Y1", "Community Chest"],
    ["A2", "Baltic Avenue", 60, [4, 20, 60, 180, 320, 450], 50],
    ["T1", "Income Tax", 200],
    ["R1", "Reading Railroad", 200, [25, 50, 100, 200]],
    ["B1", "Oriental Avenue", 100, [6, 30, 90, 270, 400, 550], 50],
    ["Z1", "Chance"],
    ["B2", "Vermont Avenue", 100, [6, 30, 90, 270, 400, 550], 50],
    ["B3", "Connecticut Avenue", 120, [8, 40, 100, 300, 450, 600], 50],
    ["X2", "Jail"],
    ["C1", "St. Charles Place", 140, [10, 50, 150, 450, 625, 750], 100],
    ["U1", "Electric Company", 150, [4, 10]],
    ["C2", "States Avenue", 140, [10, 50, 150, 450, 625, 750], 100],
    ["C3", "Virginia Avenue", 160, [12, 60, 180, 500, 700, 900], 100],
    ["R2", "Pennsylvania Railroad", 200, [25, 50, 100, 200]],
    ["D1", "St. James Place", 180, [14, 70, 200, 550, 750, 950], 100],
    ["Y2", "Community Chest"],
    ["D2", "Tennessee Avenue", 180, [14, 70, 200, 550, 750, 950], 100],
    ["D3", "New York Avenue", 200, [16, 80, 220, 600, 800, 1000], 100],
    ["X3", "Free Parking"],
    ["E1", "Kentucky Avenue", 220, [18, 90, 250, 700, 875, 1050], 150],
    ["Z2", "Chance"],
    ["E2", "Indiana Avenue", 220, [18, 90, 250, 700, 875, 1050], 150],
    ["E3", "Illinois Avenue", 240, [20, 100, 300, 750, 925, 1100], 150],
    ["R3", "B. & O. Railroad", 200, [25, 50, 100, 200]],
    ["F1", "Atlantic Avenue", 260, [22, 110, 330, 800, 975, 1150], 150],
    ["F2", "Ventnor Avenue", 260, [22, 110, 330, 800, 975, 1150], 150],
    ["U2", "Water Works", 150, [4, 10]],
    ["F3", "Marvin Gardens", 280, [24, 120, 360, 850, 1025, 1200], 150],
    ["J1", "Go To Jail"],
    ["G1", "Pacific Avenue", 300, [26, 130, 390, 900, 1100, 1275], 200],
    ["G2", "North Carolina Avenue", 300, [26, 130, 390, 900, 1100, 1275], 200],
    ["Y3", "Community Chest"],
    ["G3", "Pennsylvania Avenue", 320, [28, 150, 450, 1000, 1200, 1400], 200],
    ["R4", "Short Line", 200, [25, 50, 100, 200]],
    ["Z3", "Chance"],
    ["H1", "Park Place", 350, [35, 175, 500, 1100, 1300, 1500], 200],
    ["T2", "Luxury Tax", 75],
    ["H2", "Boardwalk", 400, [50, 200, 600, 1400, 1700, 2000], 200]
]
chest = []
chance = []