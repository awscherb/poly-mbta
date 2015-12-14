require 'open-uri'
require 'json'
require 'date'

station_code = ARGV[0]

if station_code.nil? or station_code.empty?
	puts("You must enter a station code!")
	exit
end

url = "http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=5VJxw0cEAEWShNPVo-iAtg&stop=" + station_code + "&format=json"
buffer = open(url).read

result = JSON.parse(buffer)
stop_name = result["stop_name"]

puts("Arrival information for: " + stop_name)

result["mode"].each do |mode|
	puts("+- " + mode["mode_name"])
	mode["route"].each do |route|
		puts("  +- " + route["route_name"]) 
		route["direction"].each do |direction|
			puts("    +- " + direction["direction_name"])
			direction["trip"].each do |trip|
				puts("      +- " + Time.at(trip["sch_arr_dt"].to_i).strftime("%I:%M:%S"))
end
end
end
end 
