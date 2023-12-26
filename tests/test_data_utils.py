from sedaro.branches.scenario_branch.sim_client import \
     __set_nested, set_nested, set_numeric_as_list, update_metadata, concat_results, concat_stream, concat_stream_data
from sedaro.results.utils import to_time_major

def test_set_nested_and_numeric():
    assert __set_nested({'foo.bar': [1, 2, 3], 'foo.baz': [1, 2, 3]}) == {'foo': {'bar': [1, 2, 3], 'baz': [1, 2, 3]}}
    assert __set_nested({'foo': [1, 2, 3], 'foo.bar': [1, 2, 3], 'foo.bar.baz': [1, 2, 3], 'foo.bar.baz.qux': [1, 2, 3]}) == \
         {'foo': {'bar': {'baz': {'qux': [1, 2, 3]}}}}
    d = {'foo/0': ([1, 2, 3], {'foo': {'bar.baz': [1, 2, 3], 'qux.corge': [2, 3, 4]}})}
    assert set_nested(d) == {'foo/0': ([1, 2, 3], {'foo': {'bar': {'baz': [1, 2, 3]}, 'qux': {'corge': [2, 3, 4]}}})}
    d['foo/1'] = ([1, 2, 3, 4, 5], {'foo': {'bar.baz': [1, 2, 3, 4, 5], 'bar.qux': [2, 3, 4, 5, 6]}})
    assert set_nested(d) == {
        'foo/0': ([1, 2, 3], {'foo': {'bar': {'baz': [1, 2, 3]}, 'qux': {'corge': [2, 3, 4]}}}),
        'foo/1': ([1, 2, 3, 4, 5], {'foo': {'bar': {'baz': [1, 2, 3, 4, 5], 'qux': [2, 3, 4, 5, 6]}}})
    }
    assert set_numeric_as_list({'a': [1, 2], 'b': {'0': [1, 2], '1': [1, 2]}}) == {'a': [1, 2], 'b': [[1, 2], [1, 2]]}
    assert set_numeric_as_list({'a': [1, 2], 'b': {'zero': [1, 2], 'one': [1, 2]}}) == {'a': [1, 2], 'b': {'zero': [1, 2], 'one': [1, 2]}}
    assert set_numeric_as_list(__set_nested({'a.0.0': [1, 2, 3], 'a.0.1': [4, 5, 6], 'a.1.0': [7, 8, 9], 'a.1.1': [10, 11, 12], 'b': [13, 14, 15]})) == {'a': [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], 'b': [13, 14, 15]}
    assert set_numeric_as_list(__set_nested({'a.0.0.0': [1, 2, 3], 'a.0.0.1': [4, 5, 6], 'a.0.1.0': [7, 8, 9], 'a.0.1.1': [10, 11, 12], 'a.1.0.0': [13, 14, 15], 'a.1.0.1': [16, 17, 18], 'a.1.1.0': [19, 20, 21], 'a.1.1.1': [22, 23, 24]})) == {'a': [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], [[[13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24]]]]}

def test_concat_and_update():
    main = {'counts': {'foo': 1, 'bar': 10, 'baz': 100, 'qux': 1000}}
    other = {'counts': {'baz': 1000, 'qux': 100, 'quux': 10, 'corge': 1}}
    combined = {'counts': {'foo': 1, 'bar': 10, 'baz': 1100, 'qux': 1100, 'quux': 10, 'corge': 1}}
    update_metadata(main, other)
    assert main == combined
    main = {'foo': 1, 'bar': 10, 'baz': 100, 'qux': 1000, 'counts': []}
    other = {'baz': 1000, 'qux': 100, 'quux': 10, 'corge': 1, 'counts': []}
    combined = {'foo': 1, 'bar': 10, 'baz': 100, 'qux': 1000, 'counts': []}
    update_metadata(main, other)
    assert main == combined
    main_data = {'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 4, 5]}
    other_data = {'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4, 5]}
    concat_stream_data(main_data, other_data, 5, 5)
    assert main_data == {
        'a': [1, 2, 3, 4, 5, None, None, None, None, None],
        'b': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
        'c': [None, None, None, None, None, 1, 2, 3, 4, 5]
    }
    main_data = ([1, 2, 3, 4, 5], {'foo': {'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 4, 5]}})
    other_data = ([6, 7, 8, 9, 10], {'foo': {'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4, 5]}})
    concat_stream(main_data, other_data, 'foo/0')
    assert main_data == ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], {'foo': {
        'a': [1, 2, 3, 4, 5, None, None, None, None, None],
        'b': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
        'c': [None, None, None, None, None, 1, 2, 3, 4, 5]
    }})
    main_result = {'foo/0': ([1, 2, 3, 4, 5], {'foo': {'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 4, 5]}}), 'foo/1': ([1, 2], {'foo': {'a': [1, 2]}})}
    other_result = {'foo/0': ([6, 7, 8, 9, 10], {'foo': {'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 4, 5]}}), 'foo/2': ([1, 2], {'foo': {'a': [1, 2]}})}
    concat_results(main_result, other_result)
    assert main_result == {
        'foo/0': ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], {'foo': {
            'a': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
            'b': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        }}),
        'foo/1': ([1, 2], {'foo': {'a': [1, 2]}}),
        'foo/2': ([1, 2], {'foo': {'a': [1, 2]}}),
    }

def test_concat_ragged():
    main = {'foo/0': ([1, 2, 3, 4, 5], {'foo': {
        'a.0': [1, 2, 3, 4, 5],
        'a.1': [1, 2, 3, 4, 5],
        'a.2': [1, 2, 3, 4, 5],
        'b.0': [1, 2, 3, 4, 5],
        'b.1': [1, 2, 3, 4, 5],
        'b.2': [1, 2, 3, 4, 5],
    }})}
    other = {'foo/0': ([6, 7, 8, 9, 10], {'foo': {
        'b.0': [6, 7, 8, 9, 10],
        'b.1': [6, 7, 8, 9, 10],
        'b.2': [6, 7, 8, 9, 10],
        'c.0': [6, 7, 8, 9, 10],
        'c.1': [6, 7, 8, 9, 10],
        'c.2': [6, 7, 8, 9, 10],
    }})}
    concat_results(main, other)
    result = set_nested(main)
    assert result == {'foo/0': ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], {'foo': {
        'a': [[1, 2, 3, 4, 5, None, None, None, None, None] for _ in range(3)],
        'b': [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] for _ in range(3)],
        'c': [[None, None, None, None, None, 6, 7, 8, 9, 10] for _ in range(3)]
    }})}

def test_to_time_major():
    assert to_time_major(True) == True # items other than lists or dicts are returned as is
    assert to_time_major([1, 2, 3]) == [1, 2, 3]
    assert to_time_major([[1, 2], [3, 4], [5, 6]]) == ([[1, 3, 5], [2, 4, 6]])
    assert to_time_major([[[1, 5, 9], [2, 6, 10]], [[3, 7, 11], [4, 8, 12]]]) == \
         [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]

def run_tests():
    test_set_nested_and_numeric()
    test_concat_and_update()
    test_concat_ragged()
    test_to_time_major()

run_tests()