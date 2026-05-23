def recommend_jobs(qualification, branch):

    jobs = []

    branch = branch.lower()

    if "cse" in branch:
        jobs = [
            {
                "title": "Software Engineer",
                "link": "https://www.ncs.gov.in/"
            },
            {
                "title": "SSC CGL",
                "link": "https://ssc.nic.in/"
            }
        ]

    elif "ece" in branch:
        jobs = [
            {
                "title": "ISRO",
                "link": "https://www.isro.gov.in/"
            },
            {
                "title": "DRDO",
                "link": "https://drdo.gov.in/"
            }
        ]

    else:
        jobs = [
            {
                "title": "Bank PO",
                "link": "https://ibps.in/"
            }
        ]

    return jobs