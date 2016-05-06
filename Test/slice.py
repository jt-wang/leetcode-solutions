locations = [{'shanghai': 'china'}]
tuple(locations[:])[0]['shanghai'] = 'shanghai'
print(locations)
