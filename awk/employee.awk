#!/usr/bin/awk -f

BEGIN {
    FS=":";
    print "Emp No.\tEmpName\tBasic Salary\tDA\tHRA\tGross Salary";
    print "-----------------------------------------------------------";
}

{
    emp_no = $1;
    emp_name = $2
    basic_salary = $3;
    
    da = 0.50 * basic_salary;
    hra = 0.30 * basic_salary;
    gross_salary = basic_salary + da + hra; 
    
    printf "%-8s %-10s %-14s %-8s %-8s %-12s\n", emp_no, emp_name, basic_salary, da, hra, gross_salary;
}

END {
    print "-----------------------------------------------------------";
}
