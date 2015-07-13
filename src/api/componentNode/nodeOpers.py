
'''
Created on Mar 13, 2015

@author: root
'''
import os,logging

from tornado.options import options
from utils.invokeCommand import InvokeCommand
from common.abstractOpers import AbstractOpers
from utils.exceptions import UserVisiableException


class NodeOpers(AbstractOpers):
    '''
    classdocs
    '''
    invokeCommand = InvokeCommand()
    def __init__(self):
        '''
        Constructor
        '''
    
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
