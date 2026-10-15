from typing_extensions import runtime
from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
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
C_AXIS = GREY_B


class ivt_def_graph(Scene):
    def construct(self):

        ##colour giver function
        def colour_giver(mob, indices, colors):
            for index, color in zip(indices, colors):
                if isinstance(index, (list, tuple)):
                    mob[index[0]][index[1]].set_color(color)
                else:
                    mob[index].set_color(color)
        
        ### texts for the animation
        text_1 = MathTex(r"\text{Given two distinct points on [a,b]}",font_size=32).to_corner(UP,buff=0.2)
        
        text_2 = MathTex(r"\text{let f: [a,b] } \to \mathbb{R} \text{be continuous}",font_size=32).to_corner(UP,buff=0.2)
    
        
        text_3 = MathTex(r"\text{at x = a, f(a) and at x = b, f(b)}",font_size=32).to_corner(UP,buff=0.2)
        
        text_4 = VGroup(
            MathTex(r"\text{The intermediate value theorem states that:}",font_size=32),
            MathTex(r"\forall y \text{ between } [f(a),f(b)], \kern0.5em \exists \kern0.5em x\in[a,b] \text{ such that f(x) = y}",font_size=32
        )).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_5 = MathTex(r"\text{Where [f(a),f(b)] is the interval between f(a) and f(b)}",font_size=32).to_corner(UP,buff=0.2)

        text_6 = MathTex(r"\text{what the intermediate value theorem entails...}",font_size=32).to_corner(UP,buff=0.2)

        text_7 = VGroup(MathTex(r"\text{Notice the horizontal line between f(a) and f(b)}",font_size=32),
                        MathTex(r"\text{as we go from a to b}",font_size=32)).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)
        
        text_8 = MathTex(r"\text{All y-values from f(a) to f(b) are covered}",font_size=32).to_corner(UP,buff=0.2)

        # Axes
        axes = Axes(
            x_range=[0, 4.6, 1],
            y_range=[0, 3.2, 1],
            x_length=6,
            y_length=4,
            axis_config={
                "include_ticks": False,
                "tip_shape": StealthTip,
                "tip_length": 0.2,
                "tip_width": 0.2,
            }
        )

        x_label = MathTex(r"\text{x}").next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        y_label = MathTex(r"\text{y}").next_to(axes.y_axis.get_end(), UP, buff=0.1)

        # Function
        def f(x):
            return 0.4 + 0.15*x + 0.05*x**2 + 0.02*x**3
        
        graph = axes.plot(
            f,
            x_range=[0.1, 4],
            color=C_BRIGHT_BLUE,
            stroke_width=4
        )

        # a and b
        a = 0.8
        b = 3.8

        fa = f(a)
        fb = f(b)

        # Vertical dashed lines
        a_line = DashedLine(
            axes.c2p(a,0),
            axes.c2p(a,3),
            color=C_GREEN
        )

        b_line = DashedLine(
            axes.c2p(b,0),
            axes.c2p(b,3),
            color=C_GREEN
        )

        # Labels a, b
        a_label = MathTex("a", color=C_GREEN).scale(0.7).next_to(axes.c2p(a,0), DOWN)
        b_label = MathTex("b", color=C_GREEN).scale(0.7).next_to(axes.c2p(b,0), DOWN)

        # Horizontal band f(a) to f(b)
        band = Rectangle(
            width=axes.x_length,
            height=axes.y_axis.n2p(fb)[1] - axes.y_axis.n2p(fa)[1],
            fill_color=C_RED,
            fill_opacity=0.1,
            stroke_width=0
        )

        band.move_to(axes.c2p(2.3, (fa+fb)/2))

        # Boundary lines
        fa_line = DashedLine(
            axes.c2p(0.05,fa),
            axes.c2p(4.55,fa),
            color=C_RED
        )

        fb_line = DashedLine(
            axes.c2p(0.05,fb),
            axes.c2p(4.55,fb),
            color=C_RED
        )

        # Labels f(a), f(b)
        fa_label = MathTex("f(a)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fa), LEFT)
        fb_label = MathTex("f(b)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fb), LEFT)

        # Points on curve
        p_a = Dot(axes.c2p(a,fa), color=C_BRIGHT_BLUE)
        p_b = Dot(axes.c2p(b,fb), color=C_BRIGHT_BLUE)

        p_tracker = ValueTracker(a)

        p_dot = always_redraw(
            lambda: Dot(axes.c2p(p_tracker.get_value(),f(p_tracker.get_value())))
        )

        ## Horizontal blue line and vertical line to p_dot point

        p_dot_h_line = always_redraw(
            lambda: axes.get_horizontal_line(p_dot.get_center(),color=C_BRIGHT_BLUE)
        )

        p_dot_v_line = always_redraw(
            lambda: axes.get_vertical_line(p_dot.get_center(),color=C_GREEN)
        )

        ####
        ###Animation
        ####

        self.play(FadeIn(axes,shift=UP),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeIn(VGroup(x_label,y_label)),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(Write(text_1),rate_func=smooth,run_time=2)
        self.play(Create(a_line),Create(a_label),
        Create(b_line),Create(b_label),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth,run_time=2)
        self.play(Create(graph),rate_func=smooth,run_time=10)
        self.play(Create(p_a),Create(p_b),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(ReplacementTransform(text_2,text_3),rate_func=smooth,run_time=2)
        self.play(Create(fa_line),Create(fb_line),rate_func=smooth,run_time=2)
        self.play(FadeIn(fa_label),FadeIn(fb_label),rate_func=smooth,run_time=2)

        self.wait(4)
        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth,run_time=2)
        self.play(FadeIn(band),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(ReplacementTransform(text_4,text_5),rate_func=smooth,run_time=2)
        self.play(Indicate(VGroup(band,fa_line,fb_line)),run_time=6)
        self.wait(4)

        self.play(ReplacementTransform(text_5,text_6),rate_func=smooth,run_time=2)
        self.play(Create(p_dot),Create(p_dot_h_line),rate_func=smooth,run_time=2)

        self.wait(4)
        self.play(ReplacementTransform(text_6,text_7),rate_func=smooth,run_time=2)
        self.play(p_tracker.animate.set_value(b),rate_func=smooth,run_time=10)
        self.play(ReplacementTransform(text_7,text_8),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(p_tracker.animate.set_value((a+b)/2),rate_func=smooth,run_time=4)

        self.wait(2)
        self.play(Create(p_dot_v_line),rate_func=smooth,run_time=2)
        self.wait(5)

        self.play(FadeOut(VGroup(graph,p_dot,p_dot_h_line,p_dot_v_line,band,fa_line,fb_line,fa_label,fb_label,a_line,a_label,b_line,b_label,p_a,p_b,text_8),shift=UP),rate_func=smooth,run_time=2)

        self.wait(2)




class ivt_app_roots(Scene):
    def construct(self):
        ## Texts
        text_1 = VGroup(
            MathTex(r"\text{The intermediate value theorem can be used to prove}",font_size=32),
            MathTex(r"\text{that a function possesses a root f(x) = 0}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_2 = MathTex(r"\text{to show this, given two distinct points on [a,b]}",font_size=32).to_corner(UP,buff=0.2)

        text_3 = MathTex(r"\text{let f:[a,b] } \to \mathbb{R} \text{ be continuous }",font_size=32).to_corner(UP,buff=0.2)

        text_4 = MathTex(r"\text{at x = a, f(a)} < 0",font_size=32).to_corner(UP,buff=0.2)

        text_5 = MathTex(r"\text{at x = b, f(b)} > 0",font_size=32).to_corner(UP,buff=0.2)
        
        text_6 = VGroup(
            MathTex(r"\text{As We transition From f(a)} < 0 \to \text{ f(b) } > 0 \text{ We have to pass}",font_size=32),
            MathTex(r"\text{through f(c) = 0, since we can't jump from f(a) to f(b)}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_7 = MathTex(r"\therefore \kern0.5em f(a) \cdot f(b) < 0 \kern0.5em \exists x : f(x) = 0",
        font_size=32).to_corner(UP,buff=0.2)

        # Axes
        axes = Axes(
            x_range=[0, 2.6, 0.5],
            y_range=[-1.6, 1.5, 0.5],
            x_length=6,
            y_length=5,
            axis_config={
                "color": C_AXIS,
                "include_ticks": False,
                "tip_shape":StealthTip,
                "tip_length": 0.2,
                "tip_width": 0.2
            }
        ).shift(DOWN*0.5)

        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        y_label = MathTex("y").next_to(axes.y_axis.get_end(), UP, buff=0.1)

        # Function
        def f(x):
            return 0.9 * np.sin(np.deg2rad(120*(x-1.2))) * np.exp(-0.35*(x-2))

        graph = axes.plot(
            f,
            x_range=[0.2, 2.2],
            color=C_BRIGHT_BLUE,
            stroke_width=4
        )

        # a, b, c
        a = 0.8
        b = 2
        c = 1.2

        # vertical dashed lines
        a_line = DashedLine(
            axes.c2p(a, -1.6),
            axes.c2p(a, 1.5),
            color=C_GREEN
        )

        b_line = DashedLine(
            axes.c2p(b, -1.6),
            axes.c2p(b, 1.5),
            color=C_GREEN
        )

        # labels a, b
        a_label = MathTex("a", color=C_GREEN).next_to(axes.c2p(a,0), DL)
        b_label = MathTex("b", color=C_GREEN).next_to(axes.c2p(b,0), DR)

        # sign markers
        fa_point = Dot(axes.c2p(a,f(a)), color=C_RED)
        fb_point = Dot(axes.c2p(b,f(b)), color=C_RED)

        fa_label = MathTex("f(a)<0",font_size=30, color=C_RED).next_to(fa_point, RIGHT, buff=0.2)
        fb_label = MathTex("f(b)>0",font_size=30, color=C_RED).next_to(fb_point, RIGHT, buff=0.2)

        # zero crossing marker
        root = Dot(axes.c2p(c,f(c)), color=C_MAGENTA, radius=0.06)

        root_label = MathTex("f(c)=0",font_size=30, color=C_MAGENTA).next_to(root, DR, buff=0.1)

        ## white point tracker for transition
        p_tracker = ValueTracker(a)

        p_dot = always_redraw(
            lambda: Dot(axes.c2p(p_tracker.get_value(),f(p_tracker.get_value())))
        )
        
        ### Animations.
        self.add(axes,x_label,y_label)
        self.play(Write(text_1))
        self.wait(4)
        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth,run_time=2)
        self.play(Create(a_line),Create(a_label),Create(b_line),Create(b_label),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(ReplacementTransform(text_2,text_3),rate_func=smooth,run_time=2)
        self.play(Create(graph),rate_func=smooth,run_time=6)
        self.wait(4)

        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth,run_time=2)
        self.play(FadeIn(fa_point),FadeIn(fa_label),rate_func=smooth)
        self.wait(2)
        self.play(ReplacementTransform(text_4,text_5),rate_func=smooth,run_time=2)
        self.play(FadeIn(fb_point),FadeIn(fb_label),rate_func=smooth)
        self.wait(4)

        self.play(Create(p_dot),rate_func=smooth,run_time=2)
        self.play(ReplacementTransform(text_5,text_6[0]),rate_func=smooth,run_time=2)
        self.play(p_tracker.animate.set_value(c),rate_func=smooth,run_time=7)
        self.wait(2)

        self.play(Write(text_6[1]),rate_func=smooth,run_time=2)
        self.play(Indicate(p_dot,run_time=4))
        self.wait(2)
        self.play(Create(root),Write(root_label),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(p_tracker.animate.set_value(b),rate_func=smooth,run_time=7)
        self.wait(2)
        self.play(FadeOut(p_dot),ReplacementTransform(text_6,text_7),rate_func=smooth,run_time=2)
        self.wait(5)
        self.play(FadeOut(VGroup(text_7,fa_point,fa_label,fb_point,fb_label,a_line,a_label,b_line,b_label,graph,root,root_label),shift=UP),rate_func=smooth,run_time=2)
        self.wait(2)


class ivt_non_mon_and_image(Scene):
    def construct(self):
        ##Texts 
        text_1 = MathTex(r"\text{Given two distinct points on [a,b]}",font_size=32).to_corner(UP,buff=0.2)

        text_2 = MathTex(r"\text{let f:[a,b] } \to \mathbb{R}\text{ be continuous}",font_size=32).to_corner(UP,buff=0.2)
        
        text_3 = MathTex(r"\text{At x = a, f(a) and x = b, f(b) }",font_size=32).to_corner(UP,buff=0.2)

        text_4 = VGroup(
            MathTex(r"\text{Note the f(a)} \to \text{f(b) region... all y values}",font_size=32),
                 MathTex(r"\text{within that range are still reached.}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_5 = VGroup(
            MathTex(r"\text{We can see that the function is not monotonous within }",font_size=32),
            MathTex(r"\text{[a,b] because it changes direction }",
            font_size=32)).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)
        
        text_6 = MathTex(r"\text{Note the values outside the [f(a),f(b)] band}",font_size=32).to_corner(UP,buff=0.2)

        text_7 = VGroup(
            MathTex(r"\text{Intermediate value theorem only tells us that}",font_size=32),
            MathTex(r"\text{the values between [f(a),f(b)] are taken}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_8 = VGroup(
            MathTex(r"\text{It does not give us the total image of the}",font_size=32),
            MathTex(r"\text{of the function}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_9 = VGroup(MathTex(r"\text{Notice that the image of the function is not equal to }",font_size=32),
                 MathTex(r"\text{the [f(a),f(b)] interval}",font_size=32)).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)
        text_10 = MathTex(r"\text{this happens when the function is non-monotonous}",font_size=32).to_corner(UP,buff=0.2)
        
        ##axis
        axes = Axes(
            x_range=[0, 3.1, 0.5],
            y_range=[-1.6, 1.3, 0.5],
            x_length=6,
            y_length=5,

            axis_config={
                "color": C_AXIS,
                "include_ticks": False,
                "tip_shape":StealthTip,
                "tip_length": 0.2,
                "tip_width": 0.2
            }
        ).shift(DOWN*0.5)


        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        y_label = MathTex("y").next_to(axes.y_axis.get_end(), UP, buff=0.1)

        # Function
        def f(x):
            return 0.9*np.sin(np.deg2rad(200*(x-1.0))) * np.exp(-0.35*(x-1.6)) + 0.15*(x-1.4)

        graph = axes.plot(
            f,
            x_range=[0.2, 2.9],
            color=C_BRIGHT_BLUE,
            stroke_width=4
        )

        # a and b
        a = 0.5
        b = 2.4

        fa = f(a)
        fb = f(b)

        # vertical dashed lines
        a_line = DashedLine(
            axes.c2p(a, -1.6),
            axes.c2p(a, 1.3),
            color=C_GREEN
        )

        b_line = DashedLine(
            axes.c2p(b, -1.6),
            axes.c2p(b, 1.3),
            color=C_GREEN
        )

        a_label = MathTex("a", color=C_GREEN).next_to(axes.c2p(a, 0), UL)
        b_label = MathTex("b", color=C_GREEN).next_to(axes.c2p(b, 0), UR)

        # horizontal reference lines
        fa_line = DashedLine(
            axes.c2p(0, fa),
            axes.c2p(3.1, fa),
            color=C_RED
        ).set_opacity(0.6)

        fb_line = DashedLine(
            axes.c2p(0, fb),
            axes.c2p(3.1, fb),
            color=C_RED
        ).set_opacity(0.6)

        max_y = 0.97

        max_line = DashedLine(
            axes.c2p(0, max_y),
            axes.c2p(3.1, max_y),
            color=WHITE
        )

        # labels
        fa_label = MathTex("f(a)", color=C_RED).scale(0.7).next_to(axes.c2p(0, fa), LEFT)
        fb_label = MathTex("f(b)", color=C_RED).scale(0.7).next_to(axes.c2p(0, fb), LEFT)
        
        max_label = MathTex(r"\max(f)", color=WHITE).scale(0.7).next_to(axes.c2p(0, max_y), LEFT)
        min_label = MathTex(r"\min(f) = ",color=WHITE).scale(0.7).next_to(fa_label,LEFT,buff=0.2)
        # points
        p_a = Dot(axes.c2p(a,f(a)))
        p_b = Dot(axes.c2p(b,f(b)))

        # shaded regions
        band1 = Rectangle(
            width=axes.x_length,
            height=axes.y_axis.n2p(fb)[1] - axes.y_axis.n2p(fa)[1],
            fill_color=C_RED,
            fill_opacity=0.2,
            stroke_width=0
        ).move_to(axes.c2p(1.55, (fa + fb)/2))

        band2 = Rectangle(
            width=axes.x_length,
            height=axes.y_axis.n2p(max_y)[1] - axes.y_axis.n2p(fb)[1],
            fill_color=WHITE,
            fill_opacity=0.2,
            stroke_width=0
        ).move_to(axes.c2p(1.55, (fb + max_y)/2))

        ####
        ### Animation
        ####

        self.add(axes,x_label,y_label)
        self.wait(2)
        self.play(Write(text_1),rate_func=smooth)
        self.play(FadeIn(a_label),FadeIn(b_label),Create(a_line),Create(b_line),run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth)
        self.play(Create(graph),run_time=10,rate_func=smooth)
        self.play(FadeIn(p_a),FadeIn(p_b),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3),run_time=2,rate_func=smooth)
        self.play(Create(fa_line),Create(fb_line),FadeIn(fa_label),FadeIn(fb_label),run_time=2,rate_func=smooth)
        self.play(FadeIn(band1),run_time=2,rate_func=smooth)
        self.wait(4)

        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth)
        self.play(Indicate(band1,color=C_MAGENTA),run_time=4)
        self.wait(4)
        
        self.play(FadeOut(text_4),rate_func=smooth)
        self.play(Create(max_line),rate_func=smooth)

        self.play(FadeIn(max_label),FadeIn(min_label),rate_func=smooth)
        self.wait(4)
        self.play(Write(text_5),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(text_5,text_6),run_time=2)
        self.play(FadeIn(band2),run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(text_6,text_7))
        self.play(Indicate(fa_line),Indicate(fb_line),Indicate(band1),run_time=4)  
        self.wait(4)
        self.play(ReplacementTransform(text_7,text_8),run_time=2)
        self.play(Circumscribe(graph),run_time=4)
        self.wait(5)
        self.play(ReplacementTransform(text_8,text_9),run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(text_9,text_10),run_time=2)
        self.wait(4)

