# import re
# Taking advantage of the simple database

fp = open('table_fields.txt', 'r')
data = fp.read()
fp.close()

lines = data.split('\n')
four_spaces = ' ' * 4
out = four_spaces

for line in lines:
    if line.strip(' \t\n\r') == '':
        continue
    line = line.strip(' \t\n\r')
    # print(line)
    # 2 cases, varchar or int
    if line.find('varchar') > -1:
        name = line[1:line.find('` ')]
        # print(name)
        start_bk = line.find('(', 0)
        end_bk = line.find(')', start_bk+1)
        limit = line[start_bk+1:end_bk]
        out += name.lower() + ' = models.CharField(default=None, max_length=' + limit + ')\n' + four_spaces
    else:
        name = line[1:line.find('` ')]
        # print(name)
        start_bk = line.find('(', 0)
        end_bk = line.find(')', start_bk+1)
        limit = line[start_bk+1:end_bk]
        out += name.lower() + ' = models.IntegerField(default=None)\n' + four_spaces

print(out)
