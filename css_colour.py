# 
# #F8F8F8: navbar background
# #E7E7E7: navbar border
# #777: default color
# #333: hover color (#5E5E5E for .nav-brand)
# #555: active color
# #D5D5D5: active background
# 

# 1 - Read through each record in the css file.
# 2 - Find the reference for each colour
# 3 - Find the colour code wihtin the reference
# 4 - replace the old colour with the new one.


old_colours_dict = {};
old_colours_list = [];

new_colours_dict = {};
new_colours_list = [];

found_colours = 0;
colour_count = 0;
loop_count = 0;

file_name = './static/css/style.css';
outfile_name = './static/css/style_gen.css';

write_outfile = 0;

outFile = open(outfile_name, "+w")    

with open(file_name, "r") as inFile:
    for line in inFile:
        
        if len(new_colours_list) == colour_count:
            # Check lines for colours from this point
            for colour in new_colours_list:
                new_col = colour['colour']
                code = colour['code']
                desc = colour['desc']

                if line.find(code)>=0:
                    line_split = line.split('#',1)
                    if line.find('!') > 0:
                        old_col = '#' + line_split[1].split('!',1)[0].strip()
                    else:
                        old_col = '#' + line_split[1].split(';',1)[0].strip()
                    old_colours_dict['colour'] = old_col
                    old_colours_dict['code'] = code
                    old_colours_dict['desc'] = desc
                    old_colours_list.append(old_colours_dict.copy());
                    
                    line = line.replace(old_col, new_col);

        if found_colours == 1 and loop_count > 0:
            loop_count -=1;
            line_split = line.split(':',2)
            new_colours_dict['colour'] = line_split[0].strip();
            new_colours_dict['code'] = line_split[1].strip();
            new_colours_dict['desc'] = line_split[2].strip();
            new_colours_list.append(new_colours_dict.copy());
            
        pos = line.find('colours:');
        if pos >= 0 and found_colours == 0:
            found_colours = 1;
            colour_count = int(line.split(':')[1])
            loop_count = colour_count;
        
        outFile.write(line);

inFile.close();
outFile.close()

