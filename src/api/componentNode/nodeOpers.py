
'''
Created on Mar 13, 2015

@author: root
'''
import os,logging

from tornado.options import options
from utils import retrieve_node_name
from utils.invokeCommand import InvokeCommand
from common.abstractOpers import AbstractOpers
from utils.exceptions import UserVisiableException
from utils import getClusterUUID
from utils.configFileOpers import ConfigFileOpers


class NodeOpers(AbstractOpers):
    '''
    classdocs
    '''
    confOpers = ConfigFileOpers()
    invokeCommand = InvokeCommand()
    def __init__(self):
        '''
        Constructor
        '''
        
    def create(self, params):
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
    
    def start(self):
        ret_val = os.system(options.start_moxi)

        result = {}
        if ret_val != 0:
            result.setdefault("message", "start moxi failed")
        else:
            #container_name = retrieve_node_name()
            #zkOper = Common_ZkOpers()
            #zkOper.write_started_node(container_name)
            result.setdefault("message", "start moxi successfully")
        
        return result
    
    def stop(self):
        ret_val = os.system(options.stop_moxi)
        
        result = {}
        if ret_val != 0:
            result.setdefault("message", "stop moxi failed")
        else:
            #container_name = retrieve_node_name()           
            #zkOper = Common_ZkOpers()
            #zkOper.remove_started_node(container_name)
            result.setdefault("message", "stop moxi successfully")
        
        return result

    def reload(self):
        ret_val = os.system(options.reload_moxi)
        
        result = {}
        if ret_val != 0:
            result.setdefault("message", "reload moxi failed")
        else:
            result.setdefault("message", "reload moxi successfully")
            #container_name = retrieve_node_name()
            #zkOper = Common_ZkOpers()
            #zkOper.write_started_node(container_name)
            
        return result

    def config(self, params):
        _cbase_host = params.get('CBASE_HOST')
        _cbase_bucket = params.get('CBASE_BUCKET')
        _cbase_pwd = params.get('CBASE_PWD')
        #cbase_host_list = _cbase_host.split(',') if ',' in _cbase_host else [_cbase_host]

        with open("/etc/sysconfig/moxi", 'w') as moxi:
            message = "CBASE_HOST='{0}'\nCBASE_BUCKET='{1}'\nCBASE_PWD='{2}'\nUSER='nobody'\nMAXCONN='1024'\nCPROXY_ARG='/etc/moxi.conf'\nOPTIONS=''".format(_cbase_host, _cbase_bucket, _cbase_pwd)
            moxi.write(message)

        self.invokeCommand._runSysCmd(options.reload_moxi)
        result = {}
        result.setdefault("message", "node config successfully")
        return result

    def nodestatus(self):
        ret_val = os.system(options.status_moxi)
        
        result = {}
        if ret_val != 0:
            result.setdefault("message", "moxi status failed")
        else:
            result.setdefault("message", "moxi status successfully")

            
        return result
