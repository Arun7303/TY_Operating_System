BEGIN {
    print"------------------------------------------------------"
    print "\t\tStudent Report"
    print "-----------------------------------------------------"
    print "Roll_NO\t Name \t Average \t Grade"
}

{
    Avg = ($3 + $4 + $5 + $6 + $7) / 5

    if (Avg >= 90 && Avg <= 100) {
        grade = "O"
    } else if (Avg >= 80 && Avg <= 89) {
        grade = "A"
    } else if (Avg >= 68 && Avg <= 79) {
        grade = "B"
    } else if (Avg >= 55 && Avg <= 67) {
        grade = "C"
    } else if (Avg >= 40 && Avg <= 54) {
        grade = "D"
    } else {
        grade = "F"
    }

    print $1 "\t" $2 "\t" Avg "\t" grade
}

END {
    print"------------------------------------------------------"
    print "\t\tEnd of Report"
    print"------------------------------------------------------"
}

