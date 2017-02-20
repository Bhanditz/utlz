import utlz


def test_flo():
    foo = 'AAA'
    bar = 'Bbb'
    baz = 'ccc'

    assert utlz.flo('{foo}.{bar}.{baz}') == 'AAA.Bbb.ccc'

    long_ = '{foo}.{bar}.{baz}'.format(**locals())
    assert utlz.flo('{foo}.{bar}.{baz}') == long_

    very_long = '{foo}.{bar}.{baz}'.format(foo=foo, bar=bar, baz=baz)
    assert utlz.flo('{foo}.{bar}.{baz}') == very_long
