from manim import *
import numpy as np
from scipy.stats import beta
config.background_color = '#0E0E0E'


class matrix_manipulation(Scene):
    def construct(self):
        concept_text = MathTex(r"\text{Analysis of } (A^{T}A)^{-1}").to_corner(UP,buff=0.5).set_color("#00C2CB")

        equ_1 = MathTex(r"\text{if Y = } X^{1}").move_to([-5,2,0]).scale(0.7).set_color("#1E90FF")
        statement_1 = Tex('"first column of A"').scale(0.7).move_to(equ_1.get_bottom()+[1.1,-1.2,0]).set_color("#FFB000")
        statement_2 = MathTex(r"\text{then } A^{T}A = C^{1}").scale(0.7).move_to([-4,1.5,0]).set_color("#FF6B81")

        arrow = Arrow(start=statement_1.get_top(),end = equ_1.get_bottom(),buff=0.4).set_color("#808080")
        arrow.rotate(angle=-50*DEGREES)
        self.wait(0.5)
        self.play(FadeIn(concept_text),FadeIn(equ_1))
        self.wait(0.5)
        self.play(FadeIn(statement_1),FadeIn(arrow))
        self.wait(0.5)
        self.play(FadeOut(VGroup(statement_1,arrow)),rate_func=smooth)
        self.wait(0.5)
        self.play(FadeIn(statement_2),rate_func=smooth)

        #A transpose A mobjects and its matrices mobjects
        a_transpose_a = MathTex(r"A^{T}A").scale(0.7).move_to([-5.5,-1,0]).set_color("#00C2CB")
        matrix_1 = MathTex(r"= \begin{bmatrix}"
                           r"\leftarrow & & X^{1} & \rightarrow \\" 
                           r"\leftarrow & & X^{2} & \rightarrow \\"
                           r". & . & .& . \\"
                           r"\leftarrow & & X^{d + 1} & \rightarrow"
                           r"\end{bmatrix}").scale(0.7)
        
        matrix_2 = MathTex(r"\begin{bmatrix}"
                           r"\uparrow & \uparrow &  & \uparrow \\" 
                           r" & & & \\"
                           r" X ^{1} & X^{2} & ... & X^{d+1}\\"
                           r"\downarrow & \downarrow & \downarrow & \downarrow"
                           r"\end{bmatrix}").scale(0.7).set_color("#FF7F50")
        
        matrix_group = VGroup(matrix_1,matrix_2).arrange(RIGHT,buff=0.2).next_to(a_transpose_a,RIGHT)

        self.play(FadeIn(a_transpose_a))
        self.wait(0.5)
        self.play(FadeIn(matrix_group))
        self.wait(0.5)

        #A^T X^1 analysis related mobjects are here

        matrix_3 = MathTex(r" = \begin{bmatrix}" 
                           r"\uparrow & \uparrow & & \uparrow \\"
                           r" & & & \\"
                           r"A^{T}X^{1} & . & .& . \\"
                           r" \downarrow & \downarrow & & \downarrow"
                           r"\end{bmatrix}").scale(0.7).next_to(matrix_group,RIGHT,buff=0.2).set_color("#FF5555")
        
        a_transpose_x_inverse = MathTex(r"A^{T}X^{1}").scale(0.7).next_to(matrix_3,UP).set_color("#1E90FF")
        c_inverse = MathTex(r"C^{1}").scale(0.7).move_to(matrix_3.get_bottom()+[-1,-1.5,0]).set_color("#FFD700")
        arrow_2 = Arrow(start=c_inverse.get_top(),end=matrix_3.get_bottom() ,buff=0.5).set_color("#808080")
        self.play(TransformFromCopy(matrix_group,matrix_3),FadeIn(a_transpose_x_inverse),rate_func=smooth)
        self.wait(0.5)
        self.play(FadeOut(a_transpose_x_inverse))
        self.wait(0.5)
        self.play(FadeIn(Group(c_inverse,arrow_2)))
        self.wait(0.5)
        self.play(FadeOut(VGroup(a_transpose_a,matrix_1,matrix_2,matrix_3,arrow_2,c_inverse)))
        self.wait(0.5)

        #A transpose, X i matrix
        statement_3 = MathTex(r"A^{T}X^{i} = C^{i}").scale(0.7).next_to(statement_2,DOWN).set_color("#00C2CB")
        self.play(FadeIn(statement_3))

        self.wait(0.5)

        self.play(FadeOut(*self.mobjects),rate_func=smooth)
        self.wait(0.5)


        ## Starting after fading out mobjects on the screen 

        title_text = Text("Combining both").to_corner(UP).scale(0.7).set_color("#EAEAEA")
        a_transpose_a_2_1 = MathTex(r"(A^{T}A)^{-1}").scale(0.8).set_color("#1E90FF")
        a_transpose_a_2_2 = MathTex(r"(A^{T}X^{i})").scale(0.7).set_color("#FFB000")
        a_transpose_a_2 = VGroup(a_transpose_a_2_1,a_transpose_a_2_2).arrange(RIGHT,buff=0.2).next_to(title_text,DOWN*3)

        a_transpose_a_3_1 = MathTex(r"= (A^{T}A)^{-1}").scale(0.7).set_color("#1E90FF")
        a_transpose_a_3_2 = MathTex(r"C^{i}").scale(0.7).set_color("#FF7F50")
        a_transpose_a_3 = VGroup(a_transpose_a_3_1,a_transpose_a_3_2 ).arrange(RIGHT,buff=0.2).next_to(a_transpose_a_2,DOWN*2)

        i_column_text = MathTex(r"= i^{th} \text{column of identity matrix}").scale(0.7).next_to(a_transpose_a_3,DOWN*2).align_to(a_transpose_a_3,LEFT).set_color("#EAEAEA")

        self.play(FadeIn(title_text))
        self.wait(0.5)

        self.play(FadeIn(a_transpose_a_2))
        self.wait(0.5)

        self.play(TransformFromCopy(a_transpose_a_2_1,a_transpose_a_3_1),TransformFromCopy(a_transpose_a_2_2,a_transpose_a_3_2),rate_func=smooth,lag_ratio=1)
        self.wait(0.5)
        self.play(TransformFromCopy(a_transpose_a_3,i_column_text),rate_func=smooth)
        self.wait(0.5)
        self.play(FadeOut(a_transpose_a_3))
        self.wait(0.5)

        a_transpose_a_4_1 = MathTex(r"A").set_color("#00C2CB")
        a_transpose_a_4_2 = MathTex(r"(A^{T}A)^{-1} = ").set_color("#1E90FF")
        a_transpose_a_4_3 = MathTex(r"A \times ").set_color("#FF7F50")
        a_transpose_a_4_4 = MathTex(r"i^{th} \text{ column of the identity}").set_color("#FFD700")
        a_transpose_a_4 = VGroup(a_transpose_a_4_1,a_transpose_a_4_2,a_transpose_a_4_3,
                                 a_transpose_a_4_4).arrange(RIGHT,buff=0.3).scale(0.7).next_to(i_column_text,DOWN*2)

        self.play(TransformFromCopy(a_transpose_a_2,a_transpose_a_4_2),rate_func=smooth)
        self.play(TransformFromCopy(i_column_text,a_transpose_a_4_4 ),rate_func=smooth)
        self.play(FadeIn(a_transpose_a_4_1),FadeIn(a_transpose_a_4_3),rate_func=smooth)
        self.wait(0.5)

        #The last text
        final_text = MathTex(r"X^{i}").scale(0.7).next_to(a_transpose_a_4_2,RIGHT,buff=0.3).set_color("#00FF7F")

        self.play(FadeOut(Group(i_column_text,a_transpose_a_4_1)),rate_func=smooth)
        self.wait(0.5)
        self.play(ReplacementTransform(Group(a_transpose_a_4_3,a_transpose_a_4_4),final_text),rate_func=smooth)
        self.wait(0.5)

        self.play(Group(a_transpose_a_4_2,final_text).animate.shift(2*UP))
        self.wait(0.5)
        