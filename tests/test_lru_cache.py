from typing import Callable


def test_cache_hits(capfd, cached_printer_function: Callable) -> None:
    # function should be invoked, and print to stout
    cached_printer_function(1)
    captured = capfd.readouterr()
    assert captured.out == "args=(1,) kwargs={}"
    # this time cache is used, hence no print to stdout
    cached_printer_function(1)
    captured = capfd.readouterr()
    assert captured.out == ""
    cached_printer_function(banana="x")
    captured = capfd.readouterr()
    assert captured.out == "args=() kwargs={'banana': 'x'}"
    cached_printer_function(1)
    captured = capfd.readouterr()
    assert captured.out == ""
    cached_printer_function(banana="x")
    captured = capfd.readouterr()
    assert captured.out == ""


def test_cache_misses(capfd, cached_printer_function: Callable) -> None:
    cached_printer_function(1)
    cached_printer_function(2)
    cached_printer_function(3)
    captured = capfd.readouterr()
    assert captured.out == "args=(1,) kwargs={}args=(2,) kwargs={}args=(3,) kwargs={}"
    # first cache miss, 1 should be evicted
    cached_printer_function(4)
    captured = capfd.readouterr()
    assert captured.out == "args=(4,) kwargs={}"
    # cache hit, 3, 4, 2
    cached_printer_function(2)
    # cache miss, 3 should be evicted, 4, 2, 5
    cached_printer_function(5)
    captured = capfd.readouterr()
    assert captured.out == "args=(5,) kwargs={}"
    # cache miss, 2, 5, 3
    cached_printer_function(3)
    captured = capfd.readouterr()
    assert captured.out == "args=(3,) kwargs={}"
