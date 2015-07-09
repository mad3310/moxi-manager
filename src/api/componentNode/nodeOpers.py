'''
Created on Mar 13, 2015

@author: root
'''
import os

from tornado.options import options
from utils import retrieve_node_name
from common.abstractOpers import AbstractOpers
from zk.zkOpers import Common_ZkOpers
from utils.exceptions import UserVisiableException
from utils import getClusterUUID
from utils.configFileOpers import ConfigFileOpers


class NodeOpers(AbstractOpers):
    '''
    classdocs
    '''
    confOpers = ConfigFileOpers()

    def __init__(self):
        '''
        Constructor
        '''
        
    def createNode(self, params):
        if params == {} or params is None:
            raise UserVisiableException("please set the componentNode info!")
        
        dataNodeInternalPort = params.get('dataNodeInternalPort')
        if dataNodeInternalPort is not None:
            raise UserVisiableException("no need to set the dataNodeInternalPort param!")
            
        zkOper = Common_ZkOpers()
        
        local_uuid = getClusterUUID()
        existCluster = zkOper.existCluster(local_uuid)
        if not existCluster:
            raise UserVisiableException("sync componentCluster info error! please check if sync uuid is right!")
            
        params.setdefault("dataNodeInternalPort", options.port)
        dataNodeExternalPort = params.get('dataNodeExternalPort')
        if dataNodeExternalPort is None or '' == dataNodeExternalPort:
            params.setdefault("dataNodeExternalPort", options.port)
        
        self.confOpers.setValue(options.data_node_property, params)
        dataNodeProprs = self.confOpers.getValue(options.data_node_property)
        zkOper.writeDataNodeInfo(local_uuid, dataNodeProprs)

        result = {}
        result.setdefault("message", "Configuration on this componentNode has been done successfully")    
        return result
    
    def startNode(self):
        ret_val = os.system(options.start_jetty)
        
        result = {}
        if ret_val != 0:
            result.setdefault("message", "start jetty failed")
        else:
            container_name =  retrieve_node_name()
            zkOper = Common_ZkOpers()
            zkOper.write_started_node(container_name)
            result.setdefault("message", "start jetty successfully")
        
        return result
    
    def stopNode(self):
        ret_val = os.system(options.stop_jetty)
        
        result = {}
        if ret_val != 0:
            result.setdefault("message", "stop jetty failed")
        else:
            container_name = retrieve_node_name()
            
            zkOper = Common_ZkOpers()
            zkOper.remove_started_node(container_name)
            result.setdefault("message", "stop jetty successfully")
        
        return result

    def reloadNode(self):
        ret_val = os.system(options.reload_jetty)
        
        result = {}
        if ret_val != 0:
            result.setdefault("message", "reload jetty failed")
        else:
            result.setdefault("message", "reload jetty successfully")
            container_name =  retrieve_node_name()
            zkOper = Common_ZkOpers()
            zkOper.write_started_node(container_name)
            
        return result
