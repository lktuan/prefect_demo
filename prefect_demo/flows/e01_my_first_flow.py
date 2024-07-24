# Example of processing some data
from prefect import flow, task


@task(name="Addition operator")  # this task will successfully run
def add(a: int = 0, b: int = 0) -> int:
    return a + b


@task(name="Squaring operator")  # this task will fail
def square_num(num: int = 0) -> int:
    # if True:
    #     raise ValueError
    return num**2


@flow(log_prints=True, name="Add and Square", description="My first simple flow")
def add_and_square(a: int = 2, b: int = 3):
    add_result = add(a, b)
    square_result = square_num(add_result)
    print(f"({a} + {b}) squared = {square_result}")
    return square_result
