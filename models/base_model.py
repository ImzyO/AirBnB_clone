#!/usr/bin/python3
"""module for base_model.py"""

from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    class BaseModel: defines all common methods/attributes
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """initialization of public instance attributes"""
