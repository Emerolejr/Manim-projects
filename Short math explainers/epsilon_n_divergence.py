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



class Epsilon_n_Divergence_example(Scene):
    def construct(self):
        ##Beamer block.
    

        header_block = BeamerBlock("Limits: divergence of sequences",width=14).move_to(ORIGIN)

        ###3 Colour giver function
        def colour_giver(mob,list_no,colors):
            for i,j in zip(list_no,colors):
                mob[i].set_color(j)

        ####
        ### Definition and assumptions steps 
        def_sequence_initial = MathTex(
            r"\text{for divergence: }",
            r"\exists \epsilon > 0",r" \text{ such that } ",
            r"\forall N \in \mathbb{N} ",
            r"\exists n > N",r" \text{ where } ",
            r"|a_n - L|",r"\ge \epsilon",
            font_size=40
        ).shift(2.5*UP)

        colour_giver(def_sequence_initial,(1,3,4,6,7),(C_RED,C_GREEN,C_GREEN,C_BLUE,C_RED))

        def_sequence_final = MathTex(
            r"\exists \epsilon > 0",r" \text{ such that } ",
            r"\forall N \in \mathbb{N} ",
            r"\exists n > N",r" \text{ where } ",
            r"|a_n - L|",r"\ge \epsilon",
            font_size=40
        ).shift(UP*2.5)

        colour_giver(def_sequence_final,(0,2,3,5,6),(C_RED,C_GREEN,C_GREEN,C_BLUE,C_RED))

        step_1 = MathTex(
            r"\text{Given a Sequence : }",
            r"a_n = (-1)^n\left(1 + \frac{2}{n}\right)",
            font_size=44
        )
        step_1[1].set_color(C_BLUE)

        step_2 = MathTex(
            r"\text{Assuming }",r" \lim_{n\to\infty} a_n = 0",
            font_size=42
        )
        step_2[1].set_color(C_BLUE)


        step_3 = MathTex(
            r"\text{To prove, we assumed convergence}",
            font_size=42
        )

        step_4 = MathTex(
            r"\forall \epsilon > 0,",r"\ \exists N \in \mathbb{N}",
            r"\text{ such that }",r" |a_n|",r" < ",r"\epsilon",
            r"\ \forall n \ge N",
            font_size=40
        )
        colour_giver(step_4,(0,1,3,5,6),(C_RED,C_GREEN,C_BLUE,C_RED,C_GREEN))

        def_steps = VGroup(step_1,step_2,step_3,step_4).arrange(DOWN,buff=0.7,aligned_edge=LEFT).next_to(def_sequence_final,DOWN,buff=1)
        
        ####
        ### Simplification of a_n steps
        sim_text = MathTex(r"\text{Simplying },",r"a_n", r"\text{, we have}",
                           font_size=40).shift(2.5*UP)
        sim_text[1].set_color(C_BLUE)

        step_5 = MathTex(
            r"|a_n|",r" = ",r"\left|(-1)^n\left(1 + \frac{2}{n}\right)\right|",
            font_size=42
        )
        colour_giver(step_5,(0,2),(C_BLUE,C_BLUE))

        step_6 = MathTex(
            r"|a_n|",r"=",r" 1 + \frac{2}{n}",
            font_size=42
        )
        colour_giver(step_6,(0,2),(C_BLUE,C_BLUE))

        step_7 = MathTex(
            r"1 + \frac{2}{n} > 1",r" \quad \forall n \in \mathbb{N}",
            font_size=42
        )

        colour_giver(step_7,(0,1),(C_BLUE,C_GREEN))

        step_8 = MathTex(
            r"\implies ",r"a_n ",r">",r" 1 ",r"\text{ } \forall \text{ n}"
        )
        colour_giver(step_8,(1,3,4),(C_BLUE,C_BLUE,C_GREEN))  

        simp_steps = VGroup(step_5,step_6,step_7,step_8).arrange(DOWN,buff=0.5,aligned_edge=LEFT).next_to(sim_text,DOWN,buff=1)

        ####
        ### Picking Epsilon portion
        epsilon_text = MathTex(
            r"\text{Choosing }",
            r" \epsilon = \frac{1}{2}",
            font_size=44
        ).shift(UP*2.5)

        epsilon_text[1].set_color(C_RED)

        step_9 = MathTex(
            r"\text{Recall if }",
            r" \lim_{n\to\infty} a_n = 0,",
            r"\text{then }",
            r"\forall \epsilon > 0,",r"\ \exists N \in \mathbb{N}",
            r"\text{ such that }",r" |a_n|",r"< ",r"\epsilon",
            r"\ \forall n \ge N",
            font_size=35
        )

        colour_giver(step_9,(1,3,4,6,8,9),(C_BLUE,C_RED,C_GREEN,C_BLUE,C_RED,C_GREEN))

        step_10 = MathTex(
            r"\text{But },",r" |a_n| > 1 > \frac{1}{2}",
            font_size=40
        )
        step_10[1].set_color(C_BLUE)

        step_11 = MathTex(
            r"\therefore",r" \lim_{n\to\infty} a_n \neq 0",
            font_size=44
        )
        step_11[1].set_color(C_BLUE)

        step_12 = MathTex(r"\text{Indicating divergence}",font_size=40).set_color(C_YELLOW)

        ##Indicator rectangle
        
        epsilon_steps = VGroup(step_9,step_10,step_11,step_12).arrange(DOWN,buff=0.5,aligned_edge=LEFT).next_to(epsilon_text,DOWN,buff=1)
        steps = [step_1,step_2,step_3,step_4,step_5,step_6,step_7,step_8,step_9,step_10,step_11,step_12]
        
        
        final_text = Text("Showing this graphically:")


        ###
        ## All animations start here
        ###
        self.add(header_block)

        self.play(Write(def_sequence_initial))
        self.wait(2)
        self.play(ReplacementTransform(def_sequence_initial,def_sequence_final))
        self.wait(2)


        for i in range(4):
            self.play(Write(steps[i]),rate_func=smooth)
            self.wait(3)
            if i == 3:
                self.wait(3)
                self.play(FadeOut(*steps[0:4]))
                self.play(ReplacementTransform(def_sequence_final,sim_text))
                self.wait(2)
        
        for i in range(4,8,1):
            self.play(Write(steps[i]),rate_func=smooth)
            self.wait(3)
            if i == 7:
                self.wait(3)
                self.play(FadeOut(*steps[4:8]))
                self.play(ReplacementTransform(sim_text,epsilon_text))
                self.wait(2)
        
        for i in range(8,12,1):
            if i==9:
                self.play(Indicate(step_9[6:9],color=YELLOW),rate_func=smooth)
            self.play(Write(steps[i]),rate_func=smooth)
            self.wait(3)

        self.play(FadeOut(*self.mobjects))
        self.wait(2)
        self.play(Write(final_text))
        self.wait(5)


class Epsilon_n_divergence_graph(MovingCameraScene):
    def construct(self):
        ax = Axes(
            x_range=[0, 41, 5],
            y_range=[-3.5, 2.5, 0.5],
            x_length=12,
            y_length=6,
            axis_config={"include_tip": True, "numbers_to_exclude": [], "tick_size": 0.05}
        ).add_coordinates()
        ax.to_edge(DOWN, buff=1.0)

        labels = ax.get_axis_labels(x_label="n", y_label="a_n")


        self.play(Create(ax), Write(labels), run_time=2)

        # Formula display at top of screen
        graph_formula_template = MathTex(
            r"a_n = (-1)^n\left(1 + \frac{2}{n}\right)",
            font_size=48
        )
        graph_formula_template.to_edge(UP, buff=0.5).shift(DOWN * 0.5).set_color(C_BLUE)

        self.play(Write(graph_formula_template))
        self.wait(0.5)

        # Sequence dots
        dots = VGroup()

        def seq_func(n):
            """Alternating sequence: a_n = (-1)^n (1 + 2/n)"""
            return ((-1)**n) * (1 + 2/n)
            
        self.add(dots)

        # Plot first 9 points with step-by-step substitution animation
        for n in range(1, 5):

            val = seq_func(n)
            
            # Build substitution strings: a_n -> calculation -> simplified value
            val_text_str = (
                r"a_{" + str(n) + r"} = (-1)^{" + str(n) + r"}\left(1 + \frac{2}{" + str(n) + r"}\right)"
            )
            abs_val = abs(val)
            formatted_val = f"{abs_val:.2f}"
            
            final_val_str = (
                r"a_{" + str(n) + r"} = " +
                (r"-" if val < 0 else "") +
                formatted_val
            )

            step_calc = MathTex(val_text_str, font_size=48).move_to(graph_formula_template)
            step_final = MathTex(final_val_str, font_size=48).move_to(graph_formula_template)
            
            # Animate formula transformation
            self.play(Transform(graph_formula_template, step_calc), run_time=1)
                
            self.wait(1.2)
            self.play(Transform(graph_formula_template, step_final), run_time=1)
                
            # Create and plot dot, storing y-value for epsilon highlighting
            dot = Dot(ax.c2p(n, val), color=C_BLUE, radius=0.06)
            dot.y_val = val
            dots.add(dot)
            self.play(FadeIn(dot, scale=0.5), run_time=1)
            self.wait(1.2)

        # Plot remaining points quickly without formula animation
        for n in range(6, 41):
            val = seq_func(n)
            dot = Dot(ax.c2p(n, val), color=C_BLUE, radius=0.06)
            dot.y_val = val
            dots.add(dot)
            self.add(dot)
            self.wait(0.5)



        self.play(FadeOut(VGroup(graph_formula_template)),rate_func=smooth)

        epsilon = ValueTracker(0.5)
        L = 0  # Limit value

        upper_line = DashedLine(
            start=ax.c2p(0, L + epsilon.get_value()),
            end=ax.c2p(200, L + epsilon.get_value()),
            color=C_RED
        )

        lower_line =  DashedLine(
            start=ax.c2p(0, L - epsilon.get_value()),
            end=ax.c2p(200, L - epsilon.get_value()),
            color=C_RED)
        
        region = Polygon(
            ax.c2p(0, L + epsilon.get_value()),
            ax.c2p(200, L + epsilon.get_value()),
            ax.c2p(200, L - epsilon.get_value()),
            ax.c2p(0, L - epsilon.get_value()),
            stroke_width=0,
            fill_color=C_RED,
            fill_opacity=0.2
        )
        
        label_eps = MathTex(r"\epsilon = " + f"{epsilon.get_value():.2f}", color=C_RED).set_x(ax.c2p(int(1.0/epsilon.get_value()),0)[0] + 1)

        # Vertical line marking N = 1/epsilon
        v_line =  DashedLine(
            start=ax.c2p(2, -2),
            end=ax.c2p(2, 2),
            color=C_GREEN
        )
        
        label_N = always_redraw(lambda: 
            MathTex(f"N = {ax.p2c(v_line.get_start())[0]:.1f}", color=C_GREEN
        ).next_to(v_line.get_start(),RIGHT))

        #### These are the texts that explain the graph.
        graph_text_1 = Tex(
            r"Divergence means the sequence does not converge to any limit.",
            font_size=32
        ).to_edge(UP,buff=0.8)
        
        graph_text_2 = MathTex(
            r"\exists \epsilon > 0 \ \text{such that}  ",
            r"\forall N \in \mathbb{N},  ",
            r"\exists n > N \ \text{with}  ",
            r"|a_n - L| \ge \varepsilon.",
            font_size=32
        ).to_edge(UP,buff=0.8)

        graph_text_2[0][0:3].set_color(C_RED)
        graph_text_2[1:3].set_color(C_GREEN)
        graph_text_2[3][5:].set_color(C_GREEN)


        graph_text_3 = Tex(
            r"In simple terms: we can choose an epsilon band the sequence cannot stay inside.",
            font_size=32
        ).to_edge(UP,buff=0.8)

        graph_text_4 = Tex(
            r"For example, let's pick $\epsilon = 0.5$.",
            font_size=32
        ).to_edge(UP,buff=0.8)

        graph_text_5 = Tex(
            r"No matter how we move $N$, some terms still fall outside the stripe.",
            font_size=32
        ).to_edge(UP,buff=0.8)

        graph_text_6 = Tex(
            r"Since the terms cannot be permanently trapped, the sequence diverges.",
            font_size=32
        ).to_edge(UP,buff=0.8)

        ### Graph text group
        graph_texts = VGroup(graph_text_1,graph_text_2,graph_text_3,graph_text_4,graph_text_5,graph_text_6)


        ### Text animations for Graph explanation
        def play_func():
            self.play(Create(upper_line), Create(lower_line), FadeIn(region), Write(label_eps), run_time=1.5,rate_func=smooth)
            self.play(Create(v_line), Write(label_N),rate_func=smooth)
            self.play(v_line.animate.move_to(ax.c2p(30,0)),rate_func=linear,run_time=10)

        for i in range(4):
            if i == 0:
               self.play(Write(graph_texts[i]),rate_func=smooth)
               self.wait(2)
            else:
               self.play(ReplacementTransform(graph_texts[i-1],graph_texts[i]),rate_func=smooth)
               self.wait(2)

        self.play(Create(upper_line), Create(lower_line), FadeIn(region), Write(label_eps), run_time=1.5,rate_func=smooth)
        self.play(Create(v_line), Write(label_N),rate_func=smooth)
        self.play(v_line.animate.move_to(ax.c2p(30,0)),rate_func=linear,run_time=10)
        
        for i in range(4,6,1):
            if i == 4:
                self.play(ReplacementTransform(graph_texts[i-1],graph_texts[i]),rate_func=smooth)
                self.wait(2)
            else:
                self.play(ReplacementTransform(graph_texts[i-1],graph_texts[i]),rate_func=smooth)
                self.wait(5)
        self.play(v_line.animate.move_to(ax.c2p(2,0)),rate_func=linear,run_time=10)

        self.wait(2)
        