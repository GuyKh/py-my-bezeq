from dataclasses import dataclass, field
from typing import Optional

from mashumaro import DataClassDictMixin, field_options


@dataclass
class ElectSubscriber(DataClassDictMixin):
    subscriber: str = field(metadata=field_options(alias="Subscriber"))
    is_current: bool = field(metadata=field_options(alias="IsCurrent"))
    address: str = field(metadata=field_options(alias="Address"))


@dataclass
class BaseEntity(DataClassDictMixin):
    id: int = field(metadata=field_options(alias="Id"))
    title: str = field(metadata=field_options(alias="Title"))
    sub_title: Optional[str] = field(metadata=field_options(alias="SubTitle"))
    picture: Optional[str] = field(metadata=field_options(alias="Picture"))
    order: int = field(metadata=field_options(alias="Order"))


@dataclass()
class BaseCard(BaseEntity):
    billing_service_id: Optional[str] = field(metadata=field_options(alias="BillingServiceId"))
    billing_service_code: Optional[str] = field(metadata=field_options(alias="BillingServiceCode"))
    billing_service_description: Optional[str] = field(metadata=field_options(alias="BillingServiceDescription"))
    card_type: str = field(metadata=field_options(alias="CardType"))
    service_type: str = field(metadata=field_options(alias="ServiceType"))
    makat: Optional[str] = field(metadata=field_options(alias="Makat"))
    quantity: Optional[int] = field(metadata=field_options(alias="Quantity"))
    sn: Optional[str] = field(metadata=field_options(alias="SN"))
    mac: Optional[str] = field(metadata=field_options(alias="Mac"))
    link: Optional[str] = field(metadata=field_options(alias="Link"))
    enter_link: Optional[str] = field(metadata=field_options(alias="EnterLink"))
    show_mesh_mgt: bool = field(metadata=field_options(alias="ShowMeshMgt"))
