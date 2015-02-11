import unicodecsv

from django.core.management.base import BaseCommand, CommandError
from django.db import models

from src.apps.hotel.models import City, Hotel


class Command(BaseCommand):
    args = '[data_source] [model_name]'
    help = 'Imports the hotel and city data'
    output_transaction = True

    CITY = 'city'
    HOTEL = 'hotel'

    MODEL_CHOICES = [CITY, HOTEL]

    MODELS = {
        CITY: City,
        HOTEL: Hotel,
    }

    MAPPINGS = {
        CITY: {
            'code': 'code',
            'name': 'name'
        },
        HOTEL: {
            'city': 'code',
            'code': 'code',
            'name': 'name'
        }
    }

    CITY_FIELD_NAMES = ['code', 'name']

    line_count = 0
    imported_line_count = 0
    failed_line_count = 0

    def handle(self, *args, **options):
        try:
            data_source, model_name = args
        except ValueError:
            raise CommandError('Invalid arguments, must provide: %s' % self.args)

        if model_name not in self.MODEL_CHOICES:
            raise CommandError(
                "Invalid model name choices. Valid choices are: %s." % self.MODEL_CHOICES
            )

        self.import_data(data_source, model_name)

    def import_data(self, data_source, model_name):
        for line in self.read_file(data_source, model_name):
            self.line_count += 1
            mapped_fields = {}

            for field in self.MODELS[model_name]._meta.fields:
                if field.name in self.MAPPINGS[model_name]:
                    if isinstance(field, models.fields.related.ForeignKey):
                        mapped_fields[field.name] = self.get_many_to_one_model(
                            field, self.MAPPINGS[model_name][field.name], line[field.name]
                        )
                    else:
                        mapped_fields[field.name] = line[field.name]

            try:
                c = self.MODELS[model_name](**mapped_fields)
                c.save()
            except StandardError as e:
                self.failed_line_count += 1
                self.stderr.write('Line no %s %s could not be imported. Reason %s.' %
                                  (self.line_count, line, e.message))
            else:
                self.imported_line_count += 1

        self.stdout.write('Successfully imported %s lines out of %s lines.' %
                          (self.imported_line_count, self.line_count))

        if self.failed_line_count > 0:
            self.stderr.write('Number of skipped line is %s.' % self.failed_line_count)

    def read_file(self, data_source, model_name):
        csv_file = open(data_source, 'r')
        reader = unicodecsv.DictReader(csv_file, self.MAPPINGS[model_name].keys(), encoding='utf-8', delimiter=';')
        for line in reader:
            yield line

    def get_many_to_one_model(self, related_field, lookup_field, value):
        try:
            related_model = related_field.rel.to.objects.get(**{lookup_field: value})
        except related_field.rel.to.DoesNotExist:
            related_model = None
            self.stderr.write('Line no %s: Related model %s does not exist for %s %s."' %
                              (self.line_count, related_field, lookup_field, value))

        return related_model
