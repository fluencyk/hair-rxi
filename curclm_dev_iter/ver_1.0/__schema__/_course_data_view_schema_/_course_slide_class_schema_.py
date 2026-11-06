from dataclasses import dataclass, field
from typing import Any


@dataclass
class SlideItem:
    type: str
    content: Any


@dataclass
class CCSRef:
    field: str
    stem: str
    path: list[str] = field(default_factory=list)


@dataclass
class Slide:
    index: int
    title: str
    purpose: str

    items: list[SlideItem] = field(default_factory=list)
    ccs_refs: list[CCSRef] = field(default_factory=list)
    objective_refs: list[str] = field(default_factory=list)


@dataclass
class CourseWeekSlides:
    course_ref: str
    week: int
    slides: list[Slide] = field(default_factory=list)
