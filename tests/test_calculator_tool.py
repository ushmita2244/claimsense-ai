from services.tools.calculator_tool import CalculatorTool


def test_multiplication():

    calculator = CalculatorTool()

    result = calculator.execute(
        expression="25 * 6"
    )

    assert result.output == "150"


def test_parentheses():

    calculator = CalculatorTool()

    result = calculator.execute(
        expression="(18 + 7) * 4"
    )

    assert result.output == "100"


def test_division():

    calculator = CalculatorTool()

    result = calculator.execute(
        expression="100 / 5"
    )

    assert result.output == "20"


def test_power():

    calculator = CalculatorTool()

    result = calculator.execute(
        expression="5 ** 3"
    )

    assert result.output == "125"


def test_square_root():

    calculator = CalculatorTool()

    result = calculator.execute(
        expression="sqrt(81)"
    )

    assert result.output == "9"