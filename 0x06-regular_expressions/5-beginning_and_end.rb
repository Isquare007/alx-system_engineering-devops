#!/usr/bin/env ruby
#Matches tttttt

puts ARGV[0].scan(/(^h)([a-zA-Z0-9]{1})(n$)/).join
