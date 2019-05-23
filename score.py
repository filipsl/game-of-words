import model
import config


class ScoreCounter:
    def __init__(self, board, newly_added=None, tiles_with_fixed_neighbours=None):
        self.board = board
        self.newly_added = []
        self.tiles_with_fixed_neighbours = []

    def __count_word_bonus(self, pos):
        factor = 1
        if self.board.fields[pos[0]][pos[1]].bonus == model.Bonus.BONUS_2W:
            factor = 2
        elif self.board.fields[pos[0]][pos[1]].bonus == model.Bonus.BONUS_3W:
            factor = 3
        return factor

    def __count_letter_bonus(self, pos):
        letter_factor = 1
        if self.board.fields[pos[0]][pos[1]].bonus == model.Bonus.BONUS_2L:
            letter_factor = 2
        elif self.board.fields[pos[0]][pos[1]].bonus == model.Bonus.BONUS_3L:
            letter_factor = 3
        return letter_factor

    def __get_newly_added(self):
        newly = []
        for i in range(config.BOARD_SIZE):
            for j in range(config.BOARD_SIZE):
                if self.board.fields[i][j].state == model.FieldState.TEMPORARY:
                    newly.append((i, i))
        return newly

    def __check_fixed_neighbour(self, pos, board):
        x_dirs = [1, 0, -1, 0]
        y_dirs = [0, 1, 0, -1]
        for i in range(len(x_dirs)):
            x_neigh = pos[0] + x_dirs[i]
            y_neigh = pos[1] + y_dirs[i]

            if board.fields[x_neigh][y_neigh].state == model.FieldState.FIXED:
                return True
        return False

    def __get_tiles_with_fixed_neighbours(self):
        tiles_with_fixed_neighbour = []
        for pos in self.newly_added:
            if self.__check_fixed_neighbour(pos, self.board):
                tiles_with_fixed_neighbour.append(pos)
        return tiles_with_fixed_neighbour

    def count_score(self):

        if self.newly_added is None:
            self.newly_added = self.__get_newly_added()
        if self.tiles_with_fixed_neighbours is None:
            self.tiles_with_fixed_neighbours = self.__get_tiles_with_fixed_neighbours()

        score = 0
        horizontal_sorted = sorted(self.newly_added, key=lambda x: x[1])
        vertical_sorted = sorted(self.newly_added, key=lambda x: x[0])

        if horizontal_sorted[0][0] == horizontal_sorted[1][0]:
            # horizontal word which consists of newly-added letters (with temporary state)
            word_bonus_factor = 1
            x = horizontal_sorted[0][0]
            for y in range(horizontal_sorted[0][1], -1, -1):
                if self.board.fields[x][y].state in [model.FieldState.FIXED, model.FieldState.TEMPORARY]:
                    score += self.board.fields[x][y].tile.get_value() * self.__count_letter_bonus((x, y))
                else:
                    break
            score -= self.board.fields[x][horizontal_sorted[0][1]].tile.get_value()
            for y in range(horizontal_sorted[0][1], horizontal_sorted[::-1][0][1]):
                if self.board.fields[x][y].state in [model.FieldState.FIXED, model.FieldState.TEMPORARY]:
                    score += self.board.fields[x][y].tile.get_value() * self.__count_letter_bonus((x, y))
                else:
                    break
            score -= self.board.fields[x][horizontal_sorted[::-1][0][1]].tile.get_value()
            for y in range(horizontal_sorted[::-1][0][1], config.BOARD_SIZE):
                if self.board.fields[x][y].state in [model.FieldState.FIXED, model.FieldState.TEMPORARY]:
                    score += self.board.fields[x][y].tile.get_value() * self.__count_letter_bonus((x, y))
                else:
                    break

            for pos in horizontal_sorted:
                word_bonus_factor *= self.__count_word_bonus(pos)

            score *= word_bonus_factor

            # todo -> count vertical score for every member of tiles_with_fixed_neighbours
            for pos in self.tiles_with_fixed_neighbours:
                pass


        else:
            pass