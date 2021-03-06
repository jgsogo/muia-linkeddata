#!/usr/bin/env python
# encoding: utf-8

import os
import time
import chardet
import codecs
import json

from django.core.management.base import BaseCommand, CommandError

from food.management.commands import RAFCOCommand
from food.models import Food

from optparse import make_option

class RAFCOImportError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Command(RAFCOCommand):

    args = '<directory>'
    help = 'Match Foods/Ingredients from Recipe List'


    def _parse_line(self, line):
        line = line.strip()
        line = line.encode('utf-8')

        data = [token for token in line.split(';')]
        message = '%s' % token
        return data


    def _handle_model(self, path):
        try:
            filename = os.path.join(path, 'recipes.txt')
            charenc = chardet.detect(open(filename).read())

            lines = codecs.open(filename, 'r', encoding=charenc['encoding']).readlines()
            i = errors = 0
            total = len(lines)
            all_ingredients = []

            for line in lines:
                i+=1
                errors_message = ''
                message = ''
                try:
                    data = self._parse_line(line)
                    food = Food.objects.filter(Long_Desc__icontains=u'%s' %data[0]).first()
                    if food is None:
                        self.stdout.write('Not Found!!')
                    else:
                        all_ingredients.append(u'%s;%s' % (food.NDB_No, data[0]))
                        self.stdout.write(u'%s;%s' % (food.NDB_No, data[0]))
                except RAFCOImportError as e:
                    errors +=1
                    errors_message = ' (%d errors)' % errors
                    message = 'ERROR - %s' % e
                except Exception as e:
                    errors +=1
                    errors_message = ' (%d errors)' % errors
                    message = 'ERROR - Unexpected %s' % e            
                if len(errors_message):
                    self.v('', 1, True)
                message = '%d%% [%d/%d] %s' % (int(round(float(i) / total * 100)), i, total, errors_message) + message
                self.v(message, 1, len(errors_message)==0)
            self.v('', 1, True)
            return all_ingredients, errors
        except IOError as e:
            raise CommandError('Could not open file %r' % filename)
        else:
            #f.close()
            pass


    def handle(self, *args, **options):
 
        super(Command, self).handle(*args, **options)
        
        if len(args) != 1:
            raise CommandError('Directory for Recipe Ingredients List file is needed.')

        path = args[0]
        self.v('Importing Recipe Ingredients from %r' % (path))

        t1 = time.time()
        errors = 0

        ingredients, errors = self._handle_model(path)

        outputfile = os.path.join(path, 'INGREDIENTS.txt')
        
        with open(outputfile, "w") as out:
            for ingred in ingredients:
                out.write(u'%s\n' % ingred)
            out.close()
        
        t2 = time.time()
        self.v('Exec time: ' + str(round(t2 - t1)), 1)
        return 'Import end (%d matches, %d errors)' % (len(ingredients), errors)
