from typing import Any, Dict, List, Optional, Type, Union
from pydantic import BaseModel, create_model
from app.utils.time import indo_now

STANDARD_RESPONSE_CLASS_NAME = "StandardResponseModel"


def create_standard_response(
    status: str = "",
    message: str = "",
    data: Dict[str, Any] = None,
    errors: Optional[List[str]] = None,
) -> Type[BaseModel]:
    model = create_model(
        STANDARD_RESPONSE_CLASS_NAME,
        status=(str, ""),
        message=(str, ""),
        data=(Union[Dict[str, Any], List[Any]], None),
        errors=(Optional[List[str]], None),
        timestamp=(int, 123),
    )

    return model(
        status=status,
        message=message,
        data=data,
        errors=errors,
        timestamp=int(indo_now().timestamp()),
    )
