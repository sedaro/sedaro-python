from typing import Tuple, TypeAlias

StreamData: TypeAlias = dict[str, list]
Stream: TypeAlias = Tuple[list, dict]
Streams: TypeAlias = dict[str, Stream]

def concat_stream_data(main: StreamData, other: StreamData, len_main: int, len_other: int):
    assert type(main) == dict and type(other) == dict
    for k in other:
        if k not in main:
            main[k] = [None for _ in range(len_main)]
        main[k].extend(other[k])
    for k in main:
        if k not in other:
            main[k].extend([None for _ in range(len_other)])


def concat_stream(main: Stream, other: Stream, stream_id: str):
    len_main = len(main[0])
    len_other = len(other[0])
    main[0].extend(other[0])
    stream_id_short = stream_id.split('/')[0]
    concat_stream_data(main[1][stream_id_short], other[1][stream_id_short], len_main, len_other)


def concat_results(main: Streams, other: Streams):
    for stream in other:
        if stream not in main:
            main[stream] = other[stream]
        else:  # concat stream parts
            concat_stream(main[stream], other[stream], stream)


def update_metadata(main, other):
    for k in other['counts']:
        if k not in main['counts']:
            main['counts'][k] = 0
        main['counts'][k] += other['counts'][k]


def set_numeric_as_list(d):
    if isinstance(d, dict):
        if all(key.isdigit() for key in d.keys()):  # Check if all keys are array indexes in string form
            return [set_numeric_as_list(d[key]) for key in sorted(d.keys(), key=int)]
        else:
            return {k: set_numeric_as_list(v) for k, v in d.items()}
    return d


def __set_nested(results):
    nested = {}
    for k in sorted(list(results.keys())):
        v = results[k]
        try:
            ptr = nested
            tokens = k.split('.')
            for token in tokens[:-1]:
                if token not in ptr:
                    ptr[token] = {}
                ptr = ptr[token]
            ptr[tokens[-1]] = v
        except TypeError:
            ptr = nested
            for token in tokens[:-1]:
                if type(ptr[token]) == list:
                    del ptr[token]
                    break
                else:
                    ptr = ptr[token]
            ptr = nested
            for token in tokens[:-1]:
                if token not in ptr:
                    ptr[token] = {}
                ptr = ptr[token]
            ptr[tokens[-1]] = v
    return nested


# TODO: edge case where one page has all nones for a SV, then the next page has a bunch of vectors for it
def set_nested(results):
    nested = {}
    for k in results:
        kspl = k.split('/')[0]
        nested[k] = (results[k][0], {kspl: set_numeric_as_list(__set_nested(results[k][1][kspl]))})
    return nested
