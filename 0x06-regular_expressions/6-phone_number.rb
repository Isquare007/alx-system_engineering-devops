#!/usr/bin/env ruby
#Matches tttttt

puts ARGV[0].scan(/^[\d]{10}/).join
