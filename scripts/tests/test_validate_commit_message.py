import pytest

from scripts.validate_commit_message import CommitMessage


@pytest.mark.parametrize("exercise_number", [1, 2, 3, 4])
@pytest.mark.parametrize("copilot_usage", ["NeVer", "RaReLy", "SoMeTiMeS", "OfTeN", "AlWaYs"])
@pytest.mark.parametrize("whitespace", [whitespace * size for size in range(4) for whitespace in [' ', '\t']])
@pytest.mark.parametrize("newlines", ['\n' * size for size in range(4)])
def test_expected_commit_message(
    exercise_number,
    copilot_usage,
    whitespace,
    newlines,
):
    summary = "Fake 825!!~%~Summa@ry Line!"
    body = "Fake 9d!(s8~Body Line!"

    commit_message = (
        f"{whitespace}{summary}{whitespace}{newlines}\n"
        f"{whitespace}{body}{whitespace}{newlines}\n"
        f"{whitespace}Exercise number:{whitespace}{exercise_number}{whitespace}{newlines}\n"
        f"{whitespace}Used Copilot:{whitespace}{copilot_usage}{whitespace}{newlines}"
    )
    parsed = CommitMessage.parse(commit_message)
    assert parsed.summary == summary
    assert parsed.body == body
    assert parsed.exercise_number == exercise_number
    assert parsed.copilot_usage == copilot_usage


def test_missing_body():
    summary = "Fake 825!!~%~Summa@ry Line!"
    commit_message = f"{summary}\nExercise number: 1\nUsed Copilot: never"
    parsed = CommitMessage.parse(commit_message)
    assert parsed.summary == summary
    assert parsed.body is None
    assert parsed.exercise_number == 1
    assert parsed.copilot_usage == "never"


@pytest.mark.parametrize("exercise_number", [-100, 0, 5, 100])
def test_unrecognized_exercise_number(exercise_number):
    commit_message = f"Fake 825!!~%~Summa@ry Line!\nExercise number: {exercise_number}\nUsed Copilot: never"
    parsed = CommitMessage.parse(commit_message)
    assert parsed is None


@pytest.mark.parametrize("copilot_usage", ["never1", "_rarely", "foobar", "often@", "alwayss\n"])
def test_unrecognized_copilot_usage(copilot_usage):
    commit_message = f"Fake 825!!~%~Summa@ry Line!\nExercise number: 1\nUsed Copilot: {copilot_usage}"
    parsed = CommitMessage.parse(commit_message)
    assert parsed is None
