'''
Created on Mar 8, 2015

@author: root
'''
from base import APIHandler
from tornado.web import asynchronous
from componentNode.nodeOpers import NodeOpers

class Node_Config_Handler(APIHandler):
    
    nodeOpers = NodeOpers()
    
    def post(self):
        '''
        function: set the nginx configuration file, currently, only for upstream
        url example: curl -d "upstreamName=newupstream&serverPorts=10.200.84.21:3333,10.200.84.22:3333,10.200.84.23:3333" "http://localhost:8888/cluster/node/config"
        '''
        requestParam = self.get_all_arguments()
        result = self.nodeOpers.config(requestParam)
        self.finish(result)


class Node_Start_Handler(APIHandler):
    
    node_opers = NodeOpers()
    
    @asynchronous
    def post(self):
        '''
        function: start node
        url example: curl --user root:root -d "" "http://localhost:8888/cluster/node/start"
        '''
        result = self.node_opers.start()
        self.finish(result)


class Node_Stop_Handler(APIHandler):
    
    node_opers = NodeOpers()
    
    def post(self):
        '''
        function: stop node
        url example: curl --user root:root -d "" "http://localhost:8888/node/stop"
        '''
        result = self.node_opers.stop()
        self.finish(result)


class Node_Reload_Handler(APIHandler):
    
    node_opers = NodeOpers()
    
    def post(self):
        '''
        function: reload node
        url example: curl --user root:root -d "" "http://localhost:8888/node/reload"
        '''
        result = self.node_opers.reload()
        self.finish(result)

        