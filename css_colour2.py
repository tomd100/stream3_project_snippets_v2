
def updateCSS(old_file, new_file):

    new_colours_list = getColours('colours.css')
    
    old_colours_dict = {}
    old_colours_list = []
    
    path = './static/css/'
    
    outFile = open(path + new_file, "+w")    

    with open(path + old_file, "r") as inFile:
        for line in inFile:
            
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
    
            outFile.write(line);
    
    inFile.close();
    outFile.close()

def getColours(colour_file):
    
    colours_dict = {};
    colours_list = [];
    
    found_colours = 0;

    path = './static/css/'    

    with open(path + colour_file, "r") as inFile:
        for line in inFile:
            
            pos = line.find('*/');
            if pos >= 0:
                found_colours = 0;

            if found_colours == 1:
                line_split = line.split(':',2)
                colours_dict['colour'] = line_split[0].strip();
                colours_dict['code'] = line_split[1].strip();
                colours_dict['desc'] = line_split[2].strip();
                colours_list.append(colours_dict.copy());

            pos = line.find('/*');
            if pos >= 0:
                found_colours = 1;
                
    return(colours_list)
    
updateCSS('style.css', 'style_gen.css')    
updateCSS('navbar.css', 'navbar_gen.css')    