from dataclasses import dataclass, field
from typing import List, Optional

from mashumaro import DataClassDictMixin, field_options

from my_bezeq.models.base import BaseClientResponse


@dataclass
class MenuChildItem(DataClassDictMixin):
    id: int = field(metadata=field_options(alias="id"))
    display_name: str = field(metadata=field_options(alias="displayName"))
    picture: Optional[str] = field(default=None, metadata=field_options(alias="picture"))
    link: str = field(metadata=field_options(alias="link"))
    order: int = field(metadata=field_options(alias="order"))
    menu_child_items: Optional[List["MenuChildItem"]] = field(default=None,
                                                              metadata=field_options(alias="menuChildItems"))


@dataclass
class MenuItem(DataClassDictMixin):
    id: int = field(metadata=field_options(alias="id"))
    display_name: str = field(metadata=field_options(alias="displayName"))
    picture: Optional[str] = field(default=None, metadata=field_options(alias="picture"))
    link: str = field(metadata=field_options(alias="link"))
    order: int = field(metadata=field_options(alias="order"))
    menu_child_items: List[MenuChildItem] = field(default_factory=list, metadata=field_options(alias="menuChildItems"))


@dataclass
class GetMenuResponse(BaseClientResponse):
    menu_items: List[MenuItem] = field(default_factory=list, metadata=field_options(alias="MenuItems"))
