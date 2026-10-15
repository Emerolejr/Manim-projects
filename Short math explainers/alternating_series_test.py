from typing_extensions import runtime
from manim import *
import numpy as np
import math


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


class alternating_series(Scene):
    def construct(self):
        # Header block
        header = BeamerBlock("Alternating Series Test",width=14).move_to(ORIGIN)
        self.add(header)
        self.wait(2)

        #### texts that explain the alternating series. 
        ## these are texts for slide 1

        text_1 = MathTex(r"\text{The Leibniz criterion applies to an alternating series of the form:}",font_size=35)
        text_2 = MathTex(r"\sum_{n=1}^\infty (-1)^{n} a_n",font_size=35).set_color(C_BRIGHT_BLUE)
        text_3 = MathTex(r"\text{where } ",r"a_n",r"\text{ is a sequence of positive terms that satisfies two conditions:}",font_size=35)
        text_3[1].set_color(C_BRIGHT_BLUE)

        text_4 = MathTex(r"1. \text{ }\lim_{n \to \infty} ",r"a_n",r" =",r" 0",font_size=35)
        text_4[1].set_color(C_BRIGHT_BLUE)

        text_5 = MathTex(r"2. \text{ } ",r"a_n ",r"\text{ is monotonically decreasing}",font_size=35)
        text_5[1].set_color(C_BRIGHT_BLUE)

        text_6 = MathTex(r"\text{If these conditions are met, then the series converges.}",font_size=35)

        slide_1 = VGroup(text_1,text_2,text_3,text_4,text_5,text_6).arrange(DOWN,buff=0.3,aligned_edge=LEFT)

        for i in slide_1:
            self.play(Write(i))
            self.wait(2)    
    
        self.wait(2)
        self.play(FadeOut(slide_1))
        self.wait(2)

        ### slide 2 texts
        text_7 = MathTex(r"\textbf{Why the Leibniz Criterion Works}",font_size=40)
        text_8 = MathTex(r"\text{An alternating series keeps switching from positive to negative:}",font_size=35)
        text_9 = MathTex(r"a_1 - a_2 + a_3 - a_4 + \dots",font_size=35).set_color(C_BRIGHT_BLUE)
        text_10 = MathTex(r"\text{For an alternating series to converge, } ",r" a_n ",r" \text{ must decrease monotonically.}",font_size=35)
        text_10[1].set_color(C_BRIGHT_BLUE)

        text_11 = MathTex(r"\text{Because the terms shrink, each correction in the partial  sum becomes weaker.}",font_size=35)
        text_12 = MathTex(r"\text{ The oscillations around the final value get smaller and smaller, and the sum stabilizes.}",font_size=35)


        slide_2 = VGroup(text_7,text_8,text_9,text_10,text_11,
                         text_12).arrange(DOWN,buff=0.3,aligned_edge=LEFT)

        for i in slide_2:
            self.play(Write(i))
            self.wait(2)    


        self.wait(2)
        self.play(FadeOut(slide_2))
        self.wait(1)



class ASTDemo(Scene):
    def construct(self):
        # our alternative series is a_n = sum_{n=1}^\infty (-1)^{n+1} b_n, where b_n is defined below
        # we require b_n > 0 and b_n be decreasing to 0
        def b(n):
            return 1 / n

        # global variables
        axis = NumberLine(x_range=[-0.1, 1.1, 2], length=10, numbers_to_include=[0]).shift(DOWN)

        intro = MathTex(r"\text{How does the Alternating Series Test work?", font_size=48)
        series = MathTex(r"s =", r"b_1", r"-b_2", r"+b_3", r"-b_4", r"+b_5", r"-b_6", r"+\cdots",
                         r" = \displaystyle\sum_{n=1}^\infty (-1)^{n+1} b_n", font_size=36).to_edge(UP, MED_SMALL_BUFF)
        
        series[0][0].set_color(C_GREEN)
        series[8][1:].set_color(C_BLUE)
        
        s = ValueTracker(0)  # keeps track of the partial sums so far
        sumLine = always_redraw(lambda: DashedLine(axis.n2p(s.get_value()) + 2 * DOWN,
                                                   axis.n2p(s.get_value()) + 3 * UP,
                                                   color=C_GREEN))
        
        sumText = always_redraw(lambda: MathTex(r"\text{sum so far}",
                                                color=C_GREEN, font_size=20).next_to(sumLine, DOWN, SMALL_BUFF))
        skip = True

        ############### ANIMATIONS ################

        #############

        ### Section 1 - Initial setup
        self.play(FadeIn(intro, shift=UP, run_time=2))
        self.wait(2)
        self.play(FadeOut(intro))
        self.play(FadeIn(series, shift=UP), Create(axis), run_time=2)
        self.wait(4)

        #############
        ### Section 2 - Visualizing sum of first 6 terms

        self.play(FadeIn(sumLine, sumText, run_time=2))
        self.wait(2)
        sum = 0  # an accumulator variable for the partial sums
        # consider partial sums for first 6 terms
        termHighlight = SurroundingRectangle(series[1], color=C_GREEN)  # a bound around terms added so far
        rectangleLabel = MathTex(r"s_1", font_size=24, color=C_GREEN).next_to(termHighlight, UP, SMALL_BUFF)
        arrowStart = axis.n2p(0)
        arrowFadeGroup = VGroup()
        tick_group_fade = VGroup()

        for n in range(1, 7):
            # term updating
            term = b(n)
            sum += (-1) ** (n + 1) * term

            # axis updating
            newtick = axis.get_tick(sum)
            newlabel = MathTex(r"s_{" + str(n) + "}", color=C_GREEN, font_size=24).next_to(newtick, DOWN, SMALL_BUFF)
            tick_group = VGroup(newtick,newlabel)
            tick_group_fade.add(tick_group)

            # arrow updating
            arrowEnd = axis.n2p(sum)
            newarrow = CurvedArrow(arrowStart, arrowEnd, color=C_BLUE)
            arrowlabel = MathTex(series.tex_strings[n], color=C_BLUE,
                                 font_size=24).next_to(newarrow, DOWN if n % 2 == 1 else UP, SMALL_BUFF)
            arrowGroup = VGroup(newarrow, arrowlabel)
            arrowFadeGroup.add(arrowGroup)

            arrowStart = arrowEnd
            # new term highlighting
            newRectangle = SurroundingRectangle(series[1:(n + 1)], color=C_GREEN)
            newRectangleLabel = newlabel.copy().next_to(newRectangle, UP, SMALL_BUFF).set_color(C_GREEN)

            # animations
            if n == 1:
                self.play(FadeIn(termHighlight, rectangleLabel))
            else:
                self.play(Transform(termHighlight, newRectangle),
                          Transform(rectangleLabel, newRectangleLabel))
                
              
            self.wait(2)
            if n == 1:
                self.play(FadeIn(arrowGroup),rate_func=smooth)
                self.wait(1)
                self.play(s.animate(run_time=2).set_value(sum),rate_func=smooth)
                self.wait(1)
                self.play(FadeIn(tick_group),rate_func=smooth)
                self.wait(2)
            else:
                self.play(FadeIn(arrowGroup),
                          arrowFadeGroup[n-2].animate.set_style(stroke_opacity=0.2,fill_opacity=0),
                         lag_ratio=0,rate_func=smooth)
                self.play(s.animate(run_time=2).set_value(sum),rate_func=smooth)
                self.wait(1)
                self.play(FadeOut(tick_group_fade[n-2]),FadeIn(tick_group),rate_func=smooth,run_time=3)
                self.wait(2)
                self.play(FadeOut(arrowFadeGroup[n-2]),rate_func=smooth)
                self.wait(2)

        self.play(FadeOut(arrowFadeGroup[5]),FadeOut(tick_group_fade[5]),rate_func=smooth)
        #############
        ### Section 3 - Animating sum of terms beyond first six

        alltermsRect = SurroundingRectangle(series[1:8], color=C_GREEN)
        alltermsLabel = MathTex(r"s", color=C_GREEN, font_size=24).next_to(alltermsRect, UP, SMALL_BUFF)
        self.play(Transform(termHighlight, alltermsRect),
                  Transform(rectangleLabel, alltermsLabel),
                  run_time=2)
        self.wait(1)

        nVals = [7, 8, 9, 10, 15, 20, 31, 42, 63, 100, 201, 402, 999]  # don't show all values of n, just key ones
        times = [2, 1.5, 1.5, 1.5, 1, 1, 1, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25]  # speed things up as we get deeper
        timesIndex = 0

        for n in nVals:
            # indexing no longer consecutive, so must explicitly create partial sum
            sum = math.fsum([(-1) ** (i + 1) * b(i) for i in range(1, n + 1)])

            self.play(s.animate(run_time=times[timesIndex]).set_value(sum))
            timesIndex += 1
        self.wait(2)

        sTick = axis.get_tick(sum).set_color(C_GREEN)
        sLabel = MathTex(r"s", color=C_GREEN, font_size=24).next_to(sTick, DOWN, SMALL_BUFF)
        self.play(FadeIn(sTick, sLabel))
        self.wait(1)
        self.play(FadeOut(sumLine, sumText))
        self.wait(5)
        