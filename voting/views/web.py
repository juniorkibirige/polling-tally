from voting.models import (
    District, County, Subcounty, Parish, Pollingstation
)
from django.views.generic import ListView, DetailView


class DistrictListView(ListView):
    model = District
    template_name = 'voting/districts/all.html'


class DistrictDetailView(DetailView):
    model = District
    template_name = 'voting/districts/view.html'


class CountyListView(ListView):
    model = County
    template_name = 'voting/counties/all.html'


class CountyDetailView(DetailView):
    model = County
    template_name = 'voting/counties/view.html'


class SubcountyListView(ListView):
    model = Subcounty
    template_name = 'voting/sub-counties/all.html'


class SubcountyDetailView(DetailView):
    model = Subcounty
    template_name = 'voting/sub-counties/view.html'


class ParishListView(ListView):
    model = Parish
    template_name = 'voting/parishes/all.html'


class ParishDetailView(DetailView):
    model = Parish
    template_name = 'voting/parishes/view.html'


class PollingstationListView(ListView):
    model = Pollingstation
    template_name = 'voting/polling-stations/all.html'


class PollingstationDetailView(DetailView):
    model = Pollingstation
    template_name = 'voting/polling-stations/view.html'
