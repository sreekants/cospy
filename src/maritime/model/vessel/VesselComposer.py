#!/usr/bin/python
# Filename: VesselComposer.py
# Description: Types of vessels and their properties, states and characteristics

from maritime.model.vessel.Vessel import Vessel, Type
from cos.behavior.motion.VesselModel import VesselModel
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

    def build(self, ctxt:Context, vessel:Vessel, args:ArgList, config ):
        """ Composes a vessel from a profile
        Arguments
        	ctxt -- Simulation context
        	vessel -- Reference to a new vessel to compose
        	args -- List of arguments
        """
        modelfile   = args['ship.model']
        if not modelfile:
            return
        
        filename    = ctxt.sim.config.resolve(modelfile)
        model       = ctxt.sim.fs.read_file_as_bytes(filename)

        modelconfig = self.load_model(ctxt, vessel, model)
        self.build_profile(ctxt, vessel, modelconfig)
        return

    def build_profile(self, ctxt:Context, vessel:Vessel, modelconfig ):
        """ Builds a vessel from a profile
        Arguments
        	ctxt -- Simulation context
        	vessel -- Vessel object
        	modelconfig -- Model cofiguration
        """
        
        # Add the devices int the profile
        self.add_device( ctxt, vessel, modelconfig['devices'] )
        return

    def load_model(self, ctxt, vessel:Vessel, model):
        """ Loads a vessel model
        Arguments
            ctxt -- Simulation context
            filespec -- File name
        """
        if not model:
            return
        
        vessel.model    = VesselModel()
        config          = vessel.model.load( model )
        return config


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
            info    = device.get("info", None) 
            data    = device.get("data", None)

            klassname, klass	= BootLoader.load_class(driver)

            dev     = klass( device.get("type", None), name )

            if dev is None:
                ctxt.log.error( 'Vessel.Builder' , f'Failed to create device [{name}] for vessel[{vessel.id}]' )
                continue

            vessel.devices[name]    = dev
        return


if __name__ == "__main__":
	test = VesselComposer()


