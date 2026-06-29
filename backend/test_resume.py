from database import get_latest_resume
resume = get_latest_resume()
if resume:
    print("Resume Found:\n")
    print(resume[:500])   # print first 500 characters
else:
    print("No resume found.")