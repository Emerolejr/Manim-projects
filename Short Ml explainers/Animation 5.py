from manim import *
import numpy as np
from scipy.stats import beta
config.background_color = '#0E0E0E'


class matrix_manipulation(Scene):
    def construct(self):
        concept_text = MathTex(r"\text{Analysis of } (A^{T}A)^{-1}").to_corner(UP,buff=0.5).set_color("#00C2CB")

        a_transpose_a_text = MathTex(r"(A^{T}A)").shift(LEFT).scale(0.7).set_color("#1E90FF")
        a_transpose_a_text_inverse = MathTex(r"(A^{T}A)^{-1}").scale(0.7).set_color("#FF5555")

        matrix_1 = MathTex(r"= \begin{bmatrix}"
                           r"\uparrow & \uparrow &  & \uparrow \\"
                           r"c^{1}  & c^{2} & \text{...}& c^{d + 1} \\"
                           r" &  &  &  &  \\"
                           r"\downarrow & \downarrow &  & \downarrow"
                           r"\end{bmatrix}").scale(0.7).next_to(a_transpose_a_text,RIGHT,buff=0.3).set_color("#1E90FF")

        matrix_2 = MathTex(r"\begin{bmatrix}"
                           r"\uparrow & \uparrow &  & \uparrow \\"
                           r"c^{1}  & c^{2} & \text{...}& c^{d + 1} \\"
                           r" &  &  &  &  \\"
                           r"\downarrow & \downarrow &  & \downarrow"
                           r"\end{bmatrix}^{-1}").scale(0.7).set_color("#FF5555")

        self.wait(0.5)
        self.play(FadeIn(Group(concept_text,a_transpose_a_text,matrix_1)))
        self.wait(0.5)
        self.play(matrix_1.animate.shift(RIGHT*0.7),a_transpose_a_text.animate.shift(LEFT))
        self.play(Group(matrix_1,a_transpose_a_text).animate.shift(LEFT*2))
        self.wait(0.5)

        #Positioning the inverse matrix and its matrix
        a_transpose_a_text_inverse.next_to(a_transpose_a_text,RIGHT,buff=0.5)
        matrix_2.next_to(matrix_1,RIGHT,buff=0.5)

        self.play(FadeIn(a_transpose_a_text_inverse,matrix_2))
        
        #New matrix group to help with repositiong
        matrice_1_and_2 = Group(matrix_1,matrix_2)

        matrix_3 = MathTex(r"\begin{bmatrix}"
                           r"1 & 0 & 0 & 0 & 0 \\"
                           r"0 & 1 & . & . & 0 \\"
                           r"0 & 0 & 1 & . & 0 \\"
                           r"0 & 0 & 0 & . & 1"
                           r"\end{bmatrix}_{d + 1 \times d  + 1}").scale(0.7).shift(LEFT*4.5).set_color("#8A2BE2")


        self.play(Group(a_transpose_a_text,a_transpose_a_text_inverse,matrice_1_and_2).animate.move_to(ORIGIN),rate_func=smooth)
        self.wait(0.5)
        self.play(ReplacementTransform(Group(a_transpose_a_text,a_transpose_a_text_inverse),matrix_3))
        self.wait(0.5)
        self.play(matrice_1_and_2.animate.shift(RIGHT*0.5),matrix_3.animate.shift(LEFT*0.5))

        matrix_4 = MathTex(r"\begin{bmatrix}"
                           r"\uparrow\\"
                           r"c^{1}\\"
                           r" \\"
                           r"\downarrow \\"
                           r"\end{bmatrix}").scale(0.7).next_to(matrix_3,RIGHT,buff=0.1).set_color("#FFB000" )
        
        matrix_5 = matrix_4.copy().next_to(matrice_1_and_2,RIGHT,buff=0.1).set_color("#FFB000" )
       
        self.wait(0.5)
        self.play(FadeIn(matrix_4,matrix_5))
        self.wait(0.5)

        #Another inverse matrix and the group of all the matrices | The group of all matrics help with positioning
        a_transpose_a_text_inverse_2 = MathTex(r"(A^{T}A)^{-1}").scale(0.7).next_to(matrix_1,RIGHT,buff=0.5).set_color("#FF5555")
        matrix_group = Group(matrix_3,matrix_4,matrix_1,a_transpose_a_text_inverse_2,matrix_5)

        self.play(ReplacementTransform(matrix_2,a_transpose_a_text_inverse_2))
        self.play(matrix_group.animate.arrange(RIGHT,buff=0.1))
        self.wait(0.5)

        self.play(ReplacementTransform(matrix_3,matrix_4),rate_func=smooth)
        self.wait(0.5)

        #Brace and name of brace
        brace = Brace(Group(matrix_5,a_transpose_a_text_inverse_2),direction=DOWN,sharpness=2)

        brace_name = Text("q").scale(0.5).next_to(brace,DOWN)
        brace_group = VGroup(brace,brace_name).set_color("#808080")
        self.play(FadeIn(brace_group))
        self.wait(0.5)
        self.play(FadeOut(matrix_1,matrix_4))
        self.wait(0.5)

        #Group mobjects on screen t help with repositioning. 
        self.play(Group(a_transpose_a_text_inverse_2,matrix_5,brace_group).animate.move_to(ORIGIN))
        self.wait(0.5)

        matrix_6 = MathTex(r"= \begin{bmatrix}"
                           r"1\\"
                           r"0\\"
                           r"...\\"
                           r"0"
                           r"\end{bmatrix}").scale(0.7).next_to(matrix_5,RIGHT,buff=0.1).set_color("#FF7F50")
        
        self.play(FadeIn(matrix_6))
        self.wait(0.5)

        #Surrounding rectangle 
        rect = SurroundingRectangle(VGroup(matrix_6,matrix_5,a_transpose_a_text_inverse_2,brace_group),buff=0.5).set_color("#3CB371")
        self.play(Create(rect))
        self.wait(0.5)
        