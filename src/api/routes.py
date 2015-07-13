#!/usr/bin/env python
#-*- coding: utf-8 -*-

from handlers.node import Node_Start_Handler, Node_Config_Handler, Node_Stop_Handler, Node_Reload_Handler
handlers = [         
            (r"/cluster/node/config", Node_Config_Handler),
            (r"/cluster/node/start", Node_Start_Handler),
            (r"/cluster/node/stop", Node_Stop_Handler),
            (r"/cluster/node/reload", Node_Reload_Handler),
]