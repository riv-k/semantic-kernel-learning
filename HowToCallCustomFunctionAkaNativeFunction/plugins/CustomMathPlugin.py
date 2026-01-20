import math
from typing import Annotated
from semantic_kernel.functions.kernel_function_decorator import kernel_function
# from semantic_kernel.functions import kernel_function

class CustomMathPlugin:
    @kernel_function(name="DivideAndAdd")
    def addDivide(
        self,
        num1: Annotated[float, "the first number"],
        num2: Annotated[float, "the second number"],
    ) -> Annotated[float, "the output is a float"]:
        return (float(num1) / float(num2) + float(num1))