class Handler:
    event_name = None

    def __init_subclass__(cls, **kwargs):
            if cls.event_name is None:
                raise ValueError(f"{cls.__name__} must define 'event_name'")
            super().__init_subclass__(**kwargs)

    def handle_event(self, data):
        raise NotImplementedError("Subclasses must implement the handle_event method.")