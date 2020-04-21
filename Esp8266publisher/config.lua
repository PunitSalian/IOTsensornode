-- file : config.lua
local module = {}

module.SSID = {}  
module.SSID["Pun"] = ""

module.HOST = "m13.cloudmqtt.com"  
module.PORT = 14010  
module.ID = node.chipid()

module.ENDPOINT = "nodemcu/"  
return module 
