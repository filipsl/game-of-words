import view
import config


class Event:
    def __init__(self):
        self.name = "Generic event"


class TickEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "CPU Tick Event"


class QuitEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "Quit Event"


class MouseEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "Mouse Event"


class TileBoxEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "Tile Box Event"


class EmptyFieldEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "Empty Field Event"


class GameStartedEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "Game Started Event"


# Initialize game events
class ClearScreenEvent(Event):
    def __init__(self, image_path=None):
        super().__init__()
        self.name = "CleanScreenEvent"
        self.image_path = image_path


class ScoreBoardBuildEvent(Event):
    def __init__(self, score_board):
        super().__init__()
        self.name = "ScoreBoardBuildEvent"
        self.score_board = score_board


class BoardBuildEvent(Event):
    def __init__(self, board):
        super().__init__()
        self.name = "Build Board Event"
        self.board = board


class TileBoxBuildEvent(Event):
    def __init__(self, tilebox):
        super().__init__()
        self.name = "Build TileBox Event"
        self.tilebox = tilebox


class MenuBuildEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = 'MenuBuildEvent'
        play_button = view.Button(view.ButtonShapeType.RECTANGLE, 'Play', 43, (51, 255, 53), (200, 80),
                                  config.WINDOW_WIDTH // 2 - 100, 300)
        set_difficulty_button = view.Button(view.ButtonShapeType.RECTANGLE, 'Set difficulty', 21, (51, 255, 53),
                                            (180, 80), config.WINDOW_WIDTH // 2 - 90, 400)
        edit_board_button = view.Button(view.ButtonShapeType.RECTANGLE, 'Edit board', 21, (51, 255, 53), (180, 80),
                                        config.WINDOW_WIDTH // 2 - 90, 500)
        about_button = view.Button(view.ButtonShapeType.RECTANGLE, 'About', 21, (51, 255, 53), (180, 80),
                                   config.WINDOW_WIDTH // 2 - 90, 600)
        self.buttons = []
        self.buttons.append(play_button)
        self.buttons.append(set_difficulty_button)
        self.buttons.append(edit_board_button)
        self.buttons.append(about_button)


# superior event for buttons
class ButtonEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "Button Event"


class DrawGameButtonsEvent(ButtonEvent):
    def __init__(self):
        super().__init__()
        self.name = 'DrawGameButtonsEvent'
        confirm_button = view.Button(view.ButtonShapeType.CIRCLE, 'Confirm', 20, (51, 255, 53), (60, 60), 830, 625)
        shuffle_button = view.Button(view.ButtonShapeType.RECTANGLE, 'Shuffle', 20, (51, 255, 53), (50, 50), 110, 480)
        pass_button = view.Button(view.ButtonShapeType.RECTANGLE, 'Pass', 20, (51, 255, 53), (50, 50), 110, 550)
        surrender_button = view.Button(view.ButtonShapeType.RECTANGLE, 'Surrender', 15, (51, 255, 53), (50, 50), 110,
                                       410)
        take_temps_button = view.Button(view.ButtonShapeType.RECTANGLE, 'Letters', 15, (51, 255, 53), (50, 50), 110,
                                        340)
        take_all = view.Button(view.ButtonShapeType.RECTANGLE, 'Return', 15, (51, 255, 53), (50, 50), 110,
                                        270)

        self.buttons = []
        self.buttons.append(confirm_button)
        self.buttons.append(shuffle_button)
        self.buttons.append(pass_button)
        self.buttons.append(surrender_button)
        self.buttons.append(take_temps_button)
        self.buttons.append(take_all)


class ConfirmButtonEvent(ButtonEvent):
    def __init__(self):
        super().__init__()
        self.name = "ConfirmButtonEvent"


class TakeAllButtonEvent(ButtonEvent):
    def __init__(self):
        super().__init__()
        self.name = "TakeAllButtonEvent"


class SelectFieldEvent(Event):
    def __init__(self, field, field_group):
        super().__init__()
        self.name = "SelectFieldEvent"
        # self.coords = coords
        self.field = field
        self.field_group = field_group


class ConfirmButtonPressedEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "ConfirmButtonPressedEvent"


class NewLettersButtonPressedEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "NewLettersButtonPressedEvent"


class ShuffleButtonPressedEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "ShuffleButtonPressedEvent"


class PassButtonPressedEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "PassButtonPressedEvent"


class SurrenderButtonPressedEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "SurrenderButtonPressedEvent"


class UpdateFieldEvent(Event):
    def __init__(self, field):
        super().__init__()
        self.name = "UpdateFieldEvent"
        self.field = field


class VerifyBoardEvent(Event):
    def __init__(self, board):
        super().__init__()
        self.name = "VerifyBoardEvent"
        self.board = board


class MoveRejectedEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "MoveRejectedEvent"


class NextPlayerMoveStartedEvent(Event):
    def __init__(self, game):
        super().__init__()
        self.name = "NextPlayerMoveStartedEvent"
        self.game = game


class OtherPlayerTurnEvent(Event):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "OtherPlayerTurnEvent"


class EndGameEvent(Event):
    def __init__(self, players):
        super().__init__()
        self.players = players
        self.name = "EndGameEvent"


class AboutBannerShowEvent(Event):
    def __init__(self):
        super().__init__()
        self.name = "AboutBannerShowEvent"
