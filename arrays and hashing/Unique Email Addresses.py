from typing import List


def numUniqueEmails(self, emails: List[str]) -> int:
    myset = set()

    for mail in emails:
        local_name = mail.split('@')[0].replace('.', '')
        plus_index = local_name.find('+')
        if plus_index >= 0:
            local_name = local_name[:plus_index]
        local_name = local_name + '@' + mail.split('@')[1]
        myset.add(local_name)
    print
    return len(emails) - len(myset)
