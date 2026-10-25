# File: voter_analytics/views.py
# Author: Tae Yeung Kim (kimty@bu.edu), 10/25/2026
# Description: class-based view for voter_analytics application

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Voter

import plotly 
import plotly.graph_objs as go

# Create your views here.
class VotersListView(ListView):
    '''view to display voter results'''
    model = Voter
    template_name = 'voter_analytics/voters.html'
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        voters = super().get_queryset().order_by('last_name', 'first_name')
        # look for URL parameters to filter by
        if 'party' in self.request.GET:
            party = self.request.GET['party']
            if party:
                voters = voters.filter(party_affil=party)
        if 'min_dob' in self.request.GET:
            min_dob = self.request.GET['min_dob']
            if min_dob:
                voters = voters.filter(dob__year__gte=min_dob)
        if 'max_dob' in self.request.GET:
            max_dob = self.request.GET['max_dob']
            if max_dob:
                voters = voters.filter(dob__year__lte=max_dob)
        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            if voter_score:
                voters = voters.filter(voter_score=voter_score)
        if 'v20state' in self.request.GET:
            voters = voters.filter(v20state=True)
        if 'v21town' in self.request.GET:
            voters = voters.filter(v21town=True)
        if 'v21primary' in self.request.GET:
            voters = voters.filter(v21primary=True)
        if 'v22general' in self.request.GET:
            voters = voters.filter(v22general=True)
        if 'v23town' in self.request.GET:
            voters = voters.filter(v23town=True)

        return voters

    def get_context_data(self, **kwargs):
        '''provide context variables for use in the template'''
        context = super().get_context_data(**kwargs)
        context['parties'] = Voter.objects.values_list('party_affil', flat=True).distinct().order_by('party_affil')
        context['scores'] = ['0', '1', '2', '3', '4', '5']
        context['years'] = [str(date.year) for date in Voter.objects.dates('dob', 'year')]

        return context 

class VoterDetailView(DetailView):
    '''display information for a single voter'''
    model = Voter 
    template_name = 'voter_analytics/voter_detail.html'
    context_object_name = 'v'

class GraphsListView(VotersListView):
    '''view to display graphs of aggregate voter data'''
    template_name = 'voter_analytics/graphs.html'

    def get_context_data(self, **kwargs):
        '''provide context variables for use in the template'''
        context = super().get_context_data(**kwargs)
        voters = self.get_queryset()
        n = voters.count()

        # histogram: distribution of Voters by their year of birth
        dob_counts = {} # dict
        for v in voters:
            year = v.dob.year
            dob_counts[year] = dob_counts.get(year, 0) + 1

        x = sorted(dob_counts)
        y = [dob_counts[year] for year in x]

        fig = go.Bar(x=x, y=y)
        title_text = f'Voter distribution by Year of Birth (n={n})'
        graph_div_dob = plotly.offline.plot({"data": [fig],
                                             "layout_title_text": title_text},
                                             auto_open=False,
                                             output_type="div")
        context['graph_div_dob'] = graph_div_dob

        # pie chart: distribution of voters by party affiliation
        party_counts = {} # dict
        for v in voters:
            party = v.party_affil.strip()
            party_counts[party] = party_counts.get(party, 0) + 1

        labels = list(party_counts.keys())
        values = list(party_counts.values())

        fig = go.Pie(labels=labels, values=values)
        title_text = f'Voter distribution by Party Affiliation (n={n})'
        graph_div_party = plotly.offline.plot({"data": fig,
                                               "layout_title_text": title_text},
                                               auto_open=False,
                                               output_type="div")
        context['graph_div_party'] = graph_div_party

        # histogram: how many voted in each of the 5 elections
        x = ['v20state', 'v21town', 'v21priamry', 'v22general', 'v23town']
        y = [voters.filter(v20state=True).count(),
             voters.filter(v21town=True).count(),
             voters.filter(v21primary=True).count(),
             voters.filter(v22general=True).count(),
             voters.filter(v23town=True).count()]

        fig = go.Bar(x=x, y=y)
        title_text = f'Vote Count by Election (n={n})'
        graph_div_election = plotly.offline.plot({"data": [fig],
                                                  "layout_title_text": title_text},
                                                  auto_open=False,
                                                  output_type="div")
        context['graph_div_election'] = graph_div_election

        return context


        