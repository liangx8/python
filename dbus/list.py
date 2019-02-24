import sys

import dbus

def main(argv):
    factory = dbus.SystemBus

    if len(argv) > 2:
        sys.exit(__doc__)
    elif len(argv) == 2:
        if argv[1] == '--session':
            factory = dbus.SessionBus
        elif argv[1] != '--system':
            sys.exit(__doc__)

    # Get a connection to the system or session bus as appropriate
    # We're only using blocking calls, so don't actually need a main loop here
    bus = factory()

    # This could be done by calling bus.list_names(), but here's
    # more or less what that means:

    # Get a reference to the desktop bus' standard object, denoted
    # by the path /org/freedesktop/DBus.
    dbus_object = bus.get_object('org.freedesktop.DBus',
                                 '/org/freedesktop/DBus')

    # The object /org/freedesktop/DBus
    # implements the 'org.freedesktop.DBus' interface
    dbus_iface = dbus.Interface(dbus_object, 'org.freedesktop.DBus')

    # One of the member functions in the org.freedesktop.DBus interface
    # is ListNames(), which provides a list of all the other services
    # registered on this bus. Call it, and print the list.
    services = dbus_iface.ListNames()
    services.sort()
    for service in services:
        print (service)

if __name__ == '__main__':
    main(sys.argv)
