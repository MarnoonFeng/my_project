import datetime


class StringUtils(object):

    # 取出data中key对应的value
    @staticmethod
    def get_by_key(key, data):
        # 切掉##
        data = data[data.find('QN'):]
        # 以分号分隔
        data_split = data.split(';')
        for val in data_split:
            # 如果分割后的字符串有逗号
            if ',' in val:
                val_split = val.split(',')
                for v in val_split:
                    if key in v:
                        # 如果key匹配
                        return v.split('=')[1]
            if key in val:
                val_split = val.split('=')
                if key == 'DataTime':
                    return val_split[2]
                else:
                    return val_split[1]

    # 日期格式转换存入数据库
    @staticmethod
    def timeParseDate(time_str):
        parse_time = datetime.datetime.strptime(time_str, '%Y%m%d%H%M%S')
        return parse_time


if __name__ == '__main__':
    data = '##0231QN=20201216134702246;ST=32;CN=2011;PW=123456;MN=SD370300001043;CP=&&DataTime=20201216134641;011-Rtd=73.9200,011-Flag=N;060-Rtd=1.0900,060-Flag=N;B01-Rtd=70.7000,B01-Flag=N;B00-Rtd=1395185.0000,B00-Flag=N;001-Rtd=7.0380,001-Flag=N&&0280'
    result1 = StringUtils.get_by_key('011-Rtd', data)
    print('011-Rtd的值为{}'.format(result1))
    print('<----------------------------------->')
    result2 = StringUtils.get_by_key('DataTime', data)
    parse_time = StringUtils.timeParseDate(result2)
    print('DataTime的值为{}'.format(parse_time))
    print('<----------------------------------->')
    result3 = StringUtils.get_by_key('ST', data)
    print('ST的值为{}'.format(result3))
    print('<----------------------------------->')
