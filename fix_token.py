with open('contract/index.yaml', 'r') as f:
    content = f.read()

old = '\x5bREDACTED: Supabase Service Role API Key\x5d'
new = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMifQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'

count = content.count(old)
print(f'Found {count} occurrences')
new_content = content.replace(old, new)

with open('contract/index.yaml', 'w') as f:
    f.write(new_content)
print('Done')
