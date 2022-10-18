#!/usr/bin/env ruby
#Matches tttttt

puts ARGV[0].scan(/\A\d{10}\z/).join
