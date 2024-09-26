#!/usr/bin/python3
"""
Package initializer for storage

"""
from storage.file_storage import FileStorage


storage = FileStorage()
storage.reload()
