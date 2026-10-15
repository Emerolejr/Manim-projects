from manim import *
import numpy as np
import math as m

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


class taylor_series(Scene):
    def construct(self):

        ##texts group 1

        text_1 = MathTex(r"\text{Given two Cosine functions}",font_size=32).to_corner(UP,buff=0.5)
        
        text_2 = VGroup(
            MathTex(r"\text{We can approximate using Taylor Series}",font_size=32),
            MathTex(r"\text{with different expansion points at $x_o = 0$ \text{ and }  $x_o = 2$}",font_size=32)
        ).arrange(DOWN,buff=0.2).to_corner(UP,buff=0.5)

        text_3 = MathTex(r"\text{Note Expansion points for the $x_o = 0$ \text{ and } $x_o = 2$}",font_size=32).to_corner(UP,buff=0.5)
       
        text_4 = VGroup(
            MathTex(r"\text{Accuracy of approximation depends on the location of $x_o$}",font_size=32),
            MathTex(r"\text{especially for small values of n}",font_size=32) 
        ).arrange(DOWN,buff=0.2).to_corner(UP,buff=0.5)

        text_5 = MathTex(r"\text{But note that as $n \to \infty$, both graphs matches cosine}",font_size=32).to_corner(UP,buff=0.5)

        ax_1= Axes(
            x_range=(-6, 6),
            y_range=(-1.5, 1.5),
            x_length=5,
            y_length=3,
            axis_config={
                "include_ticks":False,
                "include_numbers":False,
                "tip_shape":StealthTip
            }
        )

        ax_2 = Axes(
            x_range=(-6, 6),
            y_range=(-1.5, 1.5),
            x_length=5,
            y_length=3,
            axis_config={
                "include_ticks":False,
                "include_numbers":False,
                "tip_shape":StealthTip
            }
        )

        axes_group = Group(ax_1,ax_2).arrange(RIGHT,buff=1)
        
        labels1 = ax_1.get_axis_labels(x_label="x", y_label=MathTex(r"f(x)=\cos(x)").scale(0.8))
        graph1 = ax_1.plot(lambda x: m.cos(x), color=PINK)

        x_range = [6, 2.5, 3.5, 3.5, 4.5, 5.5, 6, 6, 6, 6,6,6]

        graphs1 = [
            ax_1.plot(lambda x, n=n: sum(
                (-1)**k * x**(2*k) / m.factorial(2*k) for k in range(n+1)
            ), color="#00E540", stroke_width=5, x_range=[-x_range[n],x_range[n]]) for n in range(12)
        ]
        
        ## this is for graph 2.
        labels2 = ax_2.get_axis_labels(x_label="x", y_label=MathTex(r"f(x)=\cos(x)").scale(0.8))

        a_val = 2  # expansion point
        graph2 = ax_2.plot(lambda x: m.cos(x), color=PINK)

        # Taylor approximation graphs centered at a_val
        x_range_lower = [-6,0,0,-1.5,-1,-2,-1.7,-2.5,-2,-3,3,-4,-4,-4.5,-4.5,-4.5,-5,-5,-5,-5.5,-6,-6,-6,-6]
        x_range_higher = [6,3,4,4.5,5,5,5.5,5.5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]

        graphs2 = [
            ax_2.plot(lambda x, n=n: sum(
                dcos(k, a_val) * (x - a_val)**k / m.factorial(k) for k in range(n+1)
            ), color="#00E540", stroke_width=5,x_range=[x_range_lower[n] ,x_range_higher[n]]) for n in range(24)
        ]

        ### the graph expansion points are defined here.
        dot_1 = Dot().move_to(ax_1.c2p(0,np.cos(0))).set_z_index(2)
        dot_2 = Dot().move_to(ax_2.c2p(2,np.cos(2))).set_z_index(2)

        dot_group = Group(dot_1,dot_2)

        ### Expansion point name
        graph_1_name = MathTex(r"\text{Expansion Point $x_o = 0$}",font_size=25).next_to(ax_1,DOWN,buff=0.5)
        graph_2_name = MathTex(r"\text{Expansion Point $x_o = 2$}",font_size=25).next_to(ax_2,DOWN,buff=0.5)

        ### The taylor series series formula for both graphs are defined here.

        # Taylor formula: general form with x_0
        taylor_general1 = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{n}",
            r"\frac{f^{(i)}(x_0)}{i!}", r"(x - x_0)^i",
            font_size=32, stroke_width=1
        ).next_to(graph_1_name, DOWN, buff=0.25).to_edge(LEFT, buff=0.3)

        x0_label1 = MathTex(r"x_0 = 0", font_size=32, color="#00E540", stroke_width=1)
        x0_label1.next_to(taylor_general1, RIGHT, buff=0.3)

        # Simplified form (x_0 = 0) — base version with n

        def make_taylor_n1(n_val):
            return MathTex(
                r"f(x)", r"=", rf"\sum_{{i=0}}^{{{n_val}}}",
                r"\frac{f^{(i)}(0)}{i!}", r"\cdot x^i",
                font_size=32, stroke_width=1
            ).next_to(graph_1_name, DOWN, buff=0.25)

        # Create formula for each n value (0 through 10) plus infinity
        taylor_n_1 = [make_taylor_n1(n) for n in range(24)]
        taylor_inf_1 = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{\infty}",
            r"\frac{f^{(i)}(0)}{i!}", r"\cdot x^i",
            font_size=32, stroke_width=1
        ).next_to(graph_1_name, DOWN, buff=0.25)

        # Taylor formula: general form with a
        taylor_general2 = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{n}",
            r"\frac{f^{(i)}(a)}{i!}", r"(x - a)^i",
            font_size=32, stroke_width=1
        ).next_to(graph_2_name, DOWN, buff=0.25)

        a_label = MathTex(rf"a = {a_val}", font_size=35, color="#00E540", stroke_width=1)
        a_label.next_to(taylor_general2, RIGHT, buff=0.5)

        # Simplified form with a substituted — base version with n
        def make_taylor_n2(n_val):
            return MathTex(
                r"f(x)", r"=", rf"\sum_{{i=0}}^{{{n_val}}}",
                rf"\frac{{f^{{(i)}}({a_val})}}{{i!}}", rf"\cdot (x - {a_val})^i",
                font_size=35, stroke_width=1
            ).next_to(graph_2_name, DOWN, buff=0.25)

        # Create formula for each n value (0 through 7) plus infinity
        taylor_n_2 = [make_taylor_n2(n) for n in range(24)]
        taylor_inf_2 = MathTex(
            r"f(x)", r"=", r"\sum_{i=0}^{\infty}",
            rf"\frac{{f^{{(i)}}({a_val})}}{{i!}}", rf"\cdot (x - {a_val})^i",
            font_size=35, stroke_width=1
        ).next_to(graph_2_name, DOWN, buff=0.25)

        ###
        ### Animation starts here
        ### 

        self.wait(4)
        self.play(FadeIn(axes_group),rate_func=smooth)
        self.play(FadeIn(text_1),rate_func=smooth)

        self.play(Create(graph1),Create(graph2),rate_func=smooth,run_time=6)
        self.play(FadeIn(labels1),FadeIn(labels2),rate_func=smooth)
        self.play(FadeOut(text_1),rate_func=smooth)
        self.play(FadeIn(text_2),rate_func=smooth)
        
        self.wait(2)
        self.play(FadeIn(taylor_general1),FadeIn(taylor_general2),rate_func=smooth)
        self.play(FadeIn(x0_label1),FadeIn(a_label),rate_func=smooth)
        self.play(FadeOut(text_2),rate_func=smooth)
        self.play(FadeIn(text_3),rate_func=smooth)

        self.play(FadeIn(graph_1_name),FadeIn(graph_2_name),rate_func=smooth)
        self.play(FadeIn(dot_group),rate_func=smooth)
        self.wait(2)
        self.play(Create(graphs1[0]),Create(graphs2[0]),rate_func=smooth)
        self.play(ReplacementTransform(taylor_general1, taylor_n_1[0]),
                  ReplacementTransform(taylor_general2, taylor_n_2[0]),
                  FadeOut(x0_label1),FadeOut(a_label))
        
        self.wait(2)
        
        counter = 0

        for i in range(0,10):
            if i%2 == 0:
                self.play(ReplacementTransform(graphs1[counter-1], graphs1[counter]),ReplacementTransform(graphs2[i-1], graphs2[i]),
                        ReplacementTransform(taylor_n_1[i-1], taylor_n_1[i]),ReplacementTransform(taylor_n_2[i-1], taylor_n_2[i]),
                        run_time=2,rate_funcs=smooth)
                counter = counter + 1
                self.wait(2)
            else:
                self.play(ReplacementTransform(graphs2[i-1], graphs2[i]),
                        ReplacementTransform(taylor_n_2[i-1], taylor_n_2[i]),ReplacementTransform(taylor_n_1[i-1],taylor_n_1[i]),
                        run_time=2,rate_func=smooth)
                self.wait(2)
        
        self.wait(2)
        self.play(FadeOut(text_3),rate_func=smooth,run_time=2)
        self.play(FadeIn(text_4),rate_func=smooth,run_time=2)
        self.wait(2)

        for i in range(10,22):
            if i%2 == 0:
                self.play(ReplacementTransform(graphs1[counter-1], graphs1[counter]),
                          ReplacementTransform(graphs2[i-1], graphs2[i]),
                        ReplacementTransform(taylor_n_1[i-1], taylor_n_1[i]),
                        ReplacementTransform(taylor_n_2[i-1], taylor_n_2[i]))
                counter = counter + 1
            else:
                self.play(ReplacementTransform(graphs2[i-1], graphs2[i]),
                        ReplacementTransform(taylor_n_2[i-1], taylor_n_2[i]),
                        ReplacementTransform(taylor_n_1[i-1],taylor_n_1[i]))
        
        self.play(ReplacementTransform(taylor_n_1[21],taylor_inf_1),
                  ReplacementTransform(taylor_n_2[21],taylor_inf_2),
        rate_func=smooth)

        self.play(FadeOut(text_4),rate_func=smooth)
        self.play(FadeIn(text_5),rate_func=smooth)
        self.wait(4)
        