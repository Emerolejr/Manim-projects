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


class legacy_code(Scene):
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

        ## These are the texts that are used within the code.
        text_1 = MathTex(
            r"\text{Consider the sequence of functions }",r" f_1, f_2, f_3, f_4, \dots",
            font_size=36
        ).to_corner(UP,buff=0.5)
        text_1[1].set_color(C_BRIGHT_BLUE)

        text_2 = MathTex(
            r"\text{Notice that the graphs approach a certain shape.}",
            font_size=36
        ).to_corner(UP,buff=0.5)

        text_3 = MathTex(
            r"\text{This straight line is the graph of a function called } ",r"f.",
            font_size=36
        ).to_corner(UP,buff=0.5)
        text_3[1].set_color(C_PURPLE)

        text_4 = MathTex(
            r"\text{We can say }",r'\lim_{n \to \infty} ',r'f_n ',r'= ',r'f',
            font_size=40
        ).to_corner(UP,buff=0.5)
        text_4[2].set_color(C_BRIGHT_BLUE)
        text_4[4].set_color(C_PURPLE)

        text_5 = MathTex(
            r"\text{Making this more precise...}",
            font_size=36
        ).to_corner(UP,buff=0.5)

        text_6 = MathTex(
            r"\text{Pick a point } ",r"x ",r" \text{ in the domain.}",
            font_size=36
        ).to_corner(UP,buff=0.5)
        text_6[1].set_color(C_GREEN)

        text_7 = MathTex(
            r"\text{We can say }",r"f_n",r"\to",r"f ",r"\text{ if }",r" f_n(x)",r" \to",r" f(x).",
            font_size=36
        ).to_corner(UP,buff=0.5)

        colour_giver(text_7,(1,3,5,7),(C_BRIGHT_BLUE,C_PURPLE,C_BRIGHT_BLUE,C_PURPLE))


        text_8 = MathTex(
            r"\text{Or better put: } \lim_{n \to \infty} ",r" f_n(x)",r" =",r" f(x)",
            font_size=40
        ).to_corner(UP,buff=0.5)
        colour_giver(text_8,(1,3),(C_BRIGHT_BLUE,C_PURPLE))

        text_8[1].set_color(C_BRIGHT_BLUE)

        text_9 = MathTex(
            r"\text{This must hold for every } ",r"x",r" \text{ in the domain.}",
            font_size=36
        ).next_to(text_8, DOWN,buff=0.2)
        text_9[1].set_color(C_GREEN)

        text_10 = MathTex(
            r"\text{This is called Pointwise Convergence.}",
            font_size=38
        ).to_corner(UP,buff=0.5)
                

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
            lambda: MathTex(rf"f_{{{int(graph_tracker.get_value())}}}",color=C_BRIGHT_BLUE).to_corner(UP,buff=0.5).shift(RIGHT*2.5)
        )

        graph2 = ax.plot(lambda x: x/3 + 2,
                         x_range=[0,10],
                        color=C_PURPLE)
        
        graph_text2 = MathTex(r"f").next_to(graph2, UP,buff=0.1).set_color(C_PURPLE)

        ## This part is for the animations of the graphs and the texts.
        self.play(Create(ax),rate_func=smooth,run_time=2)

        self.play(Write(text_1),rate_func=smooth,run_time=1.5)
        self.play(Create(graph),rate_func=smooth,run_time=1.5)

        self.play(ReplacementTransform(text_1,graph_text),rate_func=smooth,run_time=1.5)

        for i in range(1,30,1):
            self.play(graph_tracker.animate.set_value(i))
            self.wait(0.5)

        self.play(ReplacementTransform(graph_text,text_2),rate_func=smooth,run_time=1.5)
        
        self.play(Create(graph2),rate_func=smooth,run_time=1.5)
        self.wait(3)
        self.play(ReplacementTransform(text_2,text_3),Write(graph_text2),rate_func=smooth,run_time=1.5)
        self.wait(4)
        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth,run_time=1.5)
        self.wait(4)
        self.play(graph_tracker.animate.set_value(1),rate_func=smooth,run_time=1.5)
        self.play(ReplacementTransform(text_4,text_5),FadeOut(graph),rate_func=smooth,run_time=1.5)
        self.wait(1)

      
        self.play(FadeIn(graph),rate_func=smooth,run_time=1.5)
        

        self.play(ReplacementTransform(text_5,text_6),rate_func=smooth,run_time=1.5)

            ## this part picks a point x = 2 on the x axis, maps it to graph 1 and graph 30, with a redraw arrow pointing from graphs[0] to graph2 and from graphs[no_graphs-1] to graph2, respectively. 
            # It then animates the arrows moving along the graphs as n increases.
            # and a dot on each of the two points. It then animates the dots moving along the graphs as n increases, all the whilw displaying the value of f_n(x) and f(x) next to the dots, respectively.
        # Track x and n
        x = ValueTracker(2)
        n_tracker = ValueTracker(1)

        # Moving point on f_n
        dot_1 = always_redraw(
            lambda: Dot(color=C_BRIGHT_BLUE).move_to(
                ax.c2p(
                    x.get_value(),
                    (2/n_tracker.get_value()) * np.sin(x.get_value()) + x.get_value()/3 + 2
                )
            )
        )

        # Limit function point
        dot_2 = always_redraw(
            lambda: Dot(color=C_PURPLE).move_to(
                ax.c2p(
                    x.get_value(),
                    x.get_value()/3 + 2
                )
            )
        )

        # x-axis point
        dot_x = always_redraw(
            lambda: Dot(color=WHITE).move_to(
                ax.c2p(x.get_value(), 0)
            )
        )

        # Dynamic label f_n(x)
        text_fn = always_redraw(
            lambda: MathTex(
                rf"f_{{{int(n_tracker.get_value())}}}(x)",
                color=C_BRIGHT_BLUE
            ).scale(0.6).next_to(dot_1, DL, buff=0.2)
        )

        # Label f(x)
        text_f = always_redraw(
            lambda: MathTex(
                r"f(x)",
                color=C_PURPLE
            ).scale(0.6).next_to(dot_2, UP, buff=0.2)
        )

        # Arrow between points (IMPORTANT: use get_center(), not c2p again)
        arrow = always_redraw(
            lambda: Arrow(
                start=dot_1.get_center(),
                end=dot_2.get_center(),
                buff=0.1,
                tip_shape=StealthTip
            )
        )

        # Guide lines
        line_1 = always_redraw(
            lambda: ax.get_vertical_line(dot_1.get_center())
        )

        line_2 = always_redraw(
            lambda: ax.get_horizontal_line(dot_1.get_center())
        )

        line_3 = always_redraw(
            lambda: ax.get_horizontal_line(dot_2.get_center())
        )

        ### animaion of the dots, arrows and lines

        self.play(FadeIn(dot_1),FadeIn(dot_2),FadeIn(dot_x),rate_func=smooth,run_time=1.5)

        self.play(FadeIn(text_fn),FadeIn(text_f),rate_func=smooth,run_time=1.5)

        self.play(Create(line_1),Create(line_2),Create(line_3),rate_func=smooth)
        self.play(Create(arrow),rate_func=smooth,run_time=1.5)
        self.play(Uncreate(line_1),rate_func=smooth)
            
        self.wait(1)
            
        ### Moving dot_1 towards target dot.
     
        self.play(ReplacementTransform(text_6,text_7),rate_func=smooth,run_time=1.5)
        self.play(n_tracker.animate.set_value(29), run_time=10)

        self.wait(4)
        self.play(ReplacementTransform(text_7,text_8),rate_func=smooth,run_time=1.5)
        self.wait(2)
        self.play(Write(text_9),rate_func=smooth,run_time=1.5)
        self.play(Uncreate(arrow),rate_func=smooth,run_time=1.5)
        self.play(FadeOut(text_fn),FadeOut(text_f),rate_func=smooth,run_time=1.5)
        self.wait(2)

        self.play(n_tracker.animate.set_value(1), rate_func=smooth, run_time=3)

        ### Moving the x value along the x axis to show that the convergence holds for every x in the domain.
        self.play(x.animate.set_value(7),rate_func=smooth,run_time=2)
        self.play(x.animate.set_value(3),rate_func=smooth,run_time=1)
        self.play(x.animate.set_value(6),rate_func=smooth,run_time=1)
        self.play(x.animate.set_value(8),rate_func=smooth,run_time=1)
        self.wait(3)

        self.play(Create(arrow),rate_func=smooth,run_time=1.5)
        self.wait(1)
        
        self.play(FadeIn(text_fn),FadeIn(text_f),rate_func=smooth,run_time=1)
        self.play(n_tracker.animate.set_value(29), run_time=6)
        self.wait(2)

        self.play(ReplacementTransform(VGroup(text_8,text_9),text_10),rate_func=smooth,run_time=1.5)
        self.wait(2)
        self.play(n_tracker.animate.set_value(1), rate_func=smooth, run_time=3)
        self.wait(2)
        