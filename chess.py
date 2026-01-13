def parse_fen(fen):
    fen_rows = fen.split()[0].split("/")
    board = []
    
    for row in fen_rows:
        expanded_row = []
        for char in row:
            if char.isdigit():  # A digit means that many empty squares
                expanded_row.extend(["."] * int(char))
            else:
                # A letter means a piece (uppercase = White, lowercase = Black)
                expanded_row.append(char)
        board.append(expanded_row)
    return board
    
def print_board(board):
    print(" a b c d e f g h")
    for i, row in enumerate(board, start=1):
        print(8 - i + 1, " ".join(row),8 - i + 1)
        
    print(" a b c d e f g h\n")
    
# Convert chess notation (e.g., "e2") to board indices
def notation_to_index(pos):
    file = ord(pos[0].lower()) - ord('a')  # letters are columns
    rank = 8 - int(pos[1])  # numbers are rows
    
    return rank, file

def move_piece(board, move):
    # validating the movement
    if len(move) != 4:
        print("Invalid move format! Use something like e2e4.")
        return False
        
    # Split into source and destination squares
    src, dst = move[:2], move[2:]
    src_r, src_c = notation_to_index(src)  # sources of our row
    dst_r, dst_c = notation_to_index(dst)  # destination of our columns
    
    # validate the source that it has a piece in the position
    piece = board[src_r][src_c]
    if piece == ".":
        print("No piece at source square!")
        return False
    
    # Move the piece
    board[dst_r][dst_c] = piece
    board[src_r][src_c] = "."
    return True

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
board = parse_fen(fen)
count = 0
while True:
    count +=1
    white = "White"
    black = "Black"
    a = " "
    for i in range(count):
        if i %2 == 0:
            a = "White"
        else:
            a = "Black"
                
    print(a,"chance to play")
    print_board(board)  # Show the current board
    move = input("Enter your move (e.g., e2e4) or 'quit' to exit: ").strip().lower()

    if move == "quit":
        break  # Exit the loop

    if move_piece(board, move):
        print("\nAfter move", move + ":")
        print_board(board)  