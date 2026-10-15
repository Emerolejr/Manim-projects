from manim import *
config.background_color='#0E0E0E'

class gen_Ai(Scene):
    def construct(self):
        
        #Cloud mobject, gen_ai_mobjects and Lego collections mobjects
        cloud = SVGMobject("Items/Animation 3/cloud1-svgrepo-com.svg").scale(1.5).set_color(WHITE).set_fill(opacity=0.4).move_to([-3.5,-0.5,0])
        cloud_text = VGroup(Text("Random Lego"),Text("input")).arrange(DOWN).scale(0.4).move_to(cloud.get_center())
        gen_ai_model = Polygon([0,1.5,0],[3,2,0],[3,-2,0],[0,-1.5,0]).move_to([2.7,-0.5,0])
        gen_ai_text = VGroup(Text("Human"),Text("Generative"),Text("Intelligence")).arrange(DOWN).scale(0.4).move_to(gen_ai_model.get_center())

        #These are the photoes for the entire lego collection
        lego_1 = ImageMobject("Items\Animation 3\Bridge scattered.png").scale(0.4).next_to(cloud,UP,buff=1)
        lego_1_1 = ImageMobject("Items\Animation 3\Bridge.png").scale(0.5).next_to(gen_ai_model,RIGHT,buff=0.5)

        lego_2 = ImageMobject("Items\Animation 3\House scattered.png").scale(0.4).next_to(cloud,UP,buff=1)
        lego_2_2 = ImageMobject("Items\Animation 3\House.png").scale(0.5).next_to(gen_ai_model,RIGHT,buff=0.5)

        lego_3 = ImageMobject("Items\Animation 3\Car scattered.png").scale(0.4).next_to(cloud,UP,buff=1)
        lego_3_3 = ImageMobject("Items\Animation 3\Car.png").scale(0.5).next_to(gen_ai_model,RIGHT,buff=0.5)

        
        self.wait(1)
        self.play(FadeIn(cloud),FadeIn(cloud_text),rate_func=smooth)
        self.wait(1)

        self.play(FadeIn(lego_1),rate_func=smooth)
        self.wait(1)
        self.play(Wiggle(cloud),rate_func=smooth)

        self.wait(1)
        self.play(FadeOut(cloud_text),lego_1.animate.move_to(cloud.get_center()),rate_func=smooth)
        self.wait(1)
        self.play(FadeIn(gen_ai_model),FadeIn(gen_ai_text),rate_func=smooth)
        self.wait(1)
        self.play(lego_1.animate.move_to([-0.4,-0.5,0]),FadeIn(cloud_text),rate_func=smooth)

        self.wait(1)

        self.play(lego_1.animate.move_to(gen_ai_model.get_center()),FadeOut(gen_ai_text),rate_func=smooth)
        self.wait(1)

        self.play(TransformFromCopy(lego_1,lego_1_1),rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(lego_1),FadeIn(gen_ai_text),rate_func=smooth)

        self.wait(1)

        self.play(FadeOut(lego_1_1),rate_func=smooth)
        
        self.wait(1)


        #This is a defined function that repeats the entire code for the lego function above.
        def processing(entry,output):
            self.wait(1)
            self.play(FadeIn(entry),rate_func=smooth)
            self.wait(1)
            self.play(Wiggle(cloud),rate_func=smooth)

            self.wait(1)
            self.play(FadeOut(cloud_text),entry.animate.move_to(cloud.get_center()),rate_func=smooth)
    
            self.wait(1)
            self.play(entry.animate.move_to([-0.4,-0.5,0]),FadeIn(cloud_text),rate_func=smooth)

            self.wait(1)

            self.play(entry.animate.move_to(gen_ai_model.get_center()),FadeOut(gen_ai_text),rate_func=smooth)
            self.wait(1)

            self.play(TransformFromCopy(entry,output),rate_func=smooth)
            self.wait(1)
            self.play(FadeOut(entry),FadeIn(gen_ai_text),rate_func=smooth)
            self.wait(1)

            self.play(FadeOut(output),rate_func=smooth)
            
            self.wait(1)

        processing(lego_2,lego_2_2)
        self.wait(1)
        processing(lego_3,lego_3_3)

        self.wait(1)
        