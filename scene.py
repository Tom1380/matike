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


def get_internal_circumferences():
    return [Circle(radius=(1 - i / 20), color=BLUE).set_stroke(width=1) for i in range(1, 21)]


class Matike(Scene):
    def construct(self):
        main_circle = Circle(radius=1, color=PURPLE)

        radius = Line(main_circle.get_center(), (1, 0, 0)).set_color(WHITE)

        rotate_radius = Rotate(
            radius, angle=TAU, about_point=main_circle.get_center())

        brace = BraceLabel(radius, text='r')

        self.play(Create(radius))
        self.play(rotate_radius, Create(main_circle))
        self.play(Create(brace))
        self.wait(1)
        self.play(FadeOut(brace))

        # Internal circumferences
        int_circumferences = get_internal_circumferences()

        creations = [Create(circumference)
                     for circumference in int_circumferences]
        self.play(rotate_radius, *creations)

        all_circumferences = [main_circle, *int_circumferences]

        end_point = (-3, -2, 0)
        move_to_left = [ApplyMethod(c.shift, end_point)
                        for c in [radius, *all_circumferences]]

        self.play(*move_to_left)

        self.wait(1)

        # self.play(ApplyMethod(radius.shift, (6, -1, 0)))
        self.play(ApplyMethod(radius.shift, (2, -0.5, 0)))
        self.play(Rotate(radius, angle=PI / 2))

        for i, circumference in enumerate(int_circumferences):
            i = i + 1
            self.play(Transform(circumference, Line(
                (-0.5, -3 + i / 20, 0), ((-0.5 + circumference.radius * TAU, -3 + i / 20, 0)), stroke_width=1).set_color(BLUE)), run_time=0.5)

        self.wait(10)
