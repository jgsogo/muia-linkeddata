#!/usr/bin/env python
# encoding: utf-8

import os
import time
import chardet
import codecs

from django.core.management.base import CommandError

from food.management.commands import RAFCOCommand
from food import models as food_models
from allergen import models as allergen_models
from nutrients import models as nutrients_models
from diseases import models as diseases_models

class RAFCOImportError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Command(RAFCOCommand):
    args = '<directory>'

    """
    option_list = FoodCommand.option_list + (
        make_option('--format', '-f', action='store', dest='format', default='json',
            help='Format of file to import from.'),
        )
    """
    help = 'Imports data form files in <dir>'

    def _parse_line(self, line, _sep=';'):
        line = line.strip()
        line = line.encode('utf-8')

        data = [token for token in line.split(';')]
        message = '%s' % token
        return data

    def _handle_model(self, path, model_class):
        try:
            filename = os.path.join(path, '%s.txt'%model_class.filename)
            charenc = chardet.detect(open(filename).read())

            lines = codecs.open(filename, 'r', encoding=charenc['encoding']).readlines()

            i = errors = 0
            total = len(lines)
            for line in lines:
                i+=1
                errors_message = ''
                message = ''
                try:
                    data = self._parse_line(line)
                    model_class.objects.create_from_list(data)
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
            return errors
        except IOError as e:
            raise CommandError('Could not open file %r' % filename)
        else:
            #f.close()
            pass


    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        if len(args) != 1:
            raise CommandError('Directory for RAFCO files is needed.')

        t1 = time.time()

        path = args[0]
        self.v('Importing RAFCO DATA from %r' % path)

        errors = 0

#        self.v(' - Importing Allergen File')
#        errors += self._handle_model(path, allergen_models.Allergen)

#        self.v(' - Importing Nutrients File')
#        errors += self._handle_model(path, nutrients_models.Nutrient)

#        self.v(' - Importing Food Description File')
#        errors += self._handle_model(path, food_models.Food)

#        self.v(' - Importing Weight File')
#        errors += self._handle_model(path, food_models.Weight)

#        self.v(' - Importing Food Nutrients Composition File')
#        errors += self._handle_model(path, food_models.FoodNutrients)

#        self.v(' - Importing Langual Description File')
#        errors += self._handle_model(path, food_models.LangualDesc)

        self.v(' - Importing Langual Data File')
        errors += self._handle_model(path, food_models.Langual)

#        self.v(' - Importing Disease Data File')
#        errors += self._handle_model(path, diseases_models.Disease)

#        self.v(' - Importing Allergen Causes Disease Data File')
#        errors += self._handle_model(path, diseases_models.AllergenCausesDisease)

        t2 = time.time()
        self.v('Exec time: ' + str(round(t2 - t1)), 1)
        return 'Import end (%d errors)' % errors

