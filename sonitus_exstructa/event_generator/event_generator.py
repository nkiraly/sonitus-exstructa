"""
Structured Logging Event Generator
"""

import logging
import random
from string import Template
from time import sleep

DEFAULT_ACTORS = [
    'PowerManager'
]

DEFAULT_VERBS = [
    'ensuring'
]

DEFAULT_TARGETS = [
    'accumulators'
]

DEFAULT_STATES = [
    'charged'
]

DEFAULT_FAILURES = [
    'failed'
]


class EventGenerator:
    """
    Log Generator Implementation
    """

    def __init__(self, logger, actors, verbs, targets, states, failures):
        self.logger = logger
        self.actors = actors
        self.verbs = verbs
        self.targets = targets
        self.states = states
        self.failures = failures

        self._min_delay = 13
        self._max_delay = 30

        self._percent_failures = 10

        self._success_template = Template("""$actor $verb $target $state""")
        self._failure_template = Template("""$actor $failure $verb $target $state""")

    def generate(self):
        """
        Generate Log Messages Until Interrupted
        """
        while True:
            level = logging.INFO
            msg = self._generate_message(self._success_template)

            # is this message a failure
            if random.randint(1, 100) <= self._percent_failures:
                level = logging.ERROR
                msg = self._generate_message(self._failure_template)

            self.logger.log(
                level,
                msg,
            )
            sleep(random.randint(self._min_delay, self._max_delay))

    def _generate_message(self, template):
        msg = template.substitute(
            actor=random.choice(self.actors),
            verb=random.choice(self.verbs),
            target=random.choice(self.targets),
            state=random.choice(self.states),
            failure=random.choice(self.failures),
        )
        return msg
