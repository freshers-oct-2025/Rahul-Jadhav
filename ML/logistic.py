from sklearn.linear_model import LinearRegression
model = LinearRegression()

X = [[1], [2], [3], [4],[5],[6],[7] ]   # Hours studied
y = [40, 50, 60, 70,100, 120, 90]        # Marks

model.fit(X, y)

print(model.predict([[8]]))  # Predict for 5 hours
