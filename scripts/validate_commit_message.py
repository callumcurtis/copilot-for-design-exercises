#!/usr/bin/env python

import logging
import typing
import sys
import pathlib
import re


COMMIT_MESSAGE_TEMPLATE_PATH = pathlib.Path(__file__).parent.parent / ".gitmessage"
COMMIT_MESSAGE_TEMPLATE = COMMIT_MESSAGE_TEMPLATE_PATH.read_text(encoding="utf-8")


logger = logging.getLogger(__name__)


class AnsiColors:
    RED = '\033[91m'
    GREY = '\033[38m'
    YELLOW = '\033[33m'
    BOLD = '\033[1m'
    DEFAULT = '\033[0m'


class ColorFormatter(logging.Formatter):

    PLAIN_FORMAT = "%(levelname)s [%(filename)s:%(lineno)d]: %(message)s"

    LEVEL_TO_COLORED_FORMAT = {
        logging.DEBUG:      AnsiColors.GREY + PLAIN_FORMAT + AnsiColors.DEFAULT,
        logging.INFO:       AnsiColors.GREY + PLAIN_FORMAT + AnsiColors.DEFAULT,
        logging.WARNING:    AnsiColors.YELLOW + PLAIN_FORMAT + AnsiColors.DEFAULT,
        logging.ERROR:      AnsiColors.RED + PLAIN_FORMAT + AnsiColors.DEFAULT,
        logging.CRITICAL:   AnsiColors.RED + AnsiColors.BOLD + PLAIN_FORMAT + AnsiColors.DEFAULT
    }

    def format(self, record):
        fmt = self.LEVEL_TO_COLORED_FORMAT[record.levelno]
        formatter = logging.Formatter(fmt)
        return formatter.format(record)


class CommitMessage:

    def __init__(
        self,
        summary: str,
        body: typing.Optional[str],
        exercise_number: int,
        copilot_usage: str,
    ):
        self._summary = summary
        self._body = body
        self._exercise_number = exercise_number
        self._copilot_usage = copilot_usage

    @property
    def summary(self) -> str:
        return self._summary
    
    @property
    def body(self) -> typing.Optional[str]:
        return self._body
    
    @property
    def exercise_number(self) -> int:
        return self._exercise_number
    
    @property
    def copilot_usage(self) -> str:
        return self._copilot_usage
    
    @classmethod
    def parse(cls, text: str) -> 'CommitMessage':
        summary_pattern = re.compile(r"^(.{1,50})\n")
        exercise_number_pattern = re.compile(r"Exercise number:\s*([1-4])\s", re.IGNORECASE)
        copilot_usage_pattern = re.compile(r"Used Copilot:\s*(never|rarely|sometimes|often|always)(?:$|\s)", re.IGNORECASE)
        body_pattern = re.compile(r"^.{1,50}\n+(.+(?:\n|.)*.+)\n+\s*Exercise number:", re.IGNORECASE)

        summary = summary_pattern.search(text)
        exercise_number = exercise_number_pattern.search(text)
        copilot_usage = copilot_usage_pattern.search(text)
        body = body_pattern.search(text)
        
        required_match_with_error_message = [
            (summary, "Summary line is missing or is too long (max 50 chars)."),
            (exercise_number, "'Exercise number: [1-4]' is missing or has an invalid value."),
            (copilot_usage, "'Used Copilot: [never|rarely|sometimes|often|always]' is missing or has an invalid value."),
        ]

        def add_context_to_error_message(message: str) -> str:
            return (message +
                f" See {COMMIT_MESSAGE_TEMPLATE_PATH} for the required commit message format."
                f" Your commit message:\n{text}")

        for match, error_message in required_match_with_error_message:
            if not match:
                logger.error(add_context_to_error_message(error_message))
                return None

        summary = summary.group(1).strip()
        exercise_number = int(exercise_number.group(1))
        copilot_usage = copilot_usage.group(1)
        body = body.group(1).strip() if body else None

        return cls(summary, body, exercise_number, copilot_usage)


def init_logger():
    logger.setLevel(logging.DEBUG)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(ColorFormatter())

    logger.addHandler(console_handler)


def is_valid_commit_message(commit_message: str) -> bool:
    parsed = CommitMessage.parse(commit_message)

    if not parsed:
        return False

    default_summary = COMMIT_MESSAGE_TEMPLATE.partition("\n")[0]
    if default_summary == parsed.summary:
        logger.error("Commit message summary must be changed from default.")
        return False

    return True


def main():
    init_logger()
    commit_msg_filepath = pathlib.Path(sys.argv[1])

    if not is_valid_commit_message(commit_msg_filepath.read_text(encoding="utf-8")):
        exit(1)


if __name__ == "__main__":
    main()
