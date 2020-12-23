"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This class is to create the class of the game
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10       # Number of rows of bricks.
BRICK_COLS = 10     # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(window_width, window_height)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width)/2,
                            y=window_height-paddle_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'slateblue'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius, ball_radius, x=(window_width - ball_radius)/2, y=(window_height - ball_radius)/2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        self.set_velocity()
        self.get_xvelocity()
        self.get_yvelocity()

        # Set a boolean to evaluate start condition
        self.click_to_start = False

        # Crete label score
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.color = 'darkviolet'
        self.score_label.font = '-40-italic'
        self.window.add(self.score_label, x=0, y=self.score_label.height)

        # Create the end condition of the game
        self.lose = GLabel('You Lose!')
        self.win = GLabel('You Win!')
        if brick_cols <= 5:
            self.win.font = '-40-bold'
            self.lose.font = self.win.font
        else:
            self.win.font = '-90-bold'
            self.lose.font = self.win.font

        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.brick = GRect(brick_width, brick_height, x=i * (BRICK_WIDTH + BRICK_SPACING),
                                   y=BRICK_OFFSET + j * (BRICK_HEIGHT + BRICK_SPACING))
                self.brick.filled = True
                if self.brick.y - BRICK_OFFSET >= 2 * (brick_height + brick_spacing):
                    self.brick.fill_color = 'blue'
                    if self.brick.y - BRICK_OFFSET >= 4 * (brick_height + brick_spacing):
                        self.brick.fill_color = 'green'
                        if self.brick.y - BRICK_OFFSET >= 6 * (brick_height + brick_spacing):
                            self.brick.fill_color = 'yellow'
                            if self.brick.y - BRICK_OFFSET >= 8 * (brick_height + brick_spacing):
                                self.brick.fill_color = 'red'
                                if self.brick.y - BRICK_OFFSET >= 10 * (brick_height + brick_spacing):
                                    self.brick.fill_color = 'aqua'
                else:
                    self.brick.fill_color = 'indigo'
                self.window.add(self.brick)
        self.number_brick = brick_rows * brick_cols

        # Initialize our mouse listeners
        onmousemoved(self.rule)
        onmouseclicked(self.check)

    def check(self, mouse):
        # check whether the click is valid, return boolean
        ch = self.window.get_object_at(self.window.width/2, self.window.height/2)
        if ch is not None:
            self.click_to_start = True

    def rule(self, mouse):
        # make sure the center of paddle will at the same position with cursor position
        self.paddle.x = mouse.x - self.paddle.width/2
        if self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif self.paddle.x <= 0:
            self.paddle.x = 0
        return self.paddle.x

    def set_velocity(self):
        # set the velocity of ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() >= 0.5:
            self.__dx *= -1

    def get_xvelocity(self):
        return self.__dx

    def get_yvelocity(self):
        return self.__dy















