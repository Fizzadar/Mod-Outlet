#!/usr/bin/env python

# Mod Outlet
# File: manage.py
# Desc: Django's manage.py

import os
import sys

from django.core.management import execute_from_command_line


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    execute_from_command_line(sys.argv)