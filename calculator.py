import flet
from flet import (Column,Container,ElevatedButton,Page,Row,Text,UserControl,colors)


class CalculatorApp(UserControl):
    def build(self):
        self.reset()

        # User Interface
        self.result = Text(value="0", color=colors.YELLOW_ACCENT_400, size=50)
        return Container(
            width=300,
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.result], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="All Clear",
                                bgcolor=colors.BLUE_500,
                                color=colors.YELLOW_ACCENT_400,
                                expand=3,
                                on_click=self.button_clicked,
                                data="AC",
                            ),
                            ElevatedButton(
                                text="/",
                                bgcolor=colors.DEEP_ORANGE_ACCENT_700,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="/",
                            ),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="7",
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="8",
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="9",
                            ),
                            ElevatedButton(
                                text="*",
                                bgcolor=colors.DEEP_ORANGE_ACCENT_700,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="*",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="4",
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="5",
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="6",
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.DEEP_ORANGE_ACCENT_700,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="-",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="1",
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="2",
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="3",
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.DEEP_ORANGE_ACCENT_700,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="+",
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=2,
                                on_click=self.button_clicked,
                                data="0",
                            ),
                            ElevatedButton(
                                text=".",
                                bgcolor=colors.BLUE_GREY_800,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data=".",
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.DEEP_ORANGE_ACCENT_700,
                                color=colors.YELLOW_ACCENT_400,
                                expand=1,
                                on_click=self.button_clicked,
                                data="=",
                            ),
                        ]
                    ),
                ],
            ),
        )

    def button_clicked(self, e) -> None:
        data = e.control.data
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        self.update()

    def calculate(self, operand1, operand2, operator) -> float:
        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)
            
    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: Page):

    # window settings
    page.title = "Calculator App"
    page.window_height = 380
    page.window_width = 335
    page.window_resizable = False

    calc = CalculatorApp()
    page.add(calc)


if __name__ == "__main__":
    flet.app(target=main)