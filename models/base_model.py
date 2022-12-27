#!/usr/bin/python3
from models import storage

from datetime import datetime
import uuid

class BaseModel():
    def __init__(self, *args, **kwargs) -> None:

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)



    # human-readable format
    def __str__(self) -> str:
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    # to_dict will convert to something like this(json)
    # {'id': '67a61b91-d6a9-4afc-a93e-13dfc43e0cf5', 'created_at': '2022-12-15T00:33:11.126898', 'updated_at': '2022-12-15T00:34:43.881914', 'name': 'my first model', 'number': 89, '__class__': 'Basemodel'}
    def to_dict(self) -> dict:
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
    
# instance = BaseModel()
# print(instance.id)