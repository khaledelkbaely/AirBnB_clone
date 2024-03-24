#!/usr/bin/python3
"""module for City"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City"""
    state_id: str = ''
    name: str = ''
