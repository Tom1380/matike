from manim import *


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

        fade_unrolled_circumferences_out = [
            FadeOut(uc) for uc in self.unrolled_circumferences]

        filled_triangle_points = [[0, 0.5, 0],
                                  [0, -0.5, 0], [TAU, -0.5, 0]]

        filled_triangle_color = TEAL

        filled_triangle = Polygon(
            *filled_triangle_points, color=filled_triangle_color).set_fill(filled_triangle_color, opacity=0.5)

        self.play(Create(overlayed_circle), Create(filled_triangle), Uncreate(radius), *fade_unrolled_circumferences_out,
                  FadeOut(self.unrolled_main_circle), FadeOut(cloned_radius))

        self.wait(1)

        self.play(overlayed_circle.animate.shift(UP * 2), self.main_circle.animate.shift(UP * 2), filled_triangle.animate.shift(
            UP * 2), cloned_radius_brace.animate.shift(UP * 2), unrolled_main_circle_brace.animate.shift(UP * 2))

        formula = MathTex(
            r"r", r"\cdot", r"2{\pi}r", r"\over", r"2")
        formula.shift(DOWN)
        self.play(Create(formula))
        self.wait(3)

        formula2 = MathTex(
            r"r", r"\cdot", r"{\pi}r")
        formula2.shift(DOWN)
        self.play(Transform(formula, formula2))
        self.wait(3)

        formula3 = MathTex("{\pi}r^2")
        formula3.shift(DOWN)
        self.play(Transform(formula, formula3))

        self.wait(10)

    def unroll_circumferences(self):
        l = list(enumerate(self.int_circumferences))
        l = reversed(l)
        self.unrolled_circumferences = []
        for i, circumference in l:
            i = i + 1
            unrolled = Line(
                (0, -0.5 + i / 20, 0), ((0 + circumference.radius * TAU, -0.5 + i / 20, 0)), stroke_width=3).set_color(TEAL)
            self.play(Transform(circumference, unrolled), run_time=0.5)
            self.unrolled_circumferences.append(circumference)

        self.unrolled_main_circle = Line(
            (0, -0.5, 0), ((0 + self.main_circle.radius * TAU, -0.5, 0))).set_color(PURPLE)

        self.play(TransformFromCopy(self.main_circle,
                                    self.unrolled_main_circle, run_time=0.5))
