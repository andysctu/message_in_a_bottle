
def get_long(long_lat):
    return long_lat[0]

def get_lat(long_lat):
    return long_lat[1]

def vals_are_close(val1, val2):
    return abs(val1 - val2) < 0.1

class Messages:

    LONG_LAT_KEY = 'long_lat'
    TEXT_KEY = 'text'

    def __init__(self):
        self.messages = {}
        self.id_counter = 0

        self.add_fake_messages()

    def add_fake_messages(self):
        self.messages.update({
            0: {self.LONG_LAT_KEY: (43.473010, -80.540047), self.TEXT_KEY: 'Please save me.'},
            1: {self.LONG_LAT_KEY: (43.472010, -80.540047), self.TEXT_KEY: 'I\'m surrounded by fucking nerds.'},
            2: {self.LONG_LAT_KEY: (43.474010, -80.540047), self.TEXT_KEY: 'I need a makeover asap.'},
            3: {self.LONG_LAT_KEY: (43.473510, -80.540047), self.TEXT_KEY: 'You suck.'},
            4: {self.LONG_LAT_KEY: (43.473010, -80.541047), self.TEXT_KEY: 'Zero is my favorite number.'},
            5: {self.LONG_LAT_KEY: (43.473010, -80.539047), self.TEXT_KEY: 'One is my favorite number.'},
        })

        self.id_counter = 6

    def add_message(self, long_lat, text):

        self.messages[self.id_counter] = {
            self.LONG_LAT_KEY: long_lat,
            self.TEXT_KEY: text
        }

        self.id_counter += 1

    def get_messages(self, long_lat):

        msgs = []

        long_val = get_long(long_lat)
        lat_val = get_lat(long_lat)

        for key, value in self.messages.iteritems():

            msg_long_lat = value[self.LONG_LAT_KEY]
            msg_long_val = get_long(msg_long_lat)
            msg_lat_val = get_lat(msg_long_lat)

            if vals_are_close(long_val, msg_long_val) and \
                vals_are_close(lat_val, msg_lat_val):

                msgs.append(value[self.TEXT_KEY])

        return msgs
