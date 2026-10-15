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


class riemann_sums_intro(Scene):
    def construct(self):
        header = BeamerBlock("Step function",width=14,color=C_GREEN).move_to(ORIGIN)

        #### collection of texts
        text_1 = MathTex(r"\text{Let I} \subseteq \mathbb{R} \text{ be an interval}",font_size=32)
        text_2 = VGroup(
            MathTex(r"\text{A function} \phi \text{ : I } \to \mathbb{R} \text{ is called a step function if there exist",font_size=32),
            MathTex(r"\text{exists intervals  }I_1,...., I_k \text{ and constants } c_1,...,c_k \text{such that}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT)

        text_3 = MathTex(r"\phi (x) \text{ = } \sum\limits_{i = 1}^{k} c_i \chi_{I_i}(x). \kern1em \chi_{I_i}(x) = \begin{cases} \text{1,} & x \in I_i \\ 0, & \text{otherwise} \end{cases}",font_size=32)
        text_4 = MathTex(r"\bullet ",r" \kern1em \chi_{I_i}(x) \text{ determines the function}",font_size=32)
        text_5 = MathTex(r"\bullet ",r" \kern1em  c_i \text{ gives the height of the rectangle}",font_size=32)

        text_4[0].set_color(C_BRIGHT_BLUE)
        text_5[0].set_color(C_BRIGHT_BLUE)

        text_group = VGroup(text_1,text_2,text_3,text_4,text_5).arrange(DOWN,buff=0.7,aligned_edge=LEFT)

        self.play(Write(header),rate_func=smooth)
        self.wait(2)

        for i in text_group:
            self.play(Write(i),rate_func=smooth,run_time=2)
            self.wait(2)
        self.wait(2)


class reimann_sums_intro_1(Scene):
    def construct(self):

        ### texts for the name. 
        text_1 = VGroup(
            MathTex(r"\text{A step function is defined as:}",font_size=32),
            MathTex(r"\phi (x) \text{ = } \sum\limits_{i = 1}^{k} c_i \chi I_i(x). \kern1em \chi I_i(x) = \begin{cases} \text{1,} & x \in I_i \\ 0, & \text{otherwise} \end{cases}",font_size=32)
        ).arrange(DOWN,buff=0.2).to_corner(UP,buff=0.2)

        text_2 = MathTex(r"\text{To help explain the concept of a step function, here are four intervals. } I_1, I_2, I_3, I_4",font_size=32).to_corner(UP,buff=0.2)
        
        text_3 = VGroup(
            MathTex(r"\text{The indicator function } \chi_{I_i}(x) = \begin{cases} 1, & x \in I_i \\ 0, & \text{otherwise} \end{cases}",font_size=32),
            MathTex(r"\text{selects only the interval } I_i \text{, assigns it a unit value and ignores all others.}",font_size=32)
        ).arrange(DOWN, buff=0.2).to_corner(UP, buff=0.2)

        text_4 = VGroup(
            MathTex(r"\text{Taking } I_1 \text{ as the interval of interest}",font_size=32),
            MathTex(r"\text{So the indicator function becomes } \chi_{I_1}(x) = \begin{cases} 1, & x \in I_1 \\ 0, & \text{otherwise} \end{cases} ",font_size=32)
        ).arrange(DOWN,buff=0.2).to_corner(UP,0.2)
        text_5 = MathTex(r"\text{ Hence } I_2, I_3, I_4 \text{ will have zero height, while } I_1 \text{ will have a unit height}",font_size=32).to_corner(UP,buff=0.2)

        text_6 = MathTex(r"\text{The height is then scaled by } C_1",font_size=32).to_corner(UP,buff=0.2)

        text_7 = VGroup(
            MathTex(r"\text{Taking } I_2 \text{ as interval of interest.}",font_size=32),
            MathTex(r"\text{We then have } \chi_{I_2}(x) = \begin{cases} 1, & x \in I_2 \\ 0, & \text{otherwise} \end{cases} ",font_size=32)
        ).arrange(DOWN,buff=0.2).to_corner(UP,buff=0.2)

        text_8 = MathTex(r"\text{The } I_2 \text{ interval is assigned a height of 1 unit}\text{, while others have zero height} ",font_size=32).to_corner(UP,buff=0.2)

        text_9 = MathTex(r"\text{scaling by } C_2 \text{, we have...}",font_size=32).to_corner(UP,buff=0.2)

        text_10 = VGroup(
            MathTex(r"\text{Repeating the same step for the third and fourth interval...}",font_size=32),
            MathTex(r"\text{Hence } \chi_{I_3}(x) = \begin{cases} 1, & x \in I_3 \\ 0, & \text{otherwise} \end{cases} \text{ and } \chi_{I_4}(x) = \begin{cases} 1, & x \in I_4 \\ 0, & \text{otherwise} \end{cases} ",font_size=32)
        ).arrange(DOWN,buff=0.2).to_corner(UP,buff=0.2)

        text_11 = VGroup( 
            MathTex(r"\text{Together the sum of the results of all of these intervals is }",font_size=32),
            MathTex(r"\text{called a} \textbf{ step function.}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        ## Axis for the graph
        ax = Axes(
            x_range=[0,2.7,1],
            y_range=[0,5,1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": False,
                         "include_ticks": False,
                         "tip_width":0.1,
                         "tip_length":0.1
            }
        ).shift(DOWN + (LEFT*2))

        x_label = ax.get_x_axis_label("x",RIGHT)
        y_label = ax.get_y_axis_label("f(x)",UP)

        ## Creating the intervals 
        x_lines = VGroup()
        width = 0.5

        for i in np.arange(0.5,2.6,width):
            x_line = DashedLine(start=ax.c2p(i,0),end=ax.c2p(i,5),color=C_GREEN)
            x_lines.add(x_line)
        
        ###rectangles for interval I_1, I_2, I_3 and I_4 
        i_group = VGroup()
        i_texts = VGroup()
        counter = 1

        for i in np.arange(0.5,2.1,width):
            rect = Polygon(
                ax.c2p(i,0),
                ax.c2p(i,5),
                ax.c2p(i+width,5),
                ax.c2p(i+width,0),
                fill_color=C_GREEN,
                fill_opacity=0.4,
                stroke_width=0
            )
            
            i_group.add(rect)
            text = MathTex(rf"I_{{{counter}}}",font_size=32).move_to(rect.get_center())
            i_texts.add(text)
            counter = counter + 1

        ### This is for the adjustable rectangles
        c1 = ValueTracker(0)
        c2 = ValueTracker(0)
        c3 = ValueTracker(0)
        c4 = ValueTracker(0)

        c1_text = MathTex(r"C_1",font_size=28)
        c2_text = MathTex(r"C_2",font_size=28)
        c3_text = MathTex(r"C_3",font_size=28)
        c4_text = MathTex(r"C_4",font_size=28)
        func_text = MathTex(r"\phi(x) \text{ = }",r"C_1 \chi_1",r"\text{ } + \text{ } C_2  \chi_2 ",
        r"\text{ } + \text{ } C_3  \chi_3 \text{ } + \text{ } C_4 \chi_4 ",font_size=30).next_to(x_lines,RIGHT,buff=1)

        func_rect = SurroundingRectangle(func_text).set_color(C_MAGENTA)

        def adjustable_rect(start,tracker):
            rect = always_redraw(
                lambda: Polygon(
                ax.c2p(start,0),
                ax.c2p(start,tracker.get_value()),
                ax.c2p(start+width,tracker.get_value()),
                ax.c2p(start+width,0),
                fill_color=[C_MAGENTA,BLUE],
                fill_opacity=0.9,
                stroke_width=1)
            )

            return rect

        x_i_1 = adjustable_rect(0.5,c1)
        x_i_2 = adjustable_rect(1,c2)
        x_i_3 = adjustable_rect(1.5,c3)
        x_i_4 = adjustable_rect(2.0,c4)

        ## The animation starts from here.
        self.play(FadeIn(ax),FadeIn(x_label),FadeIn(y_label))
        self.wait(2)
        self.play(Write(text_1),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeIn(text_2),FadeOut(text_1),rate_func=smooth,run_time=2)
        self.play(Create(x_lines),rate_func=smooth,run_time=2)
        self.play(FadeIn(i_texts),rate_func=smooth)
        self.wait(4)
        self.play(FadeIn(text_3),FadeOut(text_2),rate_func=smooth)

        self.add(x_i_1,x_i_2,x_i_3,x_i_4)
        self.play(FadeIn(i_group))

        ## adjusting opacity of the i  group rectangles
        self.play(i_group[0].animate.set_fill(opacity=0.7),rate_func=smooth)

        for i in range(1,4,1):
            self.play(i_group[i-1].animate.set_fill(opacity=0.4),rate_func=smooth)
            self.play(i_group[i].animate.set_fill(opacity=0.7),rate_func=smooth)
            self.wait(1)
        
        self.play(FadeOut(i_group),rate_func=smooth)
        self.wait(4)

        self.play(FadeIn(text_4),FadeOut(text_3),run_time=2)

        ###code
        i_group[1].set_fill(opacity=0.4,color=RED)
        i_group[2].set_fill(opacity=0.4,color=RED)
        i_group[3].set_fill(opacity=0.4,color=RED)
        ##code 
        
        self.play(FadeIn(i_group),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeIn(text_5),FadeOut(text_4),rate_func=smooth)
        self.play(FadeOut(i_texts[0]))
        self.play(c1.animate.set_value(1),run_time=4,rate_func=smooth)
        
        self.wait(4)
        self.play(FadeOut(i_group),rate_func=smooth)
        self.wait(4)

        self.play(FadeIn(text_6),FadeOut(text_5),rate_func=smooth)
        self.play(c1.animate.set_value(1.5),run_time=4)
        c1_text.next_to(x_i_1,UP,buff=0.2)
        self.play(FadeIn(c1_text),Write(func_text[0:2]),rate_func=smooth)
        self.wait(4)
        self.play(FadeIn(text_7),FadeOut(text_6),rate_func=smooth,run_time=2)
        
        ### code
        i_group[1].set_fill(opacity=0.4,color=GREEN)
        i_group[2].set_fill(opacity=0.4,color=RED)
        i_group[3].set_fill(opacity=0.4,color=RED)
        ## code 
        
        self.play(FadeIn(VGroup(i_group[1],i_group[2],i_group[3])),rate_func=smooth)
        self.wait(4)
        self.play(FadeOut(VGroup(i_group[1],i_group[2],i_group[3])),rate_func=smooth)
        self.wait(4)
        self.play(FadeIn(text_8),FadeOut(text_7),rate_func=smooth)
        self.play(FadeOut(i_texts[1]))
        self.play(c2.animate.set_value(1),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeIn(text_9),FadeOut(text_8),rate_func=smooth,run_time=2)
        self.play(c2.animate.set_value(3.5),rate_func=smooth,run_time=4)
        c2_text.next_to(x_i_2,UP,buff=0.2)
        self.play(FadeIn(c2_text),Write(func_text[2]),rate_func=smooth)
        self.wait(4)
        self.play(FadeIn(text_10),FadeOut(text_9),rate_func=smooth,run_time=2)

        self.wait(2)
        self.play(FadeOut(i_texts[2]))
        self.play(c3.animate.set_value(5),rate_func=smooth,run_time=4)
        c3_text.next_to(x_i_3,UP,buff=0.2)
        self.play(FadeIn(c3_text),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeOut(i_texts[3]))
        self.play(c4.animate.set_value(3.4),rate_func=smooth,run_time=4)
        c4_text.next_to(x_i_4,UP,buff=0.2)
        self.play(FadeIn(c4_text),Write(func_text[3]),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeIn(text_11),FadeOut(text_10),rate_func=smooth,run_time=2)
        self.play(Create(func_rect),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(Uncreate(func_rect),rate_func=smooth)
        self.wait(6)
        self.play(FadeOut(*self.mobjects),rate_func=smooth,run_time=2)
        self.wait(4)


class riemann_sums_2_0(Scene):
    def construct(self):
        # 1. Defining Math Texts
        text_1 = VGroup(
            MathTex(r"\text{The Riemann sum for } f(x) \text{ in } [a,b] \text{ is given as}", font_size=32),
            MathTex(r"S = \sum_{i = 1}^{n} ", r"f(x_i^*)", r"\Delta x", font_size=32)
        ).arrange(DOWN, buff=0.2).to_corner(UP, buff=0.2)

        # Generating n=1 to n=5 texts dynamically to avoid manual typos
        text_group = VGroup()
        for i in range(1, 6):
            t = VGroup(
                MathTex(rf"\text{{when n = {i}}}", font_size=32),
                MathTex(rf"S = \sum_{{i = 1}}^{{{i}}} ", r"f(x_i^*)", r"\Delta x", font_size=32)
            ).arrange(DOWN, buff=0.2).to_corner(UP, buff=0.2)
            text_group.add(t)
        
        text_7 = VGroup(
            MathTex(r"\text{Hence, as } \Delta x \to 0, \text{ the Riemann Sum equals}", font_size=32),
            MathTex(r"\text{area under the curve } = \int_a^b f(x) dx", font_size=32)
        ).arrange(DOWN, buff=0.2).to_corner(UP, buff=0.2)

        # 2. Setup Axes and Graph
        axes = Axes(
            x_range=[0, 3.5, 1],
            y_range=[0, 7, 1],
            x_length=7,
            y_length=5,
            axis_config={
                "include_numbers": False,
                "include_ticks": False,
                "tip_shape": StealthTip,
                "tip_width": 0.1,
                "tip_length": 0.1
            }
        ).shift(DOWN * 0.5)

        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("f(x)")

        def f(x):
            return (x - 2)**3 + 2*(x - 2)**2 + 3
        
        graph = axes.plot(f, x_range=[0, 3], color=BLUE)

        # Define interval
        a, b = 0.2, 2.7
        line_a = DashedLine(axes.c2p(a, 0), axes.c2p(a, f(a)), color=C_GREEN)
        line_b = DashedLine(axes.c2p(b, 0), axes.c2p(b, f(b)), color=C_GREEN)
        a_label = MathTex("a", color=C_GREEN).next_to(axes.c2p(a, 0), DOWN)
        b_label = MathTex("b", color=C_GREEN).next_to(axes.c2p(b, 0), DOWN)

        # 3. Helper Functions
        dx_tracker = ValueTracker(0.5)

        def riemann_creator(n):  
            return axes.get_riemann_rectangles(
                graph,
                x_range=[a, b],
                dx=(b - a) / n,
                input_sample_type="left",
                fill_opacity=0.6,
                color=[C_MAGENTA, BLUE],
                stroke_width=1
            )
        
        riemann_dynamic = always_redraw(
            lambda: axes.get_riemann_rectangles(
                graph,
                x_range=[a, b],
                dx=dx_tracker.get_value(),
                input_sample_type="left",
                fill_opacity=0.6,
                color=[C_MAGENTA, BLUE],
                stroke_width=1
            )
        )
        
        def process(rect_group):
            dots = VGroup()
            deltas = VGroup()
            for rect in rect_group:
                # Place dot at the sample point (Top Left for 'left' rule)
                dot = Dot(rect.get_corner(UL), radius=0.06, color=C_MAGENTA)
                # Position delta_x label below the center of each rectangle
                dx_label = MathTex(r"\Delta x", font_size=24).next_to(rect, DOWN, buff=0.1).set_color(C_GREEN)
                dots.add(dot)
                deltas.add(dx_label)
            return dots, deltas

        # 4. Animation Sequence
        self.play(FadeIn(text_1))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(VGroup(line_a, line_b, a_label, b_label)))
        self.play(Create(graph), run_time=2)
        self.wait()
        self.play(FadeOut(text_1))

        current_rects = None

        for i in range(5):
            n = i + 1
            new_text = text_group[i]
            new_rects = riemann_creator(n)
            new_dots, new_deltas = process(new_rects)

            self.play(FadeIn(new_text))
            
            if i == 0:
                self.play(Create(new_rects))
            else:
                # Smoothly transition rectangles
                self.play(
                    ReplacementTransform(current_rects, new_rects),
                    FadeOut(text_group[i-1])
                )
            
            current_rects = new_rects
            
            # Highlight parts of the sum
            self.play(Indicate(new_text[1][2]),run_time=3) # Highlight Delta x
            self.play(FadeIn(new_deltas),run_time=2)
            self.wait(4)
            self.play(Indicate(new_text[1][1]),run_time=3) # Highlight f(x)
            self.play(FadeIn(new_dots),run_time=3)
            self.wait(4)
            
            # Cleanup for next iteration
            self.play(FadeOut(new_dots), FadeOut(new_deltas))

        # Show exact area once at the end
        exact_area = axes.get_area(graph, x_range=[a, b], color=[C_MAGENTA,BLUE], opacity=0.6)

        self.play(FadeIn(riemann_dynamic),rate_func=smooth)
        self.play(
            FadeOut(current_rects),
        )
        self.play(FadeOut(text_group[-1]),rate_func=smooth,run_time=1)
        self.play(FadeIn(text_7[0]),rate_func=smooth,run_time=2)

        self.play(dx_tracker.animate.set_value(0.05),run_time=10)
        self.play(Write(text_7[1]),rate_func=smooth)
        self.play(FadeOut(riemann_dynamic),FadeIn(exact_area),rate_func=smooth,run_time=2)

        self.wait(5)
        self.play(FadeOut(*self.mobjects))

class riemann_sums_2(Scene):
    def construct(self):

        ##texts for scene
        text_1 = MathTex(r"\text{Given a function, f(x) in an interval [a,b]}",font_size=32).to_corner(UP,buff=0.2)

        text_2 = VGroup(
            MathTex(r"\text{We can find the approximate area bounded bounded by the curve, }",font_size=32),
            MathTex(r"\text{and the x-axis in the [a,b] interval with the help of rectangles}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_3 = VGroup(
            MathTex(r"\text{To get the approximate area, we have to sum the area of each individual}",font_size=32),
            MathTex(r"\text{rectangle. We call this} \textbf{ the Riemann sum}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)


        text_4 = VGroup(
            MathTex(r"\textbf{Riemann Sum} \text{, S = } \sum_{i = 1}^{n} f(x_i^*) \Delta x_i",font_size=32),
            MathTex(r"\text{ Where } f(x_i) \text{ = Height of individual rectangle} ",font_size=32),
            MathTex(r"\text{ and } \Delta x_i \text{ = Width of individual rectangle}",font_size=32)
        )

        text_4_right_group = VGroup(text_4[1],text_4[2]).arrange(DOWN,aligned_edge=LEFT,buff=0.2)

        text_4_group = VGroup(text_4[0],text_4_right_group).arrange(RIGHT,buff=0.4).to_corner(UP,buff=0.2)

        text_5 = VGroup(
            MathTex(r"\text{At the moment, The riemann sum does not accurately give the}",font_size=32),
            MathTex(r"\text{area of under the curve}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_6 = MathTex(r"\text{Making } \Delta x \text{ smaller}",font_size=32).to_corner(UP,buff=0.2)

        text_7 = VGroup(
            MathTex(r"\text{Notice that the riemann sum better approximates the area as}",font_size=32),
            MathTex(r"\Delta x \text{ gets smaller}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_8 = VGroup(
            MathTex(r"\text{Hence, as } \Delta x \to 0, \text{ we can say Riemann Sum equals}",font_size=32),
            MathTex(r"\text{ area under the curve between [a,b] }",r" = ",r"\int_a^b f(x) dx",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_9 = VGroup(
            MathTex(r"\text{Thus, the Riemann sum converges to the integral, and }",font_size=32),
            MathTex(r"\text{approximates the area of a curve perfectly }",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        
        ### The axes.
        axes = Axes(
            x_range=[0,3.5,1],
            y_range=[0,7,1],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": False,
                         "include_ticks": False,
                         "tip_shape":StealthTip,
                         "tip_width":0.1,
                         "tip_length":0.1
            }
        ).shift(DOWN*0.5)

        x_label = axes.get_x_axis_label(r"\text{x}")
        y_label = axes.get_y_axis_label(r"\text{f(x)}")

        def f(x):
            return (x - 2)**3 + 2*(x - 2)**2  + 3
        
        graph = axes.plot(
            f,
            x_range = [0,3],
            color = C_BRIGHT_BLUE
        )

        ## for line a and b.
        a = 0.2
        b = 2.7
        
        line_a = DashedLine(start=axes.c2p(a,0),end=axes.c2p(a,f(a)),color=C_GREEN)
        line_b = DashedLine(start=axes.c2p(b,0),end=axes.c2p(b,f(b)),color=C_GREEN)

        a_label = MathTex(r"\text{a}",color=C_GREEN).next_to(axes.c2p(a,0),DOWN)
        b_label = MathTex(r"\text{b}",color=C_GREEN).next_to(axes.c2p(b,0),DOWN)

        dx_tracker = ValueTracker(0.5)

        rect = always_redraw(
            lambda: 
            axes.get_riemann_rectangles(
            graph,
            x_range=[a,b],
            dx = dx_tracker.get_value(),
            input_sample_type="center",
            fill_opacity=0.6,
            color=[C_MAGENTA,BLUE],
            stroke_width=1
        ))

        line_v_group = VGroup()
        line_h_group = VGroup()

        for i in range(0, len(rect)):
            line_v = Line(start=rect[i].get_bottom(),end=rect[i].get_top(),color=BLUE,stroke_width=rect[i].get_width()*100)
            line_h = Line(start=rect[i].get_left(),end=rect[i].get_right(),color=BLUE,stroke_width=rect[i].get_height()*100)
            line_h_group.add(line_h)
            line_v_group.add(line_v)
       
        ## Area under the graph
        x_vals = np.linspace(a,b,100)
        curve_points = [axes.c2p(x, (x - 2)**3 + 2*(x - 2)**2  + 3) for x in x_vals]
        bottom_points = [axes.c2p(b,0),axes.c2p(a,0)]

        area_shape = VMobject()
        area_shape.set_points_as_corners(curve_points + bottom_points)
        area_shape.set_fill(opacity=0.4,color=[C_MAGENTA,BLUE])
        area_shape.set_stroke(C_MAGENTA,width=1)

        area_text = VGroup(
            MathTex(r"\text{Area under curve}",font_size=28),
            MathTex(r"\int_a^b f(x)",font_size=28),
            color=C_MAGENTA
        ).arrange(DOWN,buff=0.2).next_to(graph.get_center(),UP,buff=0.5)
        
        area_group = VGroup(area_text,area_shape).set_z_index(2)

        ### The animations start here
        self.play(FadeIn(riemann_sum),rate_func=smooth,run_time=2)
        self.play(FadeIn(VGroup(axes,x_label,y_label)),rate_func=smooth,run_time = 2)
        self.wait(2)
        self.play(FadeOut(riemann_sum),rate_func=smooth)
        self.play(Write(text_1),rate_func=smooth)
        self.wait(2)
        self.play(Create(graph),rate_func=smooth,run_time=10)
        self.play(Create(VGroup(a_label,b_label,line_a,line_b)),rate_func=smooth,run_time=2)

        self.wait(4)
        self.play(FadeIn(area_group),run_time=4,rate_func=smooth)
        self.wait(4)
        self.play(FadeOut(area_group),run_time=4,rate_func=smooth)
        self.wait(4)
        self.play(FadeIn(text_2),FadeOut(text_1),rate_func=smooth,run_time=5)
        self.wait(4)
        self.play(FadeIn(rect),run_time=3,rate_func=smooth)
        self.wait(4)
        self.play(FadeIn(text_3),FadeOut(text_2),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeIn(text_4[0]),FadeOut(text_3),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(Write(text_4[1]),rate_func=smooth,run_time=2)
        self.play(ShowPassingFlash(line_v_group,time_width=0.2),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(Write(text_4[2]),run_time=2,rate_func=smooth)

        self.play(ShowPassingFlash(line_h_group,time_width=0.2),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(FadeIn(text_5),FadeOut(text_4),rate_func=smooth)
        self.play(FadeOut(rect),rate_func=smooth,run_time=4)
        self.wait(1)
        self.play(FadeIn(area_group))
        
        self.wait(2)

        self.play(FadeOut(area_group),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(FadeIn(rect),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(FadeIn(text_6),FadeOut(text_5),run_time=2,rate_func=smooth)
        self.wait(2)
        self.play(dx_tracker.animate.set_value(0.25),rate_func=smooth,run_time=5)
        self.wait(4)
        self.play(FadeIn(text_7),FadeOut(text_6),run_time=2,rate_func=smooth)
        self.play(dx_tracker.animate.set_value(0.1),rate_func=smooth,run_time=5)
        self.wait(4)
        self.play(FadeIn(text_8),FadeOut(text_7),run_time=2,rat_func=smooth)
        self.play(dx_tracker.animate.set_value(0.07),rate_func=smooth,run_time=5)

        for i in range(2):
            self.play(FadeOut(rect),rate_func=smooth)
            self.play(FadeIn(area_group),rate_func=smooth)
            self.wait(1)
            self.play(FadeOut(area_group),rate_func=smooth)
            self.play(FadeIn(rect),rate_func=smooth)
        
        self.wait(2)

        self.play(FadeIn(text_9),FadeOut(text_8),rate_func=smooth)
        self.wait(4)


class riemann_sums_3(Scene):
    def construct(self):

        ### This part is for the texts
        text_1 = MathTex(r"\text{Say we are given for a function on an interval [a,b]}",font_size=32).to_corner(UP,buff=0.2)
       
        text_2 = MathTex(r"\text{If we divide the [a,b] into consistent intervals to fit Reimann rectangles}",font_size=32).to_corner(UP,buff=0.2)
       
        text_3 = VGroup(
            MathTex(r"\text{Across each interval, we have to pick an } x^*_i \text{ within the } [x_{i-1},x_i] \text{ interval}",font_size=32),
            MathTex(r"\text{this will determine the height of each Riemann rectangle, } f(x^*_i)",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_4 = VGroup(
            MathTex(r"\text{Say we pick the left endpoints, such that } x^*_i = x_{i-1}",font_size=32),
            MathTex(r"\text{Note that the left-edges make contact with the function}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_5 = MathTex(r"\text{Or, Say we pick the mid-points. Here the mid-point make contact with the function}",font_size=32).to_corner(UP,buff=0.2)
        
        text_6 = VGroup(
                MathTex(r"\text{If we pick the right endpoints, such that } x^*_i = x_{i}",font_size=32),
                MathTex(r"\text{Here again, the right-edges make contact with the function}",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_7 = MathTex(r"\text{Here are the three cases side-by-side}",font_size=32).to_corner(UP,buff=0.2)
        
        text_8 = VGroup(
            MathTex(r"\text{At this point, we can see that for a monotonically increasing function.}",font_size=32),
            MathTex(r"Area_{left} < Area_{center} < Area_{right}",font_size=32)
        ).arrange(DOWN,buff=0.2).to_corner(UP,buff=0.2)

        text_9 = VGroup(
            MathTex(r"\text{Picking the minimum function value/left end-points for each interval yields}",font_size=32),
            MathTex(r"\textbf{Lower sum, }s = \sum_{i = 1}^{n} f(x_{i - 1}) \Delta x",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_10 = VGroup(
            MathTex(r"\text{Picking the maximum function value/right end-points for each interval yields}",font_size=32),
            MathTex(r"\text{Upper sum, } S = \sum_{i = 1}^{n} f(x_i) \Delta x",font_size=32)
        ).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)

        text_11 = MathTex(r"\text{Note what happens as } \Delta x \to 0 \text{ for both graphs}",font_size=32).to_corner(UP,buff=0.2)
       
        text_12 = VGroup(
            MathTex(r"\text{We can see that both the lower sum and upper sum to the integral}",font_size=32),
            MathTex(r"\lim_{n \to \infty} s_n = \lim_{n \to \infty} S_n = \int_a^b f(x) dx",font_size=32)
        ).arrange(DOWN,buff=0.2).to_corner(UP,buff=0.2)

        ###All the axes
        axes_1 = Axes(
            x_range=[0,3.3,0.5],
            y_range=[0,12,1],
            x_length=6,
            y_length=4,
            axis_config={
                "include_numbers":False,
                "include_ticks":False,
                "tip_shape":StealthTip,
                "tip_width":0.1,
                "tip_length":0.1
            }
        )

        axes_2 =Axes(
            x_range=[0,3.3,0.5],
            y_range=[0,12,1],
            x_length=6,
            y_length=4,
            axis_config={
                "include_numbers":False,
                "include_ticks":False,
                "tip_shape":StealthTip,
                "tip_width":0.1,
                "tip_length":0.1
            }
        )
        axes_3 = Axes(
            x_range=[0,3.3,0.5],
            y_range=[0,12,1],
            x_length=6,
            y_length=4,
            axis_config={
                "include_numbers":False,
                "include_ticks":False,
                "tip_shape":StealthTip,
                "tip_width":0.1,
                "tip_length":0.1
            }
        )
        x_label_1 = axes_1.get_x_axis_label(r"\text{x}",RIGHT).scale(0.8)
        y_label_1 = axes_1.get_y_axis_label(r"\text{f(x)}",UP).scale(0.8)

        x_label_2 = axes_2.get_x_axis_label(r"\text{x}",RIGHT).scale(0.8)
        y_label_2 = axes_2.get_y_axis_label(r"\text{f(x)}",UP).scale(0.8)

        x_label_3 = axes_3.get_x_axis_label(r"\text{x}",RIGHT).scale(0.8)
        y_label_3 = axes_3.get_y_axis_label(r"\text{f(x)}",UP).scale(0.8)

        ### the graphs for the rects
        a = 0.5
        b = 3.0

        def f(x):
            return x**2 + 2
        
        graph_1 = axes_1.plot(
            f,
            x_range=[0,3.2],
            color=C_BRIGHT_BLUE
        )

        graph_2 = axes_2.plot(
            f,
            x_range = [0,3.2],
            color = C_BRIGHT_BLUE
        )

        graph_3 = axes_3.plot(
            f,
            x_range = [0,3.2],
            color = C_BRIGHT_BLUE
        )

        ## this is  a function that creates reimann rectangles. 
        dx_tracker = ValueTracker(0.5)
        def create_riemann_rectangles(side,ax,graph,colour):
            rect = always_redraw(
                lambda: ax.get_riemann_rectangles(
                    graph,
                    x_range=[a,b],
                    dx = dx_tracker.get_value(),
                    stroke_width=1,
                    color = colour,
                    fill_opacity = 0.5,
                    input_sample_type=side
            )
            )
            return rect
        
        rect_1_left = create_riemann_rectangles("left",axes_1,graph_1,[C_MAGENTA,BLUE])
        rect_1_center = create_riemann_rectangles("center",axes_1,graph_1,[C_MAGENTA,BLUE])
        rect_1_right = create_riemann_rectangles("right",axes_1,graph_1,[C_MAGENTA,BLUE])

        ### This is the rects for the center and the right
        rect_2 = create_riemann_rectangles("center",axes_2,graph_2,[C_MAGENTA,BLUE])
        rect_3 = create_riemann_rectangles("right",axes_3,graph_3,[C_MAGENTA,BLUE])

        ### VGroups of the left, center and right.
        left_group = Group(axes_1,x_label_1,y_label_1,graph_1,rect_1_left)
        center_group = Group(axes_2,x_label_2,y_label_2,graph_2,rect_2)
        right_group = Group(axes_3,x_label_3,y_label_3,graph_3,rect_3)

        graph_group = Group(left_group,center_group,right_group)

        #### intervals and lines for a, b and the x_i's 
        a_label = MathTex(r"a",font_size=28).next_to(axes_1.c2p(a,0),DOWN,buff=0.2).set_color(C_GREEN)
        b_label = MathTex(r"b",font_size=28).next_to(axes_1.c2p(b,0),DOWN,buff=0.2).set_color(C_GREEN)
        x1_label =  MathTex(r"x_1",font_size=28).next_to(axes_1.c2p(a,0),DOWN,buff=0.2).set_color(C_GREEN)
        x6_label = MathTex(r"x_6",font_size=28).next_to(axes_1.c2p(b,0),DOWN,buff=0.2).set_color(C_GREEN)

        a_line = DashedLine(start = axes_1.c2p(a,0),end = axes_1.c2p(a,f(a)),color=C_GREEN)
        b_line = DashedLine(start = axes_1.c2p(b,0), end = axes_1.c2p(b,f(b)),color=C_GREEN)
        
        counter = 1
        x_label_group = VGroup(x1_label,x6_label)
        x_lines_group = VGroup()

        for i in np.arange(1.0, 3, 0.5):
            counter = counter + 1
            x_label = MathTex(rf"x_{counter}",font_size=28).next_to(axes_1.c2p(i,0),DOWN,buff=0.2).set_color(C_GREEN)
            x_line = DashedLine(axes_1.c2p(i,0),axes_1.c2p(i,f(i)),color=C_GREEN)
            x_label_group.add(x_label)
            x_lines_group.add(x_line)

        ### x*tracker.get_value()
        x_star_tracker = ValueTracker(0.5)

        f_x_star = always_redraw(
            lambda: MathTex(r"f(x^*_i)",font_size=30).next_to(axes_1.c2p(0,f(x_star_tracker.get_value())),LEFT,buff=0.5)
        )
        
        x_star = always_redraw(
            lambda: MathTex(r"x^*_i",font_size=30).next_to(axes_1.c2p(x_star_tracker.get_value(),0),DOWN,buff=0.5)
        )

        dot_star = always_redraw(
            lambda: Dot(axes_1.c2p(x_star_tracker.get_value(),f(x_star_tracker.get_value())),radius=0.06).set_color(WHITE)
        )

        x_star_h_line = always_redraw(
            lambda: axes_1.get_horizontal_line(axes_1.c2p(x_star_tracker.get_value(),f(x_star_tracker.get_value())
            )                                                    
        ))

        x_star_v_line = always_redraw(
            lambda: axes_1.get_vertical_line(axes_1.c2p(x_star_tracker.get_value(),f(x_star_tracker.get_value()))
        ))

        star_group = Group(f_x_star,x_star,dot_star,x_star_h_line,x_star_v_line)


        ##This is a function that places dots on the function
        def func_position(ax, c, rad):
            dot_group = VGroup()
            dx = 0.5  # must match your partition

            for i in np.arange(0.5, 2.6, dx):
                dot = always_redraw(
                    lambda i=i: Dot(radius=rad)
                    .set_color(C_MAGENTA)
                    .move_to(
                        ax.c2p(i + c*dx, f(i + c*dx))
                    )
                )
                dot_group.add(dot)

            return dot_group
        
        #### This create dots for axes 1
        dot_left_1 = func_position(axes_1,0,0.06)
        dot_center_1 = func_position(axes_1,0.5,0.06)
        dot_right_1 = func_position(axes_1,1,0.06)

        ### The animations start here.
        self.play(FadeIn(VGroup(axes_1,x_label_1,y_label_1)),rate_func=smooth)
        self.wait(2)
        self.play(Write(text_1),rate_func=smooth,run_time=2)
        self.play(Create(graph_1),rate_func=smooth,run_time=10)
        self.play(Create(VGroup(a_label,b_label,a_line,b_line)),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeIn(text_2),FadeOut(text_1),rate_func=smooth,run_time=2,lag_ratio=1)
        self.play(FadeOut(VGroup(a_label,b_label)),FadeIn(x_label_group),Create(x_lines_group),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeIn(text_3),FadeOut(text_2),rate_func=smooth,run_time=2,lag_ratio=1)
        self.wait(2)
        self.play(FadeIn(star_group),rate_func=smooth,run_time=2)
        self.play(x_star_tracker.animate.set_value(0.7),run_time=2,rate_func=smooth)
        self.play(x_star_tracker.animate.set_value(0.99),run_time=2,rate_func=smooth)
        self.play(x_star_tracker.animate.set_value(0.75),run_time=2,rate_func=smooth)

        self.play(FadeIn(text_4[0]),FadeOut(text_3),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(x_star_tracker.animate.set_value(0.5),run_time=2,rate_func=smooth)
        self.play(FadeOut(star_group),rate_func=smooth,run_time=2)
        self.play(FadeOut(VGroup(x1_label,x6_label,x_label_group,x_lines_group,a_line,b_line)))
        self.play(FadeIn(rect_1_left),run_time=2,rate_func=smooth)
        self.play(FadeIn(dot_left_1),run_time=2,rate_func=smooth)
        self.play(Write(text_4[1]),rate_func=smooth,run_time=2)
        self.play(Indicate(dot_left_1),run_time=2)
        self.wait(4)

        self.play(FadeIn(text_5),FadeOut(text_4),rate_func=smooth,run_time=2,lag_ratio=1)
        self.play(ReplacementTransform(rect_1_left,rect_1_center),ReplacementTransform(dot_left_1,dot_center_1),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(Indicate(dot_center_1),run_time=2)
        self.wait(2)
        self.play(FadeIn(text_6),FadeOut(text_5),rate_func=smooth,run_time=2,lag_ratio=1)
        self.play(ReplacementTransform(rect_1_center,rect_1_right),ReplacementTransform(dot_center_1,dot_right_1),rate_func=smooth)
        
        self.wait(2)
        self.play(Indicate(dot_right_1),run_time=2)
        self.wait(2)
        self.play(FadeIn(text_7),FadeOut(text_6),rate_func=smooth,run_time=2)
        self.play(FadeOut(dot_right_1))
        self.play(ReplacementTransform(rect_1_right,rect_1_left),FadeIn(center_group),FadeIn(right_group),rate_func=smooth,run_time=0.7)
        self.play(graph_group.animate.scale(0.6).arrange(RIGHT))
        self.wait(1)

        ## Extra code
        left_text = always_redraw(
            lambda: MathTex(r"\text{left-endpoints}",font_size=28).next_to(axes_1,DOWN,buff=0.7)
        )

        center_text = always_redraw(
            lambda: MathTex(r"\text{mid-points}",font_size=28).next_to(axes_2,DOWN,buff=0.7)
        )

        right_text = always_redraw(
            lambda: MathTex(r"\text{right-endpoints}",font_size=28).next_to(axes_3,DOWN,buff=0.7)
        )  

        dot_left_main = func_position(axes_1,0,0.045)
        dot_center_main = func_position(axes_2,0.5,0.045)
        dot_right_main = func_position(axes_3,1,0.045)

        ## Extra code ends here

        self.play(FadeIn(VGroup(left_text,center_text,right_text)),rate_func=smooth,run_time=2)
        self.play(FadeIn(VGroup(dot_left_main,dot_center_main,dot_right_main)),rate_func=smooth,run_time=2)
        self.wait(4)

        self.play(FadeIn(text_8),FadeOut(text_7),rate_func=smooth,run_time=2)
        self.play(Indicate(VGroup(dot_left_main,dot_center_main,dot_right_main)),run_time=3)
        self.wait(4)

        self.play(FadeOut(center_group),FadeOut(center_text),FadeOut(dot_center_main))

        graph_group.remove(center_group)

        self.play(graph_group.animate.scale(1.2).arrange(RIGHT,buff=1))
        self.wait(4)

        ### Extra code. 
        lower_sum = MathTex(r"\text{Lower sum}",font_size=28).move_to(axes_1.c2p(1.5,9))
        higher_sum = MathTex(r"\text{Upper sum}",font_size=28).move_to(axes_3.c2p(1.5,9))

        
        ## Extra code ends
        self.play(FadeIn(text_9),FadeOut(text_8),rate_func=smooth,run_time=2)
        self.play(Write(lower_sum),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeIn(text_10),FadeOut(text_9),rate_func=smooth,run_time=2)
        self.play(Write(higher_sum),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeOut(VGroup(dot_left_main,dot_right_main)))
        self.play(FadeIn(text_11),FadeOut(text_10),rate_func=smooth)
        self.play(dx_tracker.animate.set_value(0.05),rate_func=smooth,run_time=10)
        self.wait(4)

        self.play(FadeIn(text_12),FadeOut(text_11),rate_func=smooth,run_time=2)
        self.wait(5)










        



