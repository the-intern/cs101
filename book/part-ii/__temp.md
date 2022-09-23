spam = ' Hello World '
print(spam.strip())

# 'Hello World'

print(spam.lstrip())

# 'Hello World '

print(spam.rstrip())

# ' Hello World'

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

# 'BaconSpamEggs'
