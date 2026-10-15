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



class pointwise_convergence(Scene):
    def construct(self):
        #### This is the header of the file
        header = BeamerBlock("Uniform convergence of functions",width=14.5).move_to(ORIGIN)

        ### colour_giver function
        def colour_giver(mob, indices, colors):
            for index, color in zip(indices, colors):
                # If it's nested like (0,1)
                if isinstance(index, (list, tuple)):
                    mob[index[0]][index[1]].set_color(color)
                # If it's single level like 2
                else:
                    mob[index].set_color(color)

        ### Function for playing mobjects in a VGroup
        def play_mob(mob):
            for i in mob:
                self.play(Write(i),rate_func=smooth)
                self.wait(3)
        
        ### Definition of the functtion
        text_1 = VGroup(
            MathTex(r"\text{Definition }",font_size=40),
            MathTex(
            r"\text{A sequence of functions }",r" (f_n)_{n\in\mathbb{N}}",
            r"\text{ on } ",r"X \subset \mathbb{R}^n",
            r"\text{ converges pointwise to } ",r"f \text{ if}",
            font_size=35), 
            MathTex(
            r"\forall x \in X :",r"\lim_{n \to \infty}",r" f_n(x) = f(x).",font_size=35)
            ).arrange(direction=DOWN,aligned_edge=LEFT,buff=0.4).shift(UP*3)
        colour_giver(text_1,([1,1],[1,3],[2,0],[2,2]),(C_BLUE,C_BLUE,C_BLUE,C_BLUE))

        text_2 = VGroup(
            MathTex(r"\text{formal definition }",font_size=40),
            MathTex(
            r"\forall x \in X \;",
            r"\forall \epsilon > 0 \;",
            r"\exists n_0 = n_0(x,\epsilon) \;",
            r"\forall n \ge n_0 : \;",
            r"\left| f_n(x) - f(x) \right| ",r"\le",r" \epsilon",font_size=35
        )
        ).arrange(direction=DOWN,aligned_edge=LEFT,buff=0.4).next_to(text_1,DOWN,buff=0.5)
        colour_giver(text_2,([1,0],[1,1],[1,2],[1,3],[1,4],[1,6]),(C_BLUE,C_RED,C_GREEN,C_GREEN,C_BLUE,C_RED))

        ### First group of texts
        first_grouping= VGroup(text_1,text_2).arrange(aligned_edge=LEFT,direction=DOWN,buff=0.7)

        text_3 = VGroup(
            MathTex(r"\text{Order of Qualifiers}",font_size=40),
            MathTex(
            r"\forall x \in X \;",
            r"\forall \epsilon > 0 \;",
            r"\exists n_0 = n_0(x,\epsilon) \;",
            r"\forall n \ge n_0 : \;",
            r"\left| f_n(x) - f(x) \right| ",r"\le ",r"\epsilon",font_size=35
        )).arrange(direction=DOWN,aligned_edge=LEFT).shift(3*UP)

        colour_giver(text_3,([1,0],[1,1],[1,2],[1,3],[1,4],[1,6]),(C_BLUE,C_RED,C_GREEN,C_GREEN,C_BLUE,C_RED))
        
        text_4 = MathTex(
            r"\text{First, choose an arbitrary point} ",r"\forall x \in X.",font_size=35
        ).next_to(text_3,DOWN,buff=1)

        text_4[1].set_color(C_BLUE)

        text_5 = MathTex(
            r"\text{Next, choose an arbitrary tolerance } ",r"\forall \epsilon > 0.",font_size=35
        ).next_to(text_3,DOWN,buff=1)
        text_5[1].set_color(C_RED)

        text_6 = MathTex(
            r"\text{then there exists an index } ",r"n_o = n_o(x,\epsilon).",font_size=35
        ).next_to(text_3,DOWN,buff=1)
        text_6[1].set_color(C_RED)

        text_7 = MathTex(
            r"\text{Finally: }",r" \forall n \ge n_0 :",
            r"\ |f_n(x) - f(x)| ",r"\le ",r" \epsilon.",font_size=35
        ).next_to(text_3,DOWN,buff=1)

        colour_giver(text_7,(1,2,4),(C_GREEN,C_BLUE,C_RED))

        emphasis_texts = VGroup(text_4,text_5,text_6,text_7)

        second_grouping = VGroup(text_3,emphasis_texts).arrange(direction=DOWN,buff=0.8,aligned_edge=LEFT).shift(UP)
        
        text_8 = MathTex(r"\forall \text{ } x \in X").next_to(text_3,DOWN,buff=1)
        text_8.set_color(C_BLUE)

        text_8_box = SurroundingRectangle(text_8,color=C_GREEN)

        text_9 = MathTex(r"\text{We fix one point x. Everything that follows refers to that single fixed point.}"
                         ,font_size=30)

        text_10 = MathTex(r"\implies \text{ the } ",r"\epsilon ",r"\text{ convergence applies for a single point x.} ",
                          font_size=30)
        text_10[1].set_color(C_RED)
        third_grouping = VGroup(text_9,text_10).arrange(direction=DOWN,buff=0.5,aligned_edge=LEFT).next_to(text_8,DOWN,buff=0.5)
        
        #### This is the part that handles animation.

        self.add(header)

        play_mob(first_grouping)
        self.wait(3)
        self.play(FadeOut(first_grouping),rate_func=smooth)
        self.wait(3)
        self.play(Write(text_3),rate_func=smooth)
        self.wait(3)

        counter = 0

        for i in emphasis_texts[0:3]:
            line = Underline(text_3[1][counter])
            self.play(Write(i),Create(line),rate_func=smooth)
            self.wait(2)
            self.play(Unwrite(i),Uncreate(line),rate_func=smooth)
            counter = counter + 1


        line = Underline(text_3[1][3:])
        self.play(Write(emphasis_texts[3]),Create(line),rate_func=smooth)
        self.wait(2)
        self.play(Unwrite(emphasis_texts[3]),rate_func=smooth)
        self.wait(2)
        self.play(TransformFromCopy(text_3[0],text_8),Create(text_8_box),rate_func=smooth)
        self.wait(2)
        self.play(Write(text_9),rate_func=smooth)
        self.wait(2)
        self.play(Write(text_10),rate_func=smooth)
        self.wait(2)

  

class PointwiseExample(Scene):
    def construct(self):

        ### The colour giver function
        def colour_giver(mob, indices, colors):
            for index, color in zip(indices, colors):
                # If it's nested like (0,1)
                if isinstance(index, (list, tuple)):
                    mob[index[0]][index[1]].set_color(color)
                # If it's single level like 2
                else:
                    mob[index].set_color(color)

        #### The axis of the graphs
        axes = Axes(
            x_range=[0, 1.1, 0.2],
            y_range=[0, 1.1, 0.2],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True,"tip_shape":StealthTip,"include_ticks":False},
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Plot some f_n(x) = x^n
        graph_text_group = VGroup()
        graphs = VGroup()

        for n in [1,2,3,10,40]:
            graph = axes.plot(
                lambda x: x**n,
                x_range=[0, 1],
                color=C_BLUE
            )
            graph_text = MathTex(rf"f_{{{n}}}").scale(0.5).move_to(graph.point_from_proportion(0.5))
            graph_text_group.add(graph_text)
            graphs.add(graph)

        # Limit function: y = 0 for 0 ≤ x < 1
        limit_line = axes.plot(
            lambda x: 0,
            x_range=[0, 1],
            color=C_PURPLE
        )

        # Open circle at (1,0)
        open_dot = Dot(
            axes.c2p(1, 0),
            color=C_PURPLE,stroke_width=2
        )
        open_dot.set_fill(opacity=0)  # makes it open

        # Closed dot at (1,1)
        closed_dot = Dot(
            axes.c2p(1, 1),
            color=C_PURPLE
        )

        #### These are the texts for the graph animations
        text_1 = MathTex(r"\text{ Graph of }",r"f_n(x) = x^n",r", x \in [0,1]",r"\text{ where }",
                         r"f(x)" ,r"=",r" \begin{cases} "
                         r"0 & \text{if } 0 \le x < 1\\ "
                         r"1 & \text{if } x = 1 "
                         r"\end{cases}",font_size=30).to_corner(UP,buff=0.5)
        colour_giver(text_1,(1,2,4,6),(C_BLUE,C_GREEN,C_BLUE,C_GREEN))
        
        self.wait(2)
        self.play(Write(text_1),rate_func=smooth)
        self.play(Create(axes), Write(labels))
        self.play(LaggedStart(*[Create(g) for g in graphs], lag_ratio=0.5),rate_func=smooth)
        self.play(FadeIn(graph_text_group))
        self.wait(2)

        self.play(Create(limit_line))
        self.play(FadeIn(open_dot), FadeIn(closed_dot))
        self.wait(3)

        #### The epsilon texts and animation starts here
        epsilon = ValueTracker(0.1)  # choose epsilon

        text_2 = MathTex(r"\text{Picking }" r"\epsilon",r"\text{ = }",r"\text{ 0.1}").to_corner(UP,buff=0.5)

        text_3 = MathTex(r"\text{Note: Not all the function values are inside the }",r" \epsilon",r"\text{ band}",font_size=30).to_corner(UP,buff=0.5)
        
        text_3[1].set_color(C_RED)

        text_4 = MathTex(r"\text{This implies}",r"\textbf{ Pointwise convergence}",font_size=30).to_corner(UP,buff=0.5)

        text_5 = MathTex(r"\text{Note what happens as n increases, the functions jump towards } ",r"x_o = 1",font_size=30).to_corner(UP,buff=0.5)
        text_5[1].set_color(C_GREEN)

        upper_eps = axes.plot(
            lambda x: epsilon.get_value(),
            x_range=[0, 1],
            color=C_RED
        )
    
        lower_eps = axes.plot(
            lambda x: -epsilon.get_value(),
            x_range=[0, 1],
            color=C_RED
        )
        
        eps_band = axes.get_area(
            upper_eps,
            x_range=[0, 1],
            bounded_graph=lower_eps,
            color=C_RED,
            opacity=0.2
        )

        epsilon_group = VGroup(lower_eps,upper_eps,eps_band)
        epsilon_group.save_state()

        self.play(ReplacementTransform(text_1,text_2))
        self.wait(2)
        self.play(Create(upper_eps), Create(lower_eps))
        self.wait(2)

    
        self.play(epsilon_group.animate.shift(UP),rate_func=smooth)
        self.wait(2)
        self.play(epsilon_group.animate.shift(UP*0.5),run_time=1.5,rate_func=smooth)
        self.wait(2)
        self.play(Restore(epsilon_group))

        self.wait(2)
        self.play(ReplacementTransform(text_2,text_3))
        self.wait(2)

        self.play(ReplacementTransform(text_3,text_4))
        self.wait(4)
        self.play(Uncreate(eps_band),Uncreate(upper_eps),Uncreate(lower_eps))

        self.play(ReplacementTransform(text_4,text_5))

        ### x = 0, v line
        x_line = DashedLine(axes.c2p(1, 0), axes.c2p(1, 1), color=C_GREEN)
        x_label = MathTex(r"x_o = 1", font_size=30).next_to(axes.c2p(1, 0), DOWN, buff=0.1).set_color(C_GREEN)    
        
        self.play(Write(x_line), Write(x_label))

        ### Arrows by the pointing to graph texts and slowly transformed between functions
        arrows = VGroup()
        for graph, label in zip(graphs, graph_text_group):
            arrow = Arrow(label.get_bottom() + DR*0.5, label.get_bottom() , color=C_PURPLE,buff=0.1).scale(1.5)
            arrows.add(arrow)
            
        current_arrow = arrows[0]
        self.play(Create(current_arrow))

        for next_arrow in arrows[1:]:
            self.play(ReplacementTransform(current_arrow, next_arrow))
            current_arrow = next_arrow
            self.wait(1)
        
        self.wait(5)
