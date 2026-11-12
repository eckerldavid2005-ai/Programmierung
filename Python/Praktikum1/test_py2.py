import pytest
import Python.Praktikum1.p2 as p2

def test_while_loop(capsys):
    a = p2.while_loop()
    assert a == 101 or a == 100
    out = capsys.readouterr().out
    lines = out.split("\n")
    for i in range(101):
        assert str(i) in lines
    assert "101" not in lines
    assert "-" not in out

def test_add():
    for i in range(10):
        assert p2.add(i, i) == 2 * i

def test_two_return_args():
    assert p2.two_return_args(2) == (2, 4)

def test_while_loop_list(capsys):
    my_list = [1, 5, 9, 3]
    p2.while_loop_list(my_list)
    out = capsys.readouterr().out
    lines = out.split("\n")
    for i in my_list:
        assert str(i) in lines

def test_for_loop(capsys):
    p2.for_loop()
    out = capsys.readouterr().out
    lines = out.split("\n")
    for i in range(0, 100, 2):
        assert str(i) in lines
    for i in range(1, 100, 2):
        assert str(i) not in lines

def test_for_loop_list(capsys):
    my_list = range(0, 4)
    p2.for_loop_list(my_list)
    out = capsys.readouterr().out
    assert "\n".join([f"{a} : {a}" for a in my_list]) in out

def test_for_loop_dict(capsys):
    my_dict = {"A": 1, "B": 2, "C": 3}
    p2.for_loop_dict(my_dict)
    out = capsys.readouterr().out
    for key, val in my_dict.items():
        assert f"{key} : {val}" in out

def test_create_list():
    assert p2.create_list() == list(range(1, 5))

def test_create_list2():
    assert p2.create_list2() == [1, "Hallo", 3.14]

def test_create_dict():
    assert p2.create_dict() == {"Muenchen": 1488202, "Nuernberg": 515543, "Landshut": 73065}

def test_to_binary():
    assert p2.to_binary(0xA5) == "10100101"