#!/usr/bin/env python
# encoding: utf-8

import sys
from django.core.management.base import BaseCommand, CommandError

class RAFCOCommand(BaseCommand):

    def v(self, message, level=1, inplace=False):
        if level<=self.verbosity:
            if inplace:
                sys.stdout.write("\r\x1b[K" + message.__str__())
                sys.stdout.flush()
            else:
                print message

    def handle(self, *args, **options):
        self.verbosity = options.get('verbosity')

