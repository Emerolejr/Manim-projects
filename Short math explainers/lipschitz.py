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


# --- SCENES ---
class lipschitz_intro(Scene):
    def construct(self):
        header = BeamerBlock("Lipschitz continuity",width=14).move_to(ORIGIN)
        ## colour giver function
        def colour_giver(mob, indices, colors):
            for index, color in zip(indices, colors):
                if isinstance(index, (list, tuple)):
                    mob[index[0]][index[1]].set_color(color)
                else:
                    mob[index].set_color(color)
        
        ## This is slide 1.
        text_1 = MathTex(r"\textbf{Definition}",font_size=35)

        text_2 = VGroup( 
            MathTex(r"f: \mathbb{R} \to \mathbb{R} \text{ is Lipschitz continuous if:}",font_size=32),
            MathTex( r"\exists L > 0",r"\text{ such that } ",r"\forall x_1, x_2 \in \mathbb{R},",
            r"|",r"f(x_1)",r" - ",r"f(x_2)",r"| \le ",r"\text{ L }",r"|",r"x_1",    
            r" - ",r"x_2",r"|").set_font_size(32)).arrange(DOWN, buff=0.3,aligned_edge=LEFT)
        
        colour_giver(text_2,([1,0],[1,2],[1,4],[1,6],[1,8],[1,10],[1,12]),(C_PURPLE,C_GREEN,C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_PURPLE,C_GREEN,C_GREEN))
        
        text_3 = VGroup(MathTex(r"\text{Rearranging...}",font_size=32),
                        MathTex(r"\frac{|f(x_1) - f(x_2)|}{|x_1 - x_2|} \le L",
            r"\text{ for all }",r"x_1 \neq x_2",font_size=32)).arrange(DOWN,buff=0.3,aligned_edge=LEFT)
        colour_giver(text_3,([1,0],[1,2]),(C_BRIGHT_BLUE,C_GREEN))
        
    
        text_4 = MathTex(r"\text{This means the maximum value of the slope is smaller than, }",
        r"\textbf{the Lipschitz constant L}",font_size=32).arrange(DOWN,buff=0.5,aligned_edge=LEFT)
       
        align_slide_1_texts = VGroup(text_2,text_3,text_4).arrange(DOWN,buff=0.5,aligned_edge=LEFT)
        slide_1_texts = VGroup(text_1,align_slide_1_texts).arrange(DOWN,buff=0.5)
       
        self.add(header)
        self.wait(2)
        self.play(Write(text_1),rate_func=smooth)
        self.wait(2)    

        for i in align_slide_1_texts:
            self.play(Write(i),rate_func=smooth)
            self.wait(2)
        self.wait(2)
        self.play(FadeOut(align_slide_1_texts),rate_func=smooth)
        self.wait(1)

        ### This is for slide 2 texts
        text_5 = MathTex(r"\textbf{Why Lipschitz continuity} \implies \textbf{Normal Continuity}",font_size=35)

        text_6 = VGroup(MathTex(r"\text{Continuity at a point, } x_1",font_size=32),
        MathTex(r"\lim_{x_2 \to x_1} ",r"f(x_2)",r" = ",r"f(x_1)",font_size=32)
        ).arrange(DOWN,buff=0.3,aligned_edge=LEFT)

        colour_giver(text_6,([1,1],[1,3]),(C_BRIGHT_BLUE,C_BRIGHT_BLUE))
        text_6[1][0][3:].set_color(C_GREEN)
       
        text_7 = VGroup(
            MathTex(r"\text{From lipschitz continuity, we have}",font_size=32),
            MathTex(r"|",r"f(x_2)",r" - ",r"f(x_1)",r"| \le ",r"L ",r"|",r"x_2",r" - ",r"x_1",r"|",font_size=32)
        ).arrange(DOWN,buff=0.3,aligned_edge=LEFT)
        colour_giver(text_7,([1,1],[1,3],[1,5],[1,7],[1,9]),(C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_PURPLE,C_GREEN,C_GREEN))
        
        text_8 =  VGroup(
            MathTex(r"\text{if }",r"x_2 \to x_1 ",font_size=32),
            MathTex(r"\text{As RHS } \to 0 ",r"\implies ",r"LHS \to 0",font_size=32)
        ).arrange(DOWN,buff=0.3,aligned_edge=LEFT)

        text_8[0][1].set_color(C_GREEN)

        text_9 = MathTex(r"\text{So, } ",r"|",r"f(x_1)",r" - ",r"f(x_2)",r"| \to 0",r"x_2 \to x_1",font_size=32)
        colour_giver(text_9,(2,4,6),(C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_GREEN))

        text_10 = MathTex(r"\therefore",r" \lim_{x_2 \to x_1} ",r"f(x_2)",r" = ",r"f(x_1)",font_size=32)
        colour_giver(text_10,(2,4),(C_BRIGHT_BLUE,C_BRIGHT_BLUE))
        text_10[1][3:].set_color(C_GREEN)
        
        align_slide_2_texts = VGroup(text_6,text_7,text_8,text_9,text_10).arrange(DOWN,buff=0.3,aligned_edge=LEFT)
        slide_2_texts = VGroup(text_5,align_slide_2_texts).arrange(DOWN,buff=0.3)

        self.play(ReplacementTransform(text_1,text_5),rate_func=smooth)

        self.wait(2)
        for i in align_slide_2_texts:
            self.play(Write(i),rate_func=smooth)
            self.wait(2)
        self.wait(2)
        self.play(FadeOut(align_slide_2_texts),rate_func=smooth)
        self.wait(1)
        
        #### slide 3 texts.
        text_11 = MathTex(r"\textbf{How Bounded derivative} \implies \textbf{Lipschitz continuity}",font_size=35)
        
        text_12 = VGroup(MathTex(r"\text{\text{suppose the derivative is bounded}}",font_size=32),
        MathTex(r"\text{i.e. } ",r"|",r"f'(x)",r"|",r" \le ",r" M ",r"\text{ for all } x \in \mathbb{R}",font_size=32),
        MathTex(r"\text{The slope never exceeeds } M",font_size=32)).arrange(DOWN,buff=0.3,aligned_edge=LEFT)
        colour_giver(text_12,([1,2],[1,5],[1,6]),(C_BRIGHT_BLUE,C_PURPLE,C_GREEN))

        text_13 = MathTex(r"\text{So for } ",r"x_2 ",r"\text{ sufficiently close to }",r" x_1",font_size=32)
        colour_giver(text_13,(1,3),(C_BRIGHT_BLUE,C_BRIGHT_BLUE))
        
        text_14 = MathTex(r"\frac{|f(x_1) - f(x_2)|}{|x_1 - x_2|}",r" \approx ",r" |",r"f'(x_1)",r"| ",r"\le M",font_size=32)
        colour_giver(text_14,(0,3,5),(C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_PURPLE))

        text_15 = MathTex(r"\text{So, } ",r"|",r"f(x_1)",r" - ",r"f(x_2)",r"|",r" \le ",
        r" M ",r"|",r"x_1",r" - ",r"x_2",r"|",font_size=32)
        colour_giver(text_15,(2,4,7,9,11),(C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_PURPLE,C_GREEN,C_GREEN)) 

        text_16 = MathTex(r"\text{If you replace } ",r"M",r"\text{ with } ",r"L",r"\text{ you get the definition of Lipschitz continuity}",font_size=30)
        colour_giver(text_16,(1,3),(C_PURPLE,C_PURPLE))

        text_17 = MathTex(r"\text{So, } ",r"|",r"f(x_1)",r" - ",r"f(x_2)",r"| \le ",r"L ",r"|",r"x_1",r" - ",r"x_2",r"|",font_size=32)
        colour_giver(text_17,(2,4,6,8,10),(C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_PURPLE,C_GREEN,C_GREEN))
        
        align_slide_3_texts = VGroup(text_12,text_13,text_14,text_15,text_16,text_17).arrange(DOWN,buff=0.3,aligned_edge=LEFT)
        slide_3_texts = VGroup(text_11,align_slide_3_texts).arrange(DOWN,buff=0.3)

        self.play(ReplacementTransform(text_5,text_11),rate_func=smooth)
        self.wait(2)

        for i in align_slide_3_texts:
            self.play(Write(i),rate_func=smooth)
            self.wait(2)

        self.wait(2)
        self.play(FadeOut(align_slide_3_texts),rate_func=smooth)
        self.wait(1)

        ### slide 4 texts.
        text_18 = MathTex(r"\textbf{Simplest form of Lipschitz continuity}",font_size=35)
        text_19 = MathTex(r"\text{A linear function is given as }",r" f(x)",r" = ",r"ax ",r"+ ",r"b",font_size=32)
        colour_giver(text_19,(1,3,5),(C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_BRIGHT_BLUE))

        text_20 = MathTex(r"\text{The slope, } ",r"f'(x)",r" = ",r"a",font_size=32)
        colour_giver(text_20,(1,3),(C_BRIGHT_BLUE,C_BRIGHT_BLUE))

        text_21 = MathTex(r"\text{Constants are automatically bounded, so we can say Linear functions have}",r" \textbf{bounded derivatives}",font_size=32).arrange(DOWN,buff=0.2,aligned_edge=LEFT)
        text_22 = MathTex(r"\text{Recall that bounded derivatives} \implies \textbf{Lipschitz continuity}",font_size=32)
        text_23 = MathTex(r"\therefore \text{All linear functions are Lipschitz continuous}",font_size=32)
       
        align_slide_4_texts = VGroup(text_19,text_20,text_21,text_22,text_23).arrange(DOWN,buff=0.3,aligned_edge=LEFT)
        slide_4_texts = VGroup(text_18,align_slide_4_texts).arrange(DOWN,buff=0.3)
        
        self.play(ReplacementTransform(text_11,text_18),rate_func=smooth)
        self.wait(2)
        
        for i in align_slide_4_texts:
            self.play(Write(i),rate_func=smooth)
            self.wait(2)

        self.wait(5)
        self.play(FadeOut(slide_4_texts),FadeOut(header),rate_func=smooth)
        self.wait(2)




class lipschitz_graph_1(Scene):
    def construct(self):

        ### colour giver function
        def colour_giver(mob, indices, colors):
            for index, color in zip(indices, colors):
                if isinstance(index, (list, tuple)):
                    mob[index[0]][index[1]].set_color(color)
                else:
                    mob[index].set_color(color)
        
        ###Texts that help explain the graph
        text_1 = MathTex(r"\forall \text{ } x_1,x_2",r"\in \mathbb{R}",
        r"|",r"f(x_1)",r" - ",r"f(x_2)",r"|",r" < ",r"L",
        r"(",r"x_1",r" - ",r"x_2",r")",font_size=32).to_corner(UP,buff=0.2)
        colour_giver(text_1,(0,3,5,8,10,12),(C_GREEN,C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_PURPLE,C_GREEN,C_GREEN))

        text_2 = VGroup(
            MathTex(r"\text{This means the slope is always less than } ",r"L",font_size=32),
            MathTex (r"\text{at any point of the function}",font_size=32)).arrange(DOWN,aligned_edge=LEFT,buff=0.2).to_corner(UP,buff=0.2)
        text_2[0][1].set_color(C_PURPLE)

        text_3 = MathTex(r"\text{Taking a random point } ",
        r"x_o",font_size=32).to_corner(UP,buff=0.2)
        text_3[1].set_color(C_GREEN)

        text_4 = MathTex(r"\text{The maximum possible slope at point } ",
        r"x_o",r" \text{ is +} ",r"L",font_size=32).to_corner(UP,buff=0.2)
        text_4[1].set_color(C_GREEN)
        text_4[3].set_color(C_PURPLE)

        text_5 = MathTex(r"\text{The minimum possible slope at point } ",
        r"x_o",r" \text{ is -} ",r"L",font_size=32).to_corner(UP,buff=0.2)
        text_5[1].set_color(C_GREEN)
        text_5[3].set_color(C_PURPLE)

        text_6 = MathTex(r"\text{Note: Areas where } ",r"|",r"f'(x)",r"|", 
        r"\text{ is larger}",font_size=32).to_corner(UP,buff=0.2)
        text_6[2].set_color(C_BRIGHT_BLUE)
        
        text_7 = VGroup(MathTex(r"\text{If a function is} \textbf{ lipschitz continous,}"
        ,font_size=32),
        MathTex(r"\text{then the function has a } \textbf{bounded derivative}",
        font_size=32)).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)
        
        text_8 = MathTex(r"\text{As an illustration, Here's the tangent line of the graph at } ",
        r"x_o",font_size=32).to_corner(UP,buff=0.2)
        text_8[1].set_color(C_GREEN)

        text_9 = MathTex(r"\text{observe that it is bounded by the } \\ \text{region defined by } ",
        r"\text{+L and -L}",r"\text{ slopes}",font_size=32).to_corner(UP,buff=0.2)
        text_9[1].set_color(C_PURPLE)

        text_10 = MathTex(r"\text{Indicating that the function is Lipschitz continuous}",
        font_size=32).to_corner(UP,buff=0.5).to_corner(UP,buff=0.2)

        ## axis for the graph
        ax = Axes(
            x_range=[0,10,2],
            y_range=[0,12,2],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": True},
            tips=False,
        ).shift(DOWN*0.5)

        x_label = ax.get_x_axis_label("x")
        y_label = ax.get_y_axis_label("f(x)")
        
        graph = ax.plot(
            lambda x: 2*np.sin(x) + x + 1, 
            x_range =[0,10,1],
            color=C_BLUE
        )

        ### 
        # This part is for the tangent lines
        ###

        ##This is a function that calculates the function value at a given point
        def f(x):
            return 2*np.sin(x) + x + 1

        ### This is the range of value for which the L value functions will be plotted.

        tracker = ValueTracker(5)

        dot = always_redraw(
            lambda: Dot(
                ax.c2p(tracker.get_value(), f(tracker.get_value())),
                color=C_BLUE
            )
        )

        L = 3. ##This is the lipschitz conttant for the particular function

        # Axis bounds
        x_min, x_max = 0, 10
        y_min, y_max = 0, 12


        def lipschitz_segment(sign=1):
            x0 = tracker.get_value()
            y0 = f(x0)
            m = sign * L

            # Solve intersections with horizontal boundaries
            if m != 0:
                x_at_ymin = x0 + (y_min - y0) / m
                x_at_ymax = x0 + (y_max - y0) / m
            else:
                x_at_ymin = x_min
                x_at_ymax = x_max

            # Order correctly
            x_left = min(x_at_ymin, x_at_ymax)
            x_right = max(x_at_ymin, x_at_ymax)

            # Clip to x-axis bounds
            x_start = max(x_min, x_left)
            x_end = min(x_max, x_right)

            # If completely outside box, draw nothing
            if x_start >= x_end:
                return VGroup()

            return ax.plot(
                lambda x: y0 + m*(x - x0),
                x_range=[x_start, x_end],
                color=C_PURPLE
            )

        upper_line = always_redraw(lambda: lipschitz_segment(sign=1))
        lower_line = always_redraw(lambda: lipschitz_segment(sign=-1))

        upper_line_label = always_redraw(
            lambda: MathTex(r"+L").next_to(upper_line.get_end(), RIGHT,buff=0.1).set_color(C_PURPLE)
        )

        lower_line_label = always_redraw(
            lambda: MathTex(r"-L").next_to(lower_line.get_start(),LEFT,buff=0.1).set_color(C_PURPLE)
        )

        ## This part is for the absolute region
        absolute_region_1 = always_redraw(
            lambda: Polygon(
                ax.c2p(x_max, y_min),
                ax.c2p(x_max, y_max),
                upper_line.get_end(),
                dot.get_center(),
                lower_line.get_end(),
                color=C_RED,
                fill_opacity=0.1,
                stroke_width=0
            )
        )

        ## This part is for the absolute region
        absolute_region_2 = always_redraw(
            lambda: Polygon(
                ax.c2p(x_min, y_min),
                ax.c2p(x_min, y_max),
                lower_line.get_start(),
                dot.get_center(),
                upper_line.get_start(),
                color=C_RED,
                fill_opacity=0.1,
                stroke_width=0
            )
        )

        x_indicator = always_redraw(
            lambda:ax.get_vertical_line(dot.get_center()).set_color(C_GREEN)
        )

        y_indicator = always_redraw(
            lambda:ax.get_horizontal_line(dot.get_center()).set_color(C_RED)
        )

        x_o_label = always_redraw(
            lambda:MathTex(r"x_o",font_size=32,color=C_GREEN).next_to(x_indicator,DOWN,buff=0.7)
        )

        f_x_o_label = always_redraw(
            lambda:MathTex(r"f(x_o)",font_size=32,color=C_RED).next_to(y_indicator,LEFT,buff=0.7)
        )

        slope_line = always_redraw(lambda: TangentLine(graph, alpha=tracker.get_value()/10, color=C_GREEN,length=4))
        indicator_box = always_redraw(lambda: SurroundingRectangle(slope_line, color=C_GREEN, buff=0.1))


        #### All the animations of the graph start heres.
        
        self.play(FadeIn(ax),FadeIn(x_label),FadeIn(y_label),Create(graph),rate_func=smooth)
        self.wait(2)
        self.play(Write(text_1),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3),rate_func=smooth)
        self.wait(4)
        self.play(Create(dot),rate_func=smooth)
        self.play(Create(x_o_label),Create(f_x_o_label),rate_func=smooth)
        self.wait(2)
        self.play(Create(x_indicator),Create(y_indicator),rate_func=smooth)
        self.wait(2)

        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth)
        self.wait(2)
        self.play(Create(upper_line),Create(upper_line_label),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_4,text_5),rate_func=smooth)
        self.wait(2)
        self.play(Create(lower_line),Create(lower_line_label),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_5,text_6),rate_func=smooth)
        self.wait(2)
        self.play(FadeIn(absolute_region_1),FadeIn(absolute_region_2),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_6,text_7),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_7,text_8),rate_func=smooth)
        self.wait(2)
        self.play(Create(slope_line),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_8,text_9),rate_func=smooth)
        self.wait(2)
        self.play(Create(indicator_box),rate_func=smooth)
        self.wait(4)
        self.play(Uncreate(indicator_box),rate_func=smooth)
        self.play(ReplacementTransform(text_9,text_10),rate_func=smooth)
        self.wait(4)



class lipschitz_graph_2(Scene):
    def construct(self):
        ### Here is a colour giver function
        def colour_giver(mob, indices, colors):
            for index, color in zip(indices, colors):
                # If it's nested like (0,1)
                if isinstance(index, (list, tuple)):
                    mob[index[0]][index[1]].set_color(color)
                # If it's single level like 2
                else:
                    mob[index].set_color(color)

        ##Graph texts
        text_1 = MathTex(r"\text{Graph of } ",r"f(x)",r"=",r" 2x + 1",font_size=32).to_corner(UP,buff=0.2)
        colour_giver(text_1,(1,3),(C_BRIGHT_BLUE,C_BRIGHT_BLUE))

        text_2 = VGroup(
            MathTex(r"\text{Comparing y = mx + c, we can say}",font_size=32),
            MathTex(r"\text{slope of graph = 2}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_3 = VGroup(
            MathTex(r"\text{Calculating the derivative at } ",r"x_o",font_size=32),
            MathTex(r"f'(x_o)",r"\text{ = }",r" \frac{\Delta y}{\Delta x} ",r" = ",r"\frac{15 - 7}{7 - 3}",r" =",r" 2",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        colour_giver(text_3,([0,1],[1,1],[1,2],[1,4],[1,6]),(C_GREEN,C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_BRIGHT_BLUE))

        text_4 = VGroup(
            MathTex(r"\text{Constants are, by default, bounded}",font_size=32),
            MathTex(r"\text{this implies that the derivative is bounded}",font_size=32)
        ).arrange(DOWN,buff=0.2,aligned_edge=LEFT).to_corner(UP,buff=0.2)

        text_5 = MathTex(r"\text{Here is a positive slope, } ",r"L",r" = ",r"2.7 > 2",font_size=32).to_corner(UP,buff=0.2)
        colour_giver(text_5,(1,3),(C_PURPLE,C_PURPLE))

        text_6 = MathTex(r"\text{Here is a negative slope, } ",r"L",r" = ",r"-2.7 < -2",font_size=32).to_corner(UP,buff=0.2)
        colour_giver(text_6,(1,3),(C_PURPLE,C_PURPLE))
        
        text_7 = MathTex(r"\text{observe that it is bounded by the } \\ \text{region defined by } ",
        r"\text{+L and -L}",r"\text{ slopes}",font_size=32).to_corner(UP,buff=0.2)
        text_7[1].set_color(C_PURPLE)
        text_8 = MathTex(r"\forall \text{ } x_1,x_2",r"\in \mathbb{R}",
        r"|",r"f(x_1)",r" - ",r"f(x_2)",r"|",r" < ",r"L",
        r"(",r"x_1",r" - ",r"x_2",r")",font_size=32).to_corner(UP,buff=0.2)
        
        colour_giver(text_8,(0,3,5,8,10,12),(C_GREEN,C_BRIGHT_BLUE,C_BRIGHT_BLUE,C_PURPLE,C_GREEN,C_GREEN))

        #### This is the graph for the function f(x) = 2x + 1
        ax = Axes(
            x_range=[0,8,2],
            y_range=[0,18,4],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": True},
            tips=False,
        ).shift(DOWN*0.5)

        x_label = ax.get_x_axis_label("x")
        y_label = ax.get_y_axis_label("f(x)")

        graph = ax.plot(
            lambda x: 2*x + 1,
            x_range=[0,8,1],
            color=C_BRIGHT_BLUE
        )
    
        ##This is a function that calculates the function value at a given point
        def f(x):
            return 2*x + 1

        ### This is the range of value for which the L value functions will be plotted.
        tracker = ValueTracker(5)
        dot = always_redraw(
            lambda: Dot(
                ax.c2p(tracker.get_value(), f(tracker.get_value())),
                color=C_BRIGHT_BLUE
            )
        )

        L = 2.7
        x_min, x_max = 0, 8
        y_min, y_max = 0, 18

        def lipschitz_segment(sign=1):
            x0 = tracker.get_value()
            y0 = f(x0)
            m = sign * L

            # Solve intersections with horizontal boundaries
            if m != 0:
                x_at_ymin = x0 + (y_min - y0) / m
                x_at_ymax = x0 + (y_max - y0) / m
            else:
                x_at_ymin = x_min
                x_at_ymax = x_max

            # Order correctly
            x_left = min(x_at_ymin, x_at_ymax)
            x_right = max(x_at_ymin, x_at_ymax)

            # Clip to x-axis bounds
            x_start = max(x_min, x_left)
            x_end = min(x_max, x_right)

            # If completely outside box, draw nothing
            if x_start >= x_end:
                return VGroup()

            return ax.plot(
                lambda x: y0 + m*(x - x0),
                x_range=[x_start, x_end],
                color=C_PURPLE
            )

        upper_line = always_redraw(lambda: lipschitz_segment(sign=1))
        lower_line = always_redraw(lambda: lipschitz_segment(sign=-1))

        absolute_region_1 = always_redraw(
            lambda: Polygon(
                ax.c2p(x_max, y_min),
                ax.c2p(x_max, y_max),
                upper_line.get_end(),
                dot.get_center(),
                lower_line.get_end(),
                color=C_RED,
                fill_opacity=0.2,
                stroke_width=0
            )
        )

        absolute_region_2 = always_redraw(
            lambda: Polygon(
                ax.c2p(x_min, y_min),
                ax.c2p(x_min, y_max),
                lower_line.get_start(),
                dot.get_center(),
                upper_line.get_start(),
                color=C_RED,
                fill_opacity=0.2,
                stroke_width=0
            )
        )

        ### These mobjects are for the slope
        x1_line = always_redraw(
            lambda: ax.get_horizontal_line(ax.c2p(tracker.get_value()-2, f(tracker.get_value()-2)))
        )

        x2_line = always_redraw(
            lambda: ax.get_horizontal_line(ax.c2p(tracker.get_value()+2, f(tracker.get_value()+2)))
        )

        y1_line = always_redraw(
            lambda: ax.get_vertical_line(ax.c2p(tracker.get_value()-2, f(tracker.get_value()-2)))
        )

        y2_line = always_redraw(
            lambda: ax.get_vertical_line(ax.c2p(tracker.get_value()+2, f(tracker.get_value()+2)))
        )

        dx_line = always_redraw(
            lambda: DashedLine(
                ax.c2p(tracker.get_value()-2, f(tracker.get_value()-2)),
                ax.c2p(tracker.get_value()+2, f(tracker.get_value()-2)),
                color=C_GREEN
            )
        )

        dy_line = always_redraw(
            lambda: DashedLine(
                ax.c2p(tracker.get_value()+2, f(tracker.get_value()-2)),
                ax.c2p(tracker.get_value()+2, f(tracker.get_value()+2)),
                color=C_RED
            )
        )
        
        ##slope labels.
        slope_label_y = always_redraw(
            lambda: MathTex(r"\Delta y",color=C_RED).next_to(dy_line,RIGHT,buff=0.2)    
        )

        slope_label_x = always_redraw(
            lambda: MathTex(r"\Delta x",color=C_GREEN).next_to(dx_line,DOWN,buff=0.2)
        )

        x1_label = always_redraw(
            lambda: MathTex(r"x_1=3",color=C_GREEN,font_size=30).next_to(ax.c2p(tracker.get_value()-2,0),DOWN,buff=0.7)
        )

        x2_label = always_redraw(
            lambda: MathTex(r"x_2=7",color=C_GREEN,font_size=30).next_to(ax.c2p(tracker.get_value()+2, 0),DOWN,buff=0.7)
        )

        y1_label = always_redraw(
            lambda: MathTex(r"y_1=7",color=C_RED,font_size=30).next_to(ax.c2p(0, f(tracker.get_value()-2)),LEFT,buff=0.7)
        )

        y2_label = always_redraw(
            lambda: MathTex(r"y_2=15",color=C_RED,font_size=30).next_to(ax.c2p(0, f(tracker.get_value()+2)),LEFT,buff=0.7)
        )

        x_indicator = always_redraw(
            lambda:ax.get_vertical_line(dot.get_center()).set_color(C_GREEN)
        )

        y_indicator = always_redraw(
            lambda:ax.get_horizontal_line(dot.get_center()).set_color(C_RED)
        )

        x_o_label = always_redraw(
            lambda:MathTex(r"x_o",font_size=32,color=C_GREEN).next_to(ax.c2p(tracker.get_value(), 0),DOWN,buff=0.7)
        )

        f_x_o_label = always_redraw(
            lambda:MathTex(r"f(x_o)",font_size=32,color=C_RED).next_to(ax.c2p(0, f(tracker.get_value())),LEFT,buff=0.7)
        )

        slope_line = always_redraw(
            lambda: Line(
                ax.c2p(tracker.get_value()-2, f(tracker.get_value()-2)),
                ax.c2p(tracker.get_value()+2, f(tracker.get_value()+2)),
                color=C_GREEN,stroke_width=2
            ).set_z_index(2)
        )

        ####
        ### Animations for the graph and the texts
        ####
        self.play(FadeIn(ax),FadeIn(x_label),FadeIn(y_label),rate_func=smooth)
        self.wait(2)
        self.play(Create(graph),rate_func=smooth)
        self.wait(2)
        self.play(Write(text_1),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_1,text_2),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_2,text_3[0]),rate_func=smooth)  
        self.wait(2)
        self.play(FadeIn(dot))
        self.play(Create(x_o_label),Create(f_x_o_label),rate_func=smooth)
        self.play(Create(x_indicator),Create(y_indicator),rate_func=smooth)
        self.play(Create(slope_line),rate_func=smooth)
        self.wait(4)
        self.play(Uncreate(x_o_label),Uncreate(f_x_o_label),rate_func=smooth)
        self.play(Uncreate(x_indicator),Uncreate(y_indicator),rate_func=smooth)
        self.wait(2)

        self.play(Create(dx_line),Create(dy_line),rate_func=smooth)
        self.play(Create(x1_line),Create(x2_line),Create(y1_line),Create(y2_line),rate_func=smooth)
        self.play(Create(x1_label),Create(x2_label),Create(y1_label),Create(y2_label),rate_func=smooth)
        self.play(Create(slope_label_x),Create(slope_label_y),rate_func=smooth)
        self.wait(4)

        self.play(Write(text_3[1][0]),rate_func=smooth)
        self.wait(1)
        self.play(TransformMatchingShapes(VGroup(slope_label_x,slope_label_y),text_3[1][1:3]),rate_func=smooth,run_time=4)
        self.wait(2)
        self.play(TransformMatchingShapes(VGroup(x1_label,x2_label,y1_label,y2_label),text_3[1][3:5]),rate_func=smooth,run_time=4)
        self.wait(2)

        self.play(Write(text_3[1][5:]),rate_func=smooth,run_time=4)
        self.wait(4)

        self.play(ReplacementTransform(text_3,text_4),rate_func=smooth)
        self.wait(4)
        self.play(FadeOut(VGroup(dx_line,dy_line,x1_line,x2_line,y1_line,y2_line)),rate_func=smooth)
        self.wait(2)

        self.play(ReplacementTransform(text_4,text_5),rate_func=smooth)
        self.play(Create(upper_line),rate_func=smooth)
        self.wait(4)

        self.play(ReplacementTransform(text_5,text_6),rate_func=smooth)
        self.play(Create(lower_line),rate_func=smooth)
        self.wait(4)

        self.play(FadeIn(absolute_region_1),FadeIn(absolute_region_2),rate_func=smooth)
        self.wait(4)
        self.play(ReplacementTransform(text_6,text_7),rate_func=smooth)
        self.wait(2)
        self.play(ReplacementTransform(text_7,text_8),rate_func=smooth)
        self.play(Indicate(graph,color=C_GREEN),rate_func=smooth)
        self.wait(6)
        