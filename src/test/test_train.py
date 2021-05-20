import pytest

from ..metro import Metro
from ..train import Train


def test_that_train_is_created():
    metro = Metro.fromJson()
    train = Train.new(metro)

    assert train is not None
    assert train._metro is not None


def test_that_color_works():
    metro = Metro.fromJson()

    train = Train.new(metro)
    assert train._color is None

    train = Train.new(metro).color("red")
    assert train._color == "red"

    train = Train.new(metro).color("green")
    assert train._color == "green"

    with pytest.raises(Exception):
        Train.new(metro).color("$$$$")


def test_that_train_can_travel():
    metro = Metro.fromJson()
    train = Train.new(metro).origin("A").to("F").travel()
    assert len(train.shortest) == 6

    first = train.shortest[0]
    assert first.id == metro.station("A").id

    last = train.shortest[-1]
    assert last.id == metro.station("F").id

    with pytest.raises(Exception):
        Train.new(metro).origin("A").to("A").travel()


def test_that_red_train_can_travel():
    metro = Metro.fromJson()
    train = Train.red(metro).origin("A").to("H").travel()
    assert len(train.shortest) == 4

    last = train.shortest[-1]
    assert last.id == metro.station("H").id

    train = Train.red(metro).origin("A").to("F").travel()
    assert len(train.shortest) == 5

    last = train.shortest[-1]
    assert last.id == metro.station("F").id

    with pytest.raises(Exception):
        Train.red(metro).origin("A").to("G").travel()

    with pytest.raises(Exception):
        Train.red(metro).origin("G").to("A").travel()


def test_that_green_train_can_travel():
    metro = Metro.fromJson()
    train = Train.green(metro).origin("A").to("G").travel()
    assert len(train.shortest) == 4

    last = train.shortest[-1]
    assert last.id == metro.station("G").id

    train = Train.green(metro).origin("A").to("F").travel()
    assert len(train.shortest) == 6

    last = train.shortest[-1]
    assert last.id == metro.station("F").id

    with pytest.raises(Exception):
        Train.green(metro).origin("A").to("H").travel()

    with pytest.raises(Exception):
        Train.green(metro).origin("H").to("A").travel()
