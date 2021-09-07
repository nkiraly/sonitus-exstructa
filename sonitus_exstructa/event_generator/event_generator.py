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

DEFAULT_ACTIONS = [
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

    def __init__(self, logger, actors, actions, targets, states, failures):
        self.logger = logger
        self.actors = actors
        self.actions = actions
        self.targets = targets
        self.states = states
        self.failures = failures

        self._min_delay = 3
        self._max_delay = 30

        self._percent_failures = 10

        self._success_template = Template("""$actor $action $target $state""")
        self._failure_template = Template("""$actor $failure $action $target $state""")

        # private cache values for message facets
        self._actor = None
        self._action = None
        self._target = None
        self._state = None
        self._failure = None

    def generate(self):
        """
        Generate Log Messages Until Interrupted
        """
        while True:
            self._generate_values()

            # default info message success
            level = logging.INFO
            msg = self._generate_message(self._success_template)
            result = "SUCCESS"

            # is this message a failure
            if random.randint(1, 100) <= self._percent_failures:
                level = logging.ERROR
                msg = self._generate_message(self._failure_template)
                result = "FAILURE"

            self.logger.log(
                level,
                msg,
                actor=self._actor,
                action=self._action,
                target=self._target,
                state=self._state,
                result=result,
            )
            sleep(random.randint(self._min_delay, self._max_delay))

    def _generate_values(self):
        self._actor = random.choice(self.actors)
        self._action = random.choice(self.actions)
        self._target = random.choice(self.targets)
        self._state = random.choice(self.states)
        self._failure = random.choice(self.failures)

    def _generate_message(self, template):
        msg = template.substitute(
            actor=self._actor,
            action=self._action,
            target=self._target,
            state=self._state,
            failure=self._failure,
        )
        return msg
