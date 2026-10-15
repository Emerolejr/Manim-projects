from typing_extensions import runtime
from manim import *
import numpy as np

config.pixel_width = 3840
config.pixel_height = 2160
config.background_color = "#000000"

# --- CUSTOM PALETTE ---
C_BLUE        = "#0068E0"
C_BRIGHT_BLUE = "#009CDA"
C_GREEN       = "#50C878"
C_RED         = "#FF0055"
C_GRAY        = "#202020"
C_YELLOW      = "#FFD700"
C_ORANGE      = "#FF8C00"
C_PURPLE      = "#C179B9"
C_MAGENTA     = "#E000A0"
C_NEON_PURPLE = "#FF00FF"
C_BLACK       = "#000000"
C_PANEL       = "#080808"


class BeamerBlock(VGroup):
    def __init__(self, title, width=13, **kwargs):
        super().__init__(**kwargs)
        # Header bar with bright blue background
        self.header = Rectangle(width=width, height=0.5, fill_color=C_BRIGHT_BLUE, fill_opacity=1, stroke_width=0)
        
        # Title text, left-aligned with padding
        self.title = Tex(r"\textbf{" + title + "}", color=C_BLACK, font_size=52)
        self.title.align_to(self.header, LEFT).shift(RIGHT * 0.2)
        self.title.set_y(self.header.get_y()) # Center vertically in header
        
        # Grey body panel
        self.body = Rectangle(width=width, height=6.8, fill_color=C_GRAY, fill_opacity=0.5, stroke_width=0)
        self.body.next_to(self.header, DOWN, buff=0)
        
        self.add(self.body, self.header, self.title)


class inverse_explain(Scene):
    def construct(self):
        header = BeamerBlock("Theorem",width=14).move_to(ORIGIN)

        ##texts for the 
        text_1 = VGroup(
            MathTex(r"\text{Let } I \subset \mathbb{R} \text{ be an open interval and } f: I \to J := \text{im}(f)", font_size=32),
            MathTex(r"\text{a differentiable function}", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        text_2 = MathTex(
            r"\text{If } f \text{ is bijective, then it has an inverse } f^{-1}: J \to I",
            font_size=32
        )

        text_3 = MathTex(
            r"\text{For its derivative, the following holds for all } y \in J",
            font_size=32
        )

        text_4 = MathTex(
            r"(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))}",
            font_size=32
        )

        group_1 = VGroup(text_1, text_2, text_3, text_4).arrange(DOWN,aligned_edge=LEFT,buff=0.7)

        text_5 = MathTex(
            r"\text{Here is how the inverse relationship is established:}",
            font_size=32
        )

        text_6 = MathTex(
            r"\text{Applying a function and its inverse gives: } f(f^{-1}(x)) = x",
            font_size=32
        )

        text_7 = MathTex(
            r"\text{Differentiating both sides: } \frac{d}{dx}[f(f^{-1}(x))] = \frac{d}{dx}(x)",
            font_size=32
        )

        text_8 = MathTex(
            r"\text{Applying the chain rule: } f'(f^{-1}(x)) \cdot (f^{-1})'(x) = 1",
            font_size=32
        )

        text_9 = MathTex(
            r"\text{Solving for } (f^{-1})'(x): (f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}",
            font_size=32
        )

        group_2 = VGroup(text_5, text_6, text_7, text_8, text_9).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        self.add(header)
        
        for i in group_1:
            self.play(Write(i),rate_func=smooth)
            self.wait(2)
        
        self.play(FadeOut(group_1))

        for i in group_2:
            self.play(Write(i),rate_func=smooth)
            self.wait(2)

        self.wait(4)
        self.play(FadeOut(group_2),run_time=2)


class inverse_diff_graph(Scene):
    def construct(self):
        ##texts
        text_1 = MathTex(r"\text{Given the function } f(x) = 2x+2",font_size=32).to_corner(UP,buff=0.2)
        text_2 = MathTex(r"\text{reflected across y = x}",font_size=32).to_corner(UP,buff=0.2)
        text_3 = MathTex(r"\text{The inverse function is } f^{-1}(x) = \frac{x-2}{2}",font_size=32).to_corner(UP,buff=0.2)

        text_4 = MathTex(r"\text{Here is another function of the form } f(x) = x^2",font_size=32).to_corner(UP,buff=0.2)
        text_5 = MathTex(r"\text{reflected across y = x}",font_size=32).to_corner(UP,buff=0.2)
        text_6 = MathTex(r"\text{The inverse function is } f^{-1}(x) = \sqrt{x}",font_size=32).to_corner(UP,buff=0.2)
        text_7 = MathTex(r"\text{Here is how the tangent gradually changes}",font_size=32).to_corner(UP,buff=0.2)
        
        ### Axes and lines.1
        axes_1 = Axes(
            x_range=[-4,2,1],
            y_range=[-10,6,1],
            x_length=5,
            y_length=5,
            axis_config={
            "include_numbers":False,
            "include_ticks":False},
            tips=False,
        )

        x_label = axes_1.get_x_axis_label(r"x")
        y_label = axes_1.get_y_axis_label(r"y")

        def f_1(x):
            return 2*x + 2

        graph_1 = axes_1.plot(f_1, x_range=[-4,4], color=C_BRIGHT_BLUE)
        reflector_1 = axes_1.plot(lambda x: x, x_range=[-4,4], color=C_MAGENTA)

        def f_1_inv(x):
            return (x-2)/2

        graph_1_inv = axes_1.plot(
            f_1_inv, x_range=[-4,4], color=C_GREEN
        )
        
        ### Axes and lines.2
        axes_2 = Axes(
            x_range=[-0.1,2,1],
            y_range=[-0.1,4,1],
            x_length=5,
            y_length=5,
            axis_config={
            "include_numbers":False,
            "include_ticks":False},
            tips=False,
        )

        x_label_2 = axes_2.get_x_axis_label(r"x")
        y_label_2 = axes_2.get_y_axis_label(r"y")
        
        def f_2(x):
            return x**2
        graph_2 = axes_2.plot(f_2, x_range=[0,2], color=C_BRIGHT_BLUE)
        reflector_2 = axes_2.plot(lambda x: x, x_range=[0,2], color=C_MAGENTA)
       
        def f_2_inv(x):
            return np.sqrt(x)
        graph_2_inv = axes_2.plot(
            f_2_inv, x_range=[0,2], color=C_GREEN
        )


        ###About tangents
        tangent_tracker = ValueTracker(0)

        tangent_2 = always_redraw(lambda: TangentLine(graph_2,tangent_tracker.get_value()/2,length=2,color=C_RED))
        
        tangent_2_inv = always_redraw(lambda: TangentLine(graph_2_inv,tangent_tracker.get_value()/2,length=2,color=C_RED))

        tangent_dot = always_redraw(lambda: Dot(graph_2.point_from_proportion(tangent_tracker.get_value()/2),color=C_RED))
        tangent_dot_inv = always_redraw(lambda: Dot(graph_2_inv.point_from_proportion(tangent_tracker.get_value()/2),color=C_RED))

        ## Animations
        self.play(Create(axes_1),rate_func=smooth,run_time=2)
        self.play(Write(x_label),Write(y_label),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(Write(text_1),rate_func=smooth,run_time=2)
        self.play(Create(graph_1),rate_func=smooth,run_time=7)
        self.wait(4)
        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth,run_time=2)
        self.play(Create(reflector_1),rate_func=smooth,run_time=7)
        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3),rate_func=smooth,run_time=2)
        self.play(Create(graph_1_inv),rate_func=smooth,run_time=7)
        self.wait(4)
        self.play(FadeOut(axes_1,graph_1,reflector_1,graph_1_inv,x_label,y_label),run_time=2)
        self.wait(4)

        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth,run_time=2)
        
        self.play(Create(axes_2),Write(x_label_2),Write(y_label_2),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(Create(graph_2),rate_func=smooth,run_time=7)
        self.wait(4)
        self.play(ReplacementTransform(text_4,text_5),rate_func=smooth,run_time=2)
        self.play(Create(reflector_2),rate_func=smooth,run_time=7)
        self.wait(4)
        self.play(ReplacementTransform(text_5,text_6),rate_func=smooth,run_time=2)
        self.play(Create(graph_2_inv),rate_func=smooth,run_time=7)
        self.wait(4)

        self.play(ReplacementTransform(text_6,text_7),rate_func=smooth,run_time=2)
        self.play(Create(tangent_2),Create(tangent_dot),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(Create(tangent_2_inv),Create(tangent_dot_inv),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(tangent_tracker.animate.set_value(2),rate_func=smooth,run_time=10)
        self.wait(4)
        self.play(FadeOut(tangent_2,tangent_2_inv,tangent_dot,tangent_dot_inv),run_time=2)
        self.wait(4)
