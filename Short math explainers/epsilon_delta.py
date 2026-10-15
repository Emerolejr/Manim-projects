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


class function_intro(Scene):
    def construct(self):
        ## Header for function
        func_header = BeamerBlock("Formal definition",width=14).move_to(ORIGIN)

        step_1 = MathTex(
            r"\text{A function } f : \mathbb{R} \to \mathbb{R} ",
            r"\text{ is continuous at } x_0 \text{ if:}"
        ).to_edge(LEFT).shift(UP*2.5)


        function_def = MathTex(
            r"\forall \varepsilon > 0,",
            r"\exists \delta > 0,",
            r"\text{ such that }",
            r"|x - x_0| < \delta",
            r"\Rightarrow",
            r"|f(x) - f(x_0)| < \varepsilon",
            font_size=42
        ).next_to(step_1, DOWN, buff=1).set_x(0)


        # SAME semantic coloring
        function_def[0].set_color(C_RED)
        function_def[1].set_color(C_GREEN)
        function_def[3].set_color(C_BLUE)
        function_def[5].set_color(C_RED)



        # Proper aligned explanation (WITH correct line breaks)
        step_3 = MathTex(
            r"\begin{aligned}"
            r"&\Rightarrow \varepsilon > 0 \text{ (arbitrarily small)} "
            r"\Rightarrow \exists \delta(\varepsilon) > 0 "
            r"\Rightarrow \text{all } x \text{ with } |x - x_0| < \delta "
            r"\text{ are mapped to values} \\" 
            r"&\text{satisfying }|f(x) - f(x_0)| < \varepsilon"
            r"\end{aligned}",
            font_size=30
        ).next_to(function_def, DOWN, buff=1).to_edge(LEFT)

        step_3[0][1:4].set_color(C_RED)     # epsilon > 0

        # --- GREEN Slices ---
    
        step_3[0][21:28].set_color(C_GREEN) # |x - x_0| < delta
        
        self.add(func_header)

        self.wait(2)
        self.play(Write(step_1))
        self.wait(2)
        self.play(Write(function_def))
        self.wait(2)
        self.play(Write(step_3))
        self.wait(5)

        self.play(FadeOut(*self.mobjects))
        self.wait(2)


class function_graph(Scene):
    def construct(self):
        ## Header part of the graph
        graph_header = BeamerBlock("Graphical intuition ",width = 14).move_to(ORIGIN)
        
        self.add(graph_header)

        ##Graph texts for header
        graph_text_1 = MathTex(
        r"\text{Given a function } f(x)",font_size=25
        ).shift(UP*2.5)

        graph_text_2 = MathTex(
            r"\text{Pick a point } ",font_size=25
        ).shift(UP*2.5)

        graph_text_3 = MathTex(
            r"\text{An } \varepsilon\text{-band around } f(x_0)",font_size=25
        ).shift(UP*2.5)

        graph_text_4 = MathTex(
            r"\text{A corresponding } \delta\text{-strip around } x_0",font_size=25
        ).shift(UP*2.5)

        graph_text_5 = MathTex(
            r"\text{Watch } \delta \text{ adjust as } \varepsilon \text{ changes}",font_size=25
        ).shift(UP*2.5)

        graph_text_6 = MathTex(
            r"\text{If } |x - x_0| < \delta,",
            r"\text{ then } |f(x) - f(x_0)| < \varepsilon",font_size=25
        ).shift(UP*2.5)

        self.wait(2)

        #Everything about the graph and its labels
        axes = Axes(x_range=[5,11,1],y_range=[0,400,1],
                    x_length=5,y_length=4,axis_config={"include_numbers":False,
                    "tip_shape":StealthTip,"include_ticks":False,"tip_width":0.2
                    }).next_to(graph_text_1,DOWN,buff=0.7)
        
        x_label = axes.get_x_axis_label("X",edge=RIGHT).scale(0.8)
        y_label = axes.get_y_axis_label("Y").scale(0.8)

        self.wait(2)
        self.play(Write(graph_text_1),rate_func=smooth)

        graph = axes.plot(
            lambda x:( (1/2)*(x - 1)**3 + (x - 1) + 2 ),
            x_range=[5,10,1],
        ).set_color(C_BLUE)

        self.play(FadeIn(VGroup(axes,x_label,y_label),shift=UP),rate_func=smooth)
        self.play(Create(graph),rate_func=smooth)
        
        self.wait(2)
        
        ####
        # About F(x_0), x_o, Epsilon and delta 
        ####


        def f(x):
            return (1/2)*(x - 1)**3 + (x - 1) + 2

        # Fixed x0
        x0 = 8
        L = f(x0)

        point_o = Dot(axes.c2p(x0, L), color=C_BLUE )

        epsilon = ValueTracker(50)

        # Horizontal epsilon bands
        epsilon_upper = always_redraw(
            lambda: Line(
                axes.c2p(5, L + epsilon.get_value()),
                axes.c2p(11, L + epsilon.get_value()),
                color=C_RED
            )
        )

        epsilon_lower = always_redraw(
            lambda: Line(
                axes.c2p(5, L - epsilon.get_value()),
                axes.c2p(11, L - epsilon.get_value()),
                color=C_RED
            )
        )

        def find_delta():
            eps = epsilon.get_value()
            
            # search small interval around x0
            xs = np.linspace(x0 - 2, x0 + 2, 1000)
            
            valid = [x for x in xs if abs(f(x) - L) < eps]
            
            if valid:
                return min(abs(min(valid) - x0), abs(max(valid) - x0))
            return 0.1

        delta_lines = always_redraw(
            lambda: VGroup(
                DashedLine(
                    axes.c2p(x0 - find_delta(), 0),
                    axes.c2p(x0 - find_delta(), 400),
                    color=GREEN
                ),
                DashedLine(
                    axes.c2p(x0 + find_delta(), 0),
                    axes.c2p(x0 + find_delta(), 400),
                    color=GREEN
                )
            )
        )

        point_lines = axes.get_lines_to_point(axes.c2p(x0,L)).set_color(C_BLUE).set_z_index(2)

        ###Epsilon delta regions 
        
        epsilon_region = always_redraw(lambda: Polygon(
            axes.c2p(5, L + epsilon.get_value()),
            axes.c2p(11, L + epsilon.get_value()),
            axes.c2p(11, L - epsilon.get_value()),
            axes.c2p(5, L - epsilon.get_value()),
            stroke_width=0,
            fill_color=C_RED,
            fill_opacity=0.2
        ))

        delta_region = always_redraw(
            lambda: Polygon(
            axes.c2p(x0 - find_delta(), 0),
            axes.c2p(x0 - find_delta(), 400),
            axes.c2p(x0 + find_delta(), 400),
            axes.c2p(x0 + find_delta(), 0),
            stroke_width=0,
            fill_color=C_GREEN,
            fill_opacity=0.2
            )
        )

        #texts for delta, epsilon, x_o and f(x_o)
       
        epsilon_upper_text = always_redraw(
            lambda: MathTex(r"\text{f(x) + }\varepsilon").next_to(epsilon_upper.get_start(),LEFT).scale(0.7).set_color(C_RED)
        )
 
        epsilon_lower_text =always_redraw(
            lambda: MathTex(r"\text{f(x) - }\varepsilon").next_to(epsilon_lower.get_start(),LEFT).scale(0.7).set_color(C_RED)
        )

        delta_1_text = always_redraw(
            lambda: MathTex(r"x_o - \delta ").scale(0.7).next_to(delta_lines[0].get_start(),DOWN).scale(0.7).set_color(C_GREEN)
        )

        delta_2_text = always_redraw(
            lambda: MathTex(r"x_o + \delta ").scale(0.7).next_to(delta_lines[1].get_start(),DOWN).scale(0.7).set_color(C_GREEN)
        )

        x_o_text = always_redraw(
            lambda: MathTex(r"x_o").scale(0.7).next_to(axes.c2p(x0,0),DOWN).set_color(C_BLUE)
        )

        f_of_x_o = always_redraw(
            lambda: MathTex(r"f(x_o)").scale(0.7).next_to(axes.c2p(5,L),LEFT).set_color(C_BLUE)
        )

        e_and_d_texts = VGroup(epsilon_lower_text,epsilon_upper_text,delta_1_text,
                               delta_2_text,x_o_text,f_of_x_o)

        ##Animations for the epsilon and delta bounds
        self.wait(2)
        self.play(ReplacementTransform(graph_text_1,graph_text_2),rate_func=smooth)
        self.play(Create(point_o))
        self.play(Create(point_lines),Create(f_of_x_o),Create(x_o_text),rate_func=smooth)
        self.wait(4)

        self.play(ReplacementTransform(graph_text_2,graph_text_3),rate_func=smooth)

        self.play(Create(epsilon_upper), Create(epsilon_lower),
                  Write(epsilon_lower_text), Write(epsilon_upper_text),
                  FadeIn(epsilon_region),rate_func=smooth)
        
        self.wait(2)

        self.play(ReplacementTransform(graph_text_3,graph_text_4),rate_func=smooth)

        self.play(Create(delta_lines),Write(delta_1_text),Write(delta_2_text),rate_func=smooth)

        self.wait(2)
        
        self.play(ReplacementTransform(graph_text_4,graph_text_5),rate_func=smooth)

        self.play(epsilon.animate.set_value(100))
        self.play(epsilon.animate.set_value(60))
        self.play(epsilon.animate.set_value(40))
        self.play(epsilon.animate.set_value(70))

        self.wait(2)

        self.play(ReplacementTransform(graph_text_5,graph_text_6),rate_func=smooth)
        self.play(FadeIn(delta_region),rate_func=smooth,run_time=3)
        self.wait(4)

        # Fade out everything except graph_header
        everything_except_header = Group(
            *[mob for mob in self.mobjects if mob is not graph_header]
        )

        self.play(FadeOut(everything_except_header), run_time=2)
        self.wait(2)
        

class function_graph_2(Scene):
    def construct(self):
        ###### Still Graph header.
        graph_header = BeamerBlock("Graphical intuition ",width = 14).move_to(ORIGIN)
        
        self.add(graph_header)
        self.wait(2)

        ##Graph texts for header
        graph_text_1 = MathTex(
            r"\text{Given a piecewise function\ldots}",
            font_size=25
        ).shift(UP*2.5)

        graph_text_2 = MathTex(
            r"\text{Here, } \delta \text{ controls the input, and } \varepsilon \text{ measures the output change.}",
            font_size=25
        ).shift(UP*2.5)

        graph_text_3 = MathTex(
            r"\text{Note } \varepsilon \text{,as we shrink and expand  } \delta.",
            font_size=25
        ).shift(UP*2.5)

        graph_text_4 = MathTex(
            r"\text{No matter how small } \delta \text{ becomes, the function values remain separated.}",
            font_size=25
        ).shift(UP*2.5)

        graph_text_5 = MathTex(
            r"\text{Unlike the continuity case, } \delta \text{ cannot force the outputs together.}",
            font_size=25
        ).shift(UP*2.5)

        graph_text_6 = MathTex(
            r"\text{Therefore, the limit does not exist at } x = 0.",
            font_size=25
        ).shift(UP*2.5)

        graph_text_7 = MathTex(
            r"\text{Mathematically, we write this as:}",
            font_size=25
        ).shift(UP*2.5)

        graph_text_8 = MathTex(
            r"\exists \varepsilon > 0 \ \text{such that} \ "
            r"\forall \delta > 0, \ "
            r"\exists x \ \text{with} \ "
            r"|x - x_0| < \delta \ "
            r"\text{but} \ "
            r"|f(x) - L| \ge \varepsilon.",
            font_size=25
        ).shift(UP*2.5)

        ## Discontinous function - piecewise function

        axes = Axes(y_range=[-2,20,1],x_range=[-5,6,1],x_length=5,y_length=4,axis_config={"include_numbers":False,
                    "tip_shape":StealthTip,"include_ticks":False,"tip_width":0.2
                    }).next_to(graph_text_1,DOWN,buff=0.7)

        piecewise_1 = axes.plot(
            lambda x: 0.5*x**2 + 7,
            x_range=[0,5],
        ).set_color(C_BLUE)

        piecewise_2 = axes.plot(
            lambda x: - 0.25*x**2 + 4,
            x_range=[-5,0],
        ).set_color(C_BLUE)
        
        x_label = axes.get_x_axis_label("X",edge=RIGHT).scale(0.8)
        y_label = axes.get_y_axis_label("Y").scale(0.8)

        hole_1 = Circle(radius=0.05).move_to(piecewise_1.get_start()).set_color(C_BLUE)
        hole_2 = Circle(radius=0.05).move_to(piecewise_2.get_end()).set_color(C_BLUE)
        

        ### Code to help with delta and epsilon
        delta = ValueTracker(3)
        x_o = 0

        def piecewise_1_value(x):
            return 0.5*x**2 + 7
        
        def piecewise_2_value(x):
            return -0.25*x**2 + 4

        # Epsilon and delta lines and symbols

        piecewise_1_epsilon_line = always_redraw(
             lambda: DashedLine(
                start=axes.c2p(-5, piecewise_1_value(delta.get_value())),
                end=axes.c2p(6, piecewise_1_value(delta.get_value())),
                color=C_RED
            )
        )


        piecewise_2_epsilon_line = always_redraw(
            lambda: DashedLine(
                start=axes.c2p(-5, piecewise_2_value(-delta.get_value())),
                end=axes.c2p(6, piecewise_2_value(-delta.get_value())),
                color=C_RED
            )
        )

        static_epsilon = DashedLine(
            start=axes.c2p(-5,(piecewise_1_value(0) + piecewise_2_value(0))/2,0),
            end = axes.c2p(6,(piecewise_1_value(0) + piecewise_2_value(0))/2,0)
        )

        # Delta lines (vertical)
        piecewise_1_delta_line = always_redraw(
            lambda: DashedLine(
                start=axes.c2p(delta.get_value(), -2),
                end=axes.c2p(delta.get_value(), 20),
                color=C_GREEN
            )
        )

        piecewise_2_delta_line = always_redraw(
            lambda: DashedLine(
                start=axes.c2p(-delta.get_value(), -2),
                end=axes.c2p(-delta.get_value(), 20),
                color=C_GREEN
            )
        )
        
                ### Braces and tags of braces
       # Delta braces (make them always_redraw if delta moves)
        delta_1_brace = always_redraw(
            lambda: BraceBetweenPoints(
                piecewise_1_delta_line.get_start(),
                axes.c2p(0, 0),
                direction=DOWN
            ).set_color(C_GREEN)
        )

        delta_2_brace = always_redraw(
            lambda: BraceBetweenPoints(
                piecewise_2_delta_line.get_start(),
                axes.c2p(0, 0),
                direction=DOWN
            ).set_color(C_GREEN)
        )

        # Epsilon braces (DO NOT wrap get_end() in c2p)
        epsilon_1_brace = always_redraw(
            lambda: BraceBetweenPoints(
                piecewise_1_epsilon_line.get_end(),
                static_epsilon.get_end(),
                direction=RIGHT
            ).set_color(C_RED)
        )

        epsilon_2_brace = always_redraw(
            lambda: BraceBetweenPoints(
                piecewise_2_epsilon_line.get_end(),
                static_epsilon.get_end(),
                direction=RIGHT
            ).set_color(C_RED)
        )

        delta_1_text = MathTex(r"\delta").scale(0.7).next_to(delta_1_brace,DOWN).set_color(C_GREEN)
        delta_2_text = delta_1_text.copy().next_to(delta_2_brace,DOWN).set_color(C_GREEN)
        epsilon_1_text= MathTex(r"\varepsilon").scale(0.7).next_to(epsilon_1_brace,RIGHT).set_color(C_RED)
        epsilon_2_text = epsilon_1_text.copy().next_to(epsilon_2_brace,RIGHT).set_color(C_RED)

        epsilon_delta_texts_braces = VGroup(
            delta_1_brace, delta_2_brace,
            epsilon_1_brace, epsilon_2_brace,
            epsilon_1_text, epsilon_2_text,
            delta_1_text, delta_2_text
        )

        ###Animation for discontinuity graph.

        self.play(Write(graph_text_1),rate_func=smooth)
        self.play(FadeIn(VGroup(axes,x_label,y_label)))
        self.play(Create(piecewise_1),Create(piecewise_2),Create(hole_1),Create(hole_2))
        self.wait(4)

        self.play(Create(VGroup(piecewise_1_delta_line,
                                piecewise_1_epsilon_line,
                                piecewise_2_epsilon_line,
                                piecewise_2_delta_line)))
        
        self.wait(2)
        self.play(FadeIn(epsilon_delta_texts_braces))
        self.play(ReplacementTransform(graph_text_1,graph_text_2))
        self.wait(2)

        self.play(FadeOut(epsilon_delta_texts_braces))
        self.play(ReplacementTransform(graph_text_2,graph_text_3))
        
        self.play(delta.animate.set_value(2))
        self.play(delta.animate.set_value(0.2))


        for i in range(3):
            self.play(delta.animate.set_value(0.1),run_time=0.3)
            self.play(delta.animate.set_value(1),run_time=0.3)

        self.play(delta.animate.set_value(0.1),run_time=2)

        self.wait(1)

        self.play(ReplacementTransform(graph_text_3,graph_text_4))

        self.play(Indicate(VGroup(piecewise_1_epsilon_line,
                                  piecewise_2_epsilon_line)),run_time=3)
        self.wait(2)

        self.play(ReplacementTransform(graph_text_4,graph_text_5),rate_func=smooth)
        self.wait(2)
        for i in range(3):
            self.play(delta.animate.set_value(0.1),run_time=0.3,rate_func=smooth)
            self.play(delta.animate.set_value(1.5),run_time=0.2,rate_func=smooth)
        
        self.play(ReplacementTransform(graph_text_5,graph_text_6))
        self.wait(1)
        self.play(ReplacementTransform(graph_text_6,graph_text_7))
        self.wait(1)

        self.play(ReplacementTransform(graph_text_7,graph_text_8))
        self.wait(4)

        