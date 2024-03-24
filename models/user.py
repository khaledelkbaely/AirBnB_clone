#!/usr/bin/python3
"""module for User"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User"""
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
