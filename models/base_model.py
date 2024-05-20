#!/usr/bin/python3
"""
Base model modules
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base model
    """

    def __init__(self):
        """
        initialize the base model module
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        instance to save the string rep
        of the module
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        instance to return dict rep of the modules
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["updated_at"] = self.updated_at.isoformat()
        inst_dict["created_at"] = self.created_at.isoformat()
        return inst_dict

    def __str__(self):
        """
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print(f"\t{key}: ({type(my_model_json[key])}) - {my_model_json[key]}")
