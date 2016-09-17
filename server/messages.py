
def get_long(long_lat):
    return long_lat[0]

def get_lat(long_lat):
    return long_lat[1]

def vals_are_close(val1, val2):
    return abs(val1 - val2) < 20

class Messages:

    LONG_LAT_KEY = 'long_lat'
    TEXT_KEY = 'text'

    def __init__(self):
        self.messages = {}
        self.id_counter = 0

    def add_message(self, long_lat, text):

        self.messages[self.id_counter] = {
            self.LONG_LAT_KEY: long_lat,
            self.TEXT_KEY: text
        }

        self.id_counter += 1

    def get_messages(self, long_lat):

        long_val = get_long(long_lat)
        lat_val = get_lat(long_lat)

        for key, value in self.messages.iteritems():

            msg_long_lat = value[self.LONG_LAT_KEY]
            msg_long_val = get_long(msg_long_lat)
            msg_lat_val = get_lat(msg_long_lat)

            if vals_are_close(long_val, msg_long_val) and \
                vals_are_close(lat_val, msg_lat_val):

                return value[self.TEXT_KEY]