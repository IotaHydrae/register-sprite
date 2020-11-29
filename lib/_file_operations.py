# python excutable path
# RegisterSprite  Copyright (C) 2020  jessenhua (h1657802074@gmail.com)

# This file is part of RegisterSprite

# RegisterSprite is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
    @file: _file_operations.py
    @author: hz
    @version: v1.2
    @date: 2020-11-29
    @brief: register_sprite update
'''

# import **************************************************
import configparser

class FileOperations():
    def __init__(self):
        self.config = configparser.ConfigParser()
        pass

    def write_config(self, path, section, key, value):
        self.config.read(path)
        # 读取配置文件原数据，追加写入
        self.config = self.read_config_all(path)
        # 如果输入section不在目标文件中
        if section not in self.config.sections():
            self.config.add_section(section)    # 添加输入section
            self.config.set(section, key, value)    # 设置属性
            self.config.write(open(path, 'w'))
        else:
            self.config.set(section, key, value)
            self.config.write(open(path, 'w'))
        pass

    def write_config_section(self, path, section, data_dict):
        self.config.read(path)
        # 读取配置文件原数据，追加写入
        self.config = self.read_config_all(path)

        if section not in self.config.sections():
            self.config.add_section(section)    # 添加输入section
            for key in data_dict:
                self.config.set(section, key, data_dict[key])   # 设置属性
            self.config.write(open(path, 'w'))
        else:
            # section存在于目标文件中，追加属性
            for key in data_dict:
                self.config.set(section, key, data_dict[key])
            self.config.write(open(path, 'w'))

    def read_config(self, path, section, key):
        self.config.read(path)
        value = self.config.get(section, key)
        return value

    def read_config_section(self, path, section):
        self.config.read(path)
        data_dict = {}
        options = self.config.options(section)
        for option in options:
            value = self.config.get(section, option)
            data_dict[option] = value
        return data_dict

    def read_config_all(self, path):
        self.config.read(path)
        sections = self.config.sections()
        for section in sections:
            options = self.config.options(section)
            for option in options:
                value = self.config.get(section, option)
                self.config.set(section,option,value)
        return self.config

def main():
    fops = FileOperations()
    path = r"../user-config-test.ini"
    # color_section = fops.read_config_section(path, 'Color')
    # print(color_section)
    data = fops.read_config_all(path)
    print(data.sections())

    fops.write_config(path, 'Color', 'bg_color', '0xf0f0f0')
    data = fops.read_config(path, 'Color', 'bg_color')
    print(data)

    fops.write_config(path, 'Color', 'text_color', '0x000000')
    data = fops.read_config(path, 'Color', 'text_color')
    print(data)
    pass

if __name__ == '__main__':
    main()