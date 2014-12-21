#!/usr/bin/env python
# encoding: utf-8

import os
import time
import chardet
import codecs

from django.core.management.base import CommandError

from usda.management.commands import USDACommand
from usda import models as usda_models

class USDAImportError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Command(USDACommand):
    args = '<directory>'

    """
    option_list = USDACommand.option_list + (
        make_option('--format', '-f', action='store', dest='format', default='json',
            help='Format of file to import from.'),
        )
    """
    help = 'Imports data form files in <dir>'

    def _parse_line(self, line, _sep='~^'):
        line = line.strip()
        line = line.encode('utf-8')
        def validate_token(token):
            token = token.strip('~')
            return str(token) if len(token) else None

        data = [validate_token(token) for token in line.split('^')]
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
                except USDAImportError as e:
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
            raise CommandError('Directory for USDA files is needed.')

        t1 = time.time()

        path = args[0]
        self.v('Importing USDA National Nutrient Database for Standard Reference from dir %r' % path)

        errors = 0

        self.v(' - Importing LanguaL Factors Description File')
        errors += self._handle_model(path, usda_models.LangualFactorsDescription)

        self.v(' - Importing LanguaL Factors File')
        errors += self._handle_model(path, usda_models.LangualFactor)

        self.v(' - Importing Sources of Data File')
        errors += self._handle_model(path, usda_models.SourcesOfData)

        self.v(' - Importing Nutrient Definition File')
        errors += self._handle_model(path, usda_models.NutrientDefinition)

        self.v(' - Importing Data Source Link File')
        errors += self._handle_model(path, usda_models.DataSourceLink)

        self.v(' - Importing Data Derivation Code File')
        errors += self._handle_model(path, usda_models.DataDerivationCode)

        self.v(' - Importing Source Code File')
        errors += self._handle_model(path, usda_models.SourceCode)

        self.v(' - Importing Weight File')
        errors += self._handle_model(path, usda_models.Weight)

        self.v(' - Importing Nutrient Data File')
        errors += self._handle_model(path, usda_models.NutrientData)

        self.v(' - Importing Footnote File')
        errors += self._handle_model(path, usda_models.Footnote)

        self.v(' - Importing Food Group File')
        errors += self._handle_model(path, usda_models.FoodGroup)

        self.v(' - Importing Food Description File')
        errors += self._handle_model(path, usda_models.FoodDescription)

        t2 = time.time()
        self.v('Exec time: ' + str(round(t2 - t1)), 1)
        return 'Import end (%d errors)' % errors

