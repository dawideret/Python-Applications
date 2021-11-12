Teachers1 = ["Ismael", "Cody"]
Students1 = ["Josh", "Phil"]
Cleaners1 = ["Edd", "Eddy"]

SchoolOneStaff1 = [Teachers1, Students1, Cleaners1]

Teachers2 = ["Ismael", "Cody"]
Students2 = ["Josh", "Phil"]
Cleaners2 = ["Edd", "Eddy"]

SchoolTwoStaff1 = [Teachers2, Students2, Cleaners2]

StateOneSchools = [SchoolOneStaff1, SchoolTwoStaff1]


Teachers3 = ["Ismael", "Cody"]
Students3 = ["Josh", "Phil"]
Cleaners3 = ["Edd", "Eddy"]

SchoolOneStaff2 = [Teachers3, Students3, Cleaners3]

Teachers4 = ["Ismael", "Cody"]
Students4 = ["Josh", "Phil"]
Cleaners4 = ["Edd", "Eddy"]

SchoolTwoStaff2 = [Teachers4, Students4, Cleaners4]

StateTwoSchools = [SchoolOneStaff2, SchoolTwoStaff2]

CountrySchools = [StateOneSchools, StateTwoSchools]

print(CountrySchools[0][0][0][0])
