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


class non_diff_intro(Scene):
    def construct(self):
        header = BeamerBlock("Definition",width=14).move_to(ORIGIN)

        ##texts for the introduction 
        text_1 = MathTex(r"\text{A function } f:\mathbb{U} \to \mathbb{R} \text{ is called non-differentiable at } x_0 \in \mathbb{U} \text{ if the limit}",font_size=32)
        text_2 = MathTex(r"\lim_{x \to x_0} \frac{f(x)-f(x_0)}{x-x_0}",font_size=32)
        text_3 = MathTex(r"\text{does not exist. This when }",font_size=32)
        text_4 = MathTex(r"\lim_{x \to x_0^-} \frac{f(x)-f(x_0)}{x-x_0} \kern1em \text{ and } \lim_{x \to x_0^+} \kern1em \frac{f(x)-f(x_0)}{x-x_0}",font_size=32)
        text_5 = MathTex(r"\text{are different or one of the limit does not exist}",font_size=32)

        normal_group = VGroup(
            text_1,
            text_2,
            text_3,
            text_4,
            text_5
        ).arrange(DOWN,buff=0.5,aligned_edge=LEFT)

        self.wait(2)
        self.add(header)
        
        for i in normal_group:
            self.play(Write(i),rate_func=smooth,run_time=2)
        self.wait(2)


class non_diff_graph_example_1(Scene):
    def construct(self):
        
        ### texts for the name.
        text_1 = MathTex(r"\text{Given a graph of f(x) = } |x| \text{ and its derivative}",font_size=32).to_corner(UP,buff=0.2)
        text_2 = MathTex(r"\text{Notice the derivative as we go from left to right}",font_size=32).to_corner(UP,buff=0.2)
        text_3 = VGroup(
            MathTex(r"\text{Recall that for a function to be differentiable at a point}",font_size=32),
            MathTex(r"\lim_{x \to x_0^-} \frac{f(x)-f(x_0)}{x-x_0} \kern1em \text{ = } \lim_{x \to x_0^+} \frac{f(x)-f(x_0)}{x-x_0}",font_size=32)
        ).arrange(DOWN,buff=0.2).to_corner(UP,buff=0.2)

        text_4 = VGroup(
            MathTex(r"\text{In this case, we can clearly see that for the derivative plot,}",font_size=32),
            MathTex(r"\text{left hand limt is not equal to the right limit at x = 0}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_5 = MathTex(r"\text{Hence we can say that the function is non-differentiable at x = 0}",font_size=32).to_corner(UP,buff=0.2)

        ### The graph of f(x) = |x|
        # ---------------- FIRST GRAPH: f(x) = |x| ----------------
        axes1 = Axes(
            x_range=[-2.5, 2.5, 0.5],
            y_range=[-0.2, 2.5, 0.5],
            x_length=5,
            y_length=4,
            tips=False,
            axis_config={
                "include_numbers": True,
                "font_size":20
            }
        ).shift(DOWN*0.5)

        def f(x):
            return abs(x)

        main_graph = always_redraw(
            lambda: axes1.plot(
                f,
                x_range=[-2.5, 2.5],
                color=C_BRIGHT_BLUE,
                stroke_width=5
            )
        )
        graph_name_1 = MathTex(r"\text{Graph of f(x) = } |x|",font_size=32).next_to(axes1,DOWN,buff=0.2)

        key_dot = Dot(axes1.c2p(-2.5,2.5),color=C_RED)

        corner = always_redraw(
            lambda: SurroundingRectangle(
                key_dot, 
                color=C_RED)
        )

        first_graph = Group(axes1,main_graph,graph_name_1)

        ### The graph of f'(x) = |x|
        # ---------------- SECOND GRAPH: f'(x) = |x| ----------------
        axes2 = Axes(
            x_range=[-2.5, 2.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=4,
            tips=False,
            axis_config={
                "font_size":20
            },
            y_axis_config={
                "numbers_to_include":[-1,1]
            },
            x_axis_config={
                "include_numbers": True,
                "font_size":20
            }
        )

        x_label = axes2.get_x_axis_label(r"\text{x}")
        y_label = axes2.get_y_axis_label(r"\text{y}")
        axes_labels = VGroup(x_label,y_label)
        graph_name_2 = MathTex(r"\text{Graph of } f'(x)",font_size=32).next_to(axes2,DOWN,buff=0.2)

        # f'(x) = -1 for x < 0
        left_graph = axes2.plot(
            lambda x: -1,
            x_range=[-2.5, 0],
            color=C_BRIGHT_BLUE,
            stroke_width=5
        )

        # f'(x) = 1 for x > 0
        right_graph = axes2.plot(
            lambda x: 1,
            x_range=[0, 2.5],
            color=C_MAGENTA,
            stroke_width=5
        )

        # Open circles at x = 0
        open_left = Circle(radius=0.06, color=C_BLUE).move_to(
            axes2.c2p(0, -1)
        )

        open_right = Circle(radius=0.06, color=C_MAGENTA).move_to(
            axes2.c2p(0, 1)
        )

        ## for points on the left and the right 

        ### this the value tracker that is responsible for the movement of the dots.
        def tracker_func(axes_no,t,func,sign):
            def updater(mobject):
                if axes_no == 1:
                    mobject.move_to(axes1.c2p(sign*t.get_value(),func(sign*t.get_value())))
                elif axes_no == 2:
                    mobject.move_to(axes2.c2p(sign*t.get_value(),func(sign*t.get_value())))
            return updater

        ### dot tracker for everything.
        dot_tracker = ValueTracker(2.5)
        dot_tracker_left = ValueTracker(2.5)

        left_dot = Dot(axes2.c2p(dot_tracker.get_value(),-1))
        right_dot = Dot(axes2.c2p(dot_tracker.get_value(),1))
        
        
        second_graph = Group(axes2,axes_labels,left_graph,right_graph,open_left,open_right,graph_name_2)

        graph_group = Group(first_graph,second_graph)
        graph_group.arrange(RIGHT,buff=0.7).shift(DOWN*0.5)
    
        ### the animations start here. 
        self.wait(4)
        self.play(FadeIn(graph_group),rate_func=smooth,run_time=3)
        self.play(Write(text_1),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(text_1,text_2),run_time=2)
        
        ##code
        key_dot.add_updater(tracker_func(1,dot_tracker,lambda x: abs(x),-1))
        left_dot.add_updater(tracker_func(2,dot_tracker_left,lambda x: -1,-1))

        ##code
        self.wait(2)
        self.play(Create(key_dot),Create(corner),Create(left_dot))
        self.wait(2)
        self.play(dot_tracker.animate.set_value(0),dot_tracker_left.animate.set_value(0),run_time=10,rate_func=smooth)
       
        ##code
        key_dot.remove_updater(tracker_func(1,dot_tracker,lambda x: abs(x),-1))

        key_dot.add_updater(tracker_func(1,dot_tracker,lambda x: abs(x),1))
        right_dot.add_updater(tracker_func(2,dot_tracker,lambda x: 1,1))
        ##code

        self.play(Create(right_dot),rate_func=smooth)
        self.play(dot_tracker.animate.set_value(2.5),run_time=10,rate_func=smooth)

        self.play(ReplacementTransform(text_2,text_3),run_time=2)
        self.wait(5)
        self.play(ReplacementTransform(text_3,text_4),run_time=2)
        self.wait(5)

    
        
        ##code
        self.play(FadeOut(key_dot),FadeOut(corner))
        self.play(dot_tracker_left.animate.set_value(2.5),run_time=5,rate_func=linear)
        self.wait(2)
        self.play(dot_tracker.animate.set_value(0),dot_tracker_left.animate.set_value(0),run_time=5,rate_func=smooth)
        ##code
        rect = SurroundingRectangle(
            VGroup(open_left,open_right),
            buff=0.2,
            color=C_MAGENTA,
            stroke_width=2
        )

        ##code

        self.play(Create(rect),run_time=2,rate_func=smooth)
        self.wait(4)

        self.play(ReplacementTransform(text_4,text_5),run_time=2)
        self.wait(5)
        self.play(FadeOut(*self.mobjects),run_time=2,rate_func=smooth)
        self.wait(2)


class non_diff_graph_example_3(MovingCameraScene):
    def construct(self):
        ####text
        text_1 = MathTex(r"\text{Consider the function } f(x) = 2x^{1/3}",font_size=32).to_corner(UP,buff=0.2)
        
        text_2 = MathTex(r"\text{This function is continuous everywhere, including at x = 0}",font_size=32).to_corner(UP,buff=0.2)
        
        text_3 = MathTex(r"\text{Note the tangent as we go from the left to the right}",font_size=32).to_corner(UP,buff=0.2)

        text_4 = MathTex(r"\text{The slope becomes infinitely steep when x = 0}",font_size=32).to_corner(UP,buff=0.2)

        text_5 = VGroup(
            MathTex(r"\text{So although the function is continuous, it }",font_size=32),
            MathTex(r"\text{does not have a finite derivative at x = 0}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_6 = MathTex(r"\text{Therefore the function is non-differentiable at x = 0}",
                        font_size=32).to_corner(UP,buff=0.2)

        ###Axes and the rest
        def f(x):
            return 2*np.cbrt(x)
        def df(x):
            return (2/3) * (1 / (np.cbrt(x)**2)) if x != 0 else 1e6

        axes3 = Axes(
            x_range = [-2.5,2.5,1],
            y_range = [-4,4,1],
            x_length = 5,
            y_length=5,
            axis_config={
                "include_numbers":False,
                "include_ticks":False,
                "include_tip":False,
            }
        )
        
        x_label = axes3.get_x_axis_label(r"\text{x}")
        y_label = axes3.get_y_axis_label(r"\text{y}")

        graph = axes3.plot(
            f,
            x_range=[-2.5,2.5],
            color=C_BRIGHT_BLUE
        )
        graph_indicate = graph.copy().set_color(C_RED).set_z_index(2)

        ##value tracker and tangent
        tracker = ValueTracker(-2.0)

        tangent_dot = always_redraw(
            lambda: Dot(radius=0.06).move_to(axes3.c2p(tracker.get_value(),f(tracker.get_value()))).set_z_index(2).set_color(C_MAGENTA)
        )

        tangent_line = always_redraw(
            lambda: axes3.plot(
                lambda x: f(tracker.get_value()) + df(tracker.get_value())*(x-tracker.get_value()),
                x_range=[tracker.get_value()-1,tracker.get_value()+1],
                color=C_MAGENTA,
                stroke_width=5
            )
        )

        ###Animations 
        self.play(FadeIn(axes3),FadeIn(x_label),FadeIn(y_label),rate_func=smooth)
        self.play(Write(text_1),run_time=2,rate_func=smooth)
        self.play(Create(graph),run_time=8,rate_func=smooth)
        self.wait(4)

        self.play(ReplacementTransform(text_1,text_2),run_time=2,rate_func=smooth)
        self.play(Create(graph_indicate),run_time=4)
        self.play(Uncreate(graph_indicate),run_time=4)
        self.camera.frame.save_state()
        self.play(Create(tangent_dot),Create(tangent_line),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3),run_time=2,rate_func=smooth)
        self.play(tracker.animate.set_value(-0.5),run_time=4,rate_func=smooth)
        self.play(self.camera.frame.animate.scale(0.7).move_to(axes3.c2p(0,0)),run_time=4,rate_func=smooth)
        self.play(tracker.animate.set_value(-0.1),self.camera.frame.animate.scale(0.5).move_to(axes3.c2p(0,0)),run_time=4,rate_func=smooth)
        self.play(tracker.animate.set_value(0),run_time=4,rate_func=smooth)
        self.play(Restore(self.camera.frame),run_time=4,rate_func=smooth)

        self.play(ReplacementTransform(text_3,text_4),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(tracker.animate.set_value(2.5),run_time=5,rate_func=smooth)
        self.wait(4)
        self.play(FadeOut(tangent_dot),FadeOut(tangent_line),run_time=2,rate_func=smooth)
        self.play(ReplacementTransform(text_4,text_5),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_5,text_6),run_time=2,rate_func=smooth)
        self.wait(4)
