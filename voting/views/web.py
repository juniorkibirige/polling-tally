from voting.models import (
    District, County, Subcounty, Parish, Pollingstation
)
from django.views.generic import ListView, DetailView, View
from voting.forms import (
    PollingStationDataUploadForm, PollingCandidateDataUploadForm
)
from django.shortcuts import render


class DistrictListView(ListView):
    model = District
    template_name = 'voting/districts/all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Districts'
        return context


class DistrictDetailView(DetailView):
    model = District
    template_name = 'voting/districts/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'District Details'
        return context


class CountyListView(ListView):
    model = County
    template_name = 'voting/counties/all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Counties'
        return context


class CountyDetailView(DetailView):
    model = County
    template_name = 'voting/counties/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'County Details'
        return context


class SubcountyListView(ListView):
    model = Subcounty
    template_name = 'voting/sub-counties/all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Sub Counties'
        return context


class SubcountyDetailView(DetailView):
    model = Subcounty
    template_name = 'voting/sub-counties/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Subcounty Details'
        return context


class ParishListView(ListView):
    model = Parish
    template_name = 'voting/parishes/all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Parishes'
        return context


class ParishDetailView(DetailView):
    model = Parish
    template_name = 'voting/parishes/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Parish Details'
        return context


class PollingstationListView(ListView):
    model = Pollingstation
    template_name = 'voting/polling-stations/all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Polling Stations'
        return context


class PollingstationDetailView(DetailView):
    model = Pollingstation
    template_name = 'voting/polling-stations/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Polling Station Details'
        return context


class PollingStationDataUploadView(View):
    def get(self, request):
        form = PollingStationDataUploadForm()
        context = {'form': form, 'page_title': 'Upload Polling Station Data'}
        return render(request, 'voting/polling-station-dataupload.html', context)

    def post(self, request):
        pass


class PollingCandidatesDataUploadView(View):
    def get(self, request):
        form = PollingCandidateDataUploadForm()
        context = {'form': form, 'page_title': 'Upload Candidate Data'}
        return render(request, 'voting/polling-candidate-upload.html', context)

    def post(self, request):
        pass


def show_all_candidates(request):
    context = {'page_title': 'All Candidates'}
    return render(request, 'voting/candidates.html', context)
