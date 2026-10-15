from manim import *
config.background_color=WHITE


class limits(ThreeDScene):
    def construct(self):
        self.next_section(name="Scene_1",skip_animations=False) #This is the first scene

        dot = Dot().set_color('#6B1012').move_to([-3,0,0])
        wall = Rectangle(width = 0.5,height=6,color='#14014B').move_to([2.25,0,0]).set_fill(color='#14014B',opacity=1)  
        wall_name = Text("Barrier").next_to(wall,UP,buff=0.5).set_color(color='#14014B').scale(0.5)
        trace = TracedPath(dot.get_center,dissipating_time=0.05).set_color('#6B1012')

        self.wait(2)
        self.play(FadeIn(dot),Create(trace),GrowFromEdge(wall,DOWN),FadeIn(wall_name),rate_func=smooth,run_time=3)
        self.play(dot.animate.move_to([2-dot.get_radius(),0,0]),rate_func=smooth,run_time=2.694)
        self.play(dot.animate.move_to([-2,0,0]),rate_func=smooth,run_time=2.389)
        self.play(dot.animate.move_to([2-dot.get_radius(),0,0]),rate_func=smooth,run_time=2.083)
        self.play(dot.animate.move_to([-1,0,0]),rate_func=smooth,run_time=1.778) 
        self.play(dot.animate.move_to([2-dot.get_radius(),0,0]),rate_func=smooth,run_time=1.472)
        self.play(dot.animate.move_to([-0.5,0,0]),rate_func=smooth,run_time=1.167)
        self.play(dot.animate.move_to([2-dot.get_radius(),0,0]),rate_func=smooth,run_time=0.861)
        self.play(dot.animate.move_to([0,0,0]),rate_func=smooth,run_time=0.556)
        self.play(Indicate(dot),FadeOut(VGroup(wall,wall_name)),dot.animate.move_to([1.5,0,0]),FadeOut(trace))

        dot.add_updater(
            lambda m,dt: m.rotate(about_point=ORIGIN,angle=2*PI*dt)
        )

        limit = Text('The idea of limits').set_color('#14014B').scale(0.5)   
        self.play(Create(limit),rate_func=smooth)  

        self.next_section(name="Scene_2",skip_animations=False) 
        # This is a new scene

        self.play(FadeOut(*self.mobjects),rate_func=smooth)

        Texts = VGroup(Tex(f"\u2022 The idea of limits"),Tex(f"\u2022 Left and Right hand limits"), Tex(f"\u2022 Existence of limits")).scale(0.5).arrange(DOWN,aligned_edge=LEFT)

        for i in range(3):
            Texts[i].set_color('#14014B')
            self.play(FadeIn(Texts[i]),rate_func=smooth)
            self.wait(3)

        self.play(FadeOut(*self.mobjects),rate_func=smooth)
        self.wait(4)
        

        limit_definition = Text(f"A limit can be defined as the value a function approaches when it goes to a x-value").set_color('#6B1012').scale(0.3)
        limit_cursor = Rectangle(width=0.005,height=0.12).set_color('#6B1012')
        limit_cursor.move_to(limit_definition[0])
        limit_underline = Underline(limit_definition[1:6],color='#14014B',stroke_width=2,buff=0.1)
        function_underline = Underline(limit_definition[29:37],color='#14014B',stroke_width=2,buff=0.1)
        self.play(TypeWithCursor(limit_definition,limit_cursor),rate_func=smooth,run_time=4.5)
        self.play(FadeOut(limit_cursor),run_time=0.5,rate_func=smooth)
        self.wait(5)
        self.play(Create(limit_underline),Create(function_underline),rate_func=smooth,run_itime=1,lag_ratio=1)
        self.wait(10)

        func_circ = Circle(radius=1).set_color('#6B1012')
        func_name = Text("Function").next_to(func_circ,UP).scale(0.7).set_color('#6B1012')
        func_text = Text("Rule").move_to(func_circ.get_center()).set_color('#6B1012').scale(0.5)
        input_arrow = Arrow(start= [0,0,0],end = [2,0,0],stroke_width=2).next_to(func_circ.get_left(),LEFT,buff=0.1).set_color('#14014B')
        output_arrow = Arrow(start= [0,0,0],end = [2,0,0],stroke_width=2).next_to(func_circ.get_right(),RIGHT,buff=0.1).set_color('#14014B')
        input_text = Text("Input").scale(0.25).set_color('#14014B').next_to(input_arrow,DOWN)
        output_text = Text("Output").scale(0.25).set_color('#14014B').next_to(output_arrow,DOWN)

        function_whole = VGroup(func_circ,func_name,func_text,input_arrow,output_arrow,input_text,output_text)

        self.play(ReplacementTransform(VGroup(limit_definition,limit_underline,function_underline),func_name),rate_func=smooth)
        self.play(FadeIn(func_circ),FadeIn(func_text),rate_func=smooth)
        self.wait(3)
        
        self.play(Create(input_arrow),Create(output_arrow),FadeIn(input_text),FadeIn(output_text),rate_func=smooth,run_time=3)
        self.wait(2)


        self.next_section(name="second_scene",skip_animations=False)
        ##This is for the next scene
        axes_group = VGroup()
        plot_group = VGroup()
        name_group = VGroup()

        for i in range(6):
            axes = NumberPlane().scale(0.25).set_color(BLACK).set_color('#14014B')
            axes_group.add(axes)
        axes_group.arrange_in_grid(rows=3,cols=2).shift(RIGHT*2)

        for i in range(6):
            if i == 0:  
               single_plot = axes_group[i].plot(lambda x: 0.5 * x, x_range=[-6,6,0.2]).set_color('#6B1012')
               plot_group.add(single_plot)
               text = MathTex(r"f(x) = \frac{1}{2} x ").move_to(single_plot.get_center()).scale(0.5).set_color('#6B1012')
               name_group.add(text)

            elif i == 1:
               single_plot = axes_group[i].plot(lambda x: -x**2 + 2, x_range=[-2.5,2.5,0.2]).set_color('#6B1012')
               plot_group.add(single_plot)
               text = MathTex(r"f(x) = - x^2 + 2 ").move_to(single_plot.get_center()).scale(0.7).set_color('#6B1012')
               name_group.add(text)

            elif i == 2:
               single_plot = axes_group[i].plot(lambda x: np.sin(x), x_range=[-2*PI,2*PI,0.2]).set_color('#6B1012')
               plot_group.add(single_plot)
               text = MathTex(r"f(x) = sin(x) ").move_to(single_plot.get_center()).scale(0.7).set_color('#6B1012')
               name_group.add(text)

            elif i == 3:
                single_plot = axes_group[i].plot(lambda x: x**2 - 4, x_range=[-2.5,2.5,0.2]).set_color('#6B1012')
                plot_group.add(single_plot)
                text = MathTex(r"f(x) =  x^2 - 4 ").move_to(single_plot.get_center()).scale(0.7).set_color('#6B1012')
                name_group.add(text)

            elif i == 4:
                single_plot = axes_group[i].plot(lambda x: np.exp(x), x_range=[-6,1,0.2]).set_color('#6B1012')
                plot_group.add(single_plot)
                text = MathTex(r"f(x) = e^x ").move_to(single_plot.get_center()).scale(0.7).set_color('#6B1012')
                name_group.add(text)

            else:
                single_plot = axes_group[i].plot(lambda x: np.cos(x), x_range = [-2*PI,2*PI,0.2]).set_color('#6B1012')
                plot_group.add(single_plot)
                text = MathTex(r"f(x) = cos(x) ").move_to(single_plot.get_center()).scale(0.7).set_color('#6B1012')
                name_group.add(text)
        
        self.play(function_whole.animate.shift(LEFT*4).scale(0.5),FadeIn(axes_group),rate_func=smooth)

        self.play(Create(SurroundingRectangle(axes_group,color='#6B1012'),buff=0),rate_func=smooth,run_time=1)
        self.play(FadeIn(plot_group),FadeIn(name_group),rate_func=smooth,run_time=3)
        self.wait(20)

        self.play(Wiggle(axes_group[0],color='#6B1012',buff=0),rate_func=smooth,run_time=2)
        self.play(FadeOut(*self.mobjects))


        self.next_section(name="third_scene",skip_animations=False)
        #This is another section
        main_axes = NumberPlane(x_range=[0,6,1],y_range=[0,4,1],axis_config={"include_numbers":True},y_axis_config={"label_direction":LEFT}).shift(LEFT).set_color('#14014B')
        main_graph = main_axes.plot(lambda x : 0.5 * x, x_range=[0,6,1]).set_color('#6B1012')
        x_label = main_axes.get_x_axis_label("x values",DOWN)
        y_label = main_axes.get_y_axis_label("f(x)",direction=LEFT).rotate(-90*DEGREES)
        self.play(Create(main_axes),Create(main_graph),Create(x_label),Create(y_label),rate_func=smooth)
        self.wait(6)
        steady_dot = Dot(main_graph.point_from_proportion(0.7)).set_color('#14014B')
        dynamic_dot = Dot(main_graph.point_from_proportion(0.1)).set_color('#14014B')


        main_function_name = MathTex(r"f(x) = \frac{1}{2}x").scale(0.5).next_to(main_graph,UP,buff=0.2).set_color('#6B1012')
        self.play(Create(main_function_name))
    
        steady_indicator = always_redraw(
            lambda : main_axes.get_lines_to_point(steady_dot.get_center()).set_color('#14014B')
        )

        dynamic_indicator = always_redraw(
            lambda : main_axes.get_lines_to_point(dynamic_dot.get_center()).set_color('#14014B')
        )
        
        change_table = always_redraw(
            lambda : Table([['f(x)',f"{main_axes.p2c(dynamic_dot.get_center())[1]:.1f}"],
                     ["x",f" {main_axes.p2c(dynamic_dot.get_center())[0]:.1f}"]],include_outer_lines=True,element_to_mobject=Tex).set_color("#14014B").scale(0.5).move_to([3.5,1.5,0])
        )
        
        steady_table = Table([['f(x)',f"{main_axes.p2c(steady_dot.get_center())[1]:.1f}"],
                             ["x",f" {main_axes.p2c(steady_dot.get_center())[0]:.1f}"]],include_outer_lines=True,element_to_mobject=Tex).set_color("#14014B").scale(0.5).next_to(change_table,DOWN,buff=1)

        steady_name = Text("Stationary point").set_color('#14014B').scale(0.4).next_to(steady_table,UP,buff=0.1)
        changing_name = Text("Changing point").set_color('#14014B').scale(0.4).next_to(change_table,UP,buff=0.1)
       
        self.play(Create(dynamic_indicator),Create(dynamic_dot),Create(change_table),FadeIn(changing_name),rate_func=smooth)

        self.play(dynamic_dot.animate.move_to(main_graph.point_from_proportion(0.95)),rate_func=smooth,run_time=3)

        self.play(dynamic_dot.animate.move_to(main_graph.point_from_proportion(0.1)),rate_func=smooth,run_time=3)

        self.play(dynamic_dot.animate.move_to(main_graph.point_from_proportion(0.7)),rate_func=smooth,run_time=2)
        
        self.play(FadeIn(steady_dot), FadeIn(steady_indicator),FadeIn(steady_name),FadeIn(steady_table),rate_func=smooth)
        
        self.wait(4)

        self.play(Indicate(steady_dot),FadeIn(steady_table))
        self.play(dynamic_dot.animate.move_to(main_graph.point_from_proportion(0.2)),rate_func=smooth,run_time=1)
        self.play(dynamic_dot.animate.move_to(main_graph.point_from_proportion(0.9)),rate_func=smooth,run_time=1)
        self.play(dynamic_dot.animate.move_to(main_graph.point_from_proportion(0.3)),rate_func=smooth,run_time=1)
        self.play(dynamic_dot.animate.move_to(main_graph.point_from_proportion(0.95)),rate_func=smooth,run_time=1)
        self.play(dynamic_dot.animate.move_to(main_graph.point_from_proportion(0.2)),rate_func=smooth,run_time=1)

        self.wait(4)
        change_table_cell_x = always_redraw(
            lambda :change_table.get_cell((2,2),color=YELLOW)
        )
        change_table_cell_y = always_redraw(
            lambda : change_table.get_cell((1,2),color=YELLOW)
        )
        steady_table_cell_x = steady_table.get_cell((2,2),color=YELLOW)
        steady_table_cell_y = steady_table.get_cell((1,2),color=YELLOW)

        self.play(Create(steady_table_cell_y),rate_func=smooth,run_time=1.5)
        self.wait(1)
        self.play(Uncreate(steady_table_cell_y),Create(change_table_cell_x),Create(steady_table_cell_x),rate_func=smooth,run_time=1.5,lag_ratio=1)
        self.wait(1)
        self.play(dynamic_dot.animate.move_to(main_graph.point_from_proportion(0.6)),rate_func=smooth,run_time=3)

        self.add_fixed_in_frame_mobjects(changing_name,steady_name,change_table,steady_table)
        self.play(FadeOut(VGroup(change_table_cell_x,steady_table_cell_x)))
        self.move_camera(zoom=4,frame_center=dynamic_dot.get_center())
        steady_table_cell_y = steady_table.get_cell((1,2),color=YELLOW)
        self.play(Create(steady_table_cell_y),Create(change_table_cell_y),rate_func=smooth)
        self.play(dynamic_dot.animate.move_to(main_graph.point_from_proportion(0.688899999)),rate_func=smooth,run_time=5)

        self.move_camera(zoom=1,frame_center=ORIGIN)
        self.wait(10)
        
        Third_scene_mobjects = Group(*self.mobjects)
        self.next_section(name="fourth_scene",skip_animations=False)
        #This is the next section. 
        
        limit = MathTex(r"\lim_{x \to a} F(x) = L").scale(0.7).set_color('#6B1012').next_to(steady_table,DOWN,buff=0.5)

        self.play(Write(limit),run_time=4,rate_func=smooth)
        self.wait(2)
        self.play(Wiggle(limit))
        self.wait(15)
        self.play(FadeOut(Third_scene_mobjects),limit.animate.move_to((0,1.2,0)),lag_ratio=0)
        limit_title = Text("Limits").scale(0.5).move_to(ORIGIN).set_color('#6B1012')
        
        flowchart_head = Circle(radius=1).set_color(color='#14014B')
        flowchart_left = Circle(radius=1.1).set_color(color='#14014B').shift(LEFT*2.5)
        flowchart_right = Circle(radius=1.1).set_color(color='#14014B').shift(RIGHT*2.5)
        left_limit_title = Text(r"Left hand limits").set_color('#6B1012').scale(0.4)
        right_limit_title = Text(r"Right hand limits").set_color('#6B1012').scale(0.4)

        math_left_limit_title = MathTex(r"\lim_{x \to a^-} f(x) = L").next_to(flowchart_left,DOWN,buff=0.1).scale(0.7).set_color('#6B1012')
        math_right_limit_title = MathTex(r"\lim_{x \to a^+} f(x) = L").next_to(flowchart_right,DOWN,buff=0.1).scale(0.7).set_color('#6B1012')

        limit.add_updater(
            lambda mob: mob.next_to(flowchart_head,UP)
        )

        self.play(FadeIn(limit_title))
        self.wait(10)
        self.play(FadeIn(flowchart_head),limit_title.animate.move_to(flowchart_head.get_center()),rate_func=smooth,run_time=2)
        self.wait(2)
        limit_title.add_updater(
            lambda mob: mob.move_to(flowchart_head.get_center())
        )

        left_limit_title.add_updater(
            lambda mob: mob.move_to(flowchart_left.get_center())
        )

        right_limit_title.add_updater(
            lambda mob: mob.move_to(flowchart_right.get_center())
        )

        self.play(flowchart_head.animate.shift(UP*2),rate_func=smooth)

        link_left = ArcBetweenPoints(start=flowchart_head.get_left(),end = flowchart_left.get_top(),angle=45*DEGREES).set_color('#14014B')
        link_right = ArcBetweenPoints(start=flowchart_head.get_right(), end = flowchart_right.get_top(),angle=-45*DEGREES).set_color('#14014B')

        self.play(Create(link_left),FadeIn(VGroup(flowchart_left,left_limit_title)),
                  FadeIn(math_left_limit_title),
                  rate_func=smooth,lag_ratio=1,run_time=1)
        
        self.play(Create(link_right),
                  FadeIn(VGroup(flowchart_right,right_limit_title)),
                  FadeIn(math_right_limit_title),
                rate_func=smooth,lag_ratio=1,run_time=1)
            
        self.wait(4)

        limit_group = VGroup(math_left_limit_title,math_right_limit_title)
        self.play(FadeOut(VGroup(limit,limit_title,left_limit_title,
        right_limit_title,flowchart_head,flowchart_left,
        flowchart_right,link_left,link_right)),
        limit_group.animate.arrange_in_grid(rows=2,cols=1,buff=2).to_corner(UR),
        rate_func=smooth,run_time=1)

        self.wait(5)
        self.next_section(name="fifth_scene",skip_animations=False)
        #This is another section
        func_axes = NumberPlane(x_range=[0,6,1],y_range=[0,6,1],axis_config={"include_numbers":True},y_axis_config={"label_direction":LEFT}).set_color('#6B1012').scale(1)
        func_graph = func_axes.plot(lambda x: x ,x_range=[0,6,1]).set_color('#14014B')
        left_dot = Dot(func_graph.point_from_proportion(0.2)).set_color('#6B1012')
        right_dot = Dot(func_graph.point_from_proportion(0.9)).set_color('#6B1012')
        stable_dot = Dot(func_graph.point_from_proportion(0.5)).set_color('#6B1012')
    
        stable_dot_lines = always_redraw(
            lambda : func_axes.get_lines_to_point(stable_dot.get_center()).set_color('#6B1012')
        )
        
        left_dot_lines = always_redraw(
            lambda : func_axes.get_lines_to_point(left_dot.get_center()).set_color('#6B1012')
        )

        right_dot_lines = always_redraw(
            lambda : func_axes.get_lines_to_point(right_dot.get_center()).set_color('#6B1012')
        )

        func_x_axis = func_axes.get_x_axis_label("x-values",direction=DOWN).set_color('#6B1012').shift(LEFT*4 + (DOWN*0.5)).scale(0.7)
        func_y_axis = func_axes.get_y_axis_label("f(x)",direction=LEFT).set_color('#6B1012').shift(DOWN*3).rotate(90*DEGREES).scale(0.7)

        func_label = Text("f(x) = x").scale(0.7).to_corner(UP).set_color('#6B1012')
        
        self.play(FadeIn(func_axes),FadeIn(func_graph),FadeIn(func_x_axis),FadeIn(func_y_axis),FadeIn(func_label))
        self.wait(2)
        self.play(FadeIn(stable_dot),FadeIn(left_dot),FadeIn(stable_dot_lines),FadeIn(left_dot_lines))

        self.wait(2)
        self.play(math_right_limit_title.animate.set_opacity(0.3))

        self.play(FadeIn(right_dot),FadeIn(right_dot_lines))
        self.play(Wiggle(math_left_limit_title),Circumscribe(math_left_limit_title))
        self.play(left_dot.animate.move_to(func_graph.point_from_proportion(0.48)),rate_func=smooth,run_time=7)
        self.wait(2)

        self.play(left_dot.animate.move_to(func_graph.point_from_proportion(0.2)),rate_func=smooth)
        self.play(math_right_limit_title.animate.set_opacity(1),math_left_limit_title.animate.set_opacity(0.3))

        self.play(Wiggle(math_right_limit_title),Circumscribe(math_right_limit_title))
        self.play(right_dot.animate.move_to(func_graph.point_from_proportion(0.52)),rate_func=smooth,run_time=7)

        self.play(right_dot.animate.move_to(func_graph.point_from_proportion(0.9)),rate_func=smooth)     
        self.wait(15)
        self.play(math_left_limit_title.animate.set_opacity(1))
        self.play(FadeOut(*self.mobjects))

        self.wait(5)

class limits_2(ThreeDScene):
    def construct(self):
        Graph = NumberPlane(y_range=[-2,5,1],x_range=[-5,4,1],y_axis_config= {"include_numbers":True,"label_direction":LEFT},x_axis_config={"include_numbers":True}).set_color('#14014B').scale(0.8).shift(LEFT*2)
        
        func = MathTex(
            r"f(x) = \begin{cases} "
            r"x + 3 & \text{if } x > 0 \\ "
            r"-x & \text{if } x < 0 "
            r"\end{cases}"
        ).set_color('#6B1012').scale(0.5)

        piecewise_1 = Graph.plot(lambda x: x + 2, x_range=[0,3,1]).set_color('#6B1012')
        piecewise_2 = Graph.plot(lambda x: -x,x_range=[-5,0,1]).set_color('#6B1012')
        right_dot = Dot(piecewise_1.point_from_proportion(0.9)).set_color('#6B1012')
        left_dot = Dot(piecewise_2.point_from_proportion(0.1)).set_color('#6B1012')

        self.play(FadeIn(func),rate_func=smooth)
        self.play(func.animate.to_corner(UP),rate_func=smooth,run_time=2)
        self.play(FadeIn(Graph),Create(piecewise_1),Create(piecewise_2),rate_func=smooth)


        text1 = MathTex(r"\text{as x} \to \text{0 for both limits}").set_color('#14014B').scale(0.5).move_to([4,3,0])
        text2 = MathTex(r"\text{y values}").scale(0.5).set_color('#14014B').next_to(text1,DOWN,buff=0.3)

        text3 = always_redraw(
            lambda : MathTex(fr"\text{{left point: }} {Graph.p2c(left_dot.get_center())[1]:.1f}").scale(0.5).set_color('#14014B').next_to(text2,DOWN)
        )

        text4 = always_redraw(
            lambda : MathTex(fr"\text{{right point}}: {Graph.p2c(right_dot.get_center())[1]:.1f}").scale(0.5).set_color('#14014B').next_to(text3,DOWN)
        )

        self.play(FadeIn(left_dot),FadeIn(right_dot),Write(text1),Write(text2),Write(text3),Write(text4),rate_func=smooth)

        self.play(left_dot.animate.move_to(piecewise_2.point_from_proportion(0.98)),
                  right_dot.animate.move_to(piecewise_1.point_from_proportion(0.001)),rate_func=smooth,run_time=2)
    

        left_limit = Tex("Left limit = 0").set_color('#6B1012').scale(0.5).next_to(text4,DOWN,buff=2)
        right_limit = Tex("Right Limit = 2").set_color('#6B1012').scale(0.5).next_to(left_limit,DOWN,buff=0.1)
        self.play(FadeIn(left_limit),FadeIn(right_limit),rate_func=smooth)
        on_screen_mob = Group(*self.mobjects)
        self.wait(4)
        limit_text = MathTex(r"\text{Left hand limit} \neq \text{ Right hand limit}").scale(0.5).set_color('#6B1012').move_to(left_limit.get_center())
        limit_text2 = MathTex(r"\text{Left hand limit  =}  \text{ Right hand limit}").scale(0.5).set_color('#6B1012').move_to(ORIGIN)
        
        self.play(TransformMatchingShapes(VGroup(left_limit,right_limit),limit_text),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeOut(on_screen_mob),limit_text.animate.move_to(ORIGIN),rate_func=smooth,run_time=2)
        limit_exist_2 = Text("Limit exists when...").scale(0.5).set_color('#14014B').next_to(limit_text2,UP)
        limit_exist = Text("Limit does not exist when...").scale(0.5).set_color('#14014B').next_to(limit_text,UP)
        self.play(FadeIn(limit_exist))
        self.play(Wait(5))
        self.play(Transform(limit_text,limit_text2),Transform(limit_exist,limit_exist_2),rate_func=smooth)
        self.wait(5)
    
        self.play(FadeOut(Group(*self.mobjects)))
        Out_text = Text("Like, share and subscribe").scale(0.5).set_color('#6B1012').move_to(ORIGIN)
        Out_text_2 = Text("Thanks for watching").scale(0.5).set_color('#6B1012').next_to(Out_text,DOWN)

        self.play(Write(Out_text),rate_func=smooth)
        self.wait(2)
        self.play(Write(Out_text_2),rate_func=smooth)
        self.wait(15)   
