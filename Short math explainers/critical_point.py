from typing_extensions import runtime
from manim import *
import numpy as np
from sympy import symbols, diff

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


class critical_points(Scene):
    def construct(self):
        ###texts
        text_1 = MathTex(r"\text{Given a function}",font_size=32).to_corner(UP,buff=0.2)
        text_2 = MathTex(r"\text{The function has multiple maxima and minima}",font_size=32).to_corner(UP,buff=0.2)
        
        text_3 = VGroup(
            MathTex(r"\text{We can get the derivative at any point by taking}",font_size=32),
            MathTex(r"\text{the slope of the tangent line at that point}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_4 = MathTex(r"\text{The slope of the tangent is simply } \frac{\Delta y}{\Delta x}",font_size=32).to_corner(UP,buff=0.2)

        text_5 = MathTex(r"\text{But at turning points, } \Delta y = 0 \text{, which implies } \frac{\Delta y}{\Delta x} = 0",font_size=32).to_corner(UP,buff=0.2)

        text_6 = MathTex(r"\text{So the derivatives at a maxima and minima equals zero}",font_size=32).to_corner(UP,buff=0.2).to_corner(UP,buff=0.2)

        text_7 = VGroup(
            MathTex(r"\text{Note that the functions takes a convex shape around a Maxima}",font_size=32),
            MathTex(r"\text{and the second derivative is } \textbf{negative} \text{ at a Maxima}",font_size=32 )
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_8 = VGroup(
            MathTex(r"\text{While, for the Minima, the function takes a } \textbf{concave shape} \text{ around it}",font_size=32),
            MathTex(r"\text{and the second derivative is } \textbf{positive} \text{ at a Minima}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)
        

        ###axis start here
        axes_1 = Axes(
            x_range = [1/4*PI,4*PI,PI/2],
            y_range = [-1,1],
            x_length = 8,
            y_length = 5.5,
            axis_config={
                "include_numbers":False,
                "include_ticks":False
            },
            tips=False,
        ).shift(DOWN*0.5)

        ### Labels
        x_label_1 =  axes_1.get_x_axis_label(r"\text{x}",edge=RIGHT)

        y_label_1 = axes_1.get_y_axis_label(r"\text{y}",edge=UP)        

        def f(x):
            return np.sin(x)

        graph_1 = axes_1.plot(f, x_range=[1/4*PI,4*PI], color=C_BRIGHT_BLUE)
        def df(x):
            return np.cos(x)
        
        ### This is the graph of the second derivative


        def ddf(x):
            return -np.sin(x)
    
        ### dots at maxima and minima of the sin function
        dot_1 = Dot(axes_1.c2p(PI/2,1),color=C_RED)
        dot_2 = Dot(axes_1.c2p(3*PI/2,-1),color=C_RED)
        dot_3 = Dot(axes_1.c2p(5*PI/2,1),color=C_RED)
        dot_4 = Dot(axes_1.c2p(7*PI/2,-1),color=C_RED)

        dots = VGroup(dot_1,dot_2,dot_3,dot_4)
        surrounding_rect = VGroup()

        for i in dots:
            rec = SurroundingRectangle(i,color=C_RED,buff=0.1)
            surrounding_rect.add(rec)
        
        ### Groups of axes and graphs
    
        group_1 = VGroup(axes_1,x_label_1,y_label_1,graph_1,dots)

        #### The code for the tangent
        tracker = ValueTracker(PI/3)
        h = PI/6  # dx width

        dx_line = always_redraw(
            lambda: Line(
                axes_1.c2p(tracker.get_value(), f(tracker.get_value())),
                axes_1.c2p(tracker.get_value() + h, f(tracker.get_value())),
                color=C_GREEN
            )
        )

        dy_line = always_redraw(
            lambda: Line(
                axes_1.c2p(tracker.get_value() + h, f(tracker.get_value())),
                axes_1.c2p(tracker.get_value() + h, f(tracker.get_value() + h)),
                color=C_GREEN
            )
        )

        tangent = always_redraw(
            lambda: axes_1.plot(
                lambda x: df(tracker.get_value()) * (x - tracker.get_value()) + f(tracker.get_value()),
                x_range=[tracker.get_value() - 2*h, tracker.get_value() + 2*h],
                color=C_MAGENTA
            )
        )
        tangent_point = always_redraw(
            lambda: Dot(axes_1.c2p(tracker.get_value(), f(tracker.get_value())),color=C_RED)
        )
        dx_label = MathTex(r"\Delta x",font_size=24)
        dy_label = MathTex(r"\Delta y",font_size=24)


        ###This part handles the 
        tangent_group = Group()
        positions = [PI/2,3/2*PI,7/2*PI]

       
        tangent_tracker_1 = ValueTracker(5/2*PI)
        tangent_tracker_2 = ValueTracker(5/2*PI)
        tangent_tracker_3 = ValueTracker(5/2*PI)

        tangent_line_1 = always_redraw(
                lambda: axes_1.plot(
                    lambda x: df(tangent_tracker_1.get_value()) * (x - tangent_tracker_1.get_value()) + f(tangent_tracker_1.get_value()),
                    x_range=[tangent_tracker_1.get_value() - 2*h, tangent_tracker_1.get_value() + 2*h],
                    color=C_MAGENTA
                )
            )
        tangent_line_2 = always_redraw(
                lambda: axes_1.plot(
                    lambda x: df(tangent_tracker_2.get_value()) * (x - tangent_tracker_2.get_value()) + f(tangent_tracker_2.get_value()),
                    x_range=[tangent_tracker_2.get_value() - 2*h, tangent_tracker_2.get_value() + 2*h],
                    color=C_MAGENTA
                )
            )
        tangent_line_3 = always_redraw(
                lambda: axes_1.plot(
                    lambda x: df(tangent_tracker_3.get_value()) * (x - tangent_tracker_3.get_value()) + f(tangent_tracker_3.get_value()),
                    x_range=[tangent_tracker_3.get_value() - 2*h, tangent_tracker_3.get_value() + 2*h],
                    color=C_MAGENTA
                )
            )

        ### derivative texts
        dy_dx_text_1 = MathTex(r"\frac{dy}{dx} = 0",font_size=24).next_to(dot_1.get_center(),UP,buff=0.2)
        dy_dx_text_2 = MathTex(r"\frac{dy}{dx} = 0",font_size=24).next_to(dot_2.get_center(),DOWN,buff=0.2)
        dy_dx_text_3 = MathTex(r"\frac{dy}{dx} = 0",font_size=24).next_to(dot_3.get_center(),UP,buff=0.2)
        dy_dx_text_4 = MathTex(r"\frac{dy}{dx} = 0",font_size=24).next_to(dot_4.get_center(),DOWN,buff=0.2)
        
        dy_dx_group = VGroup(dy_dx_text_1,dy_dx_text_2,dy_dx_text_3,dy_dx_text_4)

        ### the updaters
        def position(direction,mob_2):
            def updater(mob,dt):
                mob.next_to(mob_2,direction)
            return updater
        
        ##Animations 
        self.play(FadeIn(VGroup(axes_1,x_label_1,y_label_1)),run_time=2)
        self.wait(2)
        self.play(Write(text_1),run_time=2,rate_func=smooth)
        self.play(Create(graph_1),run_time=10,rate_func=smooth)
        self.wait(4)

        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(Create(dots),rate_func=smooth)
        self.play(FadeIn(surrounding_rect),rate_func=smooth)
        self.wait(4)
        self.play(FadeOut(surrounding_rect),rate_func=smooth)

        self.play(ReplacementTransform(text_2,text_3),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(Create(tangent),Create(tangent_point),run_time=2)
        self.wait(2)
        self.play(Create(dx_line),Create(dy_line),run_time=2)
        self.wait(2)
        self.play(tracker.animate.set_value(2*PI),run_time=5,rate_func=smooth)
        self.play(tracker.animate.set_value(9*PI/4),run_time=2,rate_func=smooth)
        self.wait(2)

        ### Adding updaters
        dx_label.add_updater(position(DOWN,dx_line))
        dy_label.add_updater(position(RIGHT,dy_line))

        self.play(FadeIn(VGroup(dx_label,dy_label)),run_time=2)
        self.play(ReplacementTransform(text_3,text_4),run_time=2)
        self.wait(5)
        self.play(FadeOut(VGroup(dx_label,dy_label,dx_line,dy_line)))
        self.play(tracker.animate.set_value(5*PI/2),run_time=3)
        self.play(ReplacementTransform(text_4,text_5),run_time=2)
        
        self.wait(2)
        
        self.play(Create(tangent_line_1),Create(tangent_line_2),Create(tangent_line_3),run_time=2)
        self.play(tangent_tracker_1.animate.set_value(positions[0]),tangent_tracker_2.animate.set_value(positions[1]),tangent_tracker_3.animate.set_value(positions[2]),run_time=5)
        self.wait(4)
        self.play(ReplacementTransform(text_5,text_6),run_time=2)
        self.play(FadeIn(dy_dx_group),run_time=2)
        self.wait(4)

        self.play(FadeOut(tangent_line_1),FadeOut(tangent_line_2),FadeOut(tangent_line_3),run_time=2)
        self.play(FadeOut(tangent_point),run_time=2)
        self.play(FadeOut(dy_dx_group),FadeOut(tangent),run_time=2)

        ## code for the last part.
        ind_rect_max = Polygon(
            axes_1.c2p(2*PI,1),
            axes_1.c2p(3*PI,1),
            axes_1.c2p(3*PI,0),
            axes_1.c2p(2*PI,0),
            stroke_width=0,
            fill_opacity=0.3,
            fill_color=C_MAGENTA
        )

        ind_rect_min = Polygon(
            axes_1.c2p(PI,0),
            axes_1.c2p(2*PI,0),
            axes_1.c2p(2*PI,-1),
            axes_1.c2p(PI,-1),
            stroke_width=0,
            fill_opacity=0.3,
            fill_color=C_MAGENTA
        )
        dy_dx_max = MathTex(r"\frac{d^2y}{dx^2} < 0",font_size=24).next_to(axes_1.c2p(5*PI/2,1),UP,buff=0.2)
        dy_dx_min = MathTex(r"\frac{d^2y}{d^2x} > 0",font_size=24).next_to(axes_1.c2p(3*PI/2,-1),DOWN,buff=0.2)

        ####
        self.wait(2)
        self.play(ReplacementTransform(text_6,text_7),rate_func=smooth)
        self.play(FadeIn(ind_rect_max),FadeIn(dy_dx_max),rate_func=smooth,run_time=2)
        self.wait(5)
        self.play(ReplacementTransform(text_7,text_8),rate_func=smooth,run_time=2)
        self.play(ReplacementTransform(ind_rect_max,ind_rect_min),FadeIn(dy_dx_min),rate_func=smooth,run_time=2)
        self.wait(5)
        self.play(FadeOut(*self.mobjects))
        self.wait(5)


