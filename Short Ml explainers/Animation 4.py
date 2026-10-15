from manim import *
import numpy as np
from scipy.stats import norm
config.background_color = '#0E0E0E'


class gaussian_distribution(Scene):
    def construct(self):
        #Scholar logo
        logo = ImageMobject("Items\Animation_4\Logo.jpeg").scale(0.07).to_corner(UL,buff=0.1)
        self.add(logo)
        
        #The Axes, mean and standard deviation of the Gaussian curve
        axes = Axes(x_range=[-5,5,1],y_range=[0,0.3,0.05],
                    x_axis_config={"include_numbers":True,"numbers_to_include":[-4,-2,0,2,4]}).set_color("#B0B0B0").scale(0.35).to_corner(UP).shift(LEFT*3.5)
        mean = 0
        standard_deviation = 3

        gaussian_curve = axes.plot(lambda x: norm.pdf(x,mean,standard_deviation),
                                   x_range=[-5,5]).set_color("#00C9A7")
        

        gen_ai_model = Polygon([0,1.5,0],[3,2,0],[3,-2,0],[0,-1.5,0]).move_to([0,0,0]).scale(0.7)
        gen_ai_text = VGroup(Text("Generative"),
                             Text("AI")).arrange(DOWN).scale(0.35).move_to(gen_ai_model.get_center())

        #Vectors
        vector_1 = Matrix([[5],[2],[4]]).next_to(gaussian_curve,DOWN*2.2).scale(0.6)
        vector_2 = Matrix([[3],[1],[3]]).next_to(gaussian_curve,DOWN*2.2).scale(0.6)
        vector_3 = Matrix([[2],[4],[1]]).next_to(gaussian_curve,DOWN*2.2).scale(0.6)

        vectors = Group(vector_1,vector_2,vector_3)

        #Collection of images
        image_1 = ImageMobject("Items/Animation_4\Picture 1.png").next_to(gen_ai_model,RIGHT,buff=0.5)
        image_2 = ImageMobject("Items/Animation_4\Picture 3.png").next_to(gen_ai_model,RIGHT,buff=0.5)
        image_3 = ImageMobject("Items/Animation_4\Picture 4.png").next_to(gen_ai_model,RIGHT,buff=0.5)   

        images = Group(image_1,image_2,image_3)
        #This function is meant to help position the vectors and images after they interact with the generative Ai trapezoid
        
        def position(mob,position):
            self.play(mob.animate.next_to(position,RIGHT,buff=0.5),rate_func=smooth)

        #This function is meant to repeat the process of generating the images
        def process(entry,exit,vector_position,image_position):
            self.play(TransformFromCopy(gaussian_curve,entry),rate_func=smooth)
            self.wait(0.5)
            self.play(entry.animate.move_to(gen_ai_model.get_center()),FadeOut(gen_ai_text),rate_func=smooth)
            self.wait(0.5)
            self.play(FadeIn(exit),rate_func=smooth)
            position(exit,image_position)
            position(entry,vector_position)
            self.play(FadeIn(gen_ai_text))
            self.wait(0.5)

        self.wait(0.5)
        self.play(FadeIn(axes), FadeIn(Group(gen_ai_model, gen_ai_text)), FadeIn(gaussian_curve))
        self.wait(0.5)

        #Calling the function that fadeins the images and positions them
        process(vector_1,image_1,[-2,-3,0],[0.5,3,0])
        process(vector_2,image_2,vector_1.get_right(),image_1.get_right())
        process(vector_3,image_3,vector_2.get_right(),image_2.get_right())

        self.wait(0.5)
        self.play(FadeOut(Group(gen_ai_model,gen_ai_text,axes,gaussian_curve)))
        self.wait(0.5)
        self.play(vectors.animate.arrange(buff=1).move_to([0,-3,0]),images.animate.move_to([0,3,0]),rate_func=smooth)
        self.wait(0.5)
        
        #New set of mobjects. graphs and PCA text
        pca_text = Text("PCA 2D").move_to([3,-1,0]).scale(0.5)
        graph_1 = ImageMobject("Items\Animation_4\Picture 5.png").next_to(image_1,DOWN)
        graph_2 = ImageMobject("Items/Animation_4/Picture 6.png").next_to(image_2,DOWN)
        graph_3 = ImageMobject("Items\Animation_4\Picture 7.png").next_to(image_3,DOWN)

        graphs = Group(graph_1,graph_2,graph_3)

        lower_arrows = VGroup()
        upper_arrows = VGroup()

        for i in range(3):
            arrow_bottom = Arrow(start=vectors[i].get_top(),end=pca_text.get_bottom(),tip_shape=StealthTip).set_color("#00C9A7").set_stroke(width=1.5)
            arrow_top =Arrow(start=pca_text.get_top(),end=graphs[i].get_bottom(),tip_shape=StealthTip).set_color("#00C9A7").set_stroke(width=1.5)
            lower_arrows.add(arrow_bottom)
            upper_arrows.add(arrow_top)
        
        self.play(FadeIn(pca_text),FadeIn(lower_arrows),rate_func=smooth)
        self.wait(0.5)
        self.play(FadeIn(graphs),FadeIn(upper_arrows),rate_func=smooth)
        self.wait(0.5)
