"""
    First child class from service
"""
from data import generate_id
from service import Service

class YoutubeStream(Service):
    
    def start_stream(self):
        stream_reference = generate_id(10)

        print("Start stream %s en youtube" % stream_reference)

        return stream_reference

    def fill_buffer(self, stream_reference):
        
        buffer = self.retrieve_buffer_data()

        for buf in buffer:

            print("Estos devices %s estan enviandos datos a tu stream %s en youtube" % (buf, stream_reference))

    def stop_stream(self, stream_reference, notify=True, log_to_file=False, retries=3):
        if notify:
            if log_to_file:
                with open("streams.log", "a") as log:
                    log.write("Cerrando stream %s en youtube\n" % stream_reference)
            else:
                print('Cerrando stream %s en youtube' % stream_reference)
        
        
        