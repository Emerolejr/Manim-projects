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


class Cauchy_criterion_graph(MovingCameraScene):
    def construct(self):
    
        # Save initial camera state for later restoration
        self.camera.frame.save_state()

        # Adaptive scaling functions for camera zoom
        def get_scale():
            return self.camera.frame.height / config.frame_height

        def get_stroke_width():
            # Scale stroke width with camera zoom, clamped for visibility
            return max(4.0 * (get_scale() ** 0.5), 1.5)
            
        def get_font_size():
            return 36.0 * (get_scale() ** 0.5)

        # --- PART 2: GRAPH ANIMATION ---
        
        ax = Axes(
            x_range=[0, 101, 10],
            y_range=[0, 4, 0.5],
            x_length=11,
            y_length=6,
            axis_config={"include_tip": True, "numbers_to_exclude": [ ], "tick_size": 0.05}
        ).add_coordinates()
        ax.to_edge(DOWN, buff=1.0)
        
        labels = ax.get_axis_labels(x_label="n", y_label="a_n")

        # Scale axis labels based on camera zoom and position
        def scaling_updater_axis_numbers(mob):
             base_height = 0.25 * (get_scale() ** 0.5)
             for n in mob:
                 val = n.get_value()
                 if val > 6:
                     # Progressively shrink labels for larger n values
                     factor = max(0.4, 1.0 / (1.0 + (val - 6) * 0.1))
                     n.height = base_height * factor
                 else:
                     n.height = base_height
        ax.x_axis.numbers.add_updater(scaling_updater_axis_numbers)

        self.play(Create(ax), Write(labels), run_time=2)

        graph_formula_template = MathTex(r"\text{Plotting the graph of }a_n = 2 + \frac{(-1)^n}{\sqrt{n}}", font_size=48)
        graph_formula_template.to_edge(UP, buff=0.5)

        self.play(Write(graph_formula_template))
        self.wait(0.5)

        # Sequence dots
        dots = VGroup()
        
        def seq_func(n):
            """Alternating sequence: a_n = (-1)^n / n"""
            if n == 0: return 0 
            return 2 + (-1)**n/np.sqrt(n)
            
        def scaling_updater_dots(mob):
            """Scale dots based on camera zoom with gradual size decay for larger n."""
            base_width = 0.16 * (get_scale() ** 0.5)
            for i, d in enumerate(mob):
                 # Inverse decay: dots shrink gradually as n increases
                 decay_factor = 1.0 / (1.0 + i * 0.05)
                 d.width = base_width * max(0.1, decay_factor)
        
        dots.add_updater(scaling_updater_dots)
        self.add(dots)

        # Plot first 9 points with step-by-step substitution animation
        for n in range(1, 10):
            val = seq_func(n)
            
            # Create and plot dot, storing y-value for epsilon highlighting
            dot = Dot(ax.c2p(n, val), color=C_BLUE, radius=0.06)
            dot.y_val = val
            dots.add(dot)
            self.play(FadeIn(dot, scale=0.5), run_time=1)
            self.wait(1.2)

        ####Texts showing that early jumps are quite large 
        early_text = MathTex(r"\text{Note that early 'jumps' are quite large}", font_size=32).to_edge(UP, buff=0.5)
    
        self.play(ReplacementTransform(graph_formula_template,early_text))
        self.wait(2)
        self.play(ReplacementTransform(early_text,graph_formula_template))

        self.wait(2)
        for n in range(10, 100):
            val = seq_func(n)
            
            # Create and plot dot, storing y-value for epsilon highlighting
            dot = Dot(ax.c2p(n, val), color=C_BLUE, radius=0.06)
            dot.y_val = val
            dots.add(dot)
        
        self.play(FadeIn(*dots[11:]),rate_func=smooth)
        self.play(FadeOut(graph_formula_template))
        self.wait(2)

        ## Initial Zoom point of the camera
        target = ax.c2p(35, 2)
        self.wait(2)

        ### Zooming of the camera starts here

        self.play(self.camera.frame.animate.move_to(target).scale(0.5),run_time=5,rate_func=smooth)
        self.wait(2)

        self.camera.frame.add_updater(
            lambda m, dt:m.shift(RIGHT*0.05*dt),
        )

        self.wait(1)

        all_braces = VGroup()
        all_braces_text = VGroup()

        #### This portion of code is meant to create braces
        for i in range(40,90,2):
            point_one = dots[i].get_center()
            point_two = dots[i+1].get_center()
            
            brace = BraceBetweenPoints(point_one,point_two,RIGHT,stroke_width=0.05,sharpness=5).set_color(C_RED)
            brace_text = MathTex(r"\delta").scale(0.5).next_to(brace,RIGHT,buff=0.2).set_color(C_RED)

            all_braces.add(brace)
            all_braces_text.add(brace_text)

        for i in range(25):
            if i == 0:
                self.play(Create(VGroup(all_braces[i],all_braces_text[i])))
                
                self.wait(1)
            else:
                self.play(ReplacementTransform(all_braces[i-1],all_braces[i]),
                        ReplacementTransform(all_braces_text[i-1],all_braces_text[i]))
                self.wait(1)

        self.play(FadeOut(VGroup(all_braces[24],all_braces_text[24])))
    
        ### Code for Epsilon stripe.
        epsilon = ValueTracker(0.4)
        L = 2  # Limit value

        upper_line = always_redraw(lambda: DashedLine(
            start=ax.c2p(0, L + epsilon.get_value()),
            end=ax.c2p(100, L + epsilon.get_value()),
            color=C_RED,
            stroke_width=get_stroke_width()
        ))

        lower_line = always_redraw(lambda: DashedLine(
            start=ax.c2p(0, L - epsilon.get_value()),
            end=ax.c2p(100, L - epsilon.get_value()),
            color=C_RED,
            stroke_width=get_stroke_width()
        ))
        
        region = always_redraw(lambda: Polygon(
            ax.c2p(0, L + epsilon.get_value()),
            ax.c2p(100, L + epsilon.get_value()),
            ax.c2p(100, L - epsilon.get_value()),
            ax.c2p(0, L - epsilon.get_value()),
            stroke_width=0,
            fill_color=C_RED,
            fill_opacity=0.2
        ))
       
        self.play(Create(upper_line),Create(lower_line),rate_func=smooth)
        self.play(FadeIn(region),rate_func=smooth)
        self.wait(2)
        self.play(epsilon.animate.set_value(0.2),run_time=4)

        self.camera.frame.clear_updaters()
        final_text = MathTex(r"\text{Distance shrinks} \to \text{ Stability achieved.}").scale(0.3).move_to(self.camera.frame.get_center()+UP)

        self.play(Write(final_text))
        self.wait(2)






