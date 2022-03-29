def robot(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz'

    if num % 5 == 0:
        return 'buzz'

    if num % 3 == 0:
        return 'fizz'

    return str(num)


if __name__ == "__main__":
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
