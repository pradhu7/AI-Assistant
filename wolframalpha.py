import wolframalpha

client = wolframalpha.Client('A676R6-UPVGPR5LXJ')

while True:
    query = str(input('Query: '))
    res = client.query(query)
    output = next(res.result).text
    print(output)