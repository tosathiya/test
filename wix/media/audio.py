from media import Media


class Audio(Media):
    def __init__(self, audio_id, service_host, client):
        super(Audio, self).__init__(audio_id, service_host, client)

    def get_url(self):
        return "/".join(['http://%s' % self.service_host, self.id])

