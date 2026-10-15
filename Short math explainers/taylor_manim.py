"""
taylor_series.py

This script uses the Manim library to create animations that visualize the Taylor series.
It contains multiple classes, each serving a specific purpose related to the Taylor series animations for the YouTube channel "Math Simplified."

Classes:
- CosExpansion: Visualizes the Taylor series expansion of cos(x) around x = 0.
- CosExpansion2: Visualizes the Taylor series expansion of cos(x) around a different point of expansion.
- SinExpansion: Visualizes the Taylor series expansion of sin(x).
- eExpansion: Visualizes the Taylor series expansion of e^x.

Each class uses Manim to construct animations demonstrating various aspects of Taylor series video.

Functions:
- dcos(n, a): Defines the derivative of cos(x) used in the Taylor series expansions.
- maclaurine_exp(x): Computes the Maclaurin series expansion of cos(x) around x = 0.
- taylor_exp(x): Computes the Taylor series expansion of cos(x) around x = π.


"""

from manim import *
import numpy as np
import math as m

# Function definitions (dcos, maclaurine_exp, taylor_exp) are defined here.

def dcos(n,a):
   if(n%4==1):
      return -np.sin(a)
   elif(n%4==2):
      return -np.cos(a)
   elif(n%4==3):
      return np.sin(a)
   else:
      return np.cos(a)

epsilon = 0.001

def maclaurine_exp(x):
   sum = 0
   i=0
   while(abs(sum-np.cos(4))>epsilon):
    sum += dcos(i,0)*x**i/m.factorial(i)
    i+=1
   return sum,i

def taylor_exp(x):
 sum = 0
 i=0
 while(abs(sum-np.cos(4))>epsilon):
   sum += dcos(i,np.pi)*(x-np.pi)**i/m.factorial(i)
   i+=1
 return sum,i


class TaylorSeriesFormula(Scene):
    def construct(self):
        taylor_series = MathTex(
            "f(x) = ", "\\sum_{n=0}^{\infty}", "\\frac{f^{(n)}(a)}{n!}(x - a)^n"
        ).scale(1.5)
        self.play(Write(taylor_series))
        self.wait()
        


class CosExpansion(Scene):
    def construct(self):
        # Step-by-step derivative calculations (no boxes)

        deriv_steps = [
            VGroup(
                MathTex(r"f(x) = \cos(x)", font_size=40, stroke_width=1),
                MathTex(r"f(0) = \cos(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Value at origin: starts at 1", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            VGroup(
                MathTex(r"f'(x) = -\sin(x)", font_size=40, stroke_width=1),
                MathTex(r"f'(0) = -\sin(0) = 0", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Slope vanishes: flat at origin", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f''(x) = -\cos(x)", font_size=40, stroke_width=1),
                MathTex(r"f''(0) = -\cos(0) = -1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Concavity: curves downward", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f'''(x) = \sin(x)", font_size=40, stroke_width=1),
                MathTex(r"f'''(0) = \sin(0) = 0", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ No contribution (coefficient = 0)", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f^{(4)}(x) = \cos(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(4)}(0) = \cos(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Pattern repeats: adds $+\frac{x^4}{4!}$", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f^{(5)}(x) = -\sin(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(5)}(0) = -\sin(0) = 0", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ No contribution (coefficient = 0)", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            VGroup(
                MathTex(r"f^{(6)}(x) = -\cos(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(6)}(0) = -\cos(0) = -1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Adds $-\frac{x^6}{6!}$: refines the curve", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            VGroup(
                MathTex(r"f^{(7)}(x) = \sin(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(7)}(0) = \sin(0) = 0", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ No contribution (coefficient = 0)", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
        ]

        ax = Axes(
            x_range=(-6, 6),
            y_range=(-1.5, 1.5),
            x_length=9,
            y_length=4,
            axis_config={
                "include_ticks":False,
                "include_numbers":False,
                "tip_shape":StealthTip
            }
        ).shift(RIGHT)

        labels = ax.get_axis_labels(x_label="x", y_label=MathTex(r"f(x)=\cos(x)").scale(0.8))
        graph1 = ax.plot(lambda x: m.cos(x), color=PINK)

        x_range = [6, 2.5, 3.5, 3.5, 4.5, 5.5, 6, 6, 6, 6]
        
        graphs = [
            ax.plot(lambda x, n=n: sum(
                (-1)**k * x**(2*k) / m.factorial(2*k) for k in range(n+1)
            ), color="#00E540", stroke_width=5, x_range=[-x_range[n],x_range[n]]) for n in range(10)
        ]

        tex = MathTex(
            "f(x) = ", "1", " - \\frac{x^2}{2!}", " + \\frac{x^4}{4!}",
            " - \\frac{x^6}{6!}", " + \\frac{x^8}{8!} ", " - \\frac{x^{10}}{10!} ",
            " + \\frac{x^{12}}{12!} ", " - \\frac{x^{14}}{14!} ", "+ ............\\infty",
            color=BLUE
        ).scale(0.9)
        
        tex.next_to(ax, DOWN, buff=0.2).to_edge(LEFT, buff=0.3)

        # Taylor formula: general form with x_0
        taylor_general = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{n}",
            r"\frac{f^{(i)}(x_0)}{i!}", r"(x - x_0)^i",
            font_size=38, stroke_width=1
        ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        x0_label = MathTex(r"x_0 = 0", font_size=38, color="#00E540", stroke_width=1)
        x0_label.next_to(taylor_general, RIGHT, buff=0.5)

        # Simplified form (x_0 = 0) — base version with n
        def make_taylor_n(n_val):
            return MathTex(
                r"f(x)", r"=", rf"\sum_{{i=0}}^{{{n_val}}}",
                r"\frac{f^{(i)}(0)}{i!}", r"\cdot x^i",
                font_size=38, stroke_width=1
            ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        # Create formula for each n value (0 through 7) plus infinity
        taylor_n = [make_taylor_n(n) for n in range(8)]
        taylor_inf = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{\infty}",
            r"\frac{f^{(i)}(0)}{i!}", r"\cdot x^i",
            font_size=38, stroke_width=1
        ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        # Position derivative steps at the top of the screen (separate from the sum)
        for step in deriv_steps:
            step.to_edge(UP, buff=0.2).to_edge(LEFT, buff=0.3)

        recs = [
            SurroundingRectangle(VGroup(tex[0], tex[i]), color=WHITE) for i in range(1, 9)
        ]

        # === ANIMATION START ===

        # 1. Show the general Taylor formula
        self.play(Write(taylor_general))
        self.wait(2)

        # 2. Show x_0 = 0
        self.play(Write(x0_label))
        self.wait(2)

        # 3. Transform to simplified form with n=0
        self.play(
            ReplacementTransform(taylor_general, taylor_n[0]),
            FadeOut(x0_label)
        )
        self.wait(2)

        # 4. Create graph
        self.play(Create(ax), Create(graph1), Create(labels))

        # Step 0: f(0)=1 → plot constant + first term, n=0
        self.play(FadeIn(deriv_steps[0]))
        self.wait(2)
        self.play(Create(tex[0]))
        self.play(Create(VGroup(graphs[0], tex[1])))
        self.play(Create(recs[0]))
        self.wait(3)

        # Step 1: f'(0)=0 → n=1
        self.play(FadeOut(deriv_steps[0]))
        self.play(FadeIn(deriv_steps[1]), Transform(taylor_n[0], taylor_n[1]))
        self.wait(4)

        # Step 2: f''(0)=-1 → n=2, add term
        self.play(FadeOut(deriv_steps[1]))
        self.play(FadeIn(deriv_steps[2]), Transform(taylor_n[0], taylor_n[2]))
        self.wait(2)
        self.play(
            ReplacementTransform(graphs[0], graphs[1]),
            Write(tex[2]),
            Transform(recs[0], recs[1])
        )
        self.wait(3)

        # Step 3: f'''(0)=0 → n=3
        self.play(FadeOut(deriv_steps[2]))
        self.play(FadeIn(deriv_steps[3]), Transform(taylor_n[0], taylor_n[3]))
        self.wait(4)

        # Steps 4–7: higher derivatives
        for i, step_idx in enumerate([4, 5, 6, 7]):
            self.play(FadeOut(deriv_steps[step_idx - 1]))
            self.play(
                FadeIn(deriv_steps[step_idx]),
                Transform(taylor_n[0], taylor_n[step_idx])
            )
            self.wait(2)
            graph_idx = 2 + (i // 2)
            tex_idx = 3 + (i // 2)
            if step_idx % 2 == 0:
                self.play(
                    ReplacementTransform(graphs[graph_idx - 1], graphs[graph_idx]),
                    Write(tex[tex_idx]),
                    Transform(recs[0], recs[tex_idx - 1])
                )
                self.wait(3)
            else:
                self.wait(2)

        # Fade out last derivative, switch to n=∞, animate remaining terms
        self.play(FadeOut(deriv_steps[7]), Transform(taylor_n[0], taylor_inf))
        for i in range(4, 8):
            self.play(
                ReplacementTransform(graphs[i-1], graphs[i]),
                Write(tex[i+1]),
                Transform(recs[0], recs[i])
            )
            self.wait(2)

        self.play(FadeOut(recs[0]))
        self.play(Write(tex[9]))
        self.wait(5)


class CosExpansion2(Scene):
    def construct(self):
        a_val = 2  # expansion point

        # Step-by-step derivative calculations (same template as CosExpansion)

        deriv_steps = [
            VGroup(
                MathTex(r"f(x) = \cos(x)", font_size=40, stroke_width=1),
                MathTex(rf"f({a_val}) = \cos({a_val}) = {round(np.cos(a_val), 4)}", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Value at expansion point", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            VGroup(
                MathTex(r"f'(x) = -\sin(x)", font_size=40, stroke_width=1),
                MathTex(rf"f'({a_val}) = -\sin({a_val}) = {round(dcos(1, a_val), 4)}", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Slope at expansion point", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            VGroup(
                MathTex(r"f''(x) = -\cos(x)", font_size=40, stroke_width=1),
                MathTex(rf"f''({a_val}) = -\cos({a_val}) = {round(dcos(2, a_val), 4)}", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Concavity at expansion point", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            VGroup(
                MathTex(r"f'''(x) = \sin(x)", font_size=40, stroke_width=1),
                MathTex(rf"f'''({a_val}) = \sin({a_val}) = {round(dcos(3, a_val), 4)}", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Third-order correction", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            VGroup(
                MathTex(r"f^{(4)}(x) = \cos(x)", font_size=40, stroke_width=1),
                MathTex(rf"f^{{(4)}}({a_val}) = \cos({a_val}) = {round(dcos(4, a_val), 4)}", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Pattern repeats from here", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            VGroup(
                MathTex(r"f^{(5)}(x) = -\sin(x)", font_size=40, stroke_width=1),
                MathTex(rf"f^{{(5)}}({a_val}) = -\sin({a_val}) = {round(dcos(5, a_val), 4)}", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Fifth-order correction", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            VGroup(
                MathTex(r"f^{(6)}(x) = -\cos(x)", font_size=40, stroke_width=1),
                MathTex(rf"f^{{(6)}}({a_val}) = -\cos({a_val}) = {round(dcos(6, a_val), 4)}", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Refines the curve further", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
            VGroup(
                MathTex(r"f^{(7)}(x) = \sin(x)", font_size=40, stroke_width=1),
                MathTex(rf"f^{{(7)}}({a_val}) = \sin({a_val}) = {round(dcos(7, a_val), 4)}", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Seventh-order correction", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
        ]

        ax = Axes(
            x_range=[-6, 6],
            y_range=[-1.5, 1.5],
            x_length=9,
            y_length=4,
            axis_config={
                "include_ticks":False,
                "include_numbers":False,
                "tip_shape":StealthTip
            }
        ).shift(RIGHT)

        labels = ax.get_axis_labels(x_label="x", y_label=MathTex(r"f(x)=\cos(x)").scale(0.8))
        graph1 = ax.plot(lambda x: m.cos(x), color=PINK)

        # Taylor approximation graphs centered at a_val
        x_range_lower = [-6,0,0,-1.5,-1,-2,-1.7,-2.5,-2,-4]
        x_range_higher = [6,3,4,4.5,5,5,5.5,5.5,6,6]

        graphs = [
            ax.plot(lambda x, n=n: sum(
                dcos(k, a_val) * (x - a_val)**k / m.factorial(k) for k in range(n+1)
            ), color="#00E540", stroke_width=5,x_range=[x_range_lower[n] ,x_range_higher[n]]) for n in range(10)
        ]


        # Series terms displayed at the bottom

        tex = MathTex(
            "f(x) = ", f"f({a_val})",
            f" + f'({a_val})\\frac{{(x-{a_val})^1}}{{1!}}",
            f" + f''({a_val})\\frac{{(x-{a_val})^2}}{{2!}}",
            f" + f'''({a_val})\\frac{{(x-{a_val})^3}}{{3!}}",
            f" + f''''({a_val})\\frac{{(x-{a_val})^4}}{{4!}}",
            f" + f^{{(5)}}({a_val})\\frac{{(x-{a_val})^5}}{{5!}}",
            f" + f^{{(6)}}({a_val})\\frac{{(x-{a_val})^6}}{{6!}}",
            f" + f^{{(7)}}({a_val})\\frac{{(x-{a_val})^7}}{{7!}}",
            "+ ............\\infty",
            color=BLUE
        ).scale(0.55)
        tex.next_to(ax, DOWN, buff=0.2).to_edge(LEFT, buff=0.3)

        # Taylor formula: general form with a
        taylor_general = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{n}",
            r"\frac{f^{(i)}(a)}{i!}", r"(x - a)^i",
            font_size=38, stroke_width=1
        ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        a_label = MathTex(rf"a = {a_val}", font_size=38, color="#00E540", stroke_width=1)
        a_label.next_to(taylor_general, RIGHT, buff=0.5)

        # Simplified form with a substituted — base version with n
        def make_taylor_n(n_val):
            return MathTex(
                r"f(x)", r"=", rf"\sum_{{i=0}}^{{{n_val}}}",
                rf"\frac{{f^{{(i)}}({a_val})}}{{i!}}", rf"\cdot (x - {a_val})^i",
                font_size=38, stroke_width=1
            ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        # Create formula for each n value (0 through 7) plus infinity
        taylor_n = [make_taylor_n(n) for n in range(8)]
        taylor_inf = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{\infty}",
            rf"\frac{{f^{{(i)}}({a_val})}}{{i!}}", rf"\cdot (x - {a_val})^i",
            font_size=38, stroke_width=1
        ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        # Position derivative steps at the top of the screen
        for step in deriv_steps:
            step.to_edge(UP, buff=0.2).to_edge(LEFT, buff=0.3)

        recs = [
            SurroundingRectangle(VGroup(tex[0], tex[i]), color=WHITE) for i in range(1, 9)
        ]

        # === ANIMATION START ===

        # 1. Show the general Taylor formula
        self.play(Write(taylor_general))
        self.wait(2)

        # 2. Show a = a_val
        self.play(Write(a_label))
        self.wait(2)

        # 3. Transform to simplified form with n=0
        self.play(
            ReplacementTransform(taylor_general, taylor_n[0]),
            FadeOut(a_label)
        )
        self.wait(2)

        # 4. Create graph
        self.play(Create(ax), Create(graph1), Create(labels))

        # Step 0: f(a)  → plot constant + first term, n=0
        self.play(FadeIn(deriv_steps[0]))
        self.wait(2)
        self.play(Create(tex[0]))
        self.play(Create(VGroup(graphs[0], tex[1])))
        self.play(Create(recs[0]))
        self.wait(3)

        # Step 1: f'(a) → n=1
        self.play(FadeOut(deriv_steps[0]))
        self.play(FadeIn(deriv_steps[1]), Transform(taylor_n[0], taylor_n[1]))
        self.wait(2)
        self.play(
            ReplacementTransform(graphs[0], graphs[1]),
            Write(tex[2]),
            Transform(recs[0], recs[1])
        )
        self.wait(3)

        # Step 2: f''(a) → n=2
        self.play(FadeOut(deriv_steps[1]))
        self.play(FadeIn(deriv_steps[2]), Transform(taylor_n[0], taylor_n[2]))
        self.wait(2)
        self.play(
            ReplacementTransform(graphs[1], graphs[2]),
            Write(tex[3]),
            Transform(recs[0], recs[2])
        )
        self.wait(3)

        # Step 3: f'''(a) → n=3
        self.play(FadeOut(deriv_steps[2]))
        self.play(FadeIn(deriv_steps[3]), Transform(taylor_n[0], taylor_n[3]))
        self.wait(2)
        self.play(
            ReplacementTransform(graphs[2], graphs[3]),
            Write(tex[4]),
            Transform(recs[0], recs[3])
        )
        self.wait(3)

        # Steps 4–7: higher derivatives
        for step_idx in range(4, 8):
            self.play(FadeOut(deriv_steps[step_idx - 1]))
            self.play(
                FadeIn(deriv_steps[step_idx]),
                Transform(taylor_n[0], taylor_n[step_idx])
            )
            self.wait(2)
            self.play(
                ReplacementTransform(graphs[step_idx - 1], graphs[step_idx]),
                Write(tex[step_idx + 1]),
                Transform(recs[0], recs[step_idx])
            )
            self.wait(3)

        # Fade out last derivative, switch to n=∞, animate remaining terms
        self.play(FadeOut(deriv_steps[7]), Transform(taylor_n[0], taylor_inf))
        for i in range(8, 10):
            if i < len(graphs) and i < len(tex):
                self.play(
                    ReplacementTransform(graphs[i-1], graphs[i]) if i < len(graphs) else Wait(),
                )
                self.wait(1)

        self.play(FadeOut(recs[0]))
        self.play(Write(tex[9]))
        self.wait(5)

class SinExpansion(Scene):
    def construct(self):

        deriv_steps = [
            VGroup(
                MathTex(r"f(x) = \sin(x)", font_size=40, stroke_width=1),
                MathTex(r"f(0) = \sin(0) = 0", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ No contribution (coefficient = 0)", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f'(x) = \cos(x)", font_size=40, stroke_width=1),
                MathTex(r"f'(0) = \cos(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ $45^o$ slope", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f''(x) = -\sin(x)", font_size=40, stroke_width=1),
                MathTex(r"f''(0) = -\sin(0) = 0", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ No contribution (coefficient = 0)", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f'''(x) = -\cos(x)", font_size=40, stroke_width=1),
                MathTex(r"f'''(0) = -\cos(0) = -1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Concavity and covexity: curves upward and downward", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f^{(4)}(x) = \sin(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(4)}(0) = \sin(0) = 0", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ No contribution (coefficient = 0)", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f^{(5)}(x) = \cos(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(5)}(0) = \cos(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Pattern repeats: adds $+\frac{x^5}{5!}$", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f^{(6)}(x) = -\sin(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(6)}(0) = -\sin(0) = 0", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ No contribution (coefficient = 0)", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f^{(7)}(x) = -\cos(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(7)}(0) = -\cos(0) = -1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Adds $-\frac{x^7}{7!}$: refines the curve", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
        ]
        
        ax = Axes(
            x_range=[-6, 6],
            y_range=[-2, 2],
            x_length=9,
            y_length=4,
            axis_config={
                "include_numbers":False,
                "tip_shape":StealthTip,
                "include_ticks":False
            }
        ).shift(RIGHT)


        tex = MathTex(
            "f(x) = ", "x", " - \\frac{x^3}{3!}", " + \\frac{x^5}{5!}",
            " - \\frac{x^7}{7!}", " + \\frac{x^9}{9!} ", " - \\frac{x^{11}}{11!} ",
            " + \\frac{x^{13}}{13!} ", " - \\frac{x^{15}}{15!} ", "+ ............\\infty"
        )
        tex.move_to(2 * DOWN)

        labels = ax.get_axis_labels(x_label="x", y_label="f(x)=sin(x)")
        graph1 = ax.plot(lambda x: m.sin(x), color=RED)

        x_range = [1.5, 3, 3.5, 4, 5, 6, 6, 6, 6, 6]

        graphs = [
            ax.plot(lambda x, n=n: sum(
                (-1)**k * x**(2*k+1) / m.factorial(2*k+1) for k in range(n+1)
            ), color=YELLOW_E, x_range=[-x_range[n], x_range[n]]
            ) for n in range(10)
        ]

        taylor_general = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{n}",
            r"\frac{f^{(i)}(x_0)}{i!}", r"(x - x_0)^i",
            font_size=38, stroke_width=1
        ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        x0_label = MathTex(r"x_0 = 0", font_size=38, color="#00E540", stroke_width=1)
        x0_label.next_to(taylor_general, RIGHT, buff=0.5)

        # Simplified form (x_0 = 0) — base version with n

        def make_taylor_n(n_val):
            return MathTex(
                r"f(x)", r"=", rf"\sum_{{i=0}}^{{{n_val}}}",
                r"\frac{f^{(i)}(0)}{i!}", r"\cdot x^i",
                font_size=38, stroke_width=1
            ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        # Create formula for each n value (0 through 7) plus infinity
        taylor_n = [make_taylor_n(n) for n in range(8)]
        taylor_inf = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{\infty}",
            r"\frac{f^{(i)}(0)}{i!}", r"\cdot x^i",
            font_size=38, stroke_width=1
        ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        # Position derivative steps at the top of the screen (separate from the sum)
        for step in deriv_steps:
            step.to_edge(UP, buff=0.2).to_edge(LEFT, buff=0.3)

        recs = [
            SurroundingRectangle(VGroup(tex[0], tex[i]), color=WHITE) for i in range(1, 9)
        ]

        # === ANIMATION START ===

        # 1. Show the general Taylor formula
        self.play(Write(taylor_general))
        self.wait(2)

        # 2. Show x_0 = 0
        self.play(Write(x0_label))
        self.wait(2)

        # 3. Transform to simplified form with n=0
        self.play(
            ReplacementTransform(taylor_general, taylor_n[0]),
            FadeOut(x0_label)
        )
        self.wait(2)

        # 4. Create graph
        self.play(Create(ax), Create(graph1), Create(labels))

        # Step 0: f(0)=1 → plot constant + first term, n=0
        self.play(FadeIn(deriv_steps[0]))
        self.wait(2)
        self.play(Create(tex[0]))
        self.play(Create(recs[0]))
        self.wait(3)

        # Step 1: f'(0)=0 → n=1
        self.play(FadeOut(deriv_steps[0]))
        self.play(FadeIn(deriv_steps[1]), Transform(taylor_n[0], taylor_n[1]))
        self.play(Create(VGroup(graphs[0], tex[1])))
        self.wait(4)

        # Step 2: f''(0)=-1 → n=2, add term
        self.play(FadeOut(deriv_steps[1]))
        self.play(FadeIn(deriv_steps[2]), Transform(taylor_n[0], taylor_n[2]))
        self.wait(2)


        self.wait(3)

        # Step 3: f'''(0)=0 → n=3
        self.play(FadeOut(deriv_steps[2]))
        self.play(FadeIn(deriv_steps[3]), Transform(taylor_n[0], taylor_n[3]))
        self.play(
            ReplacementTransform(graphs[0], graphs[1]),
            Write(tex[2]),
            Transform(recs[0], recs[1])
        )

        self.wait(4)

        # Steps 4–7: higher derivatives
        for i, step_idx in enumerate([4, 5, 6, 7]):
            self.play(FadeOut(deriv_steps[step_idx - 1]))
            self.play(
                FadeIn(deriv_steps[step_idx]),
                Transform(taylor_n[0], taylor_n[step_idx])
            )
            self.wait(2)
            graph_idx = 2 + (i // 2)
            tex_idx = 3 + (i // 2)
            if step_idx % 2 != 0:
                self.play(
                    ReplacementTransform(graphs[graph_idx - 1], graphs[graph_idx]),
                    Write(tex[tex_idx]),
                    Transform(recs[0], recs[tex_idx - 1])
                )
                self.wait(3)
            else:
                self.wait(2)

        # Fade out last derivative, switch to n=∞, animate remaining terms
        self.play(FadeOut(deriv_steps[7]), Transform(taylor_n[0], taylor_inf))
        for i in range(4, 8):
            self.play(
                ReplacementTransform(graphs[i-1], graphs[i]),
                Write(tex[i+1]),
                Transform(recs[0], recs[i])
            )
            self.wait(2)

        self.play(FadeOut(recs[0]))
        self.play(Write(tex[9]))
        self.wait(5)


class eExpansion(Scene):
    def construct(self):

        deriv_steps = [
            VGroup(
                MathTex(r"f(x) = \exp(x)", font_size=40, stroke_width=1),
                MathTex(r"f(0) = \exp(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Value at expansion point", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f'(x) = \exp(x)", font_size=40, stroke_width=1),
                MathTex(r"f'(0) = \exp(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Slope at expansion point", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f''(x) = \exp(x)", font_size=40, stroke_width=1),
                MathTex(r"f''(0) = \exp(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Concavity at expansion point", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f'''(x) = \exp(x)", font_size=40, stroke_width=1),
                MathTex(r"f'''(0) = \exp(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Third-order correction", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f^{(4)}(x) = \exp(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(4)}(0) = \exp(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Pattern repeats identically", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f^{(5)}(x) = \exp(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(5)}(0) = \exp(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Fifth-order correction", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f^{(6)}(x) = \exp(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(6)}(0) = \exp(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Refines the curve further", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),

            VGroup(
                MathTex(r"f^{(7)}(x) = \exp(x)", font_size=40, stroke_width=1),
                MathTex(r"f^{(7)}(0) = \exp(0) = 1", font_size=40, color="#00E540", stroke_width=1),
                Tex(r"$\rightarrow$ Seventh-order correction", font_size=30, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15),
        ]

        tex = MathTex(
            "e^x = ", "1", " + \\frac{x}{1!}", " + \\frac{x^2}{2!}", 
            " + \\frac{x^3}{3!}", " + \\frac{x^4}{4!}", " + \\frac{x^5}{5!}", 
            " + \\frac{x^6}{6!}", " + \\frac{x^7}{7!}", "+ ............\\infty",
            color=BLUE
        ).move_to(2 * DOWN)

        ax = Axes(
            x_range=[-3, 1.2],
            y_range=[-0.5, 4],
            x_length=8,
            y_length=4,
            axis_config={
                "include_numbers":False,
                "tip_shape":StealthTip,
                "include_ticks":False
            }
        ).to_edge(RIGHT,buff=2).shift(UP)

        labels = ax.get_axis_labels(x_label="x", y_label=MathTex("f(x)=e^x"))
        graph1 = ax.plot(lambda x: m.e**x, color=PINK)

        def taylor_series_approx(n):
            return ax.plot(lambda x: sum(x**k / m.factorial(k) for k in range(n + 1)), color=YELLOW_E,x_range=[-2.5,1.5])

        graphs = [taylor_series_approx(n) for n in range(10)]

        taylor_general = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{n}",
            r"\frac{f^{(i)}(x_0)}{i!}", r"(x - x_0)^i",
            font_size=38, stroke_width=1
        ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        x0_label = MathTex(r"x_0 = 0", font_size=38, color="#00E540", stroke_width=1)
        x0_label.next_to(taylor_general, RIGHT, buff=0.5)

        # Simplified form (x_0 = 0) — base version with n

        def make_taylor_n(n_val):
            return MathTex(
                r"f(x)", r"=", rf"\sum_{{i=0}}^{{{n_val}}}",
                r"\frac{f^{(i)}(0)}{i!}", r"\cdot x^i",
                font_size=38, stroke_width=1
            ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        # Create formula for each n value (0 through 7) plus infinity
        taylor_n = [make_taylor_n(n) for n in range(8)]
        taylor_inf = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{\infty}",
            r"\frac{f^{(i)}(0)}{i!}", r"\cdot x^i",
            font_size=38, stroke_width=1
        ).next_to(tex, UP, buff=0.25).to_edge(LEFT, buff=0.3)

        # Position derivative steps at the top of the screen (separate from the sum)
        for step in deriv_steps:
            step.to_edge(UP, buff=0.2).to_edge(LEFT, buff=0.3)

        recs = [
            SurroundingRectangle(VGroup(tex[0], tex[i]), color=WHITE) for i in range(1, 9)
        ]

        # === ANIMATION START ===

        # 1. Show the general Taylor formula
        self.play(Write(taylor_general))
        self.wait(2)

        # 2. Show x_0 = 0
        self.play(Write(x0_label))
        self.wait(2)

        # 3. Transform to simplified form with n=0
        self.play(
            ReplacementTransform(taylor_general, taylor_n[0]),
            FadeOut(x0_label)
        )

        self.wait(2)

        # 4. Create graph
        self.play(Create(ax), Create(graph1), Create(labels))

        # Step 0: f(0)=1 → plot constant + first term, n=0
        self.play(FadeIn(deriv_steps[0]))
        self.wait(2)
        self.play(Create(tex[0]))
        self.play(Create(recs[0]))
        self.play(Create(VGroup(graphs[0], tex[1])))
        self.wait(3)

        # Step 1: f'(0)=0 → n=1
        self.play(FadeOut(deriv_steps[0]))
        self.play(FadeIn(deriv_steps[1]), Transform(taylor_n[0], taylor_n[1]))

        self.play(
            ReplacementTransform(graphs[0], graphs[1]),
            Write(tex[2]),
            Transform(recs[0], recs[1])
        )
       
        self.wait(4)

        # Step 2: f''(0)=-1 → n=2, add term
        self.play(FadeOut(deriv_steps[1]))
        self.play(FadeIn(deriv_steps[2]), Transform(taylor_n[0], taylor_n[2]))
        self.play(
            ReplacementTransform(graphs[1], graphs[2]),
            Write(tex[3]),
            Transform(recs[0], recs[1])
        )

        self.wait(2)


        self.wait(3)

        # Step 3: f'''(0)=0 → n=3
        self.play(FadeOut(deriv_steps[2]))
        self.play(FadeIn(deriv_steps[3]), Transform(taylor_n[0], taylor_n[3]))
        
        self.play(
            ReplacementTransform(graphs[2], graphs[3]),
            Write(tex[4]),
            Transform(recs[0], recs[1])
        )

        self.wait(4)

        # Steps 4–7: higher derivatives
        for i, step_idx in enumerate([4, 5, 6, 7]):
            self.play(FadeOut(deriv_steps[step_idx - 1]))
            self.play(
                FadeIn(deriv_steps[step_idx]),
                Transform(taylor_n[0], taylor_n[step_idx])
            )
            self.wait(2)
    
            self.play(
                    ReplacementTransform(graphs[step_idx - 1], graphs[step_idx]),
                    Write(tex[step_idx]),
                    Transform(recs[0], recs[step_idx - 1])
                )

            self.wait(2)

        # Fade out last derivative, switch to n=∞, animate remaining terms
        self.play(FadeOut(deriv_steps[7]), Transform(taylor_n[0], taylor_inf))
        for i in range(4, 8):
            self.play(
                ReplacementTransform(graphs[i-1], graphs[i]),
                Write(tex[i+1]),
                Transform(recs[0], recs[i])
            )
            self.wait(2)

        self.play(FadeOut(recs[0]))
        self.play(Write(tex[9]))
        self.wait(5)
