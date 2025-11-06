data={'Name':'Rahul','Age':24,'City':'Pune'}
print(data)
print(data['Name'])
print(data.get('Age'))




keys=['Rahul','Aniket','Mohan']
values=['Java','Python','JS']

d=dict (zip(keys,values))


print(d)


frameworks={'Java':'Spring','Python':['Django','FastAPI'],'JS':{'React','Vue','Angular'}}

print(frameworks)
print(frameworks['Python'])
frameworks['Java']='Spring Boot'
print(frameworks)

print(frameworks['Python'][1])


print(frameworks.values())  
print(frameworks.items())

for key, value  in frameworks:
    print(key, ":", frameworks[key])



