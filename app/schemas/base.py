from typing import Any, Dict, Optional, List, Union

from pydantic import BaseModel


class BaseResponse(BaseModel):

    status: str
    message: str
    data: Union[Dict[str, Any], List[Any], Any]
    errors: Optional[List[str]]
    timestamp: int
