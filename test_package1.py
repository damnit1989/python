# -*- coding: utf-8 -*-
# 测试python包

import test_package
# from test_package import test_package2
test_package.test_package2.test2()



if __name__ == '__main__':
    import os
    import platform
    filename_list = os.listdir('.')
    file_count, dir_count = 0,0;
    for file in filename_list:
        if os.path.isfile(file):
            file_count += 1

        else:
            dir_count += 1
        apath = os.path.abspath(file)
        print apath
        print os.path.dirname(apath)
        print os.path.split(apath)
        print os.path.basename(apath)
    print 'total',len(filename_list),'files:',file_count,'dirs:',dir_count
    
    # print platform.machine()
    # print platform.python_version()
    # print platform.release()
    # print platform.system()
    # print platform.version()