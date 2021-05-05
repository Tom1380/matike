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
    return [Circle(radius=(1 - i / 20), color=TEAL).set_stroke(width=3) for i in range(1, 21)]


class Matike(Scene):
    def construct(self):
        self.main_circle = Circle(radius=1, color=PURPLE)

        radius = Line(self.main_circle.get_center(),
                      (1, 0, 0)).set_color(WHITE)

        rotate_radius = Rotate(
            radius, angle=TAU, about_point=self.main_circle.get_center())

        brace = BraceLabel(radius, text='r')

        self.play(Create(radius))
        self.play(rotate_radius, Create(self.main_circle))
        self.play(Create(brace), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(brace))

        # Internal circumferences
        self.int_circumferences = get_internal_circumferences()

        creations = [Create(circumference)
                     for circumference in self.int_circumferences]
        self.play(rotate_radius, *creations)

        all_circumferences = [self.main_circle, *self.int_circumferences]

        end_point = (-3, 0, 0)
        move_to_left = [ApplyMethod(c.shift, end_point)
                        for c in [radius, *all_circumferences]]

        self.play(*move_to_left)

        self.wait(1)

        cloned_radius = Line(self.main_circle.get_center(),
                             (-2, 0, 0)).set_color(WHITE)

        self.play(cloned_radius.animate.shift((2.5, 0, 0)).rotate(PI / 2))

        self.unroll_circumferences()

        cloned_radius_brace = BraceLabel(
            cloned_radius, text='r', brace_direction=LEFT)

        unrolled_main_circle_brace = BraceLabel(
            self.unrolled_main_circle, text='2{\pi}r')

        self.play(Create(cloned_radius_brace),
                  Create(unrolled_main_circle_brace), run_time=0.5)

        self.wait(3)

        overlayed_circle = Circle(
            radius=1, color=PURPLE).set_fill(PURPLE, opacity=0.5)

        overlayed_circle.shift(LEFT * 3)

        self.play(Create(overlayed_circle), Uncreate(radius))

        self.wait(10)

    def unroll_circumferences(self):
        l = list(enumerate(self.int_circumferences))
        l = reversed(l)
        for i, circumference in l:
            i = i + 1
            self.play(Transform(circumference, Line(
                (0, -0.5 + i / 20, 0), ((0 + circumference.radius * TAU, -0.5 + i / 20, 0)), stroke_width=3).set_color(TEAL)), run_time=0.5)

        self.unrolled_main_circle = Line(
            (0, -0.5, 0), ((0 + self.main_circle.radius * TAU, -0.5, 0))).set_color(PURPLE)

        self.play(TransformFromCopy(self.main_circle,
                                    self.unrolled_main_circle, run_time=0.5))
