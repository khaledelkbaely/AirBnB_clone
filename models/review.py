#!/usr/bin/python3
"""module for Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""
    place_id: str = ''
    user_id: str = ''
    text: str = ''
