from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()                    # create a circle
        circle.set_fill(BLUE, opacity=0.5)   # set color and transparency

        square = Square()                    # create a square
        square.set_fill(RED, opacity=0.5)   # set color and transparency
        square.flip(RIGHT)                   # flip horizontally
        square.rotate(-3 * TAU / 8)          # rotate a certain amount

        self.play(Create(square))      # animate the creation of the square
        # interpolate the square into the circle
        self.play(Transform(square, circle))
        self.play(FadeOut(square))           # fade out animation


class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)


class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        circle.move_to(LEFT * 2)
        # place the square to the left of the circle
        square.next_to(circle, LEFT)
        # align the left border of the triangle to the left border of the circle
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)


class Matike(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(RED, opacity=0.5)   # set color and transparency

        square = Square()
        square.set_fill(PURPLE, opacity=0.5)   # set color and transparency

        triangle = Triangle()
        triangle.set_fill(GREEN, opacity=0.5)   # set color and transparency

        # place the circle two units left from the origin
        circle.move_to(LEFT * 2)
        # place the square to the left of the circle
        square.next_to(circle, LEFT)
        # align the left border of the triangle to the left border of the circle
        triangle.next_to(circle, RIGHT)

        self.play(Create(square))      # animate the creation of the square
        self.play(Transform(square, circle))
        self.play(Transform(square, triangle))
        self.wait(1)
