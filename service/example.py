### service/example: example service file to be used as a template
## HOW IT WORKS: 
## DEPENDENCIES:
# OS: 
# Python: 
## CONFIGURATION:
# required: 
# optional: 
## COMMUNICATION:
# INBOUND: 
# - IN: 
#   required: 
#   optional: 
# OUTBOUND: 

from sdk.module.service import Service

class Example(Service):
    # What to do when initializing
    def on_init(self):
        pass
        
    # What to do when running
    def on_start(self):
        pass
    
    # What to do when shutting down
    def on_stop(self):
        pass

    # What to do when receiving a request for this module
    def on_message(self, message):
        pass

    # What to do when receiving a new/updated configuration for this module    
    def on_configuration(self,message):
        pass