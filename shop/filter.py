from watch_shop import settings


class FilterQuery(object):

    def __init__(self, request):
        self.session = request.session
        filter_qr = self.session.get(settings.FILTER_SESSION_ID)
        if not filter_qr:
            filter_qr = self.session[settings.FILTER_SESSION_ID] = {}
        self.filter_qr = filter_qr

    def change(self, number):
        filter_id = 'filter_number'
        if filter_id not in self.filter_qr:
            self.filter_qr[filter_id] = {'filter': 0}
        else:
            self.filter_qr[filter_id] = {'filter': number}
        return self.save()

    def view(self):
        return self.filter_qr['filter_number']['filter']

    def save(self):
        self.session[settings.FILTER_SESSION_ID] = self.filter_qr
        self.session.modified = True
        return
