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


class uniform(Scene):
    def construct(self):
        ## Header of the file 
        header = BeamerBlock("Definition",width=14).move_to(ORIGIN)
        
        ### colour_giver function
        def colour_giver(mob, indices, colors):
            for index, color in zip(indices, colors):
                # If it's nested like (0,1)
                if isinstance(index, (list, tuple)):
                    mob[index[0]][index[1]].set_color(color)
                # If it's single level like 2
                else:
                    mob[index].set_color(color)
        
        ### Slides indicate the display of a particular set of mobjects at once on the screen

        ####
        ## Slide 1: Definition of uniform convegence
        ####

        text1 = MathTex(
            r"\text{A sequence of functions } ",r"(f_n)_{n\in\mathbb{N}}",
            r"\text{ on } ",r"X \subset \mathbb{R}^n",
            r"\text{ converges uniformly to } ",r"f",r", \text{ if}",font_size=35
        )
        colour_giver(text1,[1,3],[C_BLUE,C_GREEN])

        text2 = MathTex(
            r"\lim_{n \to \infty}",
            r"\sup_{x \in X}",
            r"| ",r"f_n(x)",r" - ",r"f(x) ",r"|",
            r"= 0",font_size=35
        )
        text2[3].set_color(C_BLUE)
        
        text3 = VGroup(MathTex(
            r"\text{Quantifier form}",font_size=35), 
            MathTex(r"\forall \epsilon > 0",
            r"\exists n_0 \forall n \ge n_0",
            r"\forall x \in X :", r"| ",r"f_n(x)",r" - ",r"f(x) ",r"| ",
            r"\le ",r"\epsilon",font_size=35
        )).arrange(DOWN, buff=0.5,aligned_edge=LEFT)

        colour_giver(text3,([1,0],[1,1],[1,2],[1,4],[1,9]),(C_RED,C_GREEN,C_BLUE,C_BLUE,C_RED))
        
        text4 = MathTex(
            r"\text{All function graphs approach the limit function}",
            r"\text{ simultaneously (uniformly).}",font_size=35
        )

        slide_1_texts = VGroup(text1,text2,text3,text4).arrange(DOWN,buff=0.7,aligned_edge=LEFT)
        
        self.add(header)

        ## Loop for playing the slide in texts 1
        for i in slide_1_texts:
            self.play(Write(i),rate_func=smooth)
            self.wait(2)

        self.wait(2)
        self.play(FadeOut(slide_1_texts),rate_func=smooth)
        self.wait(1)

        ####
        ## Slide 2: Pointwise convegence and uniform convegence
        ####

        text5 = MathTex(r"\textbf{Pointwise vs Uniform convegence}",font_size=40)
        text6 = MathTex(r"\text{Have a look at the each convergence }",font_size=35)

        text7 = VGroup(
            MathTex(r"\text{Pointwise: } ",
                        r"\forall \epsilon > 0 \text{ }",
                        r"\exists n_0",r"\forall n \ge n_0 \text{ }",
                        r"\forall x \in X :",
                        r"| ",r"f_n(x) ",r"- ",r"f(x) ",r"| ",r" \le ",r" \epsilon",font_size=35),

            MathTex(r"\text{Uniform: }", r"\forall x \in X ", r"\forall \epsilon > 0 \text{ }",
            r"\exists n_0",r"\forall n \ge n_0: \text{ }",
            r"| ",r"f_n(x)",r" - ",r"f(x) ",r"| \le ",r"\epsilon",font_size=35)
            ).arrange(DOWN,aligned_edge=LEFT)
        
        colour_giver(text7,([0,1],[0,2],[0,3],[0,4],[0,6],[0,11]),(C_RED,C_GREEN,C_GREEN,C_GREEN,C_BLUE,C_RED))
        colour_giver(text7,([1,1],[1,2],[1,3],[1,4],[1,6],[1,10]),(C_GREEN,C_RED,C_GREEN,C_GREEN,C_BLUE,C_RED))

        text8 = MathTex(r"\text{Note: The difference is the position of the quantifiers. This slight difference means}",font_size=35)
        text9 = MathTex(r"\text{the pointwise convegence applies to a given point, x}",font_size=35)
        text10 = MathTex(r"\text{while uniform convergence applies to the whole space } X \text{ simultaneously.}",font_size=35)
        ## underlines for text  9 and text 10
       
        slide_2_texts = VGroup(text6,text7,text8,text9,text10).arrange(DOWN, buff=0.5,aligned_edge=LEFT)
        
        slide_2_texts_1 = VGroup(text5,slide_2_texts).arrange(DOWN)
        slide_2_texts_1 = VGroup(text5,slide_2_texts).arrange(DOWN,buff=0.7)

        text_pointwise_underline = Underline(text7[0][1:]).set_color(C_YELLOW)
        text_uniform_underline = Underline(text7[1][1:]).set_color(C_YELLOW)

        self.play(Write(text5),rate_func=smooth)
        self.wait(2)

        for i in range(0,3,1):
            self.play(Write(slide_2_texts[i]),rate_func=smooth)
            self.wait(2.5)

        self.play(Create(text_pointwise_underline),rate_func=smooth)
        self.play(Create(text9),rate_func=smooth)
        self.wait(2)
        self.play(Uncreate(text_pointwise_underline),rate_func=smooth)

        self.wait(2)

        self.play(Create(text_uniform_underline),rate_func=smooth)
        self.play(Create(text10),rate_func=smooth)
        self.wait(2)
        self.play(Uncreate(text_uniform_underline),rate_func=smooth)
        self.wait(3)
        self.play(FadeOut(slide_2_texts_1),rate_func=smooth)

        #####
        ##    slide 3: 
        ####
        text_11 = MathTex(r"\textbf{Important notes}",font_size=40)

        text12 = VGroup(MathTex(
            r"\text{\textbullet\ Uniform }",
            r"\Rightarrow",
            r"\text{ pointwise, but not vice versa.}",font_size=30),
            MathTex(r"\text{\textbullet\ Only with uniform convergence are properties preserved:}",
            r"\text{ continuity of the limit function}",font_size=30),
            MathTex(r"\text{ and integratibility }",font_size=30)
        )

        slide_3_texts = VGroup(text_11,text12).arrange(DOWN, buff=0.5).shift(UP*1.5)

        text12.arrange(DOWN, buff=0.5,aligned_edge=LEFT)

        for i in slide_3_texts:
            self.play(Write(i),rate_func=smooth)
            self.wait(1)

        self.wait(2)
        

class uniform_example(Scene):
    def construct(self):

        ### Function to give color to specific indices of a Mobject, useful for coloring specific parts of a MathTex or VGroup without having to create separate MathTex objects for each part. It takes in the Mobject, a list of indices (which can be nested for subparts), and a list of corresponding colors. It then iterates through the indices and applies the specified color to each part of the Mobject.
        def colour_giver(mob, indices, colors):
            for index, color in zip(indices, colors):
                # If it's nested like (0,1)
                if isinstance(index, (list, tuple)):
                    mob[index[0]][index[1]].set_color(color)
                # If it's single level like 2
                else:
                    mob[index].set_color(color)

        ### texts of the page 
        text_1 = VGroup(
            MathTex(r"\textbf{Uniform convergence states}",font_size=38),
            MathTex(r"\forall \epsilon > 0 \text{ }",
            r"\exists n_0 \forall n \ge n_0 \text{ }",
            r"\forall x \in X :", r"| ",r"f_n(x)",r" - ",r"f(x) ",r"| ",
            r"\le ",r"\epsilon",font_size=30
        )).arrange(DOWN,buff=0.2).to_corner(UP,buff=0.5)

        colour_giver(text_1,([1,0],[1,1],[1,2],[1,4],[1,5],[1,9]),(C_RED,C_GREEN,C_GREEN,C_GREEN,C_BRIGHT_BLUE,C_RED))

        text_2 = MathTex(
            r"\text{ This means if we take a sequence of functions }",r"f_1,f_2,f_3...}",font_size=30
        ).to_corner(UP,buff=0.5)

        text_2[1].set_color(C_BRIGHT_BLUE)

        text_3 = MathTex(
            r"\text{and their limit function }",r"f",font_size=30
        ).to_corner(UP,buff=0.5)
       

        text_4 = MathTex(
            r"\text{Picking an }",r"\epsilon > 0",font_size=30
        ).to_corner(UP,buff=0.5)
        text_4[1].set_color(C_RED)

        text_5 = MathTex(
            r"\text{Note what happens as ",r"n",r" increases}",font_size=30
        ).to_corner(UP,buff=0.5)
        text_5[1].set_color(C_GREEN)

        text_6 = VGroup(MathTex(
            r"\text{We eventually reach an ",r"n",
            r", where subsequent functions }",font_size=30),
            MathTex(r"\text{are within }",r"\epsilon",
                    r"\text{ of the limit function}",font_size=30)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).to_corner(UP,buff=0.5)
        colour_giver(text_6,([0,1],[1,1]),(C_GREEN,C_RED))

        text_7 = MathTex(
            r"\text{We write this as for all } ",r"n \ge \text{ N} ",r"\text{ and for all } ",
            r"x \in X",font_size=30
        ).to_corner(UP,buff=0.5)
        colour_giver(text_7,(1,3),(C_GREEN,C_GREEN))

        text_8 = VGroup(
            MathTex(r"\text{Also note that } |",r"f_n(x)",r" - ",r" f(x) ",r"| \text{ is less than }",font_size=30),
            MathTex(r"\epsilon",r"\text{ for all }",r" x \in X",r"\text{, not just a single point.}",font_size=30)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).to_corner(UP,buff=0.5)
        colour_giver(text_8,([0,1],[1,0],[1,2]),(C_BRIGHT_BLUE,C_RED,C_GREEN))

        text_9 = MathTex(r"\text{ Picking a smaller } ",
                         r"\epsilon",font_size=30).to_corner(UP,buff=0.5)
        text_9[1].set_color(C_RED)

        text_10 = VGroup(
            MathTex(
            r"\text{We reach another n, where subsequent functions are} ",font_size=30),
            MathTex(r"\text{within this smaller }",
            r"\epsilon",r"\text{ of the limit function}",r"f",font_size=30
        )).arrange(DOWN, buff=0.2, aligned_edge=LEFT).to_corner(UP,buff=0.5)
        text_10[1][1].set_color(C_RED)
       
        text_11 = VGroup(
            MathTex(r"\text{ Once these conditions are met, We have a}",font_size=30),
            MathTex(r"\textbf{ uniform convergence}",font_size=30)
        ).arrange(DOWN, buff=0.2).to_corner(UP,buff=0.5)

        text_12 = VGroup(
            MathTex(r"\text{As } ",r"n",r"\text{ Continues to increase, watch how",font_size=30),
            MathTex(r"\text{ the functions get closer to the limit function }",r"f",font_size=30)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).to_corner(UP,buff=0.5)
        text_12[0][1].set_color(C_GREEN)


        ### Axes for y_range 0 - 6 and x_range 0 _ 9 
        ax = Axes(
            x_range=[0,10,1],
            y_range=[0,7,1],
            x_length=7,y_length=5,
        ).add_coordinates()

        #### plotting the function of y = (2/n)sinx + x/3 + 2 and y = x/3 + 2
       
        graph_tracker = ValueTracker(1)
        
        graph = always_redraw(
            lambda: ax.plot(lambda x: (2/graph_tracker.get_value())*np.sin(x) + x/3 + 2, color=C_BRIGHT_BLUE)
        )
        
        graph_text = always_redraw(
            lambda: MathTex(rf"f_{{{int(graph_tracker.get_value()-1)}}}",color=C_BRIGHT_BLUE).move_to(ax.c2p(2, (2/graph_tracker.get_value())*np.sin(2) + 2 + 2) + UP*0.3)
        )
        
        limit_graph= ax.plot(lambda x: x/3 + 2,
                         x_range=[0,10],
                        color=C_MAGENTA)
        
        limit_graph_text = MathTex(r"f").next_to(limit_graph,RIGHT,buff=0.1)
        epsilon_tracker = ValueTracker(0.8)

        epsilon_upper_bound = always_redraw(
            lambda: ax.plot(lambda x: x/3 + 2 + epsilon_tracker.get_value(), color=C_RED)
        )

        epsilon_lower_bound = always_redraw(
            lambda: ax.plot(lambda x: x/3 + 2 - epsilon_tracker.get_value(), color=C_RED)
        )

        epsilon_band = always_redraw(
            lambda:     Polygon(
            ax.c2p(0, 2 + epsilon_tracker.get_value()),
            ax.c2p(10, 10/3 + 2 + epsilon_tracker.get_value()),
            ax.c2p(10, 10/3 + 2 - epsilon_tracker.get_value()),
            ax.c2p(0, 2 - epsilon_tracker.get_value()),
            stroke_width=0,
            fill_color=C_RED,
            fill_opacity=0.2
        ))
        
        epsilon_higher_text = always_redraw(
            lambda: MathTex(r"\epsilon \text{ + L}",font_size=30).set_color(C_RED).next_to(epsilon_upper_bound.get_start(),LEFT,buff=0.7)
        )

        epsilon_lower_text = always_redraw(
            lambda: MathTex(r"\epsilon \text{ - L}",font_size=30).set_color(C_RED).next_to(epsilon_lower_bound.get_start(),LEFT,buff=0.7)
        )
        
        ## This part is for the animations of the graphs and the texts.

        self.play(Write(text_1))
        self.wait(2)
        self.play(Create(ax),rate_func=smooth,run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(text_1,text_2))
        self.play(Create(graph),Create(graph_text),rate_func=smooth,run_time=2)

        for i in range(2,5,1):
            self.wait(1)
            self.play(graph_tracker.animate.set_value(i))
            self.wait(3)
        
        self.play(graph_tracker.animate.set_value(2),run_time=4,rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3),rate_func=smooth)
        self.play(Create(limit_graph),Create(limit_graph_text),rate_func=smooth,run_time=3)
        self.wait(4)
        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth)
        self.wait(4)
        self.play(Create(epsilon_lower_bound),Create(epsilon_upper_bound),FadeIn(epsilon_band),rate_func=smooth)
        self.play(Write(epsilon_lower_text),Write(epsilon_higher_text))
        self.wait(4)
        self.play(ReplacementTransform(text_4,text_5),rate_func=smooth)
        self.wait(2)
        
        for i in range(2,5,1):
            self.play(graph_tracker.animate.set_value(i))
            self.wait(1)
        
        self.play(ReplacementTransform(text_5,text_6),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_6,text_7),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_7,text_8),rate_func=smooth)
        self.wait(4)
        
        self.play(ReplacementTransform(text_8,text_9))
        self.wait(4)
        self.play(epsilon_tracker.animate.set_value(0.3),run_time=4,rate_func=smooth)
        self.wait(2)

        for i in range(5,9,1):
            self.play(graph_tracker.animate.set_value(i))
            self.wait(1)
        
        self.play(ReplacementTransform(text_9,text_10),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_10,text_11),rate_func=smooth)
        self.wait(4)

        self.play(ReplacementTransform(text_11,text_12),rate_func=smooth)
        self.wait(4)
        
        self.play(graph_tracker.animate.set_value(30),rate_func=smooth,run_time=10)
        self.wait(4)
        
