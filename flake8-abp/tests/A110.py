def foo():
    return [
        # A110
        "foo",
        # A110
        "",
        # A110
        '\'',
        # A110
        "\"",
        # A110
        "\"'",
        # A110
        b"foo",
        # A110
        u"foo",
        # A110
        r"foo",
        # A110
        '''foo''',
        # A110
        """foo""",

        'foo',
        '',
        "'",
        '"',
        '\'"',
        '\xc3\xa4',
        b'\xc3\xa4',
        u'\xe4',
        r'\'\"',
    ]
