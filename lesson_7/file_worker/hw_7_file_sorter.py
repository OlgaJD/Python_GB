"""
✔Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔Каждая группа включает файлы с несколькими расширениями.
✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os
import shutil

VIDEO_EXT = ['mkv', 'mp4', 'mov', 'avi']
IMAGE_EXT = ['jpeg', 'jpg', 'bmp', 'png']
TEXT_EXT = ['txt', 'pdf', 'doc', 'docx']


def file_sorter(path):
    if os.path.isdir(path):
        os.chdir(path)
        count_video = 0
        count_image = 0
        count_txt = 0
        for file in os.listdir(path):
            if file.split('.')[-1] in VIDEO_EXT:
                video_path = os.path.join(path, 'video_files')
                if not os.path.isdir(video_path):
                    os.mkdir(video_path)
                # os.replace(file, video_path)  # PermissionError: [WinError 5] Отказано в доступе: 'file' -> 'video_path'
                shutil.move(file, video_path)
                count_video += 1
            elif file.split('.')[-1] in IMAGE_EXT:
                image_path = os.path.join(path, 'image_files')
                if not os.path.isdir(image_path):
                    os.mkdir(image_path)
                shutil.move(file, image_path)
                count_image += 1
            elif file.split('.')[-1] in TEXT_EXT:
                txt_path = os.path.join(path, 'text_files')
                if not os.path.isdir(txt_path):
                    os.mkdir(txt_path)
                shutil.move(file, txt_path)
                count_txt += 1
        print(f'Всего файлов перемещено {count_video + count_image + count_txt}.\n'
              f'Видео: {count_video}, картинки: {count_image}, текстровые: {count_txt}.')
