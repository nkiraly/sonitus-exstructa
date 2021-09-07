#!/usr/bin/env python3

from os import getenv

import click
import datetime
import logging
import structlog
import sys
from pythonjsonlogger import jsonlogger

from sonitus_exstructa.event_generator import (
    DEFAULT_ACTORS,
    DEFAULT_VERBS,
    DEFAULT_TARGETS,
    DEFAULT_STATES,
    DEFAULT_FAILURES,
    EventGenerator,
)

json_handler = logging.StreamHandler(sys.stdout)
json_handler.setFormatter(jsonlogger.JsonFormatter())

logging.basicConfig(
    format="%(message)s",
    handlers=[json_handler],
    level=logging.INFO,
)


def add_timestamp(_, __, event_dict):
    event_dict["timestamp"] = datetime.datetime.utcnow()
    return event_dict


structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        add_timestamp,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.render_to_log_kwargs,
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

_common_sonitus_exstructa_args_and_options = [
    click.option('--actor', envvar='SONITUS_EXSTRUCTA_ACTOR', multiple=True, default=DEFAULT_ACTORS,
                 help='The actors that perform verbs on targets'),
    click.option('--verb', envvar='SONITUS_EXSTRUCTA_VERB', multiple=True, default=DEFAULT_VERBS,
                 help='The verbs that actors perform on targets'),
    click.option('--target', envvar='SONITUS_EXSTRUCTA_TARGET', multiple=True, default=DEFAULT_TARGETS,
                 help='The names of targets that actors perform verbs on'),
    click.option('--state', envvar='SONITUS_EXSTRUCTA_STATE', multiple=True, default=DEFAULT_STATES,
                 help='The states that that actors get targets in'),
    click.option('--failure', envvar='SONITUS_EXSTRUCTA_FAILURE', multiple=True, default=DEFAULT_FAILURES,
                 help='How an actor failed to get a target in the specified state'),
]


def common_sonitus_exstructa_args_and_options(func):
    """
    Common Arguemnets and Options for all CLI commands
    """
    for option in reversed(_common_sonitus_exstructa_args_and_options):
        func = option(func)
    return func


@click.group()
def sonitus_exstructa():
    """
    Structure Log Generator for Logging Pipeline testing.
    """


@sonitus_exstructa.command('generate')
@common_sonitus_exstructa_args_and_options
def generate_command(
    actor,
    verb,
    target,
    state,
    failure
):
    """
    Generate structured logs with specified options
    """
    generator = EventGenerator(
        logger,
        actor,
        verb,
        target,
        state,
        failure,
    )
    generator.generate()


def main():
    """
    Sonitus Exstructa Command Line Interface Entrypoint
    """
    sonitus_exstructa()


if __name__ == "__main__":
    main()
