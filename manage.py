#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from app import create_app
from flask_script import Manager, Shell

app = create_app('default')
manager = Manager(app)

manager.add_command("shell")

if __name__ == '__main__':
    manager.run()
