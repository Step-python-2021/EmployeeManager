from config import app
from views.employee_controller import EmployeeController


if __name__ == '__main__':
    ec = EmployeeController()

    app.run(debug=True)
