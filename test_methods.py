import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sum():
    # given a = 2 and b = 5
    a = 2
    b = 5

    # when we calculate the sum
    output = methods.sum(a, b)

    # then the sum should be 7
    assert output == 7 

def test_difference():
    # given a = 2 and b = 5
    a = 2
    b = 5

    # when we calculate the difference
    output = methods.difference(a, b)

    # then the difference should be -3
    assert output == -3

def test_product():
    # given a = 2 and b = 5
    a = 2
    b = 5

    # when we calculate the product
    output = methods.product(a, b)

    # then the product should be 10
    assert output == 10

def test_quotient():
    # given a = 2 and b = 5
    a = 2
    b = 5

    # when we calculate the quotient
    output = methods.quotient(a, b)

    # then the quotient should be 0.4
    assert output == 0.4