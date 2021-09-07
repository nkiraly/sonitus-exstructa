"""
Structured Logging Event Generator
"""

DEFAULT_ACTORS = [
    'Overlord'
]

DEFAULT_VERBS = [
    'ensuring'
]

DEFAULT_TARGETS = [
    'pylons'
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

    def generate(self):
        """
        Generate Log Messages Until Interrupted
        """
        self.logger.info("Generate Message")
