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


class cauchy_sequence_algebra(Scene):
    def construct(self):
        #### Header of the text
        header = BeamerBlock("Cauchy Sequence",width=14.5).move_to(ORIGIN)

        ####
        ## Functions for repetitive tasks 
        ####

        ###  Function for colour
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
                self.wait(2)

        ###
        ## Steps for algebraic intepretation of Cauchy sequence
        ###
                
        ### First part: steps How Cauchy sequence implies Convergence

        body_font = 35

        top_text_1 = MathTex(r"\text{How Cauchy Sequence } \implies \text{Convegence}",font_size=40).shift(UP*2.5)

        step_1 = VGroup(MathTex(r"\text{Sequence }",r"a_n",
                                r"\text{ is cauchy if :}" ,font_size=body_font),
                        MathTex(r" \forall \epsilon > 0",
                                r" \text{ } \exists N(\epsilon) \text{ }",
                                r" \forall \text{ m,n} \ge \text { N: }",
                                r" |a_n - a_m|",r"<" ,r" \epsilon",font_size=body_font)
        ).arrange(direction=DOWN,buff=0.2,aligned_edge=LEFT)
        colour_giver(step_1,([0,1],[1,0],[1,1],[1,2],[1,3],[1,5]),(C_BLUE,C_RED,C_GREEN,C_GREEN,C_BLUE,C_RED))
    
        step_2 = MathTex(r"\text{For convegence: }",r"a_n ",r"\to ",r" \text{ L}",
            font_size=body_font)
        
        colour_giver(step_2,(1,3),(C_BLUE,C_BLUE))

        step_3 = VGroup(MathTex(r"\text{Then for any }",
                                r" \epsilon > 0, ",r"\text{there exists, }",
                                r" \text{N }",r" \text{such that: }",font_size=body_font),
                        MathTex(r"|a_n - a_m|",r"<",
                                r" \frac{\epsilon}{2} ",
                                r"\text{ } \forall n > N",font_size=body_font)
                                ).arrange(direction=DOWN,buff=0.2,aligned_edge=LEFT)
        colour_giver(step_3,([0,1],[0,3],[1,0],[1,2],[1,3]),(C_RED,C_BLUE,C_BLUE,C_RED,C_GREEN))

        #### These classify the step texts into how they will appear in screen. 
        first_grouped = VGroup(step_1,step_2,step_3).arrange(DOWN,aligned_edge=LEFT,buff=0.8).next_to(top_text_1,DOWN,buff=0.5)

        step_4 = VGroup(
            MathTex(r"\text{Now take }",r"\forall n \ge N",font_size=body_font),
            MathTex(r"|a_n - a_m|",r" = ",r" |a_n - L + L - a_m| ",
                    r"\le ",r" |a_n - L| + |a_m - L| ",
                    r"\text{ (Triangle inequality)}",font_size=body_font),
        ).arrange(direction=DOWN,buff=0.2,aligned_edge=LEFT)

        colour_giver(step_4,([0,1],[1,0],[1,2],[1,4]),(C_GREEN,C_BLUE,C_BLUE,C_BLUE))

        step_5 = VGroup(
            MathTex(r"\text{Each term is } ",
                    r" \frac{\epsilon}{2}",
                    r"\text{, So :}",font_size=body_font),
            MathTex(r"|a_n - a_m|",r" < ",r" \epsilon",font_size=body_font)
        
        ).arrange(direction=DOWN,buff=0.2,aligned_edge=LEFT)

        colour_giver(step_5,([0,1],[1,0],[1,2]),(C_RED,C_BLUE,C_RED))

        step_6 = MathTex(r"\therefore \text{ Convegent } \implies \text{ Cauchy}",
                         font_size=body_font)
        
        ### Second group of texts
        second_grouped = VGroup(step_4,step_5,step_6).arrange(direction=DOWN,aligned_edge=LEFT,buff=0.8).next_to(top_text_1,DOWN,0.5)

        #### Example of Cauchy sequence
        top_text_2 = MathTex(r"\text{To illustrate } \text{ Convegent } \implies \text{ Cauchy}",
                             font_size=40).shift(UP*2.5)

        step_7 = MathTex(r"\text{Given : } ",
                         r" a_n",r"= ",
                         r"2 + \frac{(-1)^2}{\sqrt{n}}",font_size=body_font)
        colour_giver(step_7,(1,3),(C_BLUE,C_BLUE))

        step_8 = MathTex(
            r"\text{Simplifying  }",r"|a_n - a_m|",
            r"=", r"\left| \left(2 + \frac{(-1)^n}{\sqrt{n}}\right)",
            r" - ",r"\left( 2 + \frac{(-1)^m}{\sqrt{m}} \right)",r"\left|",
            font_size=body_font
        )
        step_8[4:].set_color(C_BLUE)
        colour_giver(step_8,(1,3,5),(C_BLUE,C_BLUE,C_BLUE))

        step_9 = MathTex(r"=",r"\left| \frac{(-1)^n}{\sqrt{n}} - \frac{(-1)^m}{\sqrt{m}} \right|",
                         font_size=body_font)
        
        step_9[1].set_color(C_BLUE)

        step_10 = MathTex(r"\le",r"\left| \frac{(-1)^n}{\sqrt{n}} \right|",
                          r"\text{ + }",r"\left| \frac{(-1)^m}{\sqrt{m}} \right|",
                          r"\text{  (Triangle Inequality)}",
                          font_size=body_font)
        colour_giver(step_10,(1,3),(C_BLUE,C_BLUE))

        step_11 = MathTex(r"=",r"\frac{1}{\sqrt{n}}",r"\text{ + }",r"\frac{1}{\sqrt{m}}",
                          font_size=body_font)
        colour_giver(step_11,(1,3),(C_BLUE,C_BLUE))

        #### Third group of texts
        third_grouped = VGroup(step_7,step_8,step_9,step_10,step_11).arrange(direction=DOWN,buff=0.3).next_to(top_text_2,DOWN,buff=0.5)
        
        step_9.align_to(step_8[2],LEFT)
        step_10.align_to(step_8[2],LEFT)
        step_11.align_to(step_8[2],LEFT)  
        
        step_12 = VGroup(MathTex(r"\text{If }",r"\text{n,m }",r"\ge \text{N, then:}",font_size=body_font),
                         MathTex(r"\frac{1}{\sqrt{n}}",r"\le",r" \frac{1}{\sqrt{N}}",
                                 r"\text{ and }",
                                 r"\frac{1}{\sqrt{m}}",r" \le",r" \frac{1}{\sqrt{N}}",font_size=body_font)
                                 ).arrange(direction=DOWN,buff=0.2,aligned_edge=LEFT)
        
        colour_giver(step_12,([0,1],[0,2],[1,0],[1,2],[1,4],[1,6]),(C_GREEN,C_GREEN,C_GREEN,C_GREEN,C_GREEN,C_GREEN))
        
        step_13 = MathTex(r"|a_n - a_m|",r" \le ",r"\frac{1}{\sqrt{N}}",r" \text{ + }",r" \frac{1}{\sqrt{N}}",
                          font_size=body_font)
        colour_giver(step_13,(0,2,4),(C_BLUE,C_GREEN,C_GREEN))

        step_14 = MathTex(r"|a_n - a_m|",r" \le ",r"\frac{2}{\sqrt{N}}",
                          font_size=body_font)
        colour_giver(step_14,(0,2),(C_BLUE,C_GREEN))

        step_15 = MathTex(r"\text{Recall for Cauchy sequences, }",r"|a_n - a_m|",r" < ",r"\epsilon",
                          font_size=body_font)
        colour_giver(step_15,(1,3),(C_BLUE,C_RED))

        step_16 = MathTex(r"|a_n - a_m|",r" \le ",r"\frac{2}{\sqrt{N}}",r" < ",r"\epsilon",
                          font_size=body_font)
        

        #### fourth group 
        fourth_grouped = VGroup(step_12,step_13,step_14,step_15,step_16).arrange(DOWN,buff=0.35, aligned_edge=LEFT).next_to(top_text_1,DOWN,buff=0.5)

        colour_giver(step_16,(0,2,4),(C_BLUE,C_GREEN,C_RED))

        ###
        ## Finding n(e) 
        ###

        top_text_3 = MathTex(r"\text{for }",r"N(\epsilon),",r" \text{ and } ",r" \epsilon",r"\text{ choice}",
                            font_size=40).shift(UP*2.5)
        
        colour_giver(top_text_3,(1,3),(C_GREEN,C_RED))

        step_17 = MathTex(r"\frac{2}{\sqrt{N}}",r" < ",r"\epsilon",
                          font_size=body_font)
        
        colour_giver(step_17,(0,2),(C_GREEN,C_RED))


        step_18 = MathTex(r"N",r">",r"\frac{4}{\epsilon^2}",
                          font_size=body_font)
        
        colour_giver(step_18,(0,2),(C_GREEN,C_RED))

        step_19 = MathTex(r"\implies",r"\forall \epsilon > 0",r"\text{, }",r"N ",r" > ",r" \frac{4}{\epsilon^2}",
                          font_size=body_font)
        
        colour_giver(step_19,(1,3,5),(C_RED,C_GREEN,C_RED))

        step_20 = MathTex(r"\text{Say we pick }",r" \epsilon",r" = "
                          ,r" \text{ 0.5}",font_size=body_font)
        
        colour_giver(step_20,(1,3),(C_RED,C_RED))
        
        step_21 = MathTex(r"N(\epsilon)",r">",r"16",font_size=body_font)
        colour_giver(step_21,(0,2),(C_GREEN,C_GREEN))

        fifth_grouped = VGroup(step_17,step_18,step_19,step_20,step_21).arrange(DOWN,buff=0.35).next_to(top_text_3,DOWN,buff=0.5)

        last_text = MathTex(r"\text{Showing graphically}")
        ### 
        ## The animationns for the algebra of cauchy criterium
        all_grouped = VGroup(first_grouped,second_grouped,third_grouped,fourth_grouped,fifth_grouped)
        
        self.add(header)
        self.play(Write(top_text_1),rate_func=smooth)
        
        ### An animation function that controls how everything fades in and out of the function
        def fadein_and_fadeout(mob):
            play_mob(mob)
            self.wait(2)
            self.play(FadeOut(mob),rate_func=smooth)

        for i in all_grouped[0:2]:
            fadein_and_fadeout(i)
        self.play(ReplacementTransform(top_text_1,top_text_2),rate_func=smooth)

        for i in all_grouped[2:4]:
            fadein_and_fadeout(i)
        self.play(ReplacementTransform(top_text_2,top_text_3),rate_func=smooth)

        fadein_and_fadeout(all_grouped[4])

        self.play(FadeOut(*self.mobjects))
        self.play(Create(last_text))
        self.wait(2)

class cauchy_sequence_graph(Scene):
    def construct(self):
        self.next_section(name="second",skip_animations=True)
        ###  Function for colour
        def colour_giver(mob, indices, colors):
            for index, color in zip(indices, colors):
                # If it's nested like (0,1)
                if isinstance(index, (list, tuple)):
                    mob[index[0]][index[1]].set_color(color)
                # If it's single level like 2
                else:
                    mob[index].set_color(color)

        #### Graph plots.
        ax = Axes(
            x_range=[0, 101, 10],
            y_range=[0, 4, 0.5],
            x_length=11,
            y_length=6,
            axis_config={"include_tip": True, "numbers_to_exclude": [ ], "tick_size": 0.05,"tip_shape":StealthTip}
        ).add_coordinates()
        ax.to_edge(DOWN, buff=1.0)
        
        labels = ax.get_axis_labels(x_label="n", y_label="a_n")

        graph_formula_template = MathTex(r"\text{Plotting the graph of }",
                                         r"a_n = 2 + \frac{(-1)^n}{\sqrt{n}}", font_size=48)
        graph_formula_template.to_corner(UP, buff=0.5)
        graph_formula_template[1].set_color(C_BLUE)


        # Sequence dots
        dots = VGroup()
        
        ## Function that Calculate the a_n value of each term
        def seq_func(n):
            """Alternating sequence: a_n = (-1)^n / n"""
            if n == 0: return 0 
            return 2 + (-1)**n/np.sqrt(n)
        
        for n in range(1, 100):
            val = seq_func(n)

            # Create and plot dot, storing y-value for epsilon highlighting
            dot = Dot(ax.c2p(n, val), color=C_BLUE, radius=0.06)
            dot.y_val = val
            dots.add(dot)


        # Epsilon band visualization
        epsilon = ValueTracker(0.5)
        L = 2  # Limit value
        
        upper_line = always_redraw(lambda: DashedLine(
            start=ax.c2p(0, L + epsilon.get_value()/2),
            end=ax.c2p(100, L + epsilon.get_value()/2),
            color=C_RED
        ))

        lower_line = always_redraw(lambda: DashedLine(
            start=ax.c2p(0, L - epsilon.get_value()/2),
            end=ax.c2p(100, L - epsilon.get_value()/2),
            color=C_RED
        ))
        
        region = always_redraw(lambda: Polygon(
            ax.c2p(0, L + epsilon.get_value()/2),
            ax.c2p(100, L + epsilon.get_value()/2),
            ax.c2p(100, L - epsilon.get_value()/2),
            ax.c2p(0, L - epsilon.get_value()/2),
            stroke_width=0,
            fill_color=C_RED,
            fill_opacity=0.2
        ))
        
        label_eps = always_redraw(lambda: 
            MathTex(r"\epsilon = " + f"{epsilon.get_value():.2f}", color=C_RED,font_size=30)
            .next_to(upper_line, UP, buff=0.1)
            .set_x(ax.c2p(int(1.0/epsilon.get_value()),0)[0] + 1)
        )
        
        # Vertical line marking N = 4/epsilon
        v_line = always_redraw(lambda: DashedLine(
            start=ax.c2p(int(4/epsilon.get_value()**2), -1.2+L),
            end=ax.c2p(int(4/epsilon.get_value()**2), 1.2+L),
            color=C_GREEN
        ))
        
        label_N = always_redraw(lambda: 
            MathTex(f"N = {int(4/epsilon.get_value()**2)}", color=C_GREEN)
            .next_to(v_line, DOWN, buff=0.1)
            .shift(RIGHT * 0.8)
        )
        
        ### graph texts for explaining 
        graph_text_1 = MathTex(r"\text{fixing  } ",r"\epsilon ",r"=",r"\text{ 0.5}",font_size=35).to_corner(UP, buff=1.5)
        colour_giver(graph_text_1,(1,3),(C_RED,C_RED))

        graph_text_2 = MathTex(r"\text{Since }",r"\text{N }",r">",r"\frac{4}{\epsilon^2}",
                               r"\text{, We get } ",r"\text{N }",r">",r"\text{ 16}",font_size=35).to_corner(UP, buff=1.5)
        colour_giver(graph_text_2,(1,3,5,7),(C_GREEN,C_RED,C_GREEN,C_GREEN))


        graph_text_3 = MathTex(r"\text{Picking sample pairs of points after index}",r"\text{ N}",font_size=35).to_corner(UP, buff=0.5)

        graph_text_4 = MathTex(r"\text{ After index }",r"N,",r"\text{ the distance between any two terms is less than } ",r"\epsilon",font_size=35).to_corner(UP, buff=0.5)
        colour_giver(graph_text_4,(1,3),(C_GREEN,C_RED))

        graph_text_5 = MathTex(r"\text{  Adjusting }",r" \epsilon ",r"\to ",r"\text{ 0.32}",font_size=35).to_corner(UP, buff=0.5)
        colour_giver(graph_text_5,(1,3),(C_RED,C_RED))

        graph_text_6 = MathTex(r"\text{ The first pair of points no longer lie within the } ",r"\epsilon \\",r"\text{ band because it comes before index N }",font_size=35).to_corner(UP, buff=0.5)
        graph_text_6[1].set_color(C_RED)
        graph_text_7 = MathTex(r"\therefore ",r" \forall \text{n,m } > \text{ N }: ",
                               r"|a_n - a_m|",r"< ",r"\epsilon",font_size=35).to_corner(UP, buff=0.5)

        colour_giver(graph_text_7,(1,2,4),(C_GREEN,C_BLUE,C_RED))
        
        ####
        ### Animations for the graph
        ####
        
        self.next_section(name="second",skip_animations=False)

        self.play(FadeIn(ax),FadeIn(labels),rate_func=smooth)
        self.wait(2)
        self.play(FadeIn(graph_formula_template),rate_func=smooth)
        
        self.wait(2)
        self.play(FadeIn(dots))

        self.wait(2)
        self.play(FadeOut(graph_formula_template),rate_func=smooth)

        self.play(Write(graph_text_1),rate_func=smooth)
        self.play(Create(upper_line), Create(lower_line), FadeIn(region), Write(label_eps), run_time=1.5)
        self.wait(2)

        self.play(Unwrite(graph_text_1),rate_func=smooth)
        self.play(Write(graph_text_2),rate_func=smooth)
         ## V line and N line
        self.play(Create(v_line), Write(label_N))
        self.wait(2)

        self.play(TransformMatchingTex(graph_text_2,graph_text_3))
        
        self.wait(1)

        #### Animating a_m and a_n pairs of interest
        brace_group = VGroup()
        delta_group = VGroup()

        def interest_points(a,b):
            self.play(dots[a].animate.set_color(C_PURPLE).scale(1.1),
                      dots[b].animate.set_color(C_PURPLE).scale(1.1),rate_func=smooth)
            
            brace = BraceBetweenPoints(dots[a].get_center(),dots[b].get_center(),direction=RIGHT)
            delta_text = MathTex(r"\delta",font_size=20).next_to(brace,RIGHT,buff=0.1)

            brace_group.add(brace)
            delta_group.add(delta_text)
            
            self.play(Create(brace),Create(delta_text))
            self.wait(2)

        interest_points(17,20)
        self.wait(2)
        interest_points(35,40)
        self.wait(2)
        interest_points(51,60)
        self.wait(2)


        self.play(ReplacementTransform(graph_text_3,graph_text_4))

        self.wait(4)

        self.play(ReplacementTransform(graph_text_4,graph_text_5))

        self.play(epsilon.animate.set_value(0.32))

        self.wait(4)

        self.play(ReplacementTransform(graph_text_5,graph_text_6))

        self.wait(4)

        self.play(ReplacementTransform(graph_text_6,graph_text_7))

        self.wait(5)
