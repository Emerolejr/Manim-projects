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

# --- FONT CONFIGURATION ---
try:
    my_template = TexTemplate(tex_compiler="xelatex", output_format=".xdv")
    my_template.add_to_preamble(r"""
    \usepackage{fontspec}
    \usepackage{unicode-math}
    \setsansfont{Inter}[
      Scale=MatchLowercase,
      UprightFont=*-Medium,
      BoldFont=*-SemiBold,
      ItalicFont=*-MediumItalic,
      BoldItalicFont=*-SemiBoldItalic
    ]
    \setmainfont{Inter}[Scale=MatchLowercase]
    \setmathfont{STIX Math}[Scale=MatchLowercase, math-style=TeX, bold-style=ISO]
    """)
except:
    # Fallback if xelatex not set up
    my_template = TexTemplate()


class BeamerBlock(VGroup):
    def __init__(self, title, width=13, **kwargs):
        super().__init__(**kwargs)
        # Header bar with bright blue background
        self.header = Rectangle(width=width, height=0.5, fill_color=C_BRIGHT_BLUE, fill_opacity=1, stroke_width=0)
        
        # Title text, left-aligned with padding
        self.title = Tex(r"\textbf{" + title + "}", color=C_BLACK, font_size=52, tex_template=my_template)
        self.title.align_to(self.header, LEFT).shift(RIGHT * 0.2)
        self.title.set_y(self.header.get_y()) # Center vertically in header
        
        # Grey body panel
        self.body = Rectangle(width=width, height=6.8, fill_color=C_GRAY, fill_opacity=0.5, stroke_width=0)
        self.body.next_to(self.header, DOWN, buff=0)
        
        self.add(self.body, self.header, self.title)


class Epsilon_n_Intro(Scene):
    def construct(self):
        # Create Beamer Block covering most of screen
        block = BeamerBlock("Limit of a Sequence", width=13.5)
        block.move_to(ORIGIN)
        
        self.play(FadeIn(block))
        self.wait(0.5)
        
        # Add Formal Definition at the top
        def_text = Tex(
            r"$\forall$ ", r"$\epsilon$", r"$>0$", 
            r"$ \exists$ ", r"$N$", r"$\in \mathbb{N}$", 
            r"$ : \forall n > $", r"$N$", 
            r"$\implies |a_n - L| < $", r"$\epsilon$",
            font_size=42, tex_template=my_template
        )

        def_text.set_color_by_tex(r"$\epsilon$", C_BRIGHT_BLUE)
        def_text.set_color_by_tex(r"$N$", C_GREEN)
        def_text.next_to(block.header, DOWN, buff=0.3)
        
        self.play(Write(def_text), run_time=2)
        self.wait(0.5)
        
        # Two Column Layout
        # Left Column: Definition & Claim
        # Right Column: Derivation
        
        # LEFT SIDE
        l_col = VGroup()
        
        formula = MathTex(r"a_n = \frac{(-1)^n}{n}", font_size=44, tex_template=my_template)
        
        # Horizontal substitutions
        final_1 = MathTex(r"a_1 = -1", font_size=36, tex_template=my_template)
        final_2 = MathTex(r"a_2 = \frac{1}{2}", font_size=36, tex_template=my_template)
        final_3 = MathTex(r"a_3 = -\frac{1}{3}", font_size=36, tex_template=my_template)
        final_dots = MathTex(r"\dots", font_size=36, tex_template=my_template)
        
        # Arrange them horizontally
        subs_group = VGroup(final_1, final_2, final_3, final_dots).arrange(RIGHT, buff=0.5)
        
        claim_label = Tex(r"\textbf{Claim:}", color=C_MAGENTA, font_size=38, tex_template=my_template)
        claim_text = Tex(r"The sequence converges to 0.", font_size=38, tex_template=my_template)
        claim_group = VGroup(claim_label, claim_text).arrange(RIGHT, buff=0.2)
        
        l_col.add(formula, subs_group, claim_group)
        l_col.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        l_col.shift(UP * 0.5)
        
        # RIGHT SIDE
        r_col = VGroup()
        
        # Goal statement with color-coded variables
        goal_text = Tex(
            r"We want to determine ", r"$N$", r" with respect to ", r"$\epsilon$", r":", 
            font_size=36, tex_template=my_template
        )
        goal_text.set_color_by_tex(r"$N$", C_GREEN)
        goal_text.set_color_by_tex(r"$\epsilon$", C_BRIGHT_BLUE)
        
        step1 = MathTex(r"|a_n - 0| < \epsilon", font_size=38, tex_template=my_template)
        step2 = MathTex(r"\left| \frac{(-1)^n}{n} \right| < \epsilon", font_size=38, tex_template=my_template)
        step3 = MathTex(r"\frac{1}{n} < \epsilon", font_size=38, tex_template=my_template)
        step4 = MathTex(r"n > \frac{1}{\epsilon}", font_size=38, color=C_GREEN, tex_template=my_template)
        
        r_col.add(goal_text, step1, step2, step3, step4)
        r_col.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        # Arrange columns side by side
        content_group = VGroup(l_col, r_col).arrange(RIGHT, buff=1.0)
        content_group.next_to(def_text, DOWN, buff=0.5)
        
        # Bottom Text - Full Width
        bottom_text = Tex(
            r"For ", r"$\epsilon$", r" arbitrarily small, we have for ", r"$N$", r" large enough,", r"",
            r"that ", r"$a_n$", r" is arbitrarily close to ", r"$L=0$", r".",
            font_size=30, tex_template=my_template
        )
        bottom_text.set_color_by_tex(r"$\epsilon$", C_BRIGHT_BLUE)
        bottom_text.set_color_by_tex(r"$N$", C_GREEN)
        
        bottom_text.next_to(content_group, DOWN, buff=0.2)
        
        # Animation sequence
        self.play(Write(formula), run_time=1.5)
        self.wait(1)
        
        # Animate substitutions: show calculation then simplify
        calc_1 = MathTex(r"a_1 = \frac{(-1)^1}{1}", font_size=36, tex_template=my_template).move_to(final_1)
        self.play(Write(calc_1), run_time=1.5)
        self.wait(2.0)
        self.play(Transform(calc_1, final_1))
        self.wait(0.5)

        calc_2 = MathTex(r"a_2 = \frac{(-1)^2}{2}", font_size=36, tex_template=my_template).move_to(final_2)
        self.play(Write(calc_2))
        self.wait(2.0)
        self.play(Transform(calc_2, final_2))
        self.wait(0.5)

        calc_3 = MathTex(r"a_3 = \frac{(-1)^3}{3}", font_size=36, tex_template=my_template).move_to(final_3)
        self.play(Write(calc_3))
        self.wait(2.0)
        self.play(Transform(calc_3, final_3))
        self.wait(0.5)

        self.play(Write(final_dots), run_time=1.5)
        self.wait(0.5)
        
        self.play(Write(claim_group), run_time=1.5)
        self.wait(1)
        
        self.play(Write(bottom_text), run_time=2)
        self.wait(2)
        
        self.play(Write(goal_text), run_time=1.5)
        self.wait(0.5)
        
        self.play(FadeIn(step1, shift=DOWN))
        self.wait(0.5)
        self.play(ReplacementTransform(step1.copy(), step2))
        self.wait(0.5)
        self.play(ReplacementTransform(step2.copy(), step3))
        self.wait(0.5)
        self.play(ReplacementTransform(step3.copy(), step4))
        self.wait(1.5)

        # Extract result and transition to graph scene
        result_label = MathTex(r"N > \frac{1}{\epsilon}", color=C_GREEN, font_size=48, tex_template=my_template)
        result_label.move_to(step4)
        
        target_pos = [6, 3, 0] 
        
        self.play(
            FadeOut(block), FadeOut(formula), FadeOut(claim_group), FadeOut(bottom_text), FadeOut(def_text),
            FadeOut(calc_1), FadeOut(calc_2), FadeOut(calc_3), FadeOut(final_dots),
            FadeOut(goal_text), FadeOut(step1), FadeOut(step2), FadeOut(step3),
            ReplacementTransform(step4, result_label)
        )

        self.play(result_label.animate.move_to(target_pos).set_color(C_GREEN))
        self.wait(0.5)


class Epsilon_n_Graph(MovingCameraScene):
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
            x_range=[0, 30, 1],
            y_range=[-1.2, 1.2, 0.5],
            x_length=12,
            y_length=6,
            axis_config={"include_tip": True, "numbers_to_exclude": [], "tick_size": 0.05}
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
        
        # Formula display at top of screen
        graph_formula_template = MathTex(r"a_n = \frac{(-1)^n}{n}", font_size=48, tex_template=my_template)
        graph_formula_template.to_edge(UP, buff=0.5).shift(DOWN * 0.5)
        
        self.play(Write(graph_formula_template))
        self.wait(0.5)

        # Sequence dots
        dots = VGroup()
        
        def seq_func(n):
            """Alternating sequence: a_n = (-1)^n / n"""
            if n == 0: return 0 
            return ((-1)**n) / n
            
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
            
            # Build substitution strings: a_n -> calculation -> simplified value
            val_text_str = r"a_{" + str(n) + r"} = \frac{(-1)^{" + str(n) + r"}}{" + str(n) + r"}"
            final_val_str = r"a_{" + str(n) + r"} = " + (r"-" if n%2!=0 else "") + (r"1" if n==1 else r"\frac{1}{" + str(n) + r"}")
            
            step_calc = MathTex(val_text_str, font_size=48, tex_template=my_template).move_to(graph_formula_template)
            step_final = MathTex(final_val_str, font_size=48, tex_template=my_template).move_to(graph_formula_template)
            
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
        for n in range(10, 29):
            val = seq_func(n)
            dot = Dot(ax.c2p(n, val), color=C_BLUE, radius=0.06)
            dot.y_val = val
            dots.add(dot)
            self.add(dot)
            self.wait(0.5)
            
        self.play(FadeOut(graph_formula_template))
        
        # Display formal definition with color-coded epsilon and N
        graph_def_text = Tex(
            r"$\forall$", r"$\epsilon$", r"$> 0$", 
            r"$\exists$", r"$N$", r"$\in \mathbb{N}$", 
            r"$ : \forall n > $", r"$N$", 
            r"$\implies |a_n - L| < $", r"$\epsilon$",
            font_size=56
        )

        graph_def_text.set_color_by_tex(r"$\epsilon$", C_BRIGHT_BLUE)
        graph_def_text.set_color_by_tex(r"$N$", C_GREEN)
        graph_def_text.to_edge(UP, buff=0.8)
        
        # Animate definition parts sequentially with highlights
        self.play(Write(graph_def_text[0:3]), run_time=1.5)
        self.play(Indicate(graph_def_text[0:3], color=C_BRIGHT_BLUE))
        self.wait(0.5)
        

        self.play(Write(graph_def_text[3:6]), run_time=1.5)
        self.play(Indicate(graph_def_text[3:6], color=C_GREEN))
        self.wait(0.5)
        
        self.play(Write(graph_def_text[6:8]), run_time=1.5)
        self.play(Indicate(graph_def_text[6:8], color=C_GREEN))
        self.wait(0.5)
        
        self.play(Write(graph_def_text[8:10]), run_time=2.0)
        self.play(Indicate(graph_def_text[8:10], color=C_BRIGHT_BLUE))
        self.wait(1)
        
        # Epsilon band visualization
        epsilon = ValueTracker(0.6)
        L = 0  # Limit value
        
        # Highlight dots outside epsilon band
        def color_updater_dots(mob):
            curr_eps = epsilon.get_value()
            for d in mob:
                if hasattr(d, 'y_val'):
                    if abs(d.y_val) >= curr_eps - 1e-9:
                        # Outside band: highlight with glow
                        d.set_color(C_PURPLE)
                        d.set_stroke(color=C_NEON_PURPLE, width=6, opacity=0.8)
                    else:
                        # Inside band: normal appearance
                        d.set_color(C_BLUE)
                        d.set_stroke(width=0, opacity=0)
        
        dots.add_updater(color_updater_dots)

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
        
        label_eps = always_redraw(lambda: 
            MathTex(r"\epsilon = " + f"{epsilon.get_value():.2f}", color=C_RED, font_size=get_font_size(), tex_template=my_template)
            .next_to(upper_line, UP, buff=0.1 * get_scale())
            .set_x(ax.c2p(int(1.0/epsilon.get_value()),0)[0] + 1)
        )

        self.play(Create(upper_line), Create(lower_line), FadeIn(region), Write(label_eps), run_time=1.5)
        
        # Vertical line marking N = 1/epsilon
        v_line = always_redraw(lambda: DashedLine(
            start=ax.c2p(int(4/epsilon.get_value()**2), -1.2),
            end=ax.c2p(int(4/epsilon.get_value()**2), 1.2),
            color=C_GREEN,
            stroke_width=get_stroke_width()
        ))
        
        label_N = always_redraw(lambda: 
            MathTex(f"N = {int(1/epsilon.get_value())}", color=C_GREEN, font_size=get_font_size(), tex_template=my_template)
            .next_to(v_line, DOWN, buff=0.1 * get_scale())
            .shift(RIGHT * 0.8 * get_scale())
            .set_y(max(
                 ax.c2p(int(1/epsilon.get_value()), -1.2)[1], 
                 self.camera.frame.get_bottom()[1] + 0.5 * get_scale() 
            ))
        )
        
        self.play(Create(v_line), Write(label_N))
        self.wait()
        
        # Zoom animation: track N as epsilon decreases
        target_epsilon = 0.065  # Target: N ≈ 15
        
        def update_cam(mob):
            """Keep camera centered on current N value while zooming."""
            cont_N = 1.0 / epsilon.get_value()
            target_x = ax.c2p(cont_N, 0)[0]
            new_height = max(min(15.0 * epsilon.get_value(), 9.0), 2.5)
            mob.set_height(new_height)
            width = new_height * (16/9)
            mob.move_to([target_x + 0.15 * width, 0, 0])

        # Initial camera position for smooth transition
        start_height = 9.0
        start_N_pos = ax.c2p(1.0/0.6, 0)[0]
        start_width = start_height * (16/9)
        start_cam_x = start_N_pos + 0.15 * start_width
        
        self.play(
            self.camera.frame.animate.set_height(start_height).move_to([start_cam_x, 0, 0]),
            run_time=2
        )

        self.play(
            epsilon.animate.set_value(target_epsilon),
            UpdateFromFunc(self.camera.frame, update_cam),
            run_time=40, 
            rate_func=rate_functions.ease_out_cubic 
        )

        self.wait(2)
        
        self.play(Restore(self.camera.frame), run_time=3)
        
        # Final conclusion text
        conclusion = Tex(
            r"As $\epsilon$ gets smaller, $N(\epsilon) = 1/\epsilon$ gets larger.", 
            color=C_GREEN, 
            font_size=40, 
            tex_template=my_template
        )
        
        conclusion.to_corner(DR)
        self.play(Write(conclusion), run_time=3)
        self.wait(4)


class Epsilon_n_Divergence_example(Scene):
    def construct(self):
        ##Beamer block.
        block = Rectangle(width=13.5, height=0.5, fill_color=C_BRIGHT_BLUE, fill_opacity=1, stroke_width=0).to_corner(UP,buff=0)
        title_text = Text("Limit of a Sequence : divergence").next_to(block.get_left(),RIGHT).set_color(C_BLACK)
        self.add(block)
        self.add(title_text)

        def_sequence_initial = MathTex(
            r"\text{for divergence: }"
            r"\exists \epsilon > 0 \text{ such that } ",
            r"\forall N \in \mathbb{N} ",
            r"\exists n > N \text{ where } ",
            r"|a_n - L| \ge \epsilon",
            font_size=40
        ).next_to(block,DOWN)

        def_sequence_final = MathTex(
            r"\exists \epsilon > 0 \text{ such that } ",
            r"\forall N \in \mathbb{N} ",
            r"\exists n > N \text{ where } ",
            r"|a_n - L| \ge \epsilon",
            font_size=40
        ).next_to(block,DOWN)


        step_1 = MathTex(
            r"a_n = (-1)^n\left(1 + \frac{2}{n}\right)",
            font_size=44
        )

        step_2 = MathTex(
            r"\text{Assume } \lim_{n\to\infty} a_n = 0",
            font_size=42
        )

        step_3 = MathTex(
            r"\forall \epsilon > 0,\ \exists N \in \mathbb{N}",
            r"\text{ such that } |a_n| < \epsilon",
            r"\ \forall n \ge N",
            font_size=40
        )

        step_4 = MathTex(
            r"|a_n| = \left|(-1)^n\left(1 + \frac{2}{n}\right)\right|",
            font_size=42
        )

        step_5 = MathTex(
            r"|a_n| = 1 + \frac{2}{n}",
            font_size=42
        )

        step_6 = MathTex(
            r"1 + \frac{2}{n} > 1 \quad \forall n \in \mathbb{N}",
            font_size=42
        )

        step_7 = MathTex(
            r"\text{Choose } \epsilon = \frac{1}{2}",
            font_size=42
        )

        step_8 = MathTex(
            r"|a_n| \ge 1 > \frac{1}{2}",
            font_size=42
        )

        step_9 = MathTex(
            r"\exists \epsilon > 0 \text{ such that }",
            r"\forall N \in \mathbb{N},\ \exists n \ge N:",
            r"|a_n| \ge \epsilon",
            font_size=40
        )

        step_10 = MathTex(
            r"\therefore \lim_{n\to\infty} a_n \neq 0",
            font_size=44
        )

        #Definition of the sequence

        ## Sides of solutions
        left_side = VGroup(step_1,step_2,step_3,step_4,step_5).scale(0.8).arrange(DOWN,buff=0.5).align_on_border(LEFT)
        right_side = VGroup(step_6,step_7,step_8,step_9,step_10).scale(0.8).arrange(DOWN,buff=0.5).align_on_border(LEFT)

        all_sides = VGroup(left_side,right_side).arrange(RIGHT).next_to(def_sequence_initial,DOWN,buff=1)
       
        self.play(Write(def_sequence_initial))
        self.wait(5)
        self.play(ReplacementTransform(def_sequence_initial,def_sequence_final))

        #### Animations of sequence
        for i in left_side:
            self.play(Write(i))
            self.wait(2)

        for i in right_side:
            self.play(Write(i))
            self.wait(2)

        self.wait(5)

        final_text = Text("Showing this graphically:")
        self.play(FadeOut(*self.mobjects))
        self.wait(2)
        self.play(Write(final_text))
        self.wait(5)
        


class Epsilon_n_divergence_graph(MovingCameraScene):
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
            x_range=[0, 41, 1],
            y_range=[-3.5, 2.5, 0.5],
            x_length=12,
            y_length=6,
            axis_config={"include_tip": True, "numbers_to_exclude": [], "tick_size": 0.05}
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

        # Formula display at top of screen
        graph_formula_template = MathTex(
            r"a_n = (-1)^n\left(1 + \frac{2}{n}\right)",
            font_size=48
        )
        graph_formula_template.to_edge(UP, buff=0.5).shift(DOWN * 0.5)

        self.play(Write(graph_formula_template))
        self.wait(0.5)

        # Sequence dots
        dots = VGroup()

        def seq_func(n):
            """Alternating sequence: a_n = (-1)^n (1 + 2/n)"""
            return ((-1)**n) * (1 + 2/n)
            
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
        for n in range(10, 41):
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
            color=C_RED,
            stroke_width=get_stroke_width()
        )

        lower_line =  DashedLine(
            start=ax.c2p(0, L - epsilon.get_value()),
            end=ax.c2p(200, L - epsilon.get_value()),
            color=C_RED,
            stroke_width=get_stroke_width()
        )
        
        region = Polygon(
            ax.c2p(0, L + epsilon.get_value()),
            ax.c2p(200, L + epsilon.get_value()),
            ax.c2p(200, L - epsilon.get_value()),
            ax.c2p(0, L - epsilon.get_value()),
            stroke_width=0,
            fill_color=C_RED,
            fill_opacity=0.2
        )
        
        label_eps = MathTex(r"\epsilon = " + f"{epsilon.get_value():.2f}", color=C_RED, font_size=get_font_size()).next_to(upper_line, UP, buff=0.1 * get_scale()).set_x(ax.c2p(int(1.0/epsilon.get_value()),0)[0] + 1)

        # Vertical line marking N = 1/epsilon
        v_line =  DashedLine(
            start=ax.c2p(2, -2),
            end=ax.c2p(2, 2),
            color=C_GREEN,
            stroke_width=get_stroke_width()
        )
        
        label_N = always_redraw(lambda: 
            MathTex(f"N = {ax.p2c(v_line.get_start())[0]:.1f}", color=C_GREEN, font_size=get_font_size())
            .next_to(v_line, DOWN, buff=0.1 * get_scale())
            .shift(RIGHT * 0.8 * get_scale())
        )

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
            r"For example, let's pick $\varepsilon = 0.5$.",
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


        ### Text animations for Graph explanation
        self.play(Write(graph_text_1),rate_func=smooth)

        self.wait(2)
        self.play(ReplacementTransform(graph_text_1,graph_text_2),rate_func=smooth)
        self.wait(2)
        self.play(ReplacementTransform(graph_text_2,graph_text_3),rate_func=smooth)
        self.wait(2)

        self.play(ReplacementTransform(graph_text_3,graph_text_4),rate_func=smooth)
        self.play(Create(upper_line), Create(lower_line), FadeIn(region), Write(label_eps), run_time=1.5,rate_func=smooth)
        
        self.play(Create(v_line), Write(label_N),rate_func=smooth)

        self.play(ReplacementTransform(graph_text_4,graph_text_5),rate_func=smooth)
        
        self.play(v_line.animate.move_to(ax.c2p(30,0)),rate_func=linear,run_time=10)
        self.wait(2)
        self.play(ReplacementTransform(graph_text_5,graph_text_6))
        self.play(v_line.animate.move_to(ax.c2p(10,0)),rate_func=smooth)
        self.wait(5)
