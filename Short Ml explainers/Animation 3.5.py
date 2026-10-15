from manim import *
import numpy as np
from scipy.stats import norm
config.background_color = '#0E0E0E'


class gaussian_distribution(Scene):
    def construct(self):
        axes = Axes(x_range=[-5,5,1],y_range=[0,0.3,0.05],
                    x_axis_config={"include_numbers":True,"numbers_to_include":[-4,-2,0,2,4]}).set_color("#B0B0B0").scale(0.4).to_corner(UP).shift(LEFT*3)
        
        #The mean  and standard deviation of th Gaussian curve
        mean = 0
        standard_deviation = 3

        gaussian_curve = axes.plot(lambda x: norm.pdf(x,mean,standard_deviation),
                                   x_range=[-5,5]).set_color("#00C9A7")
        
        gen_ai_model = Polygon([0,1.5,0],[3,2,0],[3,-2,0],[0,-1.5,0]).move_to([2.7,-1,0]).scale(0.7)
        gen_ai_text = VGroup(Text("Generative"),
                             Text("AI")).arrange(DOWN).scale(0.3).move_to(gen_ai_model.get_center())

        #Vectors
        vector_1 = Matrix([[5],[2],[4],[1]]).next_to(gaussian_curve,DOWN*2.7).scale(0.5)
        vector_2 = Matrix([[3],[1],[3],[2]]).next_to(gaussian_curve,DOWN*2.7).scale(0.5)
        vector_3 = Matrix([[2],[4],[1],[7]]).next_to(gaussian_curve,DOWN*2.7).scale(0.5)

        #Collection of images
        image_1 = ImageMobject("Items\Animation 4/fried-chicken-with-grilled-potatoes-eggplants-tomatoes-peppers.jpg").scale(0.04).next_to(gen_ai_model,RIGHT,buff=0.5)
        image_2 = ImageMobject("Items\Animation 4/pink-flower-white-background.jpg").scale(0.04).next_to(gen_ai_model,RIGHT,buff=0.5)
        image_3 = ImageMobject("Items\Animation 4/vertical-shot-cute-dog-sitting-fluffy-white-fabric (2).jpg").scale(0.04).next_to(gen_ai_model,RIGHT,buff=0.5)


        #This function is meant to repeat the process of generating the images
        def process(entry,exit):
            self.play(TransformFromCopy(gaussian_curve,entry),rate_func=smooth)
            self.wait(1)
            self.play(entry.animate.move_to(gen_ai_model.get_center()),FadeOut(gen_ai_text),rate_func=smooth)
            self.wait(1)
            self.play(FadeOut(entry),FadeIn(exit),rate_func=smooth)
            self.wait(1)
            self.play(FadeOut(exit),FadeIn(gen_ai_text),rate_func=smooth)
            self.wait(1)

        self.wait(1)
        self.play(FadeIn(axes), FadeIn(Group(gen_ai_model, gen_ai_text)), FadeIn(gaussian_curve))
        self.wait(1)
        process(vector_1,image_1)
        process(vector_2,image_2)
        process(vector_3,image_3)
        
