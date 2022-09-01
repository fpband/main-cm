#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dotenv

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

def get_config(name: str, d_v=None, should_prompt=False):
    val = os.environ.get(name, d_v)
    if not val and should_prompt:
        try:
            val = input(f"enter {name}'s value: ")
        except EOFError:
            val = d_v
        print("\n")
    return val
