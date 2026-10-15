from manim import *
config.background_color = '#0E0E0E'


class Probability_distribution(Scene):
    def construct(self):

        ## Probability distribution and cloud Mobjects
        cloud = SVGMobject("Items/fluffy-cloud-svgrepo-com.svg",fill_color="#B0B0B0",fill_opacity=1,stroke_width=None).to_corner(UP).scale(scale_stroke=False,scale_factor=1.1)
        cloud.set_stroke(width=0.1)
        prob_distri_text = Text("Probability distribution",font="Montserrat").set_color(WHITE).scale(0.4).move_to(cloud.get_center()+[0,-0.2,0])
    
        self.wait(1)
        self.play(FadeIn(VGroup(cloud,prob_distri_text)),rate_func=smooth)
        self.wait(1)


        # Arrow + population mobjects
        arrow_1 = Arrow(start=cloud.get_bottom(),end=cloud.get_bottom()+[0,-1.2,0],tip_shape=StealthTip,buff=0.1).set_color('#00C9A7')
        population = Text("Population: H T T H T H T...").scale(0.4).next_to(arrow_1,DOWN,buff=0.2)

        self.play(GrowFromEdge(arrow_1,arrow_1.get_start()),FadeIn(population),rate_func=smooth,run_time=1)
        self.wait(1)
       
        # 2 Arrow, Sample mobjects
        heads_and_tails = Text("H T H T").scale(0.4).next_to(population,DOWN + [0,-4,0])
        sample = Text("Sample").scale(0.4).next_to(population,DOWN + [0,-4,0])
        arrow_2 = Arrow(start=population.get_bottom(),end=sample.get_top(),tip_shape=StealthTip).set_color('#00C9A7')
        
        ## Loop that sets opacity of heads and tails to zero to help with the effect of one by one transfrom from copy 
        for letter in heads_and_tails:
            letter.set_opacity(0)

        self.play(Succession(
            *[
                AnimationGroup(
                    TransformFromCopy(population[i], heads_and_tails[j]),
                    heads_and_tails[j].animate.set_opacity(1)
                )
                for i, j in zip([11, 12, 14, 15], range(4))
            ],
            lag_ratio=0.7,
            run_time=3,
            rate_func=smooth
        ))


        self.wait(1)
        self.play(heads_and_tails.animate.shift(RIGHT*2),rate_func=smooth,run_time=0.5)

        arrow_3 = Arrow(start=sample.get_right(),end=heads_and_tails.get_left(),tip_shape=StealthTip).set_color('#00C9A7')

        self.play(GrowFromPoint(arrow_2,arrow_2.get_start()),FadeIn(VGroup(arrow_3,sample)),rate_func=smooth)

        ## Binomial random variables mobjects
        arrow_4 = Arrow(start=sample.get_bottom(),end = sample.get_bottom() + [0,-1.2,0],tip_shape=StealthTip).set_color('#00C9A7')
        binomial_text = Text("Binomial Random Variables").scale(0.4).next_to(arrow_4,DOWN)

        self.play(FadeIn(binomial_text),GrowFromPoint(arrow_4,arrow_4.get_start()),rate_func=smooth)

        ## Curved arrow mobject linking probality distribution and binomial random varible texts 
        arrow_5 = CurvedArrow(start_point=binomial_text.get_left()+[-0.1,0,0],end_point=cloud.get_left()+[-0.1,0,0],tip_shape=StealthTip,angle=-120*DEGREES).set_color('#00C9A7')

        self.play(Create(arrow_5))

        self.wait(1)

        ## Parameters mobjects
        parameter = VGroup(Text("Parameters"),Text("n,p")).arrange(DOWN).scale(0.4).next_to(arrow_5,LEFT)
        
        self.play(FadeIn(parameter))
        self.wait(1)


        # Scaling down mobjects in the screen and 
        on_screen_mobjects = Group(*self.mobjects)
        self.play(on_screen_mobjects.animate.scale(0.8).shift(DOWN))
        self.wait(1)

        # Surrounding rectangle mobject and estimating data
        estimating_data_text = VGroup(Text("Estimating parameters from Sample"),
                                      Text("(training data)")).arrange(DOWN).next_to(on_screen_mobjects,UP).scale(0.5).shift(RIGHT)
        rect_estimating_data_text = SurroundingRectangle(estimating_data_text).set_color('#00C9A7')

        self.play(Write(estimating_data_text),rate_func=smooth)
        self.play(Create(rect_estimating_data_text),rate_func=smooth,run_time=1.5)
       
        self.wait(1)
        self.play(ApplyWave(VGroup(estimating_data_text,rect_estimating_data_text),RIGHT),run_time=1.5,rate_func=smooth)
        self.wait(1)
