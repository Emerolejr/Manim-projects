from manim import *
from manim.opengl import *
config.background_color="#ECEAEA"
import numpy as np


color_list = ["#CFC64A","#2A3BA0","#918F77","#4C3D6D","#595366","#3B3A26"]


class intro(MovingCameraScene):
    def construct(self):

        circles = VGroup()
        theorems = VGroup()

        for i in range(8):
            circ = Circle(radius=1.5)
            circles.add(circ)

        #First theorem.
        chord_1 = Line(start=circles[0].point_at_angle(220*DEGREES),end=circles[0].point_at_angle(320*DEGREES))
        radius_1 = Line(start=circles[0].get_center(),end=chord_1.get_center())
        theorem_1 = VGroup(chord_1,radius_1,circles[0]).set_color("#CFC64A")

        theorems.add(theorem_1)
        #####Second theorem.
        
        ### points
        p_centre = circles[1].get_center()
        p_90 = circles[1].point_at_angle(90*DEGREES)
        p_220 = circles[1].point_at_angle(220*DEGREES)
        p_270 = circles[1].point_at_angle(270*DEGREES)
        p_320 = circles[1].point_at_angle(320*DEGREES)

        line_1 = Line(start=p_centre,end=p_220)
        line_2 = Line(start=p_220,end=p_270)
        line_3 = Line(start=p_270,end=p_320)
        line_4 = Line(start=p_centre,end=p_320)

        line_5 = Line(start=p_220,end=p_90)
        line_6 = Line(start=p_90,end=p_320)

        #Measured from top to bottom
        
        angle_2 = Angle(line_1,line_4,radius=0.1)
        angle_3 = Angle(line_4,line_1,radius=0.1)

        theorem_2 = VGroup(line_1,line_2,line_3,line_4,line_5,line_6,angle_2,angle_3,circles[1]).set_color("#897BA6")
        
        theorems.add(theorem_2)
        ######Third theorem
        p_2_60 = circles[2].point_at_angle(60*DEGREES)
        p_2_90 = circles[2].point_at_angle(90*DEGREES)
        p_2_120 = circles[2].point_at_angle(120*DEGREES)
        p_2_220 =  circles[2].point_at_angle(220*DEGREES)
        p_2_320 = circles[2].point_at_angle(320*DEGREES)
        
        line_2_1 = Line(start=p_2_220,end=p_2_120)
        line_2_2 = Line(start=p_2_120,end=p_2_320)
        line_2_3 = Line(start=p_2_220,end=p_2_90)
        line_2_4 = Line(start=p_2_90,end=p_2_320)
        line_2_5 = Line(start=p_2_220,end=p_2_60)
        line_2_6 = Line(start=p_2_60,end=p_2_320)

        theorem_3 = VGroup(line_2_1,line_2_2,line_2_3,line_2_4,line_2_5,line_2_6,circles[2]).set_color("#918F77")

        theorems.add(theorem_3)
        ######Fourth theorem.

        p_3_0 = circles[3].point_at_angle(0*DEGREES)
        p_3_120 = circles[3].point_at_angle(120*DEGREES)
        p_3_180 = circles[3].point_at_angle(180*DEGREES)

        centre =Dot(circles[3].get_center())
        line_3_1 = Line(start=p_3_0,end=p_3_180)
        line_3_2 = Line(start=p_3_180,end = p_3_120)
        line_3_3 = Line(start=p_3_120,end= p_3_0)

        theorem_4 = VGroup(circles[3],centre,line_3_1,line_3_2,line_3_3).set_color("#595366")

        theorems.add(theorem_4)

        ######Fifth Theorem
        p_4_180 = circles[4].point_at_angle(180*DEGREES)
        p_4_90 = circles[4].point_at_angle(90*DEGREES)
        p_4_20 = circles[4].point_at_angle(20*DEGREES)
        p_4_260 = circles[4].point_at_angle(260*DEGREES)

        line_4_1 = Line(start=p_4_20,end=p_4_90)
        line_4_2 = Line(start=p_4_90,end=p_4_180)
        line_4_3 = Line(start=p_4_180,end=p_4_260)
        line_4_4 = Line(start=p_4_260,end=p_4_20)

        theorem_5 = VGroup(circles[4],line_4_1,line_4_2,line_4_3,line_4_4).set_color("#3B3A26")

        theorems.add(theorem_5)

        ########Theorem 6
        p_5_270 = circles[5].point_at_angle(270*DEGREES)
        p_5_170 = circles[5].point_at_angle(170*DEGREES)
        p_5_30 = circles[5].point_at_angle(30*DEGREES)

        line_5_1 = Line(start=p_5_30,end=p_5_170)
        line_5_2 = Line(start=p_5_170,end = p_5_270)
        line_5_3 = Line(start=p_5_270,end=p_5_30)

        line_5_4 = TangentLine(circles[5],0.75,length=4)

        theorem_6 = VGroup(circles[5],line_5_1,line_5_2,line_5_3,line_5_4).set_color("#3B3A26")

        theorems.add(theorem_6)
        ######Theorem 7. 
        p_6_centre = circles[6].get_center()
        p_6_270 = circles[6].point_at_angle(270*DEGREES)
        centre_6 = Dot(circles[6].get_center())
        line_6_1 = Line(start=p_6_centre,end=p_6_270)
        line_6_2 = TangentLine(circles[6],alpha=0.75,length=4)

        theorem_7 = VGroup(circles[6],line_6_1,line_6_2,centre_6).set_color("#3B3A26")

        theorems.add(theorem_7)

        ######theorem 8
        out_point = Dot().next_to(circles[7],RIGHT*15)
        p_7_centre = circles[7].get_center()
        p_7_80 = circles[7].point_at_angle(80*DEGREES)
        p_7_280 = circles[7].point_at_angle(280*DEGREES)

        line_7_1 = Line(start=p_7_centre,end=p_7_80)
        line_7_2 = Line(start=p_7_centre,end=p_7_280)

        line_7_3 = Line(start=p_7_80,end=out_point.get_center())
        line_7_4 = Line(start=p_7_280,end=out_point.get_center())

        theorem_8 = VGroup(circles[7],line_7_1,line_7_2,line_7_3,line_7_4,out_point).set_color("#595366")
        theorems.add(theorem_8)

        theorems.arrange_in_grid(rows=1,cols=8,buff=1)

        state = self.camera.frame.save_state()

        self.camera.frame.move_to(circles[0])

        self.play(FadeIn(theorems))

        self.play(self.camera.frame.animate.move_to(circles[7]),rate_func=smooth,run_time=1)
        self.wait(0.5)
        self.play(Restore(state))

        self.play(self.camera.frame.animate.set(width=theorems.width*1.2),rate_func=smooth,run_time=1)

        self.play(FadeIn(Text("Circle theorems",color="#3B3A26").scale(2).next_to(theorems,UP,buff=2)))

        self.wait(1)
        self.play(FadeOut(*self.mobjects))
        self.wait(2) 


class the_parts(Scene):
    def construct(self):
        parts_of_a_circle = Text("Parts  of a Circle").scale(0.7).set_color(BLACK)
        
        self.play(FadeIn(parts_of_a_circle,shift=RIGHT),rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(parts_of_a_circle,shift=LEFT),rate_func=smooth)
        self.wait(1)

        circle_group = VGroup()
        circle_parts = VGroup(Text("Centre"),Text("Circumference"),Text("Radius"),
                              Text("Diameter"),Text("Chord"),Text("Arc"),Text("Sector"),
                              Text("Segment"),Text("Tangent"),Text("Secant")).set_color("#3B3A26").scale(0.5)
        
        for i in range(10):
            rect = RoundedRectangle(corner_radius=0.2,width=3.5,height=1).set_color("#897BA6")
            circle_group.add(rect)
        
        circle_group.arrange_in_grid(rows=5,cols=2,buff=0.2)
        
        for i in range(10):
            circle_parts[i].move_to(circle_group[i])

        for i in range(10):
            self.play(FadeIn(circle_group[i]),FadeIn(circle_parts[i]),rate_func=smooth,run_time=0.4)
        
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        

        main_circle = Circle(radius=2).set_color("#595366")
        self.play(Create(main_circle),rate_func=smooth)
        self.wait(2)

        ###PARTS OF A CIRCLE

        #Centre of a Circle
        centre = Dot(main_circle.get_center()).set_color("#918F77")

        
        indicator_1_part_1 = Arrow(start=centre.get_center() + [1,1.5,0],end=centre.get_center(),tip_shape=StealthTip,buff=0.2,tip_length=0.3)
        indicator_1_part_2 = Line(start=indicator_1_part_1.get_start(),end=indicator_1_part_1.get_start()+[2.7,0,0])
       
        centre_name = Text("Centre").scale(0.5).next_to(indicator_1_part_2,UP,buff=0.1).set_color("#3B3A26")
        indicator_1 = VGroup(indicator_1_part_1,indicator_1_part_2).set_color("#595366").set_stroke(width=1.5)        

        self.play(FadeIn(centre),run_time=1)
        self.wait(2)

        self.play(Create(indicator_1),run_time=2,lag_ratio=1)
        self.play(FadeIn(centre_name))
        self.wait(5)

        self.play(FadeOut(indicator_1),FadeOut(centre_name),rate_func=smooth)
        self.wait(2)

        #####circumference of a circle
        
        indicator_2_part_1 = Arrow(start=main_circle.get_bottom() + [-1,-1,0],end=main_circle.get_bottom(),tip_shape=StealthTip,buff=0.2,tip_length=0.3)
        indicator_2_part_2 = Line(start=indicator_2_part_1.get_start(),end=indicator_2_part_1.get_start()+[-2.7,0,0])
        indicator_2 = VGroup(indicator_2_part_1,indicator_2_part_2).set_color("#595366").set_stroke(width=1.5)

        circumference_text = Text("Circumference").scale(0.5).next_to(indicator_2_part_2,UP,buff=0.1).set_color("#3B3A26")
        main_circle_2 = main_circle.copy().set_stroke(color=RED,width=2)

        self.wait(2)
        
        
        self.play(Create(main_circle_2),rate_func=smooth,run_time=2)
        self.play(Create(indicator_2),rate_func=smooth)
        self.play(FadeIn(circumference_text),rate_func=smooth)
        self.wait(1)

        self.play(FadeOut(circumference_text),FadeOut(indicator_2),Uncreate(main_circle_2),run_time=2,rate_func=smooth)
        self.wait(2)

        ### radius
        radius = Line(start=main_circle.get_center(),end=main_circle.get_right()).set_color("#918F77")

        radius_text = Text("Radius").scale(0.5).next_to(radius,UP,buff=0.1).set_color("#3B3A26")

        self.play(Create(radius),run_time=2,rate_func=smooth)
        self.play(FadeIn(radius_text),rate_func=smooth)
        self.wait(4)

        self.play(Uncreate(radius),FadeOut(radius_text))

        self.wait(2)

        ####Chord

        chord = Line(start=main_circle.point_at_angle(230*DEGREES),end=main_circle.point_at_angle(310*DEGREES)).set_color("#918F77")
        chord_name = Text("Chord").scale(0.5).next_to(chord,UP,buff=0.1).set_color("#3B3A26")

        self.play(Create(chord),run_time=2,rate_func=smooth)
        self.play(FadeIn(chord_name),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(Uncreate(chord),FadeOut(chord_name),rate_func=smooth)
        self.wait(2)

        #### Diameter 
        diameter = Line(start=main_circle.get_left(),end=main_circle.get_right()).set_color("#918F77")
        diameter_text = Text("Diameter").scale(0.5).next_to(diameter,UP,buff=0.1).set_color("#3B3A26")

        self.wait(3)
        self.play(Create(diameter),run_time=2,rate_func=smooth)
        self.play(FadeIn(diameter_text),rate_func=smooth)


        self.play(Uncreate(diameter),FadeOut(diameter_text),rate_func=smooth)
        self.wait(2)
        #### Arcs 
        arc_1 = ArcBetweenPoints(start=main_circle.point_at_angle(0*DEGREES),end=main_circle.point_at_angle(120*DEGREES),radius=2).set_color("#918F77").set_stroke(width=4)
        arc_2 = ArcBetweenPoints(start=main_circle.point_at_angle(120*DEGREES),end=main_circle.point_at_angle(240*DEGREES),radius=2).set_color("#918F77").set_stroke(width=4)
        arc_3 = ArcBetweenPoints(start=main_circle.point_at_angle(240*DEGREES),end=main_circle.point_at_angle(360*DEGREES),radius=2).set_color("#918F77").set_stroke(width=4)

        self.wait(3)
        self.play(Create(arc_1),Create(arc_2),Create(arc_3))
        self.wait(1)
        self.play(FadeOut(main_circle))
        arc_1.save_state()
        arc_2.save_state()
        arc_3.save_state()
        self.play(arc_1.animate.shift([1,np.sqrt(3)/2,0]),run_time=1.2,rate_func=smooth)
        self.play(arc_2.animate.shift([-1,0,0]),run_time=1.2,rate_func=smooth)
        self.play(arc_3.animate.shift([[1,-np.sqrt(3)/2,0]]),run_time=1.2,rate_func=smooth)
        self.wait(1)

        arc_1_indicator_arrow = Arrow(start=arc_1.point_from_proportion(0.5)+[1,1,0],end=arc_1.point_from_proportion(0.5),buff=0.1,tip_shape=StealthTip,tip_length=0.2)
        arc_1_indicator_line = Line(start=arc_1_indicator_arrow.get_start(),end=arc_1_indicator_arrow.get_start()+[2.5,0,0])
        arc_1_indicator = VGroup(arc_1_indicator_arrow,arc_1_indicator_line).set_color("#595366").set_stroke(width=1.5)
        arc_1_name = Text("Arc").scale(0.5).next_to(arc_1_indicator_line,UP,buff=0.1).set_color("#3B3A26")

        arc_2_indicator_arrow = Arrow(start=arc_2.point_from_proportion(0.5)+[-1,-1,0],end=arc_2.point_from_proportion(0.5),buff=0.1,tip_shape=StealthTip,tip_length=0.2)
        arc_2_indicator_line = Line(start=arc_2_indicator_arrow.get_start(),end=arc_2_indicator_arrow.get_start()+[-2.5,0,0])
        arc_2_indicator = VGroup(arc_2_indicator_arrow,arc_2_indicator_line).set_color("#595366").set_stroke(width=1.5)
        arc_2_name = Text("Arc").scale(0.5).next_to(arc_2_indicator_line,UP,buff=0.1).set_color("#3B3A26")

        arc_3_indicator_arrow = Arrow(start=arc_3.point_from_proportion(0.5)+[1,-1,0],end=arc_3.point_from_proportion(0.5),buff=0.1,tip_shape=StealthTip,tip_length=0.2)
        arc_3_indicator_line = Line(start=arc_3_indicator_arrow.get_start(),end=arc_3_indicator_arrow.get_start()+[2.5,0,0])
        arc_3_indicator = VGroup(arc_3_indicator_arrow,arc_3_indicator_line).set_color("#595366").set_stroke(width=1.5)
        arc_3_name = Text("Arc").scale(0.5).next_to(arc_3_indicator_line,UP,buff=0.1).set_color("#3B3A26")

        self.play(Create(VGroup(arc_1_indicator,arc_2_indicator,arc_3_indicator)),rate_func=smooth)
        self.play(FadeIn(VGroup(arc_1_name,arc_2_name,arc_3_name)),rate_func=smooth)
        self.wait(1)

        self.play(FadeOut(VGroup(arc_1_name,arc_2_name,arc_3_name)),Uncreate(VGroup(arc_1_indicator,arc_2_indicator,arc_3_indicator)))
        self.wait(1)
        self.play(Restore(arc_1),Restore(arc_2),Restore(arc_3),FadeIn(main_circle))
        self.wait(1)
        self.play(FadeOut(VGroup(arc_1,arc_2,arc_3)))
        self.wait(1)

        ####Segments of a circle
        chord = Line(start=main_circle.point_at_angle(200*DEGREES),end=main_circle.point_at_angle(340*DEGREES)).set_color("#918F77")

        box_1 = Rectangle(width=6,height=6).next_to(chord,UP,buff=0)
        box_2 = Rectangle(width=6,height=6).next_to(chord,DOWN,buff=0)

        section_1 = Intersection(box_1,main_circle ).set_fill(opacity=0.4,color="#CFC64A").set_stroke(width=0)
        section_2 = Intersection(box_2,main_circle ).set_fill(opacity=0.4,color="#595366").set_stroke(width=0)
       
        section_name_1 = Text("Major segment").scale(0.5).move_to(section_1.get_center()).set_color("#3B3A26")
        section_name_2 = Text("Minor segment").scale(0.5).move_to(section_2.get_center()).set_color("#3B3A26")


        self.play(Create(chord),run_time=2,rate_func=smooth)
        self.wait(4)
        self.play(FadeIn(section_1),FadeIn(section_2),rate_func=smooth,run_time=2)

        self.wait(5)
        self.play(FadeIn(section_name_1),FadeIn(section_name_2))
        self.wait(2)

        self.play(Uncreate(VGroup(section_1,section_2,chord)),FadeOut(VGroup(section_1,section_2,section_name_1,section_name_2)))
        self.wait(2)

        #### Sectors

        sector_1 = Sector(radius=2,angle=90*DEGREES,start_angle=45*DEGREES).set_fill(opacity=0).set_stroke(color="#918F77",width=2).save_state()
        sector_2 = Sector(radius=2,angle=90*DEGREES,start_angle=135*DEGREES).set_fill(opacity=0).set_stroke(color="#918F77",width=2).save_state()
        sector_3 = Sector(radius=2,angle=90*DEGREES,start_angle=225*DEGREES).set_fill(opacity=0).set_stroke(color="#918F77",width=2).save_state()
        sector_4 = Sector(radius=2,angle=90*DEGREES,start_angle=315*DEGREES).set_fill(opacity=0).set_stroke(color="#918F77",width=2).save_state()


        self.play(Create(sector_1),Create(sector_2),Create(sector_3),Create(sector_4),FadeOut(main_circle),rate_func=smooth,run_time=1)
        self.play(sector_1.animate.shift(UP),sector_2.animate.shift(LEFT),
                  sector_3.animate.shift(DOWN),sector_4.animate.shift(RIGHT),rate_func=smooth,run_time=2)
        
        sector_name_1 = Text("Sector").scale(0.5).set_color("#3B3A26").move_to(sector_1.get_center())
        sector_name_2 = sector_name_1.copy().move_to(sector_2.get_center())
        sector_name_3 = sector_name_1.copy().move_to(sector_3.get_center())
        sector_name_4 = sector_name_1.copy().move_to(sector_4.get_center())
        sector_names = VGroup(sector_name_1,sector_name_2,sector_name_3,sector_name_4)

        self.wait(2)
        
        self.play(sector_1.animate.set_fill(color="#CFC64A",opacity=0.4),sector_2.animate.set_fill(color="#4C3D6D",opacity=0.4),
                  sector_3.animate.set_fill(color="#2A3BA0",opacity=0.4),sector_4.animate.set_fill(color="#918F77",opacity=0.4))
        
        self.play(FadeIn(sector_names))

        self.wait(5)
        self.play(Restore(sector_4),Restore(sector_3),Restore(sector_2),Restore(sector_1),FadeOut(sector_names),rate_func=smooth,run_time=2)

        self.wait(2)
        self.play(FadeIn(main_circle),FadeOut(VGroup(sector_1,sector_2,sector_3,sector_4)))
        self.wait(2)

        #### Tangent
        tangent = TangentLine(main_circle,alpha=0.75,length=4).set_color("#918F77")
        tangent_name = Text("Tangent").scale(0.5).set_color("#3B3A26").next_to(tangent,DOWN,buff=0.5)

        self.play(Create(tangent),FadeIn(tangent_name))
        self.wait(2)

        self.play(FadeOut(tangent_name),Uncreate(tangent))
        self.wait(2)

        ### Secant
        p_60 = main_circle.point_at_angle(60*DEGREES)
        p_240 = main_circle.point_at_angle(240*DEGREES)

        chord_final = Line(start=p_60,end=p_240).set_color("#918F77")
        secant = Line(start=[-4,0,0],end=[4,0,0]).rotate(about_point=ORIGIN,angle=60*DEGREES).set_color("#918F77")
        secant_name = Text("Secant").scale(0.5).next_to(secant.get_center(),DOWN,buff=0.1).rotate(about_point=ORIGIN,angle=60*DEGREES).set_color("#3B3A26")

        self.play(Create(chord_final),rate_func=smooth,run_time=3)
        self.play(Create(secant),run_time=2,rate_func=smooth)
        self.play(FadeIn(secant_name))
        self.wait(8)

        last_mobjects = VGroup(main_circle,secant,secant_name,centre)
        final_dot = Dot(ORIGIN,radius=0.1).set_color("#918F77")

        self.play(Transform(last_mobjects,final_dot))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.wait(2)



class subtends(Scene):
    def construct(self):

        ######Subtends concept
        dot = Dot(ORIGIN,0.15).set_color("#918F77").set_z_index(2)
        subtends_text = Text("Subtends").scale(0.5).set_color("#3B3A26")
        self.play(dot.animate.move_to(subtends_text[0]))
        self.wait(2)

        self.play(TypeWithCursor(subtends_text,dot))
        self.wait(2)
        self.play(subtends_text.animate.shift(UP))
        self.play(FadeOut(dot))
        subtends_explanation = Text("used to describe an angle at a point formed from an arc, " \
        "chord or segment.").scale(0.4).next_to(subtends_text,DOWN).set_color("#3B3A26")

        self.play(FadeIn(subtends_explanation,shift=RIGHT),rate_func=smooth)
        self.wait(8)
        self.play(FadeOut(*self.mobjects))

        ### Subtends explantion
        main_circle = Circle(radius=1.5).set_color("#2A3BA0")
        self.play(Create(main_circle))

        p_90 = [0,1.5,0]
        p_210 = main_circle.point_at_angle(210*DEGREES)
        p_330 = main_circle.point_at_angle(330*DEGREES)

        arc = ArcBetweenPoints(start=p_210,end=p_330,radius=1.5,angle=120*DEGREES).set_color(RED).set_stroke(width=7)
        angle_line_1 = Line(end=p_210,start=p_90).set_color("#4C3D6D")
        angle_line_2 = Line(start=p_90,end=p_330).set_color("#4C3D6D")

        angle = Angle(line1=angle_line_1,line2=angle_line_2,radius=0.3).set_color("#2A3BA0")
        chord_1 = Line(start=p_210,end=p_330).set_color("#4C3D6D")
        angle_text = Text("a").scale(0.5).next_to(angle,DOWN,buff=0.1).set_color("#2A3BA0")
        
        angle_sentence_arc = Paragraph("Angle 'a' is subtended",
                                       "by the arc").scale(0.5).next_to(main_circle,RIGHT).set_color("#3B3A26")
        angle_sentence_chord = Paragraph("Angle 'a' is subtended",
                                       " by a Chord").scale(0.5).next_to(main_circle,RIGHT).set_color("#3B3A26")
        
        self.wait(1)
        self.play(Create(arc))
        self.wait(2)
        self.play(Create(angle_line_1),Create(angle_line_2),run_time=2)
        self.wait(2)
        self.play(Create(angle),Create(angle_text),Create(angle_sentence_arc))

        self.wait(1)

        self.play(Uncreate(arc),Uncreate(angle_sentence_arc))
        self.play(Create(chord_1),Create(angle_sentence_chord),run_time=2)
        self.wait(6)
        self.play(FadeOut(*self.mobjects))
        self.wait(2)

class circle_theorems(Scene):
    def construct(self):    
        main_circle = Circle(radius=2).set_color("#4C3D6D")
        
        centre = always_redraw(
            lambda:Dot(main_circle.get_center()).set_color("#3B3A26")
        )

        ########Theorem 1.
        theorem_text_1 = Text("Theorem").scale(0.7).set_color("#000000")

        theorem_1 = Paragraph("a straight line from ",
                              "the centre of a circle",
                              "that bisects a chord ",
                              "is at right angles", 
                              "to the chord",line_spacing=1).scale(0.4).set_color("#3B3A26")

        theorem_text_1.align_to(theorem_1,LEFT)

        theorem = VGroup(theorem_text_1,theorem_1).arrange_in_grid(rows=2,cols=1).set_opacity(0)

        group = VGroup(theorem,main_circle)

        self.wait(2)
        self.play(FadeIn(main_circle),FadeIn(centre))
        self.wait(1)

        self.play(group.animate.arrange(RIGHT,buff=1))
        theorem.set_opacity(1)

        ##points on theorem 1
        chord_1 = always_redraw(
            lambda:Line(start=main_circle.point_at_angle(220*DEGREES),end=main_circle.point_at_angle(320*DEGREES)).set_color("#3B3A26")
        )

        centre_line_1 = always_redraw(
            lambda: Line(end=main_circle.get_center(),start=chord_1.get_center()).set_color("#3B3A26")
        )

        angle_1 = RightAngle(chord_1,centre_line_1,length=0.2).set_color("#3B3A26")

        letter_1_1 = MathTex("a").scale(0.7).next_to(main_circle.point_at_angle(220*DEGREES),DOWN,buff=0.1).set_color("#2A3BA0")
        letter_1_2 = MathTex("b").scale(0.7).next_to(main_circle.point_at_angle(320*DEGREES),DOWN,buff=0.1).set_color("#2A3BA0")
        letter_1_3 = MathTex("c").scale(0.7).next_to(chord_1.get_center(),DOWN,buff=0.1).set_color("#2A3BA0") 
        letter_1_4 = MathTex(r"90^{o}").scale(0.6).set_color("#2A3BA0").next_to(angle_1,UR,buff=0.1)

        theorem_1_letters = VGroup(letter_1_1,letter_1_2,letter_1_3)

        text_1 = Text("|ac| = |cb|").scale(0.7).next_to(main_circle,UP,buff=0.5).set_color("#4C3D6D")

        self.play(FadeIn(theorem,shift=RIGHT))
        self.wait(2)
        self.play(Create(chord_1),Create(centre_line_1),Create(angle_1),FadeIn(letter_1_4),run_time=2)
        self.wait(2)

        line_1_1 = Line(start=chord_1.get_start(),end=chord_1.get_center()).set_color("#4C3D6D")
        line_1_2 = Line(start=chord_1.get_center(),end=chord_1.get_end()).set_color("#ACA440")
        
        self.play(Create(line_1_1),Create(line_1_2),FadeIn(theorem_1_letters),rate_func=smooth)
        self.play(TransformFromCopy(VGroup(theorem_1_letters,line_1_1,line_1_2),text_1),rate_func=smooth)
        
        self.wait(2)
        theorem_1_lines = VGroup(centre_line_1,chord_1,theorem_1_letters,line_1_1,line_1_2,angle_1,letter_1_4,text_1)
        self.wait(4)

        self.play(FadeOut(theorem_1_lines))
        self.wait(1)

        ########Theorem 2.
        theorem_2 = Paragraph(
            "The angle subtended",
            "at the centre",
            "of a circle is",
            "twice the angle",
            "that is subtended",
            "at the circumference",
            line_spacing=1).scale(0.4)

        theorem_2.set_color("#3B3A26")
        theorem_2.align_to(theorem_text_1,LEFT).next_to(theorem_text_1,DOWN)

        self.play(FadeOut(theorem_1,shift=LEFT),rate_func=smooth)
        self.wait(0.5)
        self.play(FadeIn(theorem_2,shift=RIGHT),rate_func=smooth)
        self.wait(2)

        arc_2_1 = Arc(start_angle=220*DEGREES,radius=2,angle=100*DEGREES,arc_center=main_circle.get_center()).set_stroke(width=4).set_color(RED)
        arc_2_2 = Arc(start_angle=320*DEGREES,radius=2,angle=260*DEGREES,arc_center=main_circle.get_center()).set_stroke(width=4).set_color("#4C3D6D")
        
        ##Lines. 
        p_2_center = main_circle.get_center()

        p_2_90 = main_circle.point_at_angle(90*DEGREES)
        p_2_220 = main_circle.point_at_angle(220*DEGREES)
        p_2_270 = main_circle.point_at_angle(270*DEGREES)
        p_2_320 = main_circle.point_at_angle(320*DEGREES)

        line_1 = Line(start=p_2_center,end=p_2_220).set_color("#918F77")
        line_2 = Line(end=p_2_220,start=p_2_270).set_color("#918F77")
        line_3 = Line(start=p_2_270,end=p_2_320).set_color("#918F77")
        line_4 = Line(start=p_2_center,end=p_2_320).set_color("#918F77")

        line_5 = Line(end=p_2_220,start=p_2_90).set_color("#918F77")
        line_6 = Line(start=p_2_90,end=p_2_320).set_color("#918F77")

        #Measured from top to bottom
        angle_2_1 = Angle(line_5,line_6,radius=0.3).set_color("#918F77")
        angle_2_2 = Angle(line_1,line_4,radius=0.3).set_color("#918F77")
        angle_2_3 = Angle(line_4,line_1,radius=0.3).set_color("#918F77")
        angle_2_4 = Angle(line_3,line_2,radius=0.3).set_color("#918F77")

        letter_2_1 = Text("x").scale(0.5).next_to(angle_2_1,DOWN,buff=0.1).set_color("#4C3D6D")
        letter_2_2 = Text("2y").scale(0.5).next_to(angle_2_2,UP,buff=0.6).set_color("#4C3D6D")
        letter_2_3 = Text("2x").scale(0.5).next_to(angle_2_3,DOWN,buff=0.3).set_color("#4C3D6D")
        letter_2_4 = Text("y").scale(0.5).next_to(angle_2_4,UP,buff=0.1).set_color("#4C3D6D")

        theorem_2_lines = Group(line_1,line_2,line_3,line_4,line_5,line_6,angle_2_1,angle_2_2,angle_2_3,
                                angle_2_4,letter_2_1,letter_2_2,letter_2_3,letter_2_4)
        
        self.play(FadeIn(arc_2_1),FadeIn(arc_2_2),FadeIn(theorem_2_lines))

        self.wait(8)
        self.play(FadeOut(main_circle))
        arc_2_1.save_state()
        
        self.wait(2)
        self.play(arc_2_1.animate.shift(DOWN))
        self.wait(2)
        self.play(Restore(arc_2_1))

        self.wait(4)

        self.play(FadeIn(main_circle),FadeOut(arc_2_2),FadeOut(arc_2_1))
        self.wait(5)

        self.play(FadeOut(theorem_2_lines),rate_func=smooth)
        self.wait(2)

        ########### Theorem 3

        theorem_3 = Paragraph("Angles in the", 
                              "same segment are",
                              "equal",line_spacing=1).scale(0.4).set_color("#3B3A26").align_to(theorem_text_1,LEFT).next_to(theorem_text_1,DOWN)
           
        p_3_220 = main_circle.point_at_angle(220*DEGREES)
        p_3_320 = main_circle.point_at_angle(320*DEGREES)
        p_3_90  = main_circle.point_at_angle(90*DEGREES)
        p_3_60 = main_circle.point_at_angle(60*DEGREES)
        p_3_120 = main_circle.point_at_angle(120*DEGREES)
       
        chord_3 = Line(start=p_3_220,end=p_3_320).set_color("#918F77")
        line_3_1 = Line(start=p_3_90,end=p_3_220).set_color("#918F77")
        line_3_2 = Line(start=p_3_90,end=p_3_320).set_color("#918F77")

        line_3_3 = Line(start=p_3_60, end = p_3_220).set_color("#918F77")
        line_3_4 = Line(start=p_3_60, end = p_3_320).set_color("#918F77")

        line_3_5 = Line(start = p_3_120,end = p_3_220).set_color("#918F77")
        line_3_6 = Line(start= p_3_120,end= p_3_320).set_color("#918F77")

        angle_3_1 = Angle(line_3_1,line_3_2,radius=0.3).set_color("#918F77")
        angle_3_2 = Angle(line_3_3,line_3_4,radius=0.3).set_color("#918F77")

        angle_3_3 = Angle(line_3_5,line_3_6,radius=0.3).set_color("#918F77")

        letter_3_1 = Text("a").set_color("#4C3D6D").scale(0.5).next_to(angle_3_1,DOWN,buff=0.2)
        letter_3_2 = Text("b").set_color("#4C3D6D").scale(0.5).next_to(angle_3_2,DOWN,buff=0.2)
        letter_3_3 = Text("c").set_color("#4C3D6D").scale(0.5).next_to(angle_3_3,DOWN,buff=0.2)
        
        letter_3_group = Text("a = b = c").set_color("#4C3D6D").scale(0.7).next_to(main_circle,UP,buff=0.2)

        theorem_3_lines = Group(line_3_1,line_3_2,line_3_3,line_3_4,line_3_5,line_3_6,angle_3_1,angle_3_2,
                                angle_3_3,letter_3_1,letter_3_2,letter_3_3)

        self.play(FadeOut(theorem_2,shift=LEFT))
        self.wait(1)
        self.play(FadeIn(theorem_3,shift=RIGHT))
        self.wait(2)
        self.play(Create(chord_3))
        self.wait(1)
        self.play(FadeIn(theorem_3_lines))
        self.wait(2)
        self.play(TransformFromCopy(VGroup(letter_3_1,letter_3_2,letter_3_3),letter_3_group))
        self.wait(4)

        self.play(FadeOut(theorem_3_lines),FadeOut(letter_3_group),FadeOut(chord_3))
        self.wait(2)

        ####Theorem 4
        theorem_4 = Paragraph("Angle in a", 
                              "semi-circle is a",
                              "right angle",line_spacing=1).scale(0.4).set_color("#3B3A26").align_to(theorem_text_1,LEFT).next_to(theorem_text_1,DOWN)
        
        self.play(FadeOut(theorem_3,shift=LEFT),rate_func=smooth)
        self.play(FadeIn(theorem_4,shift=RIGHT),rate_func=smooth)
        self.wait(3)

        p_4_120 = main_circle.point_at_angle(120*DEGREES)
        p_4_0 = main_circle.point_at_angle(0*DEGREES)
        p_4_180 = main_circle.point_at_angle(180*DEGREES)

        diameter_4 = Line(main_circle.point_at_angle(180*DEGREES),main_circle.point_at_angle(0*DEGREES)).set_color("#918F77")

        line_4_1 = Line(start=p_4_120,end=p_4_180).set_color("#918F77")
        line_4_2 = Line(start=p_4_120,end=p_4_0).set_color("#918F77")

        angle_4 = RightAngle(line_4_1,line_4_2,length=0.3).set_color("#918F77")
        letter_4 = MathTex(r"90^{o}").scale(0.5).next_to(angle_4,DOWN,buff=0.1).set_color("#4C3D6D")

        theorem_4_lines = VGroup(line_4_1,line_4_2)
        self.wait(4)
        self.play(Create(diameter_4),rate_func=smooth)


        self.wait(5)
        self.play(Create(theorem_4_lines),FadeIn(angle_4),FadeIn(letter_4))

        self.wait(4)
        self.play(FadeOut(theorem_4_lines),FadeOut(VGroup(diameter_4,letter_4,angle_4)),rate_func=smooth)
        self.wait(2)

        ####Theorem 5
        
        p_5_30 = main_circle.point_at_angle(30*DEGREES)
        p_5_130 = main_circle.point_at_angle(130*DEGREES)
        p_5_220 = main_circle.point_at_angle(220*DEGREES)
        p_5_320 = main_circle.point_at_angle(320*DEGREES)

        theorem_5 = Paragraph("opposite angles of", 
                              "a cyclic quadrilateral",
                              "are supplementary",line_spacing=1).scale(0.4).set_color("#3B3A26").align_to(theorem_text_1,LEFT).next_to(theorem_text_1,DOWN)
        
        line_5_1 = Line(start=p_5_30,end=p_5_130).set_color("#918F77")
        line_5_2 = Line(start=p_5_30,end=p_5_320).set_color("#918F77")

        line_5_3 = Line(start=p_5_130,end=p_5_30).set_color("#918F77")
        line_5_4 = Line(start=p_5_130,end=p_5_220).set_color("#918F77")

        line_5_5 = Line(start=p_5_220,end=p_5_130).set_color("#918F77")
        line_5_6 = Line(start=p_5_220,end=p_5_320).set_color("#918F77")

        line_5_7 = Line(start=p_5_320,end=p_5_220).set_color("#918F77")
        line_5_8 = Line(start=p_5_320,end=p_5_30).set_color("#918F77")

        angle_5_1 = Angle(line_5_1,line_5_2,radius=0.3).set_color("#918F77")
        angle_5_2 = Angle(line_5_4,line_5_3,radius=0.3).set_color("#918F77")
        angle_5_3 = Angle(line_5_6,line_5_5,radius=0.3).set_color("#918F77")
        angle_5_4 = Angle(line_5_8,line_5_7,radius=0.3).set_color("#918F77")

        letter_5_1 = Text("a").scale(0.5).next_to(angle_5_1,DL,buff=0.1).set_color("#4C3D6D")
        letter_5_2 = Text("b").scale(0.5).next_to(angle_5_2,DR,buff=0.1).set_color("#4C3D6D")
        letter_5_3 = Text("c").scale(0.5).next_to(angle_5_3,UR,buff=0.1).set_color("#4C3D6D")
        letter_5_4 = Text("d").scale(0.5).next_to(angle_5_4,UL,buff=0.1).set_color("#4C3D6D")

        statement_5_1 = Text("a + c = 180").scale(0.5).next_to(main_circle,UP,buff=0.5).set_color("#4C3D6D")
        statement_5_2 = Text("b + d = 180").scale(0.5).next_to(statement_5_1,UP,buff=0.5).set_color("#4C3D6D")

        theorem_5_lines = VGroup(line_5_1,line_5_2,line_5_3,line_5_4,line_5_5,line_5_6,line_5_7,line_5_8,
                                 angle_5_1,angle_5_2,angle_5_3,angle_5_4,letter_5_1,letter_5_2,letter_5_3,
                                 letter_5_4)

        self.wait(3)
        self.play(FadeOut(theorem_4,shift=LEFT),rate_func=smooth)
        self.play(FadeIn(theorem_5,shift=RIGHT),rate_func=smooth)
        self.wait(1)
        self.play(FadeIn(theorem_5_lines))
        self.wait(2)

        self.play(TransformFromCopy(VGroup(letter_5_1,letter_5_3),statement_5_1))
        self.play(TransformFromCopy(VGroup(letter_5_3,letter_5_4),statement_5_2))
        
        self.wait(2)

        self.play(FadeOut(theorem_5_lines,statement_5_1,statement_5_2))
        self.wait(1)

        #####Theorem 6
        theorem_6 = Paragraph("The angle between", 
                              "a tangent and a chord",
                              "is equal to the angle",
                              "in the opposite segment",line_spacing=1).scale(0.4).set_color("#3B3A26").align_to(theorem_text_1,LEFT).next_to(theorem_text_1,DOWN)
        
        chord_6 = Line(start=main_circle.point_at_angle(270*DEGREES),end=main_circle.point_at_angle(150*DEGREES)).set_color("#3B3A26")
        tangent_6 = TangentLine(main_circle,alpha=0.75,length=5).set_color("#918F77")
        box_1 = Rectangle(width=7,height=4).next_to(chord_6,UP,buff=0)
        box_2 = Rectangle(width=4,height=4).next_to(chord_6,DOWN,buff=0).align_to(main_circle.point_at_angle(270*DEGREES),RIGHT)

        box_1.rotate(angle=-60*DEGREES,about_point=main_circle.point_at_angle(150*DEGREES))
        box_2.rotate(angle=-60*DEGREES,about_point=main_circle.point_at_angle(270*DEGREES))

        section_1 = Intersection(box_1,main_circle ).set_fill(opacity=0.7,color="#CFC64A").set_stroke(width=0).set_opacity(0.7)
        section_2 = Intersection(box_2,main_circle ).set_fill(opacity=0.7,color=RED).set_stroke(width=0).set_opacity(0.7)

        section_name_1 = Text("S1").scale(0.4).set_color("#3B3A26").move_to(section_1.get_center())
        section_name_2 = Text("S2").scale(0.4).set_color("#3B3A26").move_to(section_2.get_center()+[-0.4,0,0])
        p_6_60 = main_circle.point_at_angle(60*DEGREES)

        line_6_1 = Line(start=p_6_60,end=chord_6.get_start()).set_color(BLACK)
        line_6_2 = Line(start=p_6_60,end=chord_6.get_end()).set_color(BLACK)

        invisible_tangent_line = Line(start=main_circle.point_at_angle(270*DEGREES),end=main_circle.point_at_angle(270*DEGREES)+[-2,0,0])
        angle_6_1 = Angle(line_6_2,line_6_1,radius=0.2).set_color("#3B3A26")
        angle_6_2 = Angle(chord_6,invisible_tangent_line,radius=0.2).set_color("#3B3A26")
        
        letter_6_1 = MathTex(r"\theta").scale(0.7).next_to(angle_6_1,DL,buff=0.1).set_color(BLACK)
        letter_6_2 = MathTex(r"\theta").scale(0.7).next_to(angle_6_2,LEFT,buff=0.05).set_color(BLACK)      

        theorem_6_lines = VGroup(line_6_1,line_6_2,angle_6_1,angle_6_2,letter_6_1,letter_6_2)

        self.play(FadeOut(theorem_5,shift=LEFT),rate_func=smooth)
        self.play(FadeIn(theorem_6,shift=RIGHT),rate_func=smooth)
        self.wait(3)

        self.play(Create(chord_6),Create(tangent_6))
        self.wait(5)
        self.play(FadeIn(section_1),FadeIn(section_2),FadeIn(section_name_1),FadeIn(section_name_2))
        self.wait(5)
        self.play(FadeIn(theorem_6_lines))
        self.wait(4)
        self.play(FadeIn(letter_6_1),FadeIn(letter_6_2),rate_func=smooth)
        self.wait(5)

        self.play(FadeOut(theorem_6_lines),Uncreate(chord_6),FadeOut(VGroup(section_1,section_2,section_name_1,section_name_2,tangent_6)))
        self.wait(4)

        ### Theorem 7
        theorem_7 = Paragraph("Two tangents drawn", 
                              "from a point to",
                              "a circle are equal",line_spacing=1).scale(0.4).set_color("#3B3A26").align_to(theorem_text_1,LEFT).next_to(theorem_text_1,DOWN)

        out_point = Dot().next_to(main_circle,RIGHT*19).set_color("#4C3D6D")

        self.play(FadeOut(theorem_6,shift=LEFT))
        self.play(FadeIn(theorem_7,shift=RIGHT))

        main_circle.save_state()
        theorem_7.save_state()
        theorem_text_1.save_state()

        group.add(out_point,theorem_7)
        theorem.remove(theorem_1)

        self.wait(2)
        self.play(FadeIn(out_point))
        
        self.play(group.animate.move_to(ORIGIN))

        p_7_centre = main_circle.get_center()
        p_7_80 = main_circle.point_at_angle(80*DEGREES)
        p_7_280 = main_circle.point_at_angle(280*DEGREES)

        line_7_1 = Line(start=p_7_80,end=out_point.get_center()).set_color("#4C3D6D")
        line_7_2 = Line(start=p_7_280,end=out_point.get_center()).set_color("#4C3D6D")

        letter_7_1 = Text("a").scale(0.7).next_to(p_7_80,UP,buff=0.2).set_color("#4C3D6D")
        letter_7_2 = Text("b").scale(0.7).next_to(p_7_280,DOWN,buff=0.2).set_color("#4C3D6D")
        letter_7_3 = Text("c").scale(0.7).next_to(out_point.get_center(),UP,buff=0.2).set_color("#4C3D6D")
        statement_7_1 = Text("|ac| = |bc|").scale(0.7).next_to(main_circle,UP,buff=0.7).set_color("#4C3D6D")

        theorem_7_lines = VGroup(out_point,line_7_1,line_7_2,letter_7_1,letter_7_2,letter_7_3)
        
        self.wait(1)
        self.play(Create(line_7_1),Create(line_7_2))
        self.wait(2)
        self.play(FadeIn(letter_7_1),FadeIn(letter_7_2),FadeIn(letter_7_3))
        
        self.wait(1)
        self.play(TransformFromCopy(VGroup(letter_7_1,letter_7_2,letter_7_3),statement_7_1),rate_func=smooth)
        self.wait(3)

        self.play(FadeOut(statement_7_1),FadeOut(theorem_7_lines),FadeOut(out_point))
        self.wait(2)
        self.play(Restore(main_circle),Restore(theorem_7),Restore(theorem_text_1))
        self.wait(2)
        self.play(FadeOut(theorem_7,shift=LEFT))
        self.wait(2)

        ###### Theorem 8
        theorem_8 = Paragraph("The angle between",
                              "a tangent and the",
                              "radius, at the point",
                              "where the tangent",
                              "touches the circle",
                              "is a right angle",line_spacing=1).scale(0.4).set_color("#3B3A26").align_to(theorem_text_1,LEFT).next_to(theorem_text_1,DOWN)
        
        self.play(FadeIn(theorem_8,shift=RIGHT))
        self.wait(1)

        radius_8 = Line(start=main_circle.point_at_angle(270*DEGREES),end= main_circle.get_center()).set_color("#918F77")
        tangent_8 = TangentLine(main_circle,alpha=0.75,length=4).set_color("#918F77")
        angle_8 = RightAngle(radius_8,tangent_8,length=0.3).set_color("#918F77")
        letter_8 = MathTex(r"90^{o}").scale(0.7).next_to(angle_8,UR,buff=0.1).set_color("#4C3D6D")
        theorem_8_lines = VGroup(radius_8,tangent_8,angle_8)
        
        self.wait(5)
        self.play(Create(theorem_8_lines),rate_func=smooth)
        self.play(FadeIn(letter_8),rate_func=smooth)
        self.wait(8)
        self.play(FadeOut(*self.mobjects))
        self.wait(2)


class closing_scene(Scene):
    def construct(self):
        thanks_emoji = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\smile-svgrepo-com.svg").scale(0.3).shift(UP*2)
        like_emoji = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\like-svgrepo-com.svg").scale(0.3)
        share_emoji = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\share-svgrepo-com.svg").scale(0.3)
        subscribe_emoji = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\youtube-svgrepo-com.svg").scale(0.3)

        customer_group = VGroup(like_emoji,share_emoji,subscribe_emoji).arrange_in_grid(1,3,buff=2)

        thanks = Text("Thank you").scale(0.5).next_to(thanks_emoji,DOWN).set_color(BLACK)
        like = Text("Like").scale(0.5).next_to(like_emoji,DOWN).set_color(BLACK)
        share = Text("Share").scale(0.5).next_to(share_emoji,DOWN).set_color(BLACK)
        subscribe = Text("Subscribe").scale(0.5).next_to(subscribe_emoji,DOWN).set_color(BLACK)

        self.play(FadeIn(like_emoji),FadeIn(like),rate_func=smooth,run_time=2)
        self.wait(2)

        self.play(FadeIn(share_emoji),FadeIn(share),rate_func=smooth,run_time=2)
        self.wait(2)

        self.play(FadeIn(subscribe_emoji),FadeIn(subscribe),rate_func=smooth,run_time=2)
        self.wait(2)

        self.play(FadeIn(thanks),FadeIn(thanks_emoji),rate_func=smooth,run_time=2)
        self.wait(7)
