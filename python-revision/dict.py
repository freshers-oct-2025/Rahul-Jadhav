def traverse_dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            traverse_dict(v)
        else:
            print(k, ":", v)

sample = {
    "user": {
        "personal": {"name": "Rahul", "age": 22},
        "skills": {"python": "mid", "aws": "beginner"}
    }
}

traverse_dict(sample)
