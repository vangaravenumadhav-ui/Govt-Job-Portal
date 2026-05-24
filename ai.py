def recommend_jobs(branch):

    branch = branch.lower()

    jobs = {

        "cse": [
            "Software Engineer",
            "Data Scientist",
            "Cyber Security Officer"
        ],

        "ece": [
            "Electronics Engineer",
            "ISRO Scientist",
            "Communication Engineer"
        ],

        "eee": [
            "Electrical Engineer",
            "Power Plant Engineer",
            "Government Technician"
        ],

        "civil": [
            "Civil Engineer",
            "Site Engineer",
            "Government Contractor"
        ],

        "mechanical": [
            "Mechanical Engineer",
            "Automobile Engineer",
            "Production Engineer"
        ]
    }

    return jobs.get(branch, ["No jobs found"])