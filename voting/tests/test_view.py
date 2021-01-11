from django.test import TestCase


class DistrictTestCase(TestCase):
    def test_district_url_loads(self):
        r = self.client.get('/district')
        content = r.content.decode('utf8')
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('districts.html')
        self.assertInHTML('<title>Districts</title>', content)

    def test_district_view_page_loads(self):
        pass


class CountyTestCase(TestCase):
    def test_county_url(self):
        r = self.client.get('/county')
        content = r.content.decode('utf8')
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('counties.html')
        self.assertInHTML('<title>Counties</title>', content)


class SubcountyTestCase(TestCase):
    def test_subcounty_url_loads(self):
        r = self.client.get('/subcounty')
        content = r.content.decode('utf8')
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('subounties.html')
        self.assertInHTML('<title>Subcounties</title>', content)

    def test_subcounty_view_page_loads(self):
        pass


class ParishTestCase(TestCase):
    def test_parish_url_loads(self):
        r = self.client.get('/parish')
        content = r.content.decode('utf8')
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('parishes.html')
        self.assertInHTML('<title>Parishes</title>', content)

    def test_parish_view_page_loads(self):
        pass


class PollingStationTestCase(TestCase):
    def test_polling_station_url_loads(self):
        r = self.client.get('/pollingstation')
        content = r.content.decode('utf8')
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('polling-stations.html')
        self.assertInHTML('<title>Polling Stations</title>', content)

    def test_parish_view_page_loads(self):
        pass


class UploadPollingStationTestCase(TestCase):
    def test_polling_data_upload_page(self):
        r = self.client.get('/pollingstation-dataupload')
        content = r.content.decode('utf8')
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('polling-station-dataupload.html')
        self.assertInHTML('<title>Upload Polling Station Data</title>', content)


class UploadCandidateTestCase(TestCase):
    def test_polling_candidate_upload_page(self):
        r = self.client.get('/pollingcandidate-dataupload')
        content = r.content.decode('utf8')
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('polling-candidate-upload.html')
        self.assertInHTML('<title>Upload Polling Candidate Data </title>', content)

    def test_candidate_page_loads(self):
        r = self.client.get('/candidates')
        content = r.content.decode('utf8')
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed('candidates.html')
        self.assertInHTML('<title>All Candidates</title>', content)
