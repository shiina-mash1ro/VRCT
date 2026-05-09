from dataclasses import dataclass
from typing import Protocol, Optional


@dataclass
class TranscriptionEvent:
    type: str  # partial|final
    text: str
    source: str  # mic|speaker
    language: Optional[str] = None
    segment_id: Optional[str] = None
    confidence: float = 0.0


class ASRBackend(Protocol):
    def transcribe(self, audio_wav: bytes, language: Optional[str] = None) -> str:
        ...
