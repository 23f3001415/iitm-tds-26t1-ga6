from dataclasses import dataclass

from hypothesis import given, strategies as st


@dataclass(frozen=True)
class RankedValue:
    value: int
    tag: int

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return isinstance(other, RankedValue) and self.value == other.value


@st.composite
def ranked_value_lists(draw):
    duplicated_value = draw(st.integers())
    tail = draw(st.lists(st.integers(), max_size=8))
    values = [duplicated_value, duplicated_value, *tail]
    return [RankedValue(value=v, tag=i) for i, v in enumerate(values)]


@given(ranked_value_lists())
def test_sort_ranked_queue_matches_stable_sorted_order(items):
    result = sort_ranked_queue(items)
    expected = sorted(items, key=lambda item: item.value)

    assert [item.value for item in result] == [item.value for item in expected]
    assert [item.tag for item in result] == [item.tag for item in expected]
