import time
from pathlib import Path

class FileInfo:
    def __init__(self, file_path):
        self.path = Path(file_path)
        self.file_name = self.path.name
        self.size = self.path.stat().st_size
        self.ctime = self.path.stat().st_ctime
        self.mtime = self.path.stat().st_mtime
        self.atime = self.path.stat().st_atime
    
    def get_filename(self):
        return self.file_name
    
    def get_size(self):
        return self.size
    
    def get_path(self):
        return str(self.path)
    
    def get_creation_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.ctime))
    
    def get_modification_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.mtime))
    
    def get_access_time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.atime))
    
    def __str__(self):
        return '找到相关文件 -> ' + self.file_name + ' (' + str(self.size) + ' 字节)\n位置: ' + str(self.path) + '\n创建时间: ' + self.get_creation_time() + '\n修改时间: ' + self.get_modification_time() + '\n访问时间: ' + self.get_access_time()

class FileSearcher:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.file_infos = []
    
    def traverse_directory(self):
        '遍历目录并收集文件信息'
        # 首先显示根目录
        print(self.root_dir.name)
        
        # 然后遍历所有子目录和文件
        for root in sorted(self.root_dir.rglob('*')):
            if root != self.root_dir:
                if root.is_dir():
                    # 显示目录结构
                    level = len(root.relative_to(self.root_dir).parts)
                    indent = ' ' * 4 * level
                    print(indent + root.name)
                else:
                    # 显示文件
                    level = len(root.relative_to(self.root_dir).parts) - 1
                    indent = ' ' * 4 * level
                    subindent = ' ' * 4 * (level + 1)
                    print(subindent + root.name)
                    self.file_infos.append(FileInfo(root))
    
    def search_by_name(self, keyword):
        '根据文件名搜索文件'
        results = []
        for file_info in self.file_infos:
            if keyword.lower() in file_info.get_filename().lower():
                results.append(file_info)
        return results

# 测试代码
if __name__ == '__main__':
    # 指定要搜索的根目录
    root_directory = 'target'
    
    # 创建文件搜索器实例
    searcher = FileSearcher(root_directory)
    
    # 遍历目录
    print('路径结构如下：')
    searcher.traverse_directory()
    
    # 搜索文件
    while True:
        keyword = input('\n请输入想要搜索的文件名：')
        if not keyword:
            break
        
        results = searcher.search_by_name(keyword)
        if results:
            for i, result in enumerate(results, 1):
                print('\n找到相关文件（' + str(i) + '）-> ' + result.get_filename() + ' (' + str(result.get_size()) + ' 字节)')
                print('位置: ' + result.get_path())
                print('创建时间: ' + result.get_creation_time())
                print('修改时间: ' + result.get_modification_time())
                print('访问时间: ' + result.get_access_time())
        else:
            print('找不到相关文件！')