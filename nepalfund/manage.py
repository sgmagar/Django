#!/usr/bin/env python
import os
import sys
import socket

if __name__ == "__main__":
    if socket.gethostname() == 'ip-172-31-48-66':
    	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nepalfund.settings")
    else:
       os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nepalfund.settings_dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
