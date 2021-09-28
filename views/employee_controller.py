from flask import render_template, request
from werkzeug.utils import secure_filename
from os import path
from config import app
from models.employee import Employee


class EmployeeController(object):

    @staticmethod
    @app.route('/', methods=['GET', 'POST'])
    def add():
        if request.method == 'GET':
            return render_template('home/index.html')
        elif request.method == 'POST':
            name = request.form.get('name')
            surname = request.form.get('surname')
            file = request.files.get('image')
            filename = secure_filename(file.name)
            extensions = ['png', 'jpg', 'jpeg', 'gif', 'bmp']
            size_limit = 10 * 1024 * 1024  # 10Mb

            if filename.split('.')[-1] not in extensions:
                message = 'Wrong file format!'
                mess_color = 'red'
            elif len(file.read()) > size_limit:
                message = f'Size limit of {size_limit} Mb'
                mess_color = 'red'
            else:
                local_dir = path.dirname(path.abspath(__file__))
                root_dir = path.abspath(local_dir + '\\..\\')
                save_dir = root_dir + '\\media\\upload'
                save_path = path.join(save_dir, filename)
                file.stream.seek(0)
                file.save(save_path)

                photo = f'../media/upload/{filename}'
                Employee.add_employee(name, surname, photo)

                message = 'Employee successfully added'
                mess_color = 'green'

            return render_template('home/index_info.html', context={
                'message': message,
                'mess_color': mess_color
            })
        else:
            return render_template('access/page403.html')
