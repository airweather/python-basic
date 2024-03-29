import random
class Tic_Tac_Toe:

    # 게임판 생성
    def __init__(self) :
        # 전역변수로 생성
        self.board = []
    # 게임판 초기화
    def create_board(self) :
        for i in range(3):
            row = []
            for j in range(3):
                row.append('*')
                self.board.append(row)
    # 첫 플레이어 선택
    def select_first_player(self) :
        if random.randint(0,1) === 0:
            return 'X'
        else:
            return 'O'

    # 기호 표시
    def mark_spot(self, row, col, player):
        self.board[row][col] = player
        
    # 승리 상태 확인
    def is_win(self, player):

        n = len(self.board)
        # 행 확인
        for i in range(n):
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win == True:
                return win
        # 열 확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win == True:
                return win
        # 대각선 확인
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win == True:
            return win
    

    # 잔여 빈칸 여부 확인
    def is_board_full(self):
        for row in self.board:
            for item in row:
                if item =="*":
                    return False
        return True
    # 플레이어 변경
    def next_player(self, player):
        # if player == 'O':
        #     return 'X'
        # else:
        #     return 'O'
        
        return 'X' if player == 'O' else 'O'

    # 현재 게임판 상태 출력
    def show_board(self):
        for row in self.board:
            for item in row :
                print(item, end=" ")
            print()
            

    # 게임 루프 시작
    def start(self):

        # 새 게임판 생성
        # 첫 플레이어 선택
        # 게임 루프 시작
        while True:
            # 다음 플레이어 안내
            # 현재 게임판 상태 출력
            # 사용자 입력 대기, 컴퓨터일 경우 랜덤 위치 반환
            # row, col 입력값이 0, 0인 경우 게임 종료
            # 입력된 위치 표시
            # 현재 플레이어가 이겼는지 확인
            # 게임판 가득참 확인
            # 플레이어 변경
        # 최종 게임판 출력
    # 게임 생성
    TTT = Tic_Tac_Toe():

    # 게임 시작
    TTT.start() :