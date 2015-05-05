#!/usr/bin/python

from dbus import Bus, DBusException

bus = Bus(Bus.TYPE_SESSION)

def get_clem():
    try:
        return bus.get_object('org.mpris.clementine', '/Player')
    except DBusException:
        #print "\x02Either Clementine is not running or you have something wrong with your D-Bus setup."
        return None

def command_np():
    clem = get_clem()
#    clemtl = bus.get_object('org.mpris.clementine', '/TrackList')
#    clemgl = clemtl.GetLength()
    clemp = bus.get_object('org.mpris.clementine', '/Player')
    clemmd = clemp.GetMetadata()
    if clem:
        pos = clem.PositionGet()
        return (clemmd['artist'] + " - " + clemmd['title'])
    return "?"

print(command_np())
