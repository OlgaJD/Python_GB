from file_worker import setting, sorter, renamer

setting([('mkv', 2), ('mp4', 1), ('mov', 4), ('avi', 1),
         ('jpeg', 1), ('bmp', 2), ('png', 1),
         ('txt', 2), ('doc', 3), ('docx', 1),
         ('xlsx', 1), ('py', 2), ('sql', 1)], r'C:\Users\Admin\Desktop\test_hw7')

sorter(r'C:\Users\Admin\Desktop\test_hw7')
renamer('NEW', 5, 'py', 'txt', [2, 5],
        r'C:\Users\Admin\Desktop\test_hw7')
