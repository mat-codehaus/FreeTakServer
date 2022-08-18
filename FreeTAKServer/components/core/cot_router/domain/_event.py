from digitalpy.model.load_configuration import Configuration
from .model_constants import EventVariables as vars
import uuid
from datetime import datetime as dt
from FreeTAKServer.components.core.abstract_component.cot_node import CoTNode

class Event(CoTNode):
    # TODO: fix emergency methods
    # Event.py
    # Python implementation of the Class Event
    # represents a TAK event: this class is instantiated with a standard set of
    #    values.
    # Generated by Enterprise Architect
    # Created on: 11-Feb-2020 11:08:07 AM
    # Original author: Corvo
    #

    # event as an XML
    #<?xml version="1.0" encoding="UTF-8" standalone="yes"?><event version="2.0" uid="Linux-ABC.server-ping" type="b-t-f" time="2020-02-14T20:32:31.444Z" start="2020-02-14T20:32:31.444Z" stale="2020-02-15T20:32:31.444Z" how="h-g-i-g-o"> 
        
        #default constructor

    def __init__(self, configuration: Configuration, model):        
        super().__init__(self.__class__.__name__, configuration, model)
        self.cot_attributes["version"] = None
        self.cot_attributes["uid"] = None
        self.cot_attributes["type"] = None
        self.cot_attributes["how"] = None
        self.cot_attributes["stale"] = None
        self.cot_attributes["start"] = None
        self.cot_attributes["time"] = None


        # flag to determin e if this event is a geo chcat if so, will be added as a
        # prefix to the uid
        
        # starting time when an event should be considered valid
        start = "%Y-%m-%dT%H:%M:%SZ"
        # basic event
        # Gives a hint about how the coordinates were generated
        

        # Schema version of this event instance (e.g.  2.0)
            
        # time stamp: when the event was generated
        time = "%Y-%m-%dT%H:%M:%SZ" 
        
        # Hierarchically organized hint about event type (defaultis is 'a-f-G-I'
        # for infrastructure)
        
            # ending time when an event should no longer be considered valid
        stale = "%Y-%m-%dT%H:%M:%SZ" 
        
            # Globally unique name for this information on this event can have
            # additional information attached.
        # e.g.  -ping means that this request is a ping
        
        # flag to determine if this event is a Ping, in this case append to the UID

    def getstart(self): 
        return self.cot_attributes["start"]
    
    # start setter
    def setstart(self, start=0):
        DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
        if start == None:
            timer = dt.datetime
            now = timer.utcnow()
            zulu = now.strftime(DATETIME_FMT)
            self.start = zulu
        else:
            self.cot_attributes["start"]=start

    
    # how getter
    def gethow(self): 
        return self.cot_attributes["how"]
    
        
    # how setter
    def sethow(self, how=0):  
        self.cot_attributes["how"]=how 

    # uid getter
    def getuid(self): 
        return self.cot_attributes["uid"]
    
    # uid setter
    def setuid(self, uid):
        if uid == None:
            self.uid = str(uuid.uuid1())

        else:
            self.cot_attributes["uid"]=uid

    # version getter
    def getversion(self): 
        return self.cot_attributes["version"]
    
    # version setter
    def setversion(self, version):  
        self.cot_attributes["version"]=version 

    # time getter
    def gettime(self): 
        return self.cot_attributes["time"]
    
    # time setter
    def settime(self, time=0):
        DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
        if time == None:
            timer = dt.datetime
            now = timer.utcnow()
            zulu = now.strftime(DATETIME_FMT)
            self.time = zulu
        else:
            self.cot_attributes["time"]=time
        
    # stale getter
    def getstale(self): 
        return self.cot_attributes["stale"]
    
    # stale setter
    def setstale(self, stale = None,staletime=60):
        if stale == None:
            DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
            timer = dt.datetime
            now = timer.utcnow()
            zulu = now.strftime(DATETIME_FMT)
            add = dt.timedelta(seconds=staletime)
            stale_part = dt.datetime.strptime(zulu, DATETIME_FMT) + add
            self.cot_attributes["stale"]=stale_part.strftime(DATETIME_FMT)
        else:
            self.cot_attributes["stale"]=stale

    # type getter
    def gettype(self): 
        return self.cot_attributes["type"]
    
    # type setter
    def settype(self, type=0):  
        self.cot_attributes["type"]=type

    def getpoint(self):
        return self.cot_attributes["point"]

    # type setter
    def setpoint(self, point=None):
        self.cot_attributes["point"]=point

    def getdetail(self):
        return self.cot_attributes["detail"]

    # type setter
    def setdetail(self, detail=None):
        self.cot_attributes["detail"]=detail
