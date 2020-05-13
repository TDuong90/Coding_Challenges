--List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT employees.emp_no, first_name, last_name, gender, salaries.salary FROM employees
INNER JOIN salaries 
ON employees.emp_no = salaries.salary;

--List employees who were hired in 1986.
SELECT emp_no, first_name, last_name,hire_date FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31'
ORDER BY hire_date ASC

--List the manager of each department with the following information: 
--department number, department name, the manager's employee number, last name, first name, and start and end employment dates

SELECT d.dept_no, d.dept_name, m.emp_no, e.first_name, e.last_name, m.from_date, e.hire_date FROM dept_manager as m
INNER JOIN  departments as d
ON m.dept_no = d.dept_no 
INNER JOIN employees e
ON e.emp_no = m.emp_no

--List the department of each employee with the following information: 
--employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, dept_name FROM dept_emp as de
INNER JOIN departments as d
ON de.dept_no = d.dept_no
INNER JOIN employees as e
ON de.emp_no = e.emp_no

--List all employees whose first name is "Hercules" and last names begin with "B."
SELECT * FROM employees
WHERE first_name IN('Hercules') AND last_name ILIKE ('B%')

--List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM dept_emp as de
INNER JOIN departments as d
ON de.dept_no = d.dept_no
INNER JOIN employees as e
ON de.emp_no = e.emp_no
WHERE dept_name = 'Sales'

--List all employees in the Sales and Development departments, 
--including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM dept_emp as de
INNER JOIN departments as d
ON de.dept_no = d.dept_no
INNER JOIN employees as e
ON de.emp_no = e.emp_no
WHERE dept_name = 'Sales' or dept_name = 'Development'

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name, count(last_name) AS "frequency count" FROM employees
GROUP BY last_name 
ORDER BY COUNT(last_name) ASC;
