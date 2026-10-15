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


class graphical_epsilon_criterion(Scene):
    def construct(self):
           
        ### Texts that explain the concept of the graph
        # 1. Hook
        text_1 = MathTex(
            r"\text{What are limits?}",
            font_size=36
        ).to_corner(UP, buff=0.2)

        # 2. Visual focus
        text_2 = MathTex(
            r"\text{There is a hole at }", r"x_0",

            font_size=36
        ).to_corner(UP, buff=0.2)
        text_2[1].set_color(C_BLUE)


        # 3. Value vs limit
        text_3 = VGroup(
            MathTex(r"f(x_0) = \text{Function value}", font_size=34),
            MathTex(r"L = \text{limit}", font_size=34)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).to_corner(UP, buff=0.2)
        text_3[1][0].set_color(C_RED)


        # 4. Core idea (MOST IMPORTANT)
        text_4 = VGroup(
            MathTex(r"\text{If } x \text{ is close to } x_0,", font_size=36),
            MathTex(r"\text{then } f(x) \text{ is close to } L", font_size=36)
        )


        # 5. Epsilon-delta (compressed)
        text_5 = VGroup(
            MathTex(r"\text{For every }", r"\epsilon", font_size=34),
            MathTex(r"\text{there exists }", r"\delta", font_size=34)
        )
        text_5[0][1].set_color(C_RED)
        text_5[1][1].set_color(C_GREEN)


        # 6. Relationship (clean + visual)
        text_6 = VGroup(
            MathTex(r"x \in x_0 \pm \delta", font_size=34),
            MathTex(r"f(x) \in L \pm \epsilon", font_size=34)
        )
        text_6[0].set_color(C_GREEN)
        text_6[1].set_color(C_RED)


        # 7. Key insight (punchy)
        text_7 = VGroup(
            MathTex(r"\text{The limit ignores } f(x_0)", font_size=36),
            MathTex(r"\text{it only tracks where } f(x) \text{ goes}", font_size=34)
        )


        # 8. Two-sided condition
        text_8 = VGroup(
            MathTex(r"\text{Both sides must agree}", font_size=36),
            MathTex(r"\text{same value from left and right}", font_size=34)
        )


        # 9. Continuity (strong ending)
        text_9 = VGroup(
            MathTex(r"\text{Continuity means}", font_size=36),
            MathTex(r"f(x_0) = L", font_size=38)
        )

        ### The axes for the graph
        ax = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 3, 0.5],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": False,"include_ticks": False,
            "tip_shape":StealthTip,"tip_length":0.1,"tip_width":0.1},
        ).shift(DOWN)

        x_label = ax.get_x_axis_label("x")
        y_label = ax.get_y_axis_label("y")
        # function
        def f(x):
            return 1 + 0.35*(x-1.2) + 0.18*(x-1.2)**3

        x0 = 1.2
        L = 1
        f_x0 = 1.9

        # left piece
        graph_left = ax.plot(
            f,
            x_range=[0, x0-0.02],
            color=BLUE
        )

        # right piece
        graph_right = ax.plot(
            f,
            x_range=[x0+0.02, 3],
            color=BLUE
        )

        # open circle (limit point)
        hole = Circle(
            radius=0.06,
            color=BLUE,
            stroke_width=3
        ).move_to(ax.c2p(x0, L)).set_z_index(2)

        hole.set_fill(opacity=0)

        # filled point (actual function value)
        value_point = Dot(
            ax.c2p(x0, f_x0),
            color=C_RED
        )

        ### These are for the epsilon, delta and x_0, f(x_0) lines
        x_o_line = ax.get_vertical_line(ax.c2p(x0, f(x0)), color=C_GREEN)
        limit_line = ax.get_horizontal_line(ax.c2p(x0, f(x0)), color=C_RED)
        f_xo_line = ax.get_horizontal_line(ax.c2p(x0, f_x0), color=C_BLUE)

        x_o_label = MathTex(r"x_0",font_size=30).next_to(ax.c2p(x0, 0), DOWN, buff=0.4).set_color(C_GREEN)
        limit_label = MathTex(r"L",font_size=30).next_to(ax.c2p(0, f(x0)), LEFT, buff=0.4).set_color(C_RED)
        f_xo_label = MathTex(r"f(x_0)",font_size=30).next_to(ax.c2p(0, f_x0), LEFT, buff=0.4).set_color(C_BRIGHT_BLUE)


        # epsilon band
        epsilon = ValueTracker(0)

        epsilon_band_upper = always_redraw(
            lambda: Line(
                ax.c2p(0, L + epsilon.get_value()),
                ax.c2p(3, L + epsilon.get_value()),
                color=C_RED
            )
        )

        epsilon_band_lower = always_redraw(
            lambda: Line(
                ax.c2p(0, L - epsilon.get_value()),
                ax.c2p(3, L - epsilon.get_value()),
                color=C_RED
            )
        )

        epsilon_band_higher_text = always_redraw(
            lambda: MathTex(r"L + \epsilon",font_size=30).next_to(epsilon_band_upper.get_start(), LEFT, buff=0.4).set_color(C_RED)
        )

        epsilon_band_lower_text = always_redraw(
            lambda: MathTex(r"L - \epsilon",font_size=30).next_to(epsilon_band_lower.get_start(), LEFT, buff=0.4).set_color(C_RED)
        )

        epsilon_band = always_redraw(
            lambda: Polygon(
                ax.c2p(0, L + epsilon.get_value()),
                ax.c2p(3, L + epsilon.get_value()),
                ax.c2p(3, L - epsilon.get_value()),
                ax.c2p(0, L - epsilon.get_value()),
                stroke_width=0,
                fill_color=C_RED,
                fill_opacity=0.2
            )
        )

        ## delta lines
        def find_delta():
            eps = epsilon.get_value()
            
            # search small interval around x0
            xs = np.linspace(x0 - 2, x0 + 2, 1000)
            
            valid = [x for x in xs if abs(f(x) - L) < eps]
            
            if valid:
                return min(abs(min(valid) - x0), abs(max(valid) - x0))
            return 0.1

        delta_tracker = ValueTracker(0)

        delta_lines_1 = always_redraw(
            lambda: VGroup(
                DashedLine(
                    ax.c2p(x0 - delta_tracker.get_value(), 0),
                    ax.c2p(x0 - delta_tracker.get_value(), 3),
                    color=C_GREEN
                ),
                DashedLine(
                    ax.c2p(x0 + delta_tracker.get_value(), 0),
                    ax.c2p(x0 + delta_tracker.get_value(), 3),
                    color=C_GREEN
                )
            )
        )

        ### This particular delta automatically adjusts.
        delta_lines_2 = always_redraw(
            lambda: VGroup(
                DashedLine(
                    ax.c2p(x0 - find_delta(), 0),
                    ax.c2p(x0 - find_delta(), 3),
                    color=C_GREEN
                ),
                DashedLine(
                    ax.c2p(x0 + find_delta(), 0),
                    ax.c2p(x0 + find_delta(), 3),
                    color=C_GREEN
                )
            )
        ).set_opacity(0)

        delta_text_1 = always_redraw(
            lambda: MathTex(r"x + \delta",font_size=30).next_to(ax.c2p(x0 + find_delta(), 0), DOWN, buff=0.4).set_color(C_GREEN)
        )

        delta_text_2 = always_redraw(
            lambda: MathTex(r"x - \delta",font_size=30).next_to(ax.c2p(x0 - find_delta(), 0), DOWN, buff=0.4).set_color(C_GREEN)
        )

        ### These are the dots that will move from the left to right. 
        dot_left = Dot(graph_left.get_start()).scale(1.3)
        dot_right = Dot(graph_right.get_end()).scale(1.3)

        ###
        #### Here is where the animation starts ####
        ###
        
        self.play(FadeIn(ax),FadeIn(x_label),FadeIn(y_label),run_time=2,rate_func=smooth)
        self.wait(2)
        self.play(Write(text_1),rate_func=smooth)

        self.play(Create(graph_left), Create(graph_right), run_time=2,rate_func=smooth)
        self.wait(2)

        self.play(Create(hole), run_time=2,rate_func=smooth)
        self.wait(2)

        self.play(Create(value_point), run_time=2,rate_func=smooth)
        self.wait(2)

        self.play(ReplacementTransform(text_1,text_2),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(Indicate(hole),Indicate(value_point),run_time=4)
        self.play(ReplacementTransform(text_2,text_3),run_time=2,rate_func=smooth)

        self.play(Create(x_o_line), Create(limit_line),Create(f_xo_line), run_time=2,rate_func=smooth)
        self.play(Create(x_o_label),Create(limit_label),Create(f_xo_label),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(FadeOut(f_xo_line),FadeOut(f_xo_label),run_time=2,rate_func=smooth)
        self.wait(2)
        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth)

        self.wait(2)

        ### Dealing with epsilon
        self.play(Unwrite(text_4),rate_func=smooth)
        self.play(Write(limit_definition),rate_func=smooth)
        self.play(Indicate(limit_definition[0]),run_time=4)
        self.wait(2)
        self.play(Write(text_5),rate_func=smooth)
        self.wait(2)

        self.play(Create(epsilon_band_upper),Create(epsilon_band_lower),rate_func=smooth)
        self.wait(2)
        self.play(epsilon.animate.set_value(0.4),run_time=5,rate_func=smooth)
        self.wait(2)
        self.play(Create(epsilon_band_higher_text),Create(epsilon_band_lower_text),run_time=3,rate_func=smooth)
        self.play(FadeIn(epsilon_band),run_time=2,rate_func=smooth)
        self.wait(3)

        ## Dealing with delta.
        self.play(Indicate(limit_definition[1]),run_time=4)
        self.wait(2)
        self.play(ReplacementTransform(text_5,text_6),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(Create(delta_lines_1),run_time=2,rate_func=smooth)

        self.play(delta_tracker.animate.set_value(find_delta()),run_time=4,rate_func=smooth)
        self.play(FadeIn(delta_lines_2),run_time=2,rate_func=smooth)
        self.wait(1)
        self.play(delta_lines_2.animate.set_opacity(1),run_time=2,rate_func=smooth)
        self.play(delta_lines_1.animate.set_opacity(0.5),run_time=2,rate_func=smooth)
        self.wait(2)

        self.play(Indicate(limit_definition[2:6]),run_time=4)
        self.wait(2)
        self.play(ReplacementTransform(text_6,text_7),rate_func=smooth,run_time=1.2)
        self.play(delta_tracker.animate.set_value(0),rate_func=smooth,run_time=1)
        self.play(delta_tracker.animate.set_value(0.3),rate_func=smooth,run_time=0.3)
        self.play(delta_tracker.animate.set_value(0.2),rate_func=smooth,run_time=0.7)
        self.play(delta_tracker.animate.set_value(find_delta()),rate_func=smooth,run_time=2)
        self.play(FadeOut(delta_lines_1),run_time=2)
        self.wait(2)
        self.play(Indicate(limit_definition[6:]),run_time=4)
        self.play(Create(delta_text_1),Create(delta_text_2),run_time=2,rate_func=smooth)
        self.wait(2)

        self.play(epsilon.animate.set_value(0.2),run_time=5,rate_func=smooth)
        self.wait(4)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set_width(5).move_to(ax.c2p(x0, L)),
        epsilon.animate.set_value(0.08),run_time=10,rate_func=smooth)
        self.wait(2)
        self.play(Restore(self.camera.frame),run_time=7,rate_func=smooth)
        self.wait(2)
    
        self.play(ReplacementTransform(text_7,text_8),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(text_8,text_9),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(ReplacementTransform(text_9,text_10),rate_func=smooth,run_time=2)

        ## controls movement of the left dot and the right dot to the limits
        self.wait(2)
        self.play(Create(dot_left),Create(dot_right))
    
        left_path = graph_left.copy()
        right_path = graph_right.copy()
        left_path.pointwise_become_partial(graph_left,0,0.95)
        right_path.pointwise_become_partial(graph_right,0,0.95)

        self.play(MoveAlongPath(dot_left,left_path),
        MoveAlongPath(dot_right,right_path.reverse_direction()),run_time = 10)

        self.wait(2)
        self.play(Indicate(hole),run_time=4)
        self.wait(2)
        self.play(FadeOut(VGroup(delta_text_1,delta_text_2,epsilon_band_upper,epsilon_band_lower,epsilon_band_higher_text,epsilon_band_lower_text,delta_lines_2,
        dot_left,dot_right,epsilon_band,dot_left,dot_right,text_10,limit_definition)),run_time=2,rate_func=smooth)

        self.wait(4)

        ## this is the continuity animation
        self.play(Write(text_11),run_time=2,rate_func=smooth)
        dot_left.move_to(graph_left.get_start())
        self.wait(2)
        self.play(ReplacementTransform(text_11,text_12),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(Indicate(hole),Indicate(value_point),run_time=5)
        self.wait(2)
        self.play(Create(dot_left),run_time=2,rate_func=smooth)

        self.wait(2)
        self.play(MoveAlongPath(dot_left,graph_left),run_time = 5)
        self.wait(1)
        self.play(value_point.animate.move_to(ax.c2p(x0, f(x0))),run_time=2,rate_func=smooth)
        self.play(ReplacementTransform(text_12,text_13),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(dot_left.animate.move_to(graph_right.get_start()),run_time=2,rate_func=smooth)
        self.play(MoveAlongPath(dot_left,graph_right),rate_func=smooth,run_time=4)
        self.wait(4)
        

class two_sided_limits(Scene):
    def construct(self):
        ### Texts here.
        text_1 = MathTex(r"\text{Given a piecewise function}",font_size=32).to_corner(UP,buff=0.5)

        text_2 = MathTex(r"\text{Picking an } ",r"\epsilon > \text{ 0}",font_size=32).to_corner(UP,buff=0.5)
        text_2[1].set_color(C_RED)
        text_3 = MathTex(r"\text{Shrinking the } ",r"\epsilon",r"\kern0.5em value",font_size=32).to_corner(UP,buff=0.5)
        text_3[1].set_color(C_RED)

        text_4 = VGroup(
            MathTex(r"\text{We can see that for a sufficiently small } ",r"\epsilon",r" \text{ we cannot find } ",r"\delta",font_size=30),
            MathTex(r"\text{such that all function values within the } ",r"\delta ",r"\text{ interval lie inside within the } ",r"\epsilon ",r"\text{band}",font_size=30)
        ).arrange(aligned_edge=LEFT,direction=DOWN,buff=0.3).to_corner(UP,buff=0.5)

        text_4[0][1].set_color(C_RED)
        text_4[0][3].set_color(C_GREEN)
        text_4[1][1].set_color(C_GREEN)
        text_4[1][3].set_color(C_RED)

        text_5 = MathTex(r"\text{Note the two points approaching from either side of the graph}",font_size=30).to_corner(UP,buff=0.5)
        
        text_6 = VGroup(MathTex(r"\text{Since they are approaching different function values,}",font_size=30),
                        MathTex(r"\text{ We can say the }",r"\textbf{limit does not exist}",font_size=30)).arrange(aligned_edge=LEFT,direction=DOWN).to_corner(UP,buff=0.5)

        # Axes
        ax = Axes(
            x_range=[-1, 3, 1],
            y_range=[-1, 2.2, 1],
            x_length=8,
            y_length=5,
            axis_config={
                "include_ticks": False,
                "include_numbers": False,
                "stroke_width": 2,
            }
        ).shift(DOWN)

        x_label = ax.get_x_axis_label(MathTex("x"))
        y_label = ax.get_y_axis_label(MathTex("f(x)"))

        # Functions
        def left_func(x):
            return 1.2/(1+np.exp(-5*(x+0.3)))

        def right_func(x):
            return 0.5 + 0.8/(1+np.exp(-5*(x-1.3)))
            
        # Graph branches
        left_graph = ax.plot(
            left_func,
            x_range=[-1, 1],
            color=BLUE,
            stroke_width=6
        )

        right_graph = ax.plot(
            right_func,
            x_range=[1, 2.8],
            color=RED,
            stroke_width=6
        )    

        # x0 vertical dashed line
        x0 = 1

        x0_line = DashedLine(
            ax.c2p(x0, -0.5),
            ax.c2p(x0, 2),
            color=GRAY
        )

        x0_label = MathTex("x_0").scale(0.7).next_to(
            ax.c2p(x0, 0), DOWN
        )
        
        # Left limit line
        L_minus = 1.2

        left_limit = DashedLine(
            ax.c2p(-1, L_minus),
            ax.c2p(1, L_minus),
            dash_length=0.05,
            color=BLUE
        )

        Lm_label = MathTex("L_-").scale(0.7).next_to(
            ax.c2p(-0.1, L_minus), LEFT
        )

        # Right limit line
        L_plus = 0.6

        right_limit = DashedLine(
            ax.c2p(0, L_plus),
            ax.c2p(2.4, L_plus),
            dash_length=0.05,
            color=RED
        )

        Lp_label = MathTex("L_+").scale(0.7).next_to(
            ax.c2p(2.4, L_plus), RIGHT
        )

        # Candidate limit (between the two)
        L = (L_minus + L_plus) / 2

        limit_line = DashedLine(
            ax.c2p(-1, L),
            ax.c2p(2.8, L),
            color=GREEN
        )

        limit_label = MathTex("L").scale(0.7).next_to(
            ax.c2p(-0.8, L), LEFT
        )

        # Trackers
        epsilon = ValueTracker(0.8)

        # Epsilon band
        eps_upper = always_redraw(
            lambda: Line(
                ax.c2p(-1, L + epsilon.get_value()),
                ax.c2p(2.8, L + epsilon.get_value()),
                color=C_RED
            )
        )

        eps_lower = always_redraw(
            lambda: Line(
                ax.c2p(-1, L - epsilon.get_value()),
                ax.c2p(2.8, L - epsilon.get_value()),
                color=C_RED
            )
        )

        eps_band = always_redraw(
            lambda: Polygon(
                ax.c2p(-1,L - epsilon.get_value()),
                ax.c2p(-1,L + epsilon.get_value()),
                ax.c2p(2.8,L + epsilon.get_value()),
                ax.c2p(2.8, L - epsilon.get_value()),
                stroke_width=0,
                fill_color=C_RED,
                fill_opacity=0.2
            )
        )

        epsilon_1_brace = always_redraw(
            lambda: BraceBetweenPoints(
                eps_upper.get_end(),
                limit_line.get_end(),
                direction=RIGHT
            ).set_color(C_RED)
        )

        epsilon_2_brace = always_redraw(
            lambda: BraceBetweenPoints(
                eps_lower.get_end(),
                limit_line.get_end(),
                direction=RIGHT
            ).set_color(C_RED)
        )

        epsilon_1_text= MathTex(r"\epsilon").scale(0.7).next_to(epsilon_1_brace,RIGHT).set_color(C_RED)
        epsilon_2_text = epsilon_1_text.copy().next_to(epsilon_2_brace,RIGHT).set_color(C_RED)

        # Delta interval
        delta_left = always_redraw(
            lambda: DashedLine(
                ax.c2p(x0 - epsilon.get_value()+0.1, -1),
                ax.c2p(x0 - epsilon.get_value()+0.1, 2),
                color=C_GREEN
            )
        )

        delta_right = always_redraw(
            lambda: DashedLine(
                ax.c2p(x0 + epsilon.get_value()-0.1, -1),
                ax.c2p(x0 + epsilon.get_value()-0.1, 2),
                color=C_GREEN
            )
        )

        ### These are dots and their surrounding rectangle to help illustrate limits
        dot_left = Dot().move_to(left_graph.get_start()).set_color(BLUE).scale(1.3)
        dot_right = Dot().move_to(right_graph.get_end()).set_color(RED).scale(1.3)

        # Delta brace
        delta_brace = always_redraw(
            lambda: BraceBetweenPoints(
                ax.c2p(x0 - epsilon.get_value()+0.1, -0.7),
                ax.c2p(x0 + epsilon.get_value()-0.1, -0.7),
                direction=DOWN
            ).set_color(C_GREEN)
        )

        delta_label = always_redraw(
            lambda: MathTex(r"\delta",font_size=30).next_to(delta_brace,DOWN).set_color(C_GREEN)
        )

        # Add dynamic elements

        ### Animation tasks.
        self.play(Create(ax), Create(x_label), Create(y_label))
        self.play(Create(left_graph),Create(right_graph),Create(x0_line), Create(x0_label),rate_func=smooth)
        self.play(Write(text_1),rate_func=smooth)

        # Start with large epsilon (both branches inside)

        self.play(ReplacementTransform(text_1,text_2),run_time=2,rate_func=smooth)
        self.play(Create(eps_lower),Create(eps_upper),FadeIn(eps_band))
        self.play(Create(epsilon_1_brace),Create(epsilon_2_brace),Create(epsilon_1_text),
        Create(epsilon_2_text),rate_func=smooth)
        self.wait(1)
        self.play(Create(delta_brace),Create(delta_label),
        Create(delta_right),Create(delta_left),rate_func=smooth,run_time=1)

        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(FadeOut(VGroup(epsilon_1_brace,epsilon_2_brace,epsilon_1_text,epsilon_2_text)))
        self.play(epsilon.animate.set_value(0.7), run_time=2)
        self.wait(2)

        # Shrink epsilon between the two one-sided limits
        self.play(epsilon.animate.set_value(0.4), run_time=3)
        self.wait(2)

        # Try shrinking delta
        self.play(epsilon.animate.set_value(0.1))

        self.wait(2)

        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth)
        self.wait(2)

        self.play(FadeOut(VGroup(delta_brace,delta_label,delta_right,delta_left,
        eps_band,eps_lower,eps_upper)),rate_func=smooth)

        self.wait(4)
        self.play(ReplacementTransform(text_4,text_5),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(FadeIn(dot_left),FadeIn(dot_right),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(Indicate(dot_left),Indicate(dot_right),run_time=5)
        right_path = right_graph.copy()
        left_path = left_graph.copy()

        self.play(MoveAlongPath(dot_left,left_path),MoveAlongPath(dot_right,right_path.reverse_direction())
        , ReplacementTransform(text_5,text_6),Create(left_limit),
        Create(right_limit),rate_func=smooth,lag_ratio=0.5,run_time=10)

        self.wait(4)
