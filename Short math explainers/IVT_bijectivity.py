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
C_AXIS = GREY_B



class injectivity(Scene):
    def construct(self):

        #### these are for the texts 
        text_1 = MathTex(r"\text{Let us prove that monotocity } \implies \text{ injectivity}",font_size=32).to_corner(UP,buff=0.5)
        text_2 = MathTex(r"\text{Given two distinct points on the x-axis [a,b]}",font_size=32).to_corner(UP,buff=0.5)

        text_3 = MathTex(r"\text{Let f:[a:b]} \to \mathbb{R} \text{ be a continuous and monotonous}",font_size=32).to_corner(UP,buff=0.5)
        text_4 = MathTex(r"\text{note these distint points}",font_size=32).to_corner(UP,buff=0.5)
    
        text_5 = VGroup(
            MathTex(r"\text{Every function value is bigger than the one before it}",font_size=32),
            MathTex(r"\text{and every y-value gets taken once}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT).to_corner(UP,buff=0.5)

        text_6 = MathTex(r"\text{This means monotonicity} \implies \text{ injectivity}",font_size=32).to_corner(UP,buff=0.5)
        
        text_7= VGroup(
            MathTex(r"\text{so we can say:}",font_size=32),
            MathTex(r"\textbf{f is injective}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT).to_corner(UP,buff=0.5)

        ## For the axes and the graph
        axes = Axes(
            x_range=[0, 3.1, 0.5],
            y_range=[-1, 0.85, 0.25],
            x_length=5,
            y_length=4,
            axis_config={
                "color": C_AXIS,
                "include_ticks": False,
                "tip_shape":StealthTip,
                "tip_width":0.2
            }
        )

        x_label = MathTex(r"\text{x}").scale(0.9).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex(r"\text{y}").scale(0.9).next_to(axes.y_axis.get_end(), UP)

        # Function
        def f(x):
            return 0.9*np.log(x+0.35) - 0.4
        
        graph = axes.plot(
            f,
            x_range=[0.2, 2.9],
            color=C_BLUE,
            stroke_width=4
        )

        # a and b
        a = 0.6
        b = 2.6

        fa = f(a)
        fb = f(b)

        # Vertical dashed lines
        a_line = DashedLine(
            axes.c2p(a,-1),
            axes.c2p(a,0.85),
            color=C_GREEN
        )

        b_line = DashedLine(
            axes.c2p(b,-1),
            axes.c2p(b,0.85),
            color=C_GREEN
        )

        a_label = MathTex(r"\text{a}", color=C_GREEN).scale(0.7).next_to(axes.c2p(a,0), DL)
        b_label = MathTex(r"\text{b}", color=C_GREEN).scale(0.7).next_to(axes.c2p(b,0), DR)

        # fa and fb label

        fa_label = MathTex(r"\text{f(a)}", color=C_RED).scale(0.7).next_to(axes.c2p(0,fa), LEFT,buff=0.1)
        fb_label = MathTex(r"\text{f(b)}", color=C_RED).scale(0.7).next_to(axes.c2p(0,fb), LEFT,buff=0.1)

        ### vertical label
         # Boundary lines
        fa_line = DashedLine(
            axes.c2p(0,fa),
            axes.c2p(3.1,fa),
            color=C_RED
        )

        fb_line = DashedLine(
            axes.c2p(0,fb),
            axes.c2p(3.1,fb),
            color=C_RED
        )

        ### these are for the three distinct points
        c = 0.8
        d = 1.5
        e = 2.2

        fc = f(c)
        fd = f(d)
        fe = f(e)

        p_1 = Dot(axes.c2p(c,fc),color=WHITE)
        p_2 = Dot(axes.c2p(d,fd),color=WHITE).set_z_index(2)
        p_3 = Dot(axes.c2p(e,fe),color=WHITE)
        p_group = VGroup(p_1,p_2,p_3)

        p_2_h_line = DashedLine(
            axes.c2p(0,fd),
            axes.c2p(3.1,fd),
            color=C_RED
        ).set_opacity(0.6)

        ###This part is for the animations.

        self.add(axes,x_label,y_label)
        self.play(Write(text_1),run_time=2,rate_func=smooth)
        self.wait(2)
        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth,run_time=2)

        self.play(Create(a_line),Create(b_line),Create(a_label),Create(b_label),run_time=3,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3),run_time=2,rate_func=smooth)
        self.play(Create(graph),run_time=8,rate_func=smooth)

        self.wait(4)
        self.play(Create(fa_line),Create(fb_line),rate_func=smooth)
        self.play(Write(fa_label),Write(fb_label),run_time=3,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_3,text_4),run_time=2,rate_func=smooth)
        self.play(FadeIn(p_1),FadeIn(p_2),FadeIn(p_3),run_time=3,rate_func=smooth)
        self.wait(4)

        self.play(ReplacementTransform(text_4,text_5[0]),run_time=2,rate_func=smooth)

        for i in range(3):
            self.play(Indicate(p_group[2-i],scale_factor=1.5),run_time=1)
            self.wait(0.5)

        self.play(Write(text_5[1]),run_time=2,rate_func=smooth)
        self.wait(1)
        self.play(Create(p_2_h_line),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_5,text_6),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_6,text_7))
        self.wait(4)
        self.play(text_7[1].animate.to_corner(UL,buff=0.5))
        self.play(FadeOut(VGroup(p_group,p_2_h_line,fa_label,fb_label,text_7[0])))
        self.wait(4)


class surjectivity(Scene):
    def construct(self):

        ### For the texts
        text_1 = MathTex(r"\textbf{For Proving Surjectivity}",font_size=32).to_corner(UP,buff=0.5)
        text_2 = MathTex(r"\text{Given f between bounds [a,b]}",font_size=32).to_corner(UP,buff=0.5)
        text_3 = MathTex(r"\text{at x = a, f(a)}",font_size=32).to_corner(UP,buff=0.5)
        text_4 = MathTex(r"\text{at x = b, f(b)}",font_size=32).to_corner(UP,buff=0.5)
        
        text_5 = VGroup(MathTex(r"\text{Notice the horizontal line between f(a) and f(b)}",font_size=32),
                        MathTex(r"\text{as we go from a to b}",font_size=32)).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)
    
        text_6 = VGroup(
            MathTex(r"\text{All values of y  between f(a) and f(b)}",font_size=32),
            MathTex(r"\text{are covered by f(x) function}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_7 = MathTex(r"\text{Hence the function f:[a,b] } \to \text{ [f(a),f(b)] is surjective}",font_size=32).to_corner(UP,buff=0.5)
        
        text_8 = MathTex(r"\text{im(f) = [f(a),f(b)]}",font_size=32)

        ## For the axes and the graph
        axes = Axes(
            x_range=[0, 3.1, 0.5],
            y_range=[-1, 0.85, 0.25],
            x_length=5,
            y_length=4,
            axis_config={
                "color": C_AXIS,
                "include_ticks": False,
                "tip_shape":StealthTip,
                "tip_width":0.2
            }
        )
        text_8.next_to(axes,LEFT,buff=1)

        x_label = MathTex(r"\text{x}").scale(0.9).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex(r"\text{y}").scale(0.9).next_to(axes.y_axis.get_end(), UP)

        # Function
        def f(x):
            return 0.9*np.log(x+0.35) - 0.4
        
        graph = axes.plot(
            f,
            x_range=[0.2, 2.9],
            color=C_BLUE,
            stroke_width=4
        )

        # a and b
        a = 0.6
        b = 2.6

        fa = f(a)
        fb = f(b)

        # Vertical dashed lines
        a_line = DashedLine(
            axes.c2p(a,-1),
            axes.c2p(a,0.85),
            color=C_GREEN
        )

        b_line = DashedLine(
            axes.c2p(b,-1),
            axes.c2p(b,0.85),
            color=C_GREEN
        )

        a_label = MathTex(r"\text{a}", color=C_GREEN).scale(0.7).next_to(axes.c2p(a,0), DL)
        b_label = MathTex(r"\text{b}", color=C_GREEN).scale(0.7).next_to(axes.c2p(b,0), DR)

        # Horizontal lines
        fa_line = DashedLine(
            axes.c2p(0,fa),
            axes.c2p(3.1,fa),
            color=C_RED
        ).set_opacity(0.6)

        fb_line = DashedLine(
            axes.c2p(0,fb),
            axes.c2p(3.1,fb),
            color=C_RED
        ).set_opacity(0.6)

        fa_label = MathTex("f(a)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fa), LEFT)
        fb_label = MathTex("f(b)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fb), LEFT)

        # Highlight region
        rect_tracker = ValueTracker(0)
        rect_height = axes.y_axis.n2p(fb)[1] - axes.y_axis.n2p(fa)[1]

        band = always_redraw(
            lambda:
            Rectangle(
            width=axes.x_length,
            height=rect_tracker.get_value(),
            fill_color=C_MAGENTA,
            fill_opacity=0.2,
            stroke_width=0
        ).next_to(fa_line,UP,buff=0)
        )

        ##tracked point
        p_tracker = ValueTracker(a)
        p_tracker_dot = always_redraw(
            lambda: Dot(axes.c2p(p_tracker.get_value(),f(p_tracker.get_value())))
        )

        p_tracker_dot_h_line = always_redraw(
            lambda: axes.get_horizontal_line(p_tracker_dot.get_center()).set_color(C_BRIGHT_BLUE)
        )

        ## pinned texts

        pinned_text_1 = MathTex(r"\textbf{f is continuous}",font_size=32).to_corner(UL,buff=0.5)
        ## the animations start here.
        self.add(axes,a_label,b_label,a_line,b_line,graph,pinned_text_1)
        self.play(Write(text_1))
        self.wait(2)

        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth)
        self.wait(2)
        self.play(ReplacementTransform(text_2,text_3),rate_func=smooth,run_time=2)
        self.play(Create(fa_line),run_time=2,rate_func=smooth)
        self.play(FadeIn(fa_label),rate_func=smooth)
        self.wait(2)
        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth,run_time=2)
        self.play(Create(fb_line),run_time=2,rate_func=smooth)
        self.play(FadeIn(fb_label),rate_func=smooth)
        self.wait(2)

        self.play(FadeIn(band),rate_func=smooth)
        self.play(rect_tracker.animate.set_value(rect_height),run_time=5,rate_func=smooth)

        self.wait(4)
        self.play(Create(p_tracker_dot),Create(p_tracker_dot_h_line),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_4,text_5),run_time=2,rate_func=smooth)
        self.play(p_tracker.animate.set_value(b),run_time=7,rate_func=smooth)

        self.wait(4)
        self.play(FadeOut(p_tracker_dot),FadeOut(p_tracker_dot_h_line))
        self.play(ReplacementTransform(text_5,text_6),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_6,text_7),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(Write(text_8),rate_func=smooth)
        self.play(Indicate(VGroup(band,fa_line,fb_line)),run_time=5)
        self.wait(2)




class bijective(Scene):
    def construct(self):

        ###texts for the graph
        text_1 = VGroup(
            MathTex(r"\text{Every value from [f(a),f(b)] is taken exactly once}",font_size=32),
            MathTex(r"\text{because of injectivity.}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.5)
        
        text_2 = VGroup(
            MathTex(r"\text{Because f is injective and surjective onto}",font_size=32),
            MathTex(r"\text{[f(a),f(b)], f is bijective}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.5)

        text_3 = VGroup(
            MathTex(r"\text{Because f is bijective, an inverse function}",font_size=32),
            MathTex(r"f^{-1} \text{ exists}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.5)

        text_4 = VGroup(
            MathTex(r"\text{we find the inverse function by reflecting the}",font_size=32),
            MathTex(r"\text{function across the diagonal since } f^{-1}(f(x))=x",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.5)

        text_5 = MathTex(r"\text{Note that } f^{-1} \text{ is also continuous}",font_size=32).to_corner(UP,buff=0.5)

        text_6 = MathTex(r"\text{And it is also monotonous}",font_size=32).to_corner(UP,buff=0.5)

        text_7 = MathTex(r"\text{Hence we can say } f^{-1} \text{ is continuous and monotonous}",font_size=32).to_corner(UP,buff=0.5)

        ###Axes and graphs

        axes = Axes(
            x_range=[0, 3.1, 0.5],
            y_range=[-1, 0.85, 0.25],
            x_length=5,
            y_length=4,
            axis_config={
                "color": C_AXIS,
                "include_ticks": False,
                "tip_shape": StealthTip,
                "tip_width": 0.2
            }
        ).shift(DOWN)

        #axes 2
        axes_2 = Axes(
            x_range=[-3.1, 3.1, 0.5],
            y_range=[-3.1, 3.1, 0.5],
            x_length=6.2,
            y_length=6.2,
            axis_config={
                "color": C_AXIS,
                "include_ticks": False,
                "tip_shape": StealthTip,
                "tip_width": 0.2
            }
        ).shift(DOWN)

        # --- LABELS -------------------------------------------------------

        x_label = MathTex(r"\text{x}").scale(0.9).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex(r"\text{y}").scale(0.9).next_to(axes.y_axis.get_end(), UP)

        x_label_2 = MathTex(r"\text{x}").scale(0.9).next_to(axes_2.x_axis.get_end(), RIGHT)
        y_label_2 = MathTex(r"\text{y}").scale(0.9).next_to(axes_2.y_axis.get_end(), UP)

        # functions

        def f(x):
            return 0.9*np.log(x + 0.35) - 0.4
        def f_inv(x):
            return np.exp((x + 0.4) / 0.9) - 0.35

        # original graph

        graph_f_1 = axes.plot(
            f,
            x_range=[0.2, 2.9],
            color=C_BRIGHT_BLUE,
            stroke_width=4
        )

        graph_f_2 = axes_2.plot(
            f,
            x_range=[0.2, 2.9],
            color=C_BRIGHT_BLUE,
            stroke_width=4
        )

        # Reflected graph

        graph_f_inv = graph_f_2.copy().apply_function(
            lambda p: axes_2.c2p(*axes_2.p2c(p)[::-1])
        )

        # Reflection line

        reflector = axes_2.plot(
            lambda x: x,
            x_range=[-1.5, 3],
            color=C_MAGENTA,
            stroke_width=2
        )

        ###tracker for inverse function graph
        p_tracker = ValueTracker(-1)

        p_tracker_dot = always_redraw(
            lambda: Dot(axes_2.c2p(p_tracker.get_value(), f_inv(p_tracker.get_value())), color=C_BRIGHT_BLUE)
        )
        
        p_tracker_dot_h_line = always_redraw(
            lambda: DashedLine(
                axes_2.c2p(0, f_inv(p_tracker.get_value())),
                p_tracker_dot.get_center(),
                color=C_BRIGHT_BLUE,
                stroke_width=4
            )
        )
        
        # a and b
        a = 0.6
        b = 2.6

        fa = f(a)
        fb = f(b)

        # Vertical dashed lines
        a_line = DashedLine(
            axes.c2p(a,-1),
            axes.c2p(a,0.85),
            color=C_GREEN
        )

        b_line = DashedLine(
            axes.c2p(b,-1),
            axes.c2p(b,0.85),
            color=C_GREEN
        )

        a_label = MathTex(r"\text{a}", color=C_GREEN).scale(0.7).next_to(axes.c2p(a,0), DL)
        b_label = MathTex(r"\text{b}", color=C_GREEN).scale(0.7).next_to(axes.c2p(b,0), DR)

        # Horizontal lines
        fa_line = DashedLine(
            axes.c2p(0,fa),
            axes.c2p(3.1,fa),
            color=C_RED
        ).set_opacity(0.6)

        fb_line = DashedLine(
            axes.c2p(0,fb),
            axes.c2p(3.1,fb),
            color=C_RED
        ).set_opacity(0.6)

        fa_label = MathTex("f(a)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fa), LEFT)
        fb_label = MathTex("f(b)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fb), LEFT)


        ### for the band and trackers before reflection
                # Highlight region
        rect_tracker = ValueTracker(0)
        rect_height = axes.y_axis.n2p(fb)[1] - axes.y_axis.n2p(fa)[1]

        band = always_redraw(
            lambda:
            Rectangle(
            width=axes.x_length,
            height=rect_tracker.get_value(),
            fill_color=C_MAGENTA,
            fill_opacity=0.2,
            stroke_width=0
        ).next_to(fa_line,UP,buff=0)
        )

        ##tracked point
        p_tracker_1 = ValueTracker(a)
        p_tracker_dot_1 = always_redraw(
            lambda: Dot(axes.c2p(p_tracker_1.get_value(),f(p_tracker_1.get_value())))
        )

        p_tracker_dot_h_line_1 = always_redraw(
            lambda: axes.get_horizontal_line(p_tracker_dot_1.get_center()).set_color(C_BRIGHT_BLUE)
        )

        
        ###Animated graphs and texts 

        self.add(graph_f_1, axes, x_label, y_label)
        self.play(Create(a_line),Create(b_line),run_time=2,rate_func=smooth)
        self.play(Create(a_label),Create(b_label),run_time=2,rate_func=smooth)
        self.wait(2)
        self.play(Create(fa_line),Create(fb_line),run_time=2,rate_func=smooth)
        self.play(Create(fa_label),Create(fb_label),run_time=2,rate_func=smooth)
        self.wait(2)
        self.play(Write(text_1),rate_func=smooth)
        self.play(Create(p_tracker_dot_1),Create(p_tracker_dot_h_line_1),run_time=2,rate_func=smooth)
        self.play(p_tracker_1.animate.set_value(b),run_time=7,rate_func=smooth)
        self.wait(2)
        
        self.play(Uncreate(p_tracker_dot_1),Uncreate(p_tracker_dot_h_line_1),run_time=2,rate_func=smooth)
        self.wait(5)
        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth,run_time=2)
        self.play(Create(band),run_time=1,rate_func=smooth)
        self.play(rect_tracker.animate.set_value(rect_height),run_time=7,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeOut(VGroup(a_line,a_label,fa_line,fa_label,fb_line,fb_label,b_line,b_label,band)),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(
            Transform(graph_f_1, graph_f_2),
            Transform(axes, axes_2),
            Transform(x_label, x_label_2),
            Transform(y_label, y_label_2),
            run_time=2,
            rate_func=smooth
        )

        self.play(Create(reflector),run_time=4,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth,run_time=2)
        self.play(Create(graph_f_inv),run_time=10,rate_func=smooth)
        self.play(ReplacementTransform(text_4,text_5),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(text_5,text_6),rate_func=smooth,run_time=2)
        self.wait(1)
        self.play(Create(p_tracker_dot),Create(p_tracker_dot_h_line),run_time=2,rate_func=smooth)
        self.play(p_tracker.animate.set_value(0.5),run_time=7,rate_func=smooth)
        self.wait(2)
        self.play(FadeOut(p_tracker_dot),FadeOut(p_tracker_dot_h_line))
        self.wait(2)
        self.play(ReplacementTransform(text_6,text_7),rate_func=smooth,run_time=2)
        self.wait(4)



class counter_example(Scene):
    def construct(self):
        ##texts for the graph

        text_1 = MathTex(r"\text{at x=a, f(a) and at x=b,f(b)}}",font_size=32).to_corner(UP,buff=0.5)
        text_2 = MathTex(r"\text{Here is the [f(a),f(b)] range}",font_size=32).to_corner(UP,buff=0.5)

        text_3 = MathTex(r"\text{Given a horizontal line}",font_size=32).to_corner(UP,buff=0.5)

        text_4 = MathTex(r"\text{Note that it crosses through} \textbf{ multiple y-values}",font_size=32).to_corner(UP,buff=0.5)

        text_5 = MathTex(r"\text{this implies that the function is not injective}",font_size=32).to_corner(UP,buff=0.5)

        text_6 = MathTex(r"\text{Here is the min and max of this function}",font_size=32).to_corner(UP,buff=0.5)

        text_7 = VGroup(
            MathTex(r"\text{if the function is } \textbf{not monotonous } \text{,it jumps }",font_size=32),
            MathTex(r"\text{ out of the [f(a),f(b)] range as seen here}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT).to_corner(UP,buff=0.5)

        text_8 = VGroup(
            MathTex(r"\text{Since the im(f)=[max(f),min(f)] is larger than [f(a),f(b)],}",font_size=32),
            MathTex(r"\text{the function is not surjective}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT).to_corner(UP,buff=0.5)

        text_9 = VGroup(
            MathTex(r"\text{both monotonocity and continuity are required}",font_size=32),
            MathTex(r"\text{Hence the function not bijective}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT).to_corner(UP,buff=0.5)
        

        # Axes
        axes = Axes(
            x_range=[0, 3.1, 0.5],
            y_range=[-1.6, 1.3, 0.5],
            x_length=6,
            y_length=4,
            axis_config={
                "color": C_AXIS,
                "include_ticks": False,
                "tip_shape": StealthTip,
                "tip_width": 0.2
            }
        )

        x_label = MathTex("x").scale(0.7).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("y").scale(0.7).next_to(axes.y_axis.get_end(), UP)

        # Function
        def f(x):
            return 0.9*np.sin(np.deg2rad(200*(x-1.0))) * np.exp(-0.35*(x-1.6)) + 0.15*(x-1.4)

        graph = axes.plot(
            f,
            x_range=[0.2, 2.9],
            color=C_BLUE,
            stroke_width=4
        )

        # a and b
        a = 0.5
        b = 2.4

        fa = f(a)
        fb = f(b)

        # Vertical dashed lines
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

        a_label = MathTex("a", color=C_GREEN).scale(0.7).next_to(axes.c2p(a,0), DL,buff=0.1)
        b_label = MathTex("b", color=C_GREEN).scale(0.7).next_to(axes.c2p(b,0), DR,buff=0.1)

        # Horizontal reference lines
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

        horizontal_line = DashedLine(
            axes.c2p(0, 0.1),
            axes.c2p(3.1, 0.1),
            color=C_MAGENTA
        )

        max_line = DashedLine(
            axes.c2p(0, max_y),
            axes.c2p(3.1, max_y),
            color=WHITE
        )
        ##points of intersection with the horizontal line
        p_1 = Dot(axes.c2p(1.0404,0.1),color=WHITE)
        p_2 = Dot(axes.c2p(1.8907,0.1),color=WHITE)

        # Labels
        fa_label = MathTex("f(a)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fa), LEFT,buff=0.1)
        fb_label = MathTex("f(b)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fb), LEFT,buff=0.1)

        max_label = MathTex(r"\max(f)", color=WHITE).scale(0.7).next_to(axes.c2p(0,max_y), LEFT,buff=0.1)
        min_label = MathTex(r"\min(f)=", color=WHITE).scale(0.7).next_to(fa_label, LEFT,buff=0.1)
        # Shaded regions
        band1 = Rectangle(
            width=axes.x_length,
            height=axes.y_axis.n2p(fb)[1] - axes.y_axis.n2p(fa)[1],
            fill_color=C_MAGENTA,
            fill_opacity=0.2,
            stroke_width=0
        ).move_to(axes.c2p(1.55,(fa+fb)/2))

        band2 = Rectangle(
            width=axes.x_length,
            height=axes.y_axis.n2p(max_y)[1] - axes.y_axis.n2p(fb)[1],
            fill_color=WHITE,
            fill_opacity=0.2,
            stroke_width=0
        ).move_to(axes.c2p(1.55,(fb+max_y)/2))

        # Add everything
        self.add(axes,x_label,y_label)
        self.wait(1)
        self.play(Create(graph),run_time=10,rate_func=smooth)
        self.wait(1)
        self.play(Write(text_1))
        self.play(Create(a_line),Create(b_line),run_time=2,rate_func=smooth)
        self.play(Create(a_label),Create(b_label),run_time=2,rate_func=smooth)
        self.play(Create(fa_line),Create(fb_line),run_time=2,rate_func=smooth)
        self.play(Create(fa_label),Create(fb_label),run_time=2,rate_func=smooth)
       
        self.wait(2)
        self.play(ReplacementTransform(text_1,text_2),run_time=2,rate_func=smooth)
        self.play(Create(band1),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3),run_time=2,rate_func=smooth)
        self.play(Create(horizontal_line),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_3,text_4),run_time=2,rate_func=smooth)
        self.play(Create(p_1),Create(p_2),run_time=2,rate_func=smooth)
        self.wait(1)
        self.play(Indicate(VGroup(p_1,p_2),run_time=2))
        self.wait(5)

        self.play(Uncreate(horizontal_line),Uncreate(VGroup(p_1,p_2)),run_time=2,rate_func=smooth)
        self.play(ReplacementTransform(text_4,text_5),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_5,text_6),run_time=2,rate_func=smooth)
        self.play(Create(max_line),run_time=2,rate_func=smooth)
        self.play(Write(max_label),Write(min_label),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_6,text_7),run_time=2,rate_func=smooth)
        self.play(Create(band2),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_7,text_8),run_time=2,rate_func=smooth)

        self.play(Indicate(VGroup(max_line,fb_line,band1,band2),color=YELLOW),run_time=4)
        self.play(Indicate(VGroup(fa_line,fb_line,band1),color=BLUE),run_time=4)

        self.wait(4)
        self.play(ReplacementTransform(text_8,text_9),run_time=2,rate_func=smooth)
        self.play(Indicate(graph),run_time=4)
        self.wait(4)





        

