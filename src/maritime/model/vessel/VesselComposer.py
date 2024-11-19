#!/usr/bin/python
# Filename: VesselComposer.py
# Description: Types of vessels and their properties, states and characteristics

from maritime.model.vessel.Vessel import Vessel, Type
from cos.core.kernel.Context import Context
from cos.core.kernel.Configuration import Configuration
from cos.core.kernel.BootLoader import BootLoader
from cos.core.utilities.ArgList import ArgList

import yaml

class VesselComposer:
    def __init__(self ):
         """ Constructor
         """
         return

    def build(self, ctxt:Context, vessel:Vessel, args:ArgList ):
        """ Composes a vessel from a profile
        Arguments
        	ctxt -- Simulation context
        	vessel -- Reference to a new vessel to compose
        	args -- List of arguments
        """
        profile = args['profile']
        if profile is not None:
            self.build_profile( ctxt, vessel, Configuration.resolve_path(profile) )
        return

    def build_profile(self, ctxt:Context, vessel:Vessel, filename:str ):
        """ Builds a vessel from a profile
        Arguments
        	ctxt -- Simulation context
        	vessel -- Vessel object
        	filename -- File name
        """
        config	    = yaml.safe_load(ctxt.sim.fs.read_file_as_bytes(filename))

        # Add the devices int the profile
        self.add_device( ctxt, vessel, config['devices'] )

        return


    def add_device(self, ctxt:Context, vessel:Vessel, devices ):
        """ Adds a devices to the vessel
        Arguments
        	ctxt -- Simulation context
        	vessel -- Vessel object
        	devices -- List of devices to attach to the vessel
        """
        if devices is None or len(devices) == 0:
            return

        for device in devices:
            name    = device["name"]
            driver  = device["driver"]
            dev     = ctxt.sim.devices.create(
                        name,
                        device["type"],
                        device["info"],
                        device["data"] )

            if dev is None:
                ctxt.log.error( 'Vessel.Builder' , f'Failed to create device [{name}] for vessel[{vessel.id}]' )
                continue

            # Load the device driver for the device
            klassname, klass	    = BootLoader.load_class(driver)

            vessel.devices[name]    = klass(ctxt, vessel, dev, device["args"])
        return


if __name__ == "__main__":
	test = VesselComposer()


