from manim import *
config.background_color=WHITE


class intro(Scene):
    def construct(self):
        interest = Text("Simple and compound interest").scale(0.5).set_color('#14014B')

        self.wait(2.5)
        self.play(FadeIn(interest),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(interest.animate.shift(UP),rate_func=smooth)
        indicate_interest = always_redraw(
            lambda: Underline(interest[17:25]).set_color('#14014B')
        )

        loading_bar = Rectangle(color='#14014B',width=2.5,height=0.3).next_to(interest,DOWN)
        k = ValueTracker(0)

        progress = always_redraw(
            lambda: DecimalNumber(k.get_value(),0,unit="%").set_color('#6B1012').scale(0.4).next_to(loading_bar,DOWN)
        )
        loading = Line(start=loading_bar.get_left(),end=loading_bar.get_right(),stroke_width=30,color='#6B1012')
        
        self.play(FadeIn(loading_bar))
        self.play(Create(loading),k.animate.set_value(100),FadeIn(progress),run_time=10,lag_ratio=0,rate_func=smooth)
        self.play(Create(indicate_interest))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        
        customer = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\person-svgrepo-com (1).svg").scale(0.5).shift(RIGHT*2).set_color('#14014B')
        bank = SVGMobject("YOUTUBE/FOR THE_ANALYST/Simple and Compound interest/bank-svgrepo-com.svg").scale(0.5).shift(LEFT*2).set_color('#14014B')
        
        lender_text = always_redraw(
            lambda : Text("Lender").scale(0.35).next_to(bank,DOWN).set_color(BLACK)
        )

        borrower_text = always_redraw(
            lambda: Text("Borrower").scale(0.35).next_to(customer,DOWN).set_color(BLACK)
        )

        lender_group = VGroup(bank,lender_text)
        borrower_group = VGroup(customer,borrower_text)
        self.wait(5)
        self.play(FadeIn(lender_text),FadeIn(bank),rate_func=smooth)
        self.wait(2)
        self.play(FadeIn(customer),FadeIn(borrower_text),rate_func=smooth)
        self.wait(1)
        self.play(customer.animate.shift(RIGHT+UP),bank.animate.shift(LEFT+UP),rate_func=smooth)

        coin_1_arc_top = ArcBetweenPoints(end=lender_group.get_top()+[1.5,1,0],start=lender_group.get_top()+[0,0.4,0],angle=-60*DEGREES).set_color('#14014B')
        coin_1_arc_bottom = ArcBetweenPoints(start=lender_group.get_bottom()+[1.5,-1,0],end=lender_group.get_bottom()+[0,-0.4,0],angle=-60*DEGREES).set_color('#14014B')

        coin_2_arc_top = ArcBetweenPoints(end=borrower_group.get_top()+[0,0.4,0],start=borrower_group.get_top()+[-1.5,1,0],angle=-60*DEGREES).set_color('#14014B')
        coin_2_arc_bottom = ArcBetweenPoints(start=borrower_group.get_bottom()+[0,-0.4,0],end=borrower_group.get_bottom()+[-1.5,-1,0],angle=-60*DEGREES).set_color('#14014B')

        coin_1 = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\coin-svgrepo-com (1).svg").scale(0.2)
        coin_2 = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\coin-svgrepo-com (1).svg").scale(0.2)
        Money_1_top = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\money-svgrepo-com.svg").scale(0.2)
        Money_1_bottom= SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\money-svgrepo-com.svg").scale(0.2)
        Money_2_top = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\money-svgrepo-com.svg").scale(0.2)
        Money_2_bottom = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\money-svgrepo-com.svg").scale(0.2)
        add_1 = Text("+").scale(0.5).set_color('#14014B')
        add_2 = add_1.copy()

        prin_plus_int_1 = VGroup(coin_1,add_1,Money_1_bottom).arrange(LEFT,buff=0.1).move_to(coin_1_arc_bottom.get_start())
        prin_plus_int_2 = VGroup(coin_2,add_2,Money_2_bottom).arrange(LEFT,buff=0.1).move_to(coin_2_arc_bottom.get_start())
        
        Money_1_top.move_to(coin_1_arc_top.get_start())
        Money_2_top.move_to(coin_2_arc_top.get_start())

        coin_1_name = always_redraw(
            lambda : Text("Interest").scale(0.3).next_to(coin_1,DOWN).set_color(BLACK)
        )

        coin_2_name = always_redraw(
            lambda : Text("Interest").scale(0.3).next_to(coin_2,DOWN).set_color(BLACK)
        )

        Money_1_name = always_redraw(
            lambda : Text("Principal").scale(0.3).next_to(Money_1_top,UP).set_color(GREEN)
        )

        Money_2_name = always_redraw(
            lambda : Text("Principal").scale(0.3).next_to(Money_2_top,UP).set_color(GREEN)
        )

        everything_borrower = VGroup(prin_plus_int_2,borrower_group)
        everything_lender = VGroup(prin_plus_int_1,lender_group)

        interest_1 = Text("Compensation for parting with money").scale(0.3).set_color(BLACK).next_to(coin_1_arc_bottom,DOWN,buff=1)
        interest_2 = Text("Charge for borrowing money").scale(0.3).set_color(BLACK).next_to( coin_2_arc_bottom ,DOWN,buff=1)

        self.wait(5)

        self.play(FadeIn(Money_2_name),FadeIn(Money_2_top),FadeIn(Money_2_name),FadeIn(coin_2_name),FadeIn(coin_2_name),rate_func=smooth)
        self.wait(1)
        self.play(MoveAlongPath(Money_2_top,coin_2_arc_top),MoveAlongPath(prin_plus_int_2,coin_2_arc_bottom),FadeIn(interest_2),Create(Underline(interest_2).set_color(BLACK)),rate_func=smooth,lag_ratio=0,run_time=3)
       
        self.wait(2)
        self.play(FadeIn(Money_1_name),FadeIn(Money_1_top),FadeIn(prin_plus_int_1),FadeIn(coin_1_name),run_time=3,rate_func=smooth)
        self.wait(1)

        self.play(MoveAlongPath(Money_1_top,coin_1_arc_top),MoveAlongPath(prin_plus_int_1,coin_1_arc_bottom),FadeIn(interest_1),Create(Underline(interest_1).set_color(BLACK)),rate_func=smooth,lag_ratio=0,run_time=3)

        self.wait(3)
        self.play(FadeOut(*self.mobjects))
        self.wait(2)

class main_scene(Scene):
    def construct(self):
        principal = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\money-svgrepo-com.svg").scale(0.4)
        principal_name = always_redraw(
            lambda: Text("Principal").scale(0.3).set_color(GREEN).next_to(principal,UP)
        )

        interest_main = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\coin-svgrepo-com (1).svg").scale(0.4).shift(RIGHT*2)
        
        interest_main_name = always_redraw(
            lambda :Text("Interest = Percentage of Principal").scale(0.3).set_color(BLACK).next_to(interest_main,UP)
        )

        rate = Text("Rate").set_color(BLACK).scale(0.3).next_to(interest_main_name[9:18],UP,buff=0.2)

        self.wait(2)
        self.play(FadeIn(principal),FadeIn(principal_name),rate_func=smooth)
        self.wait(2)
        self.play(principal.animate.shift(LEFT*2),TransformFromCopy(principal,interest_main),FadeIn(interest_main_name),rate_func=smooth,run_time=2)

        rate_indicator = SurroundingRectangle(interest_main_name[9:19],buff=0).set_color(BLACK)

        self.play(Create(rate_indicator),FadeIn(rate),lag_ratio=1,rate_func=smooth,run_time=2)
        self.wait(2)
        
        self.play(FadeOut(VGroup(interest_main,interest_main_name,rate,rate_indicator)),principal.animate.move_to(ORIGIN),rate_func=smooth)
        principal_text = Text("The money loaned or borrowed").scale(0.3).set_color(BLACK).next_to(principal,DOWN)
        typer = Rectangle(color=BLACK,width=0.01,height=0.15).move_to(principal_text[0])
        self.play(TypeWithCursor(principal_text,typer),rate_func=smooth,run_time=3)
        self.play(FadeOut(typer))
        self.wait(5)
        self.play(FadeOut(*self.mobjects))
        self.wait(5)

class second_scene(Scene):
    def construct(self):
        bank = SVGMobject("YOUTUBE/FOR THE_ANALYST/Simple and compound interest/bank-svgrepo-com.svg").scale(0.5).move_to([0,3,0])
        jake = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\person-svgrepo-com (1).svg").scale(0.3).next_to(bank,(DOWN)+(LEFT*2),buff=1)
        john = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\person-svgrepo-com (1).svg").scale(0.3).next_to(bank,(DOWN)+(RIGHT*2),buff=1)

        bank_name = always_redraw(
            lambda: Text("Bank").next_to(bank,DOWN).set_color('#14014B').scale(0.5)
        )

        jake_name = always_redraw(
            lambda :Text("John").scale(0.5).set_color('#14014B').next_to(jake,DOWN)
        )

        john_name = always_redraw(
            lambda:Text("Jake").scale(0.5).set_color('#14014B').next_to(john,DOWN)
        )

        jake_loan = Text("$ 1000").scale(0.5).next_to(jake_name,DOWN).set_color(BLACK)
        john_loan = Text("$ 1000").scale(0.5).next_to(john_name,DOWN).set_color(BLACK)

        loaned_amount = Text("Loan").set_color("#640808").scale(0.5).next_to(jake_loan,LEFT*2.5)

        jake_person = VGroup(jake,jake_name)
        john_person = VGroup(john,john_name)
        bank_group = VGroup(bank,bank_name)

        jake_tracker = ValueTracker(1000)
        john_tracker = ValueTracker(1000)

        jake_loan_repayment = always_redraw(
            lambda : DecimalNumber(jake_tracker.get_value(),0).scale(0.6).set_color('#6B1012').next_to(jake,UP)
        )

        john_loan_repayment = always_redraw(
            lambda : DecimalNumber(john_tracker.get_value(),0).scale(0.6).set_color('#6B1012').next_to(john,UP)
        )

        jake_dollars = Text("$ ").scale(0.6).set_color('#6B1012').next_to(jake_loan_repayment,LEFT,buff=0.01)
        john_dollars = Text("$ ").scale(0.6).set_color('#6B1012').next_to(john_loan_repayment,LEFT,buff=0.01)

        self.play(Succession(FadeIn(jake_person),FadeIn(john_person),FadeIn(bank_group),lag_ratio=1),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(TransformFromCopy(bank,jake_loan),TransformFromCopy(bank,john_loan),FadeIn(loaned_amount),rate_func=smooth)
        self.wait(4)

        jake_years = VGroup(Text("1st year: $100"),Text("2nd year: $100"),Text("3rd year: $100")).arrange(DOWN,buff=0.5).set_color(BLACK).scale(0.5).next_to(jake_loan,DOWN)
        john_years = VGroup(Text("1st year: $100"),Text("2nd year: $110"),Text("3rd year: $121")).arrange(DOWN,buff=0.5).set_color(BLACK).scale(0.5).next_to(john_loan,DOWN)

        jake_details = VGroup(Text("Simple interest"),Text("Rate = 10%")).arrange(DOWN,buff=0.5).set_color(BLACK).next_to(jake_loan_repayment,UP).scale(0.4)
        john_details = VGroup(Text("Compound interest"),Text("Rate = 10%")).arrange(DOWN,buff=0.5).set_color(BLACK).next_to(john_loan_repayment,UP).scale(0.4)
       
        plus_interest = Text("+ interests").scale(0.5).next_to(john_loan,RIGHT,buff=0.05).set_color(BLACK)
        principal_underline = Underline(john_loan).set_color("#0C5206")

        self.wait(3)
        self.play(FadeOut(bank_group),FadeOut(loaned_amount))
        self.play(FadeIn(jake_details),rate_func=smooth,run_time=2)
        self.wait(4)
        self.play(FadeIn(john_details),rate_func=smooth,run_time=2)
        self.play(FadeIn(jake_loan_repayment),FadeIn(john_loan_repayment),FadeIn(john_dollars),FadeIn(jake_dollars),rate_func=smooth,run_time=2)
        self.wait(4)

        def collect_and_print(input,output,position,tracker):
            process = DecimalNumber(input * 0.1,0).scale(0.5).set_color(BLACK)
            process.next_to(position,RIGHT*2)
            percentage(process)
            self.play(TransformFromCopy(position,process),rate_func=smooth)
            self.wait(1)
            self.play(Transform(process,output),rate_func=smooth,run_time=1)
            self.play(tracker.animate.set_value(tracker.get_value()+(input*0.1)),rate_func=smooth)

        def percentage(posi):
            ten_percent = Text("10%").scale(0.3).set_color("#083304").next_to(posi,UP)
            self.play(Create(ten_percent),ten_percent.animate.shift([0,0.1,0]),run_time=1,rate_func=smooth)
            self.play(FadeOut(ten_percent),rate_func=smooth,run_time=1)

        collect_and_print(1000,jake_years[0],jake_loan,jake_tracker)
        collect_and_print(1000,jake_years[1],jake_loan,jake_tracker)
        collect_and_print(1000,jake_years[2],jake_loan,jake_tracker)

        self.wait(8)
        repayment_underline = Underline(john_loan_repayment).set_color(BLACK)
        self.play(Create(repayment_underline),run_time=1.5,rate_func=smooth)
        self.wait(2)
        self.play(Create(principal_underline),rate_func=smooth)
        self.play(FadeIn(plus_interest),rate_func=smooth)
        self.play(FadeOut(principal_underline),FadeOut(plus_interest),FadeOut(repayment_underline),rate_func=smooth)
        self.wait(10)
        collect_and_print(1000,john_years[0],john_loan_repayment,john_tracker)
        self.wait(4)
        collect_and_print(1100,john_years[1],john_loan_repayment,john_tracker)
        self.wait(4)
        collect_and_print(1210,john_years[2],john_loan_repayment,john_tracker)

        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        self.wait(5)

class new_third_scene(Scene):
    def construct(self):
        simple_interest = Text("Simple interest is interest on principal").scale(0.5).shift(UP).set_color(BLACK)
        compound_interest = Text("Compound interest is the interest on principal + previous interests").scale(0.5).set_color(BLACK)
        
        simple_typer = Rectangle(width=0.01,height=0.3).set_color(BLACK).move_to(simple_interest[0])
        compound_typer = Rectangle(width=0.01,height=0.3).set_color(BLACK).move_to(compound_interest[0])

        simple_interest_underline = Underline(simple_interest[16:36]).set_color('#14014B')
        compound_interest_underline = Underline(compound_interest[21:58]).set_color('#14014B')
        
        self.play(TypeWithCursor(simple_interest,simple_typer),Create(simple_interest_underline),rate_func=smooth,run_time=3)
        self.play(Wait(1),FadeOut(simple_typer))
        self.play(TypeWithCursor(compound_interest,compound_typer),Create(compound_interest_underline),rate_func=smooth,run_time=5)
        self.play(FadeOut(compound_typer),rate_func=smooth)
        self.wait(1)


class fourth_scene(Scene):
    def construct(self):
        jake = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\person-svgrepo-com (1).svg").move_to([0,1,0]).scale(0.5).shift(LEFT*2)
        jake_name = Text("John").scale(0.5).next_to(jake,DOWN).set_color('#14014B')
        jake_loan = Text("$1300").scale(0.5).next_to(jake_name,DOWN).scale(0.5)
        jake_years = VGroup(Text("1st year: $100"),Text("2nd year: $100"),Text("3rd year: $100")).arrange(DOWN,buff=0.5).set_color(BLACK).scale(0.5).next_to(jake_loan,DOWN)

        john = SVGMobject("YOUTUBE\FOR THE_ANALYST\Simple and compound interest\person-svgrepo-com (1).svg").move_to([0,1,0]).scale(0.5).shift(RIGHT*2)
        john_name = Text("Jake").scale(0.5).next_to(john,DOWN).set_color('#14014B')
        john_loan = Text("$ 1331").scale(0.5).next_to(john_name,DOWN).scale(0.5)
        john_years = VGroup(Text("1st year: $100"),Text("2nd year: $110"),Text("3rd year: $121")).arrange(DOWN,buff=0.5).set_color(BLACK).scale(0.5).next_to(john_loan,DOWN)

        jake_tracker = ValueTracker(1300)
        john_tracker = ValueTracker(1331)

        jake_loan_repayment = always_redraw(
            lambda : DecimalNumber(jake_tracker.get_value(),0).scale(0.6).set_color('#6B1012').next_to(jake,UP)
        )

        john_loan_repayment = always_redraw(
            lambda : DecimalNumber(john_tracker.get_value(),0).scale(0.6).set_color('#6B1012').next_to(john,UP)
        )

        jake_details = VGroup(Text("Simple interest"),Text("Rate = 10%")).arrange(DOWN,buff=0.5).set_color(BLACK).next_to(jake_loan_repayment,UP).scale(0.4)
        john_details = VGroup(Text("Compound interest"),Text("Rate = 10%")).arrange(DOWN,buff=0.5).set_color(BLACK).next_to(john_loan_repayment,UP).scale(0.4)
        
        line_for_jake = Underline(jake_years[2],buff=0.2).set_color('#6B1012')
        line_for_john = Underline(john_years[2],buff=0.2).set_color('#6B1012')

        jake_fifty = Text("fiftieth year: $ 100").scale(0.5).set_color(BLACK).next_to(line_for_jake,DOWN)
        john_fifty = Text("fiftieth year: $ 10,672").scale(0.5).set_color(BLACK).next_to(line_for_john,DOWN)
        
        jake_dollars = always_redraw(
            lambda : Text("$").scale(0.6).set_color('#6B1012').next_to(jake_loan_repayment,LEFT,buff=0.02)
        )
        
        john_dollars = always_redraw(
            lambda : Text("$").scale(0.6).set_color('#6B1012').next_to(john_loan_repayment,LEFT,buff=0.02)
        )
        
        self.add(jake,jake_loan,jake_name,jake_years,jake_loan_repayment,jake_details,jake_dollars,john,john_loan,john_name,john_years,john_loan_repayment,john_details,john_dollars)
        self.wait(2)

        for i in range(3):
            compound_underline = Underline(john_years[i]).set_color(BLACK)
            self.play(Create(compound_underline),rate_func=smooth,run_time=0.7)
            self.wait(0.3)
            self.play(Uncreate(compound_underline),rate_func=smooth,run_time=0.5)

        self.wait(1)
        rectangle = SurroundingRectangle(jake_years).set_color(BLACK)
        self.play(Create(rectangle),rate_func=smooth)
        self.wait(0.5)
        self.play(Uncreate(rectangle),rate_func=smooth)
        self.wait(4)
        self.play(Create(line_for_jake),Create(line_for_john),Create(john_fifty),Create(jake_fifty),rate_func=smooth)
        self.play(Create(SurroundingRectangle(john_fifty).set_color('#6B1012')),Create(SurroundingRectangle(jake_fifty).set_color('#6B1012')),rate_func=smooth)
        final_texts = Text("After 50 years").move_to([0,2.5,0]).set_color(BLACK)
        self.play(FadeOut(VGroup(jake_details,john_details)),rate_func=smooth)
        self.play(FadeIn(final_texts),jake_tracker.animate.set_value(6000),john_tracker.animate.set_value(117391),john_loan_repayment.animate.shift([0.2,0,0]),rate_func=smooth)
        self.wait(10)
        
        
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

        self.play(FadeIn(share_emoji),FadeIn(share),rate_func=smooth)
        self.play(FadeIn(subscribe_emoji),FadeIn(subscribe),rate_func=smooth)
        
        self.wait(3)
        self.play(FadeIn(thanks),FadeIn(thanks_emoji),rate_func=smooth)
        self.wait(5)