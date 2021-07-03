from src.utils.operations import addition, subtraction, multiplication, division


def test_addition():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function addition
    THEN:  the resulting is the addition of the two numbers
    """
    assert addition(1,2) == 3
    assert addition(0,1) == 1
    assert addition(100,23) == 123
    pass


def test_subtraction():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function subtraction
    THEN:  the resulting is the subtraction of the two numbers
    """
    pass


def test_multiplication():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function multiplication
    THEN:  the resulting is the multiplication of the two numbers
    """
    pass


def test_division():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function division
    THEN:  the resulting is the division of the two number
    """
    pass


def test_division_exception_on_zero():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function division
    THEN:  the resulting is the division of the two number

    Hint: https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
    """
    pass
