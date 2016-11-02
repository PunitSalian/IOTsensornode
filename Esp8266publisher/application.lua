-- file : application.lua MAIN application file readin sensor data and publishing
local module = {}  
m = nil

dofile('adxl345.lua') --import adxl345 library
-- Sends a simple ping to the broker with sensor data as payload
local function send_ping()  
   local X,Y,Z=adxl()--read adxl value
   local temp=(adc.read(0)/1024)*100 --read photoresistor
   m:publish(config.ENDPOINT .. "sensor",X.."/"..Y.."/"..Z.."/"..temp,0,0)

end

-- Sends my id to the broker for registration
local function register_myself()  
    m:subscribe(config.ENDPOINT .. config.ID,0,function(conn)
        print("Successfully subscribed to data endpoint")
    end)
end


local function mqtt_start()  
    m = mqtt.Client(config.ID, 120,"CLOUDMQQT USERNAME","CLOUDMQQT PASSWORD")
    -- register message callback beforehand
    m:on("message", function(conn, topic, data) 
      if data ~= nil then
        print(topic .. ": " .. data)
        -- do something, we have received a message
      end
    end)
    -- Connect to broker
    m:connect(config.HOST, config.PORT, 0, 1, function(con) 
        register_myself()
        -- And then pings each 3000 milliseconds
        tmr.stop(6)
        tmr.alarm(6, 3000, 1, send_ping)
    end) 

end

function module.start()  
  adxlinit()
  mqtt_start()
end

return module  
