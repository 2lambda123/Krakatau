# Mapping from test name -> tuple of argument lists.
registry = {
    'ArgumentTypes': (['42', 'false'], ['43', 'true'], ['1', '1', '1']),
    'ArrayTest': ([], ['x']),
    'BadInnerTest': ([],),
    'BoolizeTest': ([],),
    'ControlFlow': ([], ['.Na', 'q'], ['ddKK', '-2'], ['hB7X', '-1'],
                    ['R%%X', '0', '0'], ['>OE=.K', '#FF'],
                    ['95', ' ', 'x', 'x']),
    'DoubleEdge': ([], ['x']),
    'DuplicateInit': ([], ['5', '-7'], ['x', 'x', 'x']),
    'floattest': ([],),
    'NullInference': ([], ['alice'], ['bob', 'carol']),
    'OddsAndEnds': ([], ['x'], ['42'], ['4'], ['-2'], ['-0x567'], ['-5678']),
    'OldVersionTest': ([],),
    'SkipJSR': ([], ['x', 'x', 'x', 'x']),
    'splitnew': ([], ['-0'], ['-0', ''], ['-0', '', '', ''],
                 ['-0', '', '', '', '', '', '', '', '', '', '', '', '', '']),
    'StaticInitializer': ([],),
    'Switch': ([], ['0'], ['0', '1'], ['0', '1', '2'], ['0', '1', '2', '3'],
               ['0', '1', '2', '3', '4']),
    'Synchronized': ([], [''], ['', '', '', '']),
    'TryCatchTest': ([], ['bad'], ['bad', 'boy'], ['good'], [u'f'], ['=', '='],
                     ['<<', '<', ':', '>', '>>']),
    'UnicodeTest': ([],),
    'whilesize': ([], ['x'], ['x', 'x'], ['x', 'xx', 'x'],
                  ['The', 'Quick', 'Brown', 'Fox', 'Jumped', 'Over', 'The', 'Lazy', 'Dogs.'],
                  ['46', '08'], ['4608']),
}