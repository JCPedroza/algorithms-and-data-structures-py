from . import queue_list

test_subjects = [queue_list]


def validate_state(queue, exp_len: int, exp_is_empty: bool, exp_peek: int = 0) -> None:
    assert len(queue) == exp_len
    assert queue.is_empty() == exp_is_empty

    if not queue.is_empty():
        assert queue.peek() == exp_peek


def test_queue():
    for subject in test_subjects:
        queue = subject.structure()
        validate_state(queue, 0, True)

        queue.enqueue(2)
        validate_state(queue, 1, False, 2)

        queue.enqueue(4)
        validate_state(queue, 2, False, 2)

        queue.enqueue(6)
        validate_state(queue, 3, False, 2)

        assert queue.dequeue() == 2
        validate_state(queue, 2, False, 4)

        queue.clear()
        validate_state(queue, 0, True)
