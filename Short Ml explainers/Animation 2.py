from manim import *
import numpy as np
from scipy.stats import beta
config.background_color = '#0E0E0E'


class Beta_distribution(Scene):
    def construct(self):
        #Probability density function and beta function mathtex
        probability_density_function = MathTex(r"F(x) = \frac{x^{\alpha - 1}(1-x)^{\beta - 1}}{\beta(\alpha,\beta)}").scale(0.8)
        beta_function = MathTex(r"B(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}").scale(0.8)

        prob_den_func_text = Text("The probability density function").scale(0.4)
        beta_func_text = Text("it is parameterized by two variables").scale(0.4)
        
        equations_and_functions = VGroup(prob_den_func_text,probability_density_function,beta_func_text,beta_function).arrange(DOWN).to_corner(UP)

        self.wait(1)
        for i in range(4):
            self.play(FadeIn(equations_and_functions[i]),rate_func=smooth)
            self.wait(1)

        self.wait(1)
        self.play(equations_and_functions.animate.scale(0.7).to_corner(UP))

        #These are the valuetrackers and the decimal numbers of alpha and beta

        beta_tracker = ValueTracker(6)
        alpha_tracker = ValueTracker(1)

        #This is included to help me with the positioning
        line = Line(start=[0,0,0], end = [1,0,0]).next_to(equations_and_functions,DOWN,buff=0.5)

        beta_number = always_redraw(
            lambda : VGroup(MathTex(r"\beta = "),DecimalNumber(beta_tracker.get_value(),0)).arrange(RIGHT).scale(0.7).set_color("#F5B041").next_to(line,RIGHT,buff=0)
        )

        alpha_number = always_redraw(
            lambda : VGroup(MathTex(r"\alpha = "),DecimalNumber(alpha_tracker.get_value(),0)).arrange(RIGHT).scale(0.7).set_color("#F5B041").next_to(line,LEFT,buff=0)
        )

        axes = Axes(x_range=[0,1,0.1],y_range=[0,5,0.5],axis_config={"tip_shape":StealthTip},x_axis_config={"include_numbers":True,"numbers_to_include":[0,0.5,1]},
                    y_axis_config={"include_numbers":True,"numbers_to_include":[0,2,4]}).set_color("#B0B0B0").scale(0.5).to_corner(DOWN)
        y_labels = axes.get_y_axis_label("f(x)",direction = LEFT+DOWN,buff=0.2).set_color("#B0B0B0")

        curve = always_redraw(
            lambda: axes.plot(
                lambda x: beta.pdf(x, alpha_tracker.get_value(), beta_tracker.get_value()),
                x_range=[0, 1],
                color="#00C9A7"
            )
        )

        self.wait(1)
        self.play(FadeIn(alpha_number),FadeIn(beta_number),rate_func=smooth)

        self.wait(1)
        self.play(FadeIn(axes),FadeIn(y_labels),rate_func=smooth)
        self.wait(1)
        self.play(FadeIn(curve),rate_func=smooth)
        self.wait(1)

        self.play(alpha_tracker.animate.set_value(6),beta_tracker.animate.set_value(1),rate_func=smooth,run_time=6,lag_ratio=0)
        self.wait(1)