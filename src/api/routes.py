#!/usr/bin/env python
#-*- coding: utf-8 -*-


from handlers.admin import AdminConf, AdminUser, AdminReset
from handlers.cluster import Cluster_Handler, Sync_Handler, Cluster_Start_Handler, Cluster_Stop_Handler, Cluster_Reload_Handler
from handlers.node import Node_Start_Handler, Node_Handler, Node_Config_Handler, Node_Stop_Handler, Node_Reload_Handler, Node_Status_Handler
handlers = [
            #(r"/admin/conf", AdminConf),
            #(r"/admin/user", AdminUser),
            #(r"/admin/reset", AdminReset),
            
            #(r"/cluster", Cluster_Handler),
            #(r"/cluster/sync", Sync_Handler),
            #(r"/cluster/status", Cluster_Handler),
            
            #(r"/cluster/start", Cluster_Start_Handler),
            #(r"/cluster/reload", Cluster_Reload_Handler),
            #(r"/cluster/stop", Cluster_Stop_Handler),
            
            #(r"/cluster/node", Node_Handler),
            (r"/cluster/node/config", Node_Config_Handler),
            (r"/cluster/node/start", Node_Start_Handler),
            (r"/cluster/node/stop", Node_Stop_Handler),
            (r"/cluster/node/reload", Node_Reload_Handler),
            #(r"/cluster/node/status", Node_Status_Handler),
]