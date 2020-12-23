"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

This program is to create a object interaction game
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    lives = NUM_LIVES
    dx = graphics.get_xvelocity()
    dy = graphics.get_yvelocity()

    while True:
        if lives > 0:
            pause(FRAME_RATE)

            if graphics.click_to_start:
                graphics.ball.move(dx, dy)

                # check whether the collision happen
                upper_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                upper_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                lower_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
                lower_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                            graphics.ball.y + graphics.ball.width)

                if upper_left is not None:
                    if upper_left is graphics.paddle:
                        dy *= -1
                        graphics.ball.move(3 * dx, 3 * dy)
                    else:
                        if upper_left is not graphics.score_label:
                            graphics.window.remove(upper_left)
                            graphics.score += 1
                            graphics.score_label.text = 'Score: ' + str(graphics.score)
                            dy *= -1

                else:
                    if upper_right is not None and not graphics.score_label:
                        if upper_right is graphics.paddle:
                            dy *= -1
                            graphics.ball.move(3 * dx, 3 * dy)
                        else:
                            graphics.window.remove(upper_right)
                            graphics.score += 1
                            graphics.score_label.text = 'Score: ' + str(graphics.score)
                            dy *= -1

                    else:
                        if lower_right is not None and not graphics.score_label:
                            if lower_right is graphics.paddle:
                                dy *= -1
                                graphics.ball.move(3 * dx, 3 * dy)
                            else:

                                graphics.window.remove(lower_right)
                                graphics.score += 1
                                graphics.score_label.text = 'Score: ' + str(graphics.score)
                                dy *= -1

                        else:
                            if lower_left is not None and not graphics.score_label:
                                if lower_left is graphics.paddle:
                                    dy *= -1
                                    graphics.ball.move(3 * dx, 3 * dy)
                                else:

                                    graphics.window.remove(lower_right)
                                    graphics.score += 1
                                    graphics.score_label.text = 'Score: ' + str(graphics.score)
                                    dy *= -1

                # Check whether the ball is out of boundary
                if graphics.ball.x + graphics.ball.width - 1 >= graphics.window.width or graphics.ball.x <= 0:
                    dx *= -1
                if graphics.ball.y <= 0:
                    dy *= -1
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    lives -= 1
                    if lives > 0:
                        # Reset ball position, return boolean false and ready to next click
                        graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width)/2,
                                            y=(graphics.window.height - graphics.ball.height)/2)
                    graphics.click_to_start = False

                # Set the win condition
                if graphics.score == graphics.number_brick:
                    graphics.window.add(graphics.win, x=(graphics.window.width - graphics.win.width) / 2,
                                        y=((graphics.window.height - graphics.win.height) / 2))
                    break

        else:
            # Set the lose condition
            graphics.window.add(graphics.lose, x=(graphics.window.width-graphics.lose.width)/2,
                                y=((graphics.window.height-graphics.lose.height)/2))
            break


if __name__ == '__main__':
    main()
