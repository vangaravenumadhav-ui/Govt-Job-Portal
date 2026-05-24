def recommend_jobs(branch):

    branch = branch.lower()

    jobs = {

        "cse": [
            {
                "title": "Software Engineer",
                "apply_link": "https://www.linkedin.com/jobs/"
            },

            {
                "title": "Data Scientist",
                "apply_link": "https://www.naukri.com/data-scientist-jobs"
            },

            {
                "title": "Cyber Security Officer",
                "apply_link": "https://www.indeed.com/q-cyber-security-jobs.html"
            }
        ],

        "ece": [
            {
                "title": "Electronics Engineer",
                "apply_link": "https://www.naukri.com/electronics-engineer-jobs"
            },

            {
                "title": "ISRO Scientist",
                "apply_link": "https://www.isro.gov.in/Careers.html"
            }
        ],

        "mechanical": [
            {
                "title": "Mechanical Engineer",
                "apply_link": "https://www.naukri.com/mechanical-engineer-jobs"
            }
        ]
    }

    return jobs.get(branch, [])