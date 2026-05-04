# flake8: noqa
line_2 = "line_2"


def func_1():
    line_1 = "f1_line_1_1"
    line_2 = "f1_line_1_2"

    def func_2():
        line_1 = "f2_line_1"
        line_2 = "f2_line_2"

        def func_3():
            line_1 = "f3_line_1"
            line_2 = "f3_line_2"

    class class_1:
        line_1 = "c1_line_1"
        line_2 = "c1_line_2"

        def func_4(self):
            line_1 = "c1_f4_line_1"
            line_2 = "c1_f4_line_2"


class class_2:
    line_1 = "c2_line_1"
    line_2 = "c2_line_2"

    def func_5(self):
        line_1 = "c2_f5_line_1"
        line_2 = "c2_f5_line_2"
