from prefect_demo.flows.e01_my_first_flow import add_and_square


def test_add_and_square():
    assert add_and_square(4, 8) == 144, "function add_and_square() not working properly"
