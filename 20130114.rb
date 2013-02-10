class Problem_20130114

  def initialize(input)
    @input_file = input
  end

  def solve

    hex = "00000000 48 65 6C 6C 6F 20 57 6F 72 6C 64"
    string = "Hello World"
    file = File.new(@input_file)
    line = ""
    line_count = 1
    line_length =  16
    current_length = 1
    file.each_char do |x|
      if (current_length == 16)
        puts line_count.to_s(16).rjust(8, '0') << " " <<  line
        line = ""
        current_length = 0
        line_count = line_count + 1
      else
        x.unpack("H*").each do |y|
          line << y.to_s << " "
        end
        current_length = current_length + 1
      end



    end


  end


  def result
    @results
  end

end

problem = Problem_20130114.new "input.txt"
problem.solve

#puts "Hello World".unpack('H*')