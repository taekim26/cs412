# File: voter_analytics/models.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/25/2026
# Description: data model for voter_analytics application

from django.db import models

# Create your models here.
class Voter(models.Model):
    '''store/represent the data of one voter at Newton, MA'''
    voter_id = models.CharField(max_length=15)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    addr_st_num = models.CharField(max_length=10)
    addr_st_name = models.CharField(max_length=50)
    addr_apt_num = models.CharField(max_length=20, blank=True)
    addr_zip_code = models.CharField(max_length=10)
    dob = models.DateField()
    dor = models.DateField()
    party_affil = models.CharField(max_length=2)
    prec_num = models.IntegerField()
    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()
    voter_score = models.IntegerField()

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.first_name} {self.last_name}'

def load_data():
    '''function to load data records from CSV file into Django model instances'''
    # delete existing records to avoid duplicates
    Voter.objects.all().delete()
    filename = '/Users/taeyeungkim/Desktop/Academics/Fall 26/CASCS 412/newton_voters.csv'
    f = open(filename, 'r')
    # discard headers
    f.readline() 

    for line in f:
        fields = line.strip().split(',')
        try:
            # create a new instance of Voter object with this record from CSV
            voter = Voter(
                voter_id = fields[0],
                last_name = fields[1],
                first_name = fields[2],
                addr_st_num = fields[3],
                addr_st_name = fields[4],
                addr_apt_num = fields[5],
                addr_zip_code =fields[6],
                dob = fields[7],
                dor = fields[8],
                party_affil = fields[9],
                prec_num = fields[10],
                v20state = fields[11].strip().upper() == 'TRUE',
                v21town = fields[12].strip().upper() == 'TRUE',
                v21primary = fields[13].strip().upper() == 'TRUE',
                v22general = fields[14].strip().upper() == 'TRUE',
                v23town = fields[15].strip().upper() == 'TRUE',
                voter_score = fields[16],
            )
            voter.save()
            print(f'Created voter: {voter}')
        except:
            print(f"Skipped: {fields}")

    print(f'Done. Created {len(Voter.objects.all())} Voters.')



