from pydantic import BaseModel, Field
from datetime import timezone, datetime


class Event(BaseModel):
    """
    The base event.

    Parameters
    -----------
    - name `(str)`: The name or type of the event.
    - timestamp `(datetime, optional)`: Timestamp of when the event occurred.
    - source `(str, optional)`: Source or origin of the event.
    - serializer_format `(str, optional)`: supported formats are protobuf & flatbuffers. protobuf is defualt.
    """
    name: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    source: str
    serializer_format: str = 'protobuf'
