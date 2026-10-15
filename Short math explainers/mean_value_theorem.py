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

class MeanValueTheorem(Scene):
    def construct(self):
        ##the texts for the theorem
        title = MathTex(r"\text{The Mean Value Theorem}",font_size=40)

        text_1 = MathTex(r"\text{Given an interval of [a,b]}",font_size=32).to_corner(UP,buff=0.2)

        text_2 = VGroup(
            MathTex(r"\text{Let f[a,b] } \to \mathbb{R} \text{ be defined on a compact interval}",font_size=32),
            MathTex(r"\text{i.e. closed and bounded}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_3 = MathTex(r"\text{f[a,b] also has the following properties}",font_size=32).to_corner(UP,buff=0.5)
       
        text_4 = VGroup( 
            MathTex(r"\text{1. f is continuous on [a,b]}",font_size=32),
            MathTex(r"\text{2. f is differentiable on (a,b)}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_5 = MathTex(r"\text{There exists some C in [a,b]}",font_size=32).to_corner(UP,buff=0.2)
        text_6 = VGroup(
            MathTex(r"\text{such that the} \textbf{ slope of the secant through (a,f(a)) and (b,f(b))}",font_size=32),
            MathTex(r"\text{is equal to the} \textbf{ slope of the tangent at (c,f(c))}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_7 = MathTex(r"\text{Mathematically, } f'(c) = \frac{f(b)-f(a)}{b-a}",font_size=32).to_corner(UP,buff=0.2)
       
        text_8 = MathTex(r"\text{We can also say...}",font_size=32).to_corner(UP,buff=0.2)

        text_9 = VGroup(
            MathTex(r"\text{The instanstaneous rate of change,}",r"\textbf{ f'(c)}",r"\text{ thus matches}",font_size=32),
            MathTex(r"\text{the average rate of  change, }",r"\frac{f(b)-f(a)}{b-a}",r"\text{ at some point C in [a,b]}",font_size=32),
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_10 = VGroup(
            MathTex(r"\text{Note that depending the shape of the graph}",font_size=32),
            MathTex(r"\text{there can be multiple values of C}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_11 = MathTex(r"\text{for instance...}",font_size=32).to_corner(UP,buff=0.2)

        text_12 = MathTex(r"\text{Here is the secant line for this graph}",font_size=32).to_corner(UP,buff=0.2)

        text_13 = VGroup(
            MathTex(r"\text{Here we have two points whose gradients}",font_size=32),
            MathTex(r"\text{are equal to the gradient of the secant line}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_14 = VGroup(
            MathTex(r"\text{Hence we can say there exists}",font_size=32),
            MathTex(r"\textbf{at least one C in [a,b]}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        # Axes
        axes = Axes(
            x_range=[0, 4.6, 0.5],
            y_range=[0, 2.6, 0.5],
            x_length=9,
            y_length=5,
            axis_config={"color": C_AXIS,
            "tip_shape":StealthTip,
            "tip_length":0.2,
            "tip_width":0.2,
            "include_ticks":False
            }
        ).shift(DOWN*0.5)

        x_label = MathTex(r"\text{x}").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex(r"\text{y}").next_to(axes.y_axis.get_end(), UP)

        # Function
        def f(x):
            return 1.2 - 0.6*x + 0.2*x**2
        def df(x):
            return -0.6 + 0.4*x

        graph = axes.plot(
            f,
            x_range=[0.1, 4.3],
            color=C_BRIGHT_BLUE,
            stroke_width=4
        )

        # a and b
        a = 0.8
        b = 3.8

        fa = f(a)
        fb = f(b)

        # Vertical dashed lines
        a_line = DashedLine(axes.c2p(a,0), axes.c2p(a,2.5), color=C_GREEN)
        b_line = DashedLine(axes.c2p(b,0), axes.c2p(b,2.5), color=C_GREEN)

        a_label = MathTex("a", color=C_GREEN).scale(0.7).next_to(axes.c2p(a,0), DOWN)
        b_label = MathTex("b", color=C_GREEN).scale(0.7).next_to(axes.c2p(b,0), DOWN)

        # Points on curve
        point_a = Dot(axes.c2p(a, fa), color=C_MAGENTA).set_z_index(2)
        point_b = Dot(axes.c2p(b, fb), color=C_MAGENTA).set_z_index(2)  

        # Horizontal projections
        proj_a = DashedLine(axes.c2p(a,fa), axes.c2p(0,fa), color=C_RED)
        proj_b = DashedLine(axes.c2p(b,fb), axes.c2p(0,fb), color=C_RED)

        fa_label = MathTex("f(a)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fa), LEFT)
        fb_label = MathTex("f(b)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fb), LEFT)

        # Secant slope
        m_sec = (fb - fa) / (b - a)

        # Secant line
        secant = axes.plot(
            lambda x: fa + m_sec*(x - a),
            x_range=[a-0.3, b+0.3],
            color=C_MAGENTA,
            stroke_width=4
        ).set_opacity(0.8)

        secant_copy = secant.copy().set_color(C_ORANGE).set_z_index(2)
        # Label for slope
        xmid = 0.5*(a+b)
        ymid = fa + m_sec*(xmid - a)

        slope_label = MathTex(
            r"\frac{f(b)-f(a)}{b-a}",
            color=C_MAGENTA
        ).scale(0.5).next_to(axes.c2p(xmid, ymid), UP).shift(RIGHT*0.5)

        # Point c
        c = ValueTracker(a)

        c_point = always_redraw(
            lambda: Dot(axes.c2p(c.get_value(),f(c.get_value())), color=WHITE).set_z_index(2)
        )

        c_line = always_redraw(
            lambda: DashedLine(axes.c2p(c.get_value(),0), axes.c2p(c.get_value(),f(c.get_value())), color=WHITE)
        )

        c_label = always_redraw(
            lambda: MathTex("c", color=WHITE).scale(0.7).next_to(axes.c2p(c.get_value(),0), DOWN)
        )

        # Tangent line (same slope as secant)
        tangent = always_redraw(
            lambda: axes.plot(
            lambda x: f(c.get_value()) + df(c.get_value())*(x - c.get_value()),
            x_range=[c.get_value()-0.8, c.get_value()+0.8],
            color=C_MAGENTA,
            stroke_width=4
        ))

        

        # Final equality label
        derivative_label = MathTex(
            r"f'(c)",
            color=WHITE
        ).scale(0.5)

        def position(direction,mob):
            def update(mob):
                mob.next_to(axes.c2p(c.get_value(),f(c.get_value())), direction)
            return update

        # The animation starts here
        self.play(FadeIn(title,shift=UP*0.5),run_time=2,rate_func=smooth)
        self.wait(2)
        
        self.play(FadeOut(title,shift=DOWN*0.5),run_time=2,rate_func=smooth)

        self.wait(2)
        self.play(FadeIn(VGroup(axes,x_label,y_label)),rate_func=smooth)
        self.wait(2)
        self.play(Write(text_1),rate_func=smooth,run_time=2)
        self.play(Create(a_line),Create(b_line),FadeIn(a_label),FadeIn(b_label),rate_func=smooth,run_time=2)
        
        self.wait(4)
        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth,run_time=2)
        self.play(Create(graph),run_time=10,rate_func=smooth)
        self.play(FadeIn(point_a),FadeIn(point_b),rate_func=smooth,run_time=2)
        self.play(Create(proj_a),Create(proj_b),FadeIn(fa_label),FadeIn(fb_label),rate_func=smooth,run_time=4)
        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeOut(text_3),rate_func=smooth,run_time=2)
        self.play(Write(text_4[0]),rate_func=smooth,run_time=2)
        self.wait(1)
        self.play(Write(text_4[1]),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(text_4,text_5),run_time=2,rate_func=smooth)
        self.play(FadeIn(c_point),FadeIn(c_label),Create(c_line),Create(tangent),rate_func=smooth,run_time=2)
        self.wait(2)

        self.play(c.animate.set_value(b),run_time=4,rate_func=smooth)
        self.play(c.animate.set_value(a),run_time=4,rate_func=smooth)
        self.play(c.animate.set_value(2.5),run_time=4,rate_func=smooth)
        self.play(c.animate.set_value(2.3),run_time=4,rate_func=smooth) 
        self.wait(4)

        #code
        tangent_copy = tangent.copy().set_color(C_ORANGE).set_z_index(2)
        #code

        self.play(ReplacementTransform(text_5,text_6[0]),run_time=2,rate_func=smooth)
        self.play(Create(secant),rate_func=smooth,run_time=5)
        self.play(Write(slope_label),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(Write(text_6[1]),rate_func=smooth,run_time=2)

        derivative_label.add_updater(position(DR,derivative_label))

        self.play(Write(derivative_label),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(ReplacementTransform(text_6,text_7),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(ReplacementTransform(text_7,text_8),run_time=2,rate_func=smooth)
        self.wait(4)

        self.play(FadeOut(text_8),run_time=2,rate_func=smooth)
        self.wait(2)

        self.play(Write(text_9[0][0]),rate_func=smooth,run_time=2)
        self.play(Create(tangent_copy),run_time=5,rate_func=smooth)
        self.wait(2)

        self.play(ReplacementTransform(derivative_label.copy(),text_9[0][1]),run_time=2,rate_func=smooth)
        self.play(Write(text_9[0][2]),rate_func=smooth)
        self.wait(4)

        self.play(FadeOut(tangent_copy),run_time=2,rate_func=smooth)
        self.play(Write(text_9[1][0]),run_time=2,rate_func=smooth)
        
        self.play(Create(secant_copy),run_time=5,rate_func=smooth)
        self.wait(2)
        self.play(ReplacementTransform(slope_label.copy(),text_9[1][1]),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(FadeOut(secant_copy),run_time=2,rate_func=smooth)
        self.play(Write(text_9[1][2]),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(text_9,text_10),run_time=2,rate_func=smooth) 
        self.wait(4)

        self.play(FadeOut(VGroup(graph,a_line,b_line,a_label,b_label,point_a,
        point_b,proj_a,proj_b,fa_label,fb_label,secant,slope_label,c_line,c_point,
        c_label,tangent,derivative_label,text_10)),run_time=2,rate_func=smooth)

        #### this is the part for the second graph.
        # Function
        def f_2(x):
            return 1.2 + 0.3*x + 0.3*np.sin(2*x)
        
        def df_2(x):
            return 0.3 + 0.6*np.cos(2*x)

        graph_2 = axes.plot(
            f_2,
            x_range=[0, 4.3],
            color=C_BRIGHT_BLUE,
            stroke_width=4
        )

        # a and b
        a_1 = 0
        b_1 = np.pi

        fa_1 = f_2(a_1)
        fb_1 = f_2(b_1)

        # Vertical lines
        a_line_1 = DashedLine(axes.c2p(a_1,0), axes.c2p(a_1,2.5), color=C_GREEN)
        b_line_1 = DashedLine(axes.c2p(b_1,0), axes.c2p(b_1,2.5), color=C_GREEN)

        a_label_1= MathTex("a", color=C_GREEN).scale(0.7).next_to(axes.c2p(a_1,0), DOWN)
        b_label_1 = MathTex("b", color=C_GREEN).scale(0.7).next_to(axes.c2p(b_1,0), DOWN)

        # Points at a and b
        point_a_1 = Dot(axes.c2p(a_1,fa_1), color=C_MAGENTA).set_z_index(2)
        point_b_1 = Dot(axes.c2p(b_1,fb_1), color=C_MAGENTA).set_z_index(2)

        # Horizontal projections
        proj_a_1 = DashedLine(axes.c2p(a_1,fa_1), axes.c2p(0,fa_1), color=C_RED)
        proj_b_1 = DashedLine(axes.c2p(b_1,fb_1), axes.c2p(0,fb_1), color=C_RED)

        fa_label_1 = MathTex("f(a)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fa_1), LEFT)
        fb_label_1 = MathTex("f(b)", color=C_RED).scale(0.7).next_to(axes.c2p(0,fb_1), LEFT)

        # Secant slope
        m_sec_1 = (fb_1 - fa_1) / (b_1 - a_1)

        # Secant line
        secant_1 = axes.plot(
            lambda x: fa_1 + m_sec_1*(x - a_1),
            x_range=[a_1-0.3, b_1+0.3],
            color=C_MAGENTA,
            stroke_width=4
        ).set_opacity(0.8)

        # Label for slope
        xmid_1 = 0.5*(a_1+b_1)
        ymid_1 = fa_1 + m_sec_1*(xmid_1 - a_1)

        slope_label_1 = MathTex(
            r"\frac{f(b)-f(a)}{b-a}",
            color=C_MAGENTA
        ).scale(0.5).next_to(axes.c2p(xmid_1, ymid_1), UP).shift(RIGHT*0.5)
        
        # c1 and c2
        c1 = np.pi/4
        c2 = 3*np.pi/4

        c_tracker_1 = ValueTracker(a_1)
        c_tracker_2 = ValueTracker(a_1)


        fc1 = f_2(c1)
        fc2 = f_2(c2)

        # Tangent lines (parallel to secant)
        tangent1 = always_redraw(
            lambda: axes.plot(
            lambda x: f_2(c_tracker_1.get_value()) + df_2(c_tracker_1.get_value())*(x - c_tracker_1.get_value()),
            x_range=[c_tracker_1.get_value()-0.8, c_tracker_1.get_value()+0.8],
            color=C_MAGENTA,
            stroke_width=4
        )
        )
        tangent2 = always_redraw(
            lambda: axes.plot(
            lambda x: f_2(c_tracker_2.get_value()) + df_2(c_tracker_2.get_value())*(x - c_tracker_2.get_value()),
            x_range=[c_tracker_2.get_value()-0.8, c_tracker_2.get_value()+0.8],
            color=C_MAGENTA,
            stroke_width=4
        )
        )

        # Vertical lines for c1, c2
        c1_line = always_redraw(
            lambda: DashedLine(axes.c2p(c_tracker_1.get_value(),f_2(c_tracker_1.get_value())), axes.c2p(c_tracker_1.get_value(),0), color=WHITE)
        )

        c2_line = always_redraw(
            lambda: DashedLine(axes.c2p(c_tracker_2.get_value(),f_2(c_tracker_2.get_value())), axes.c2p(c_tracker_2.get_value(),0), color=WHITE)
        )

        # Points
        c1_point = always_redraw(
            lambda: Dot(axes.c2p(c_tracker_1.get_value(),f_2(c_tracker_1.get_value())), color=WHITE).set_z_index(2)
        )
        c2_point = always_redraw(
            lambda: Dot(axes.c2p(c_tracker_2.get_value(),f_2(c_tracker_2.get_value())), color=WHITE).set_z_index(2)
        )

        # Labels
        c1_label = always_redraw(
            lambda: MathTex("c_1", color=WHITE).scale(0.7).next_to(axes.c2p(c_tracker_1.get_value(),0), DOWN)
        )
        c2_label = always_redraw(
            lambda: MathTex("c_2", color=WHITE).scale(0.7).next_to(axes.c2p(c_tracker_2.get_value(),0), DOWN)
        )

        f_c1_label = always_redraw(
            lambda: MathTex("f(c_1)", color=WHITE).scale(0.5).next_to(axes.c2p(c_tracker_1.get_value(),f_2(c_tracker_1.get_value())), UP,buff=0.3)
        )
        f_c2_label = always_redraw(
            lambda: MathTex("f(c_2)", color=WHITE).scale(0.5).next_to(axes.c2p(c_tracker_2.get_value(),f_2(c_tracker_2.get_value())), DR,buff=0.3)
        )


        #### animations for the second graph
        self.play(Write(text_11),run_time=2,rate_func=smooth)
        self.wait(2)
        self.play(Create(a_line_1),Create(b_line_1))
        self.play(FadeIn(a_label_1),FadeIn(b_label_1))
        self.wait(1)
        self.play(Create(graph_2),run_time=10,rate_func=smooth)
        self.play(Create(point_a_1),Create(point_b_1))
        self.play(Create(proj_a_1),Create(proj_b_1),run_time=2,rate_func=smooth)
        self.play(FadeIn(fa_label_1),FadeIn(fb_label_1))
        self.wait(4)
        self.play(ReplacementTransform(text_11,text_12),run_time=2,rate_func=smooth)
        self.play(Create(secant_1),run_time=5,rate_func=smooth)
        self.play(Write(slope_label_1),run_time=2,rate_func=smooth)
        
        self.wait(4)
        self.play(ReplacementTransform(text_12,text_13),run_time=2,rate_func=smooth)
        
        
        self.play(Create(c1_point),Create(c2_point),run_time=2,rate_func=smooth)
        self.play(Create(c1_line),Create(c2_line),run_time=2,rate_func=smooth)
        self.play(FadeIn(c1_label),FadeIn(c2_label),run_time=2,rate_func=smooth)
        self.play(FadeIn(f_c1_label),FadeIn(f_c2_label),run_time=2,rate_func=smooth)
        self.wait(2)
        self.play(Create(tangent1),Create(tangent2),run_time=5,rate_func=smooth)
        self.play(c_tracker_1.animate.set_value(c1),c_tracker_2.animate.set_value(c2),run_time=10,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_13,text_14),run_time=2,rate_func=smooth)
        self.wait(6)
        self.play(FadeOut(*self.mobjects),rate_func=smooth,run_time=2)
        self.wait(2)
