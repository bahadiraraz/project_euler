t = 0
(1..999).each do |i|
  if i % 3 == 0 or i % 5 == 0
    t += i
  end
end
puts t
