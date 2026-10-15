from manim import *

class derivative(Scene):
    def construct(self):

        ### These are the texts and symbols for the right column of the  
        slope_text_1 = MathTex(
            r"\text{Let the slope of the secant line be }", r"M_s"
        ).scale(0.7).set_color(ORANGE)
        slope_text_1[1].set_color(BLUE)

        slope_text_2 = MathTex(
            r"M_s", r"=", r"\frac{\Delta y}{\Delta x}"
        ).scale(0.7)

        slope_text_2[0].set_color(BLUE)
        
        slope_text_2[2][0:2].set_color(RED)
        slope_text_2[2][3:].set_color(BLUE)

        slope_text_3 = MathTex(
            r"M_s", r"=", r"\frac{f(x_o +\Delta x)-f(x)}{\Delta x}"
        ).scale(0.7)

        slope_text_3[0].set_color(BLUE)
        
        slope_text_3[2][0:14].set_color(RED)
        slope_text_3[2][14:].set_color(BLUE)


        slope_text_4 = MathTex(
            r"\text{As } \Delta x \to 0,\ \text{the secant line approaches the tangent}"
        ).scale(0.7)
      
        slope_text_4[0][2:4].set_color(BLUE)

        slope_text_5 = MathTex(
            r"M_t", r"=", r"\lim_{\Delta x \to 0} M_s"
        ).scale(0.7)

        slope_text_5[0].set_color(BLUE)
        
        slope_text_5[2].set_color(BLUE)

        slope_text_6 = MathTex(
            r"\text{where } M_t \text{ is the slope of the tangent line}"
        ).scale(0.7)
        
        slope_text_6[5:6].set_color(BLUE)

        slope_text_7 = MathTex(
            r"f'(x)", r"=", r"\lim_{\Delta x \to 0}",
            r"\frac{f(x_o +\Delta x)-f(x)}{\Delta x}"
        ).scale(0.7)

        slope_text_7[0].set_color(BLUE)
        slope_text_7[2].set_color(BLUE)
        slope_text_7[3][0:14].set_color(RED)
        slope_text_7[3][14:].set_color(BLUE)


        # Group and arrange
        right_column = VGroup(
            slope_text_1,
            slope_text_2,
            slope_text_3,
            slope_text_4,
            slope_text_5,
            slope_text_6,
            slope_text_7,
        ).scale(0.8).arrange(DOWN,aligned_edge=LEFT,buff=0.35)

        right_column.to_edge(RIGHT, buff=0.1).shift(UP*0.5)

        ### These are the texts, symbols, and the axes on the left column of the screen.

        axes = Axes(x_range=[0,11],y_range=[0,90],x_length=5,y_length=4,
                     axis_config={"include_numbers":False,"tip_shape":StealthTip,"include_ticks":False})
        axes.shift(LEFT*3)

        y_label = Text("Y").next_to(axes.get_y_axis(),LEFT,buff=0.3).scale(0.8).set_color(YELLOW)
        x_label = Text("X").next_to(axes.get_x_axis(),DOWN,buff=0.3).scale(0.8).set_color(YELLOW)

        self.wait(2)
        self.play(FadeIn(axes,shift=DOWN),FadeIn(y_label,shift=RIGHT),FadeIn(x_label,shift=UP),rate_func=smooth)
        self.wait(2)

        graph = axes.plot(lambda x: x**2 - 5*x + 30 ,x_range=[0.5,10]).set_color(BLUE)

        self.play(Create(graph),rate_func=smooth)

        ## Point P and Q. 
        point_p = Dot(graph.point_from_proportion(0.4))
        point_q = Dot(graph.point_from_proportion(0.9))

        point_p_text = Text("P").scale(0.6).next_to(point_p,UP).set_color(YELLOW)
        point_q_text = Text("Q").scale(0.6).next_to(point_q,UP).set_color(YELLOW)

        p_indicator_lines = always_redraw(
            lambda: axes.get_lines_to_point(point_p.get_center()).set_color(BLUE)
        )

        q_indicator_lines = always_redraw(
            lambda: axes.get_lines_to_point(point_q.get_center()).set_color(RED)
        )

        delta_x_line = always_redraw(
            lambda: DashedLine(start = point_p.get_center(),end=(point_q.get_x(),point_p.get_y(),0)).set_color(BLUE)
        )
        
        secant_line = always_redraw(
            lambda : Line(start= point_p.get_center(),
            end=point_q.get_center()).set_length(np.sqrt((point_p.get_x() - point_q.get_x())**2 + (point_q.get_y() - point_p.get_y())**2) + 2.5).set_color(RED)
        )

        ### Graph notations. dx, dy, f(x), x + dx, f(x + dx)
        delta_x_label = MathTex(r"\Delta x").scale(0.7).next_to(delta_x_line,DOWN).set_color(BLUE)
        delta_y_label = MathTex(r"\Delta y").scale(0.7).move_to(q_indicator_lines.get_right()+[0.5,0.5,0]).set_color(RED)

        ### Cordinates of point P and Q relative to the axes.
        x1,y1 = axes.p2c(point_p.get_center())
        x2,y2 = axes.p2c(point_q.get_center())

        x_1 = MathTex(r"x_o").scale(0.7).next_to(axes.c2p(x1,0,0),DOWN).set_color(BLUE)
        x_2 = MathTex(r"x_o",r"\text{ + }" + r"\Delta x").scale(0.7).next_to(axes.c2p(x2,0,0),DOWN).set_color(BLUE)

        f_of_x_1 = MathTex(r"f(x_o)").scale(0.7).next_to(axes.c2p(0,y1,0),LEFT).set_color(RED)
        f_of_x_2 = MathTex(r"\text{f(} "+ r"x_o +"+ r"\Delta x)}").scale(0.7).next_to(axes.c2p(0,y2,0),LEFT).set_color(RED)

        self.wait(3)
        self.play(Create(point_p),Create(point_q),Create(q_indicator_lines),Create(p_indicator_lines),Create(delta_x_line),
        Create(point_p_text),Create(point_q_text))

        self.play(Create(secant_line))
        
        self.play(FadeIn(VGroup(x_1,x_2,f_of_x_1,f_of_x_2)))
        self.wait(1)
        self.play(Create(delta_x_label),Create(delta_y_label))
        self.wait(2)
        self.play(Write(slope_text_1))
        self.wait(1)
        self.play(Write(slope_text_2))
        self.wait(2)
        self.play(ReplacementTransform(slope_text_2.copy(),slope_text_3))
        self.wait(2)
        self.play(Write(slope_text_4))
        self.wait(1)

        def update(mob,alpha):
            p = interpolate(0.9,0.4001,alpha)
            mob.move_to(graph.point_from_proportion(p))

        self.play(FadeOut(VGroup(x_2,f_of_x_2,delta_x_label,delta_y_label,point_q_text)))
        self.play(UpdateFromAlphaFunc(point_q,update))
        self.wait(2)
        self.play(Write(VGroup(slope_text_5,slope_text_6)))
        self.wait(2)
        self.play(Write(slope_text_7),rate_func=smooth)
        self.wait(5)

