class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parseEmail(email):
                emailSpitted = email.split("@")
                localName = emailSpitted[0]
                domainName = emailSpitted[1]

                if '+' in localName:
                    localName = localName[:localName.index('+')]

                if '.' in localName:
                    localName = localName.replace('.', '')

                
                return localName + '@' + domainName

        out = set()
        for email in emails:
            out.add(parseEmail(email))


        return len(out)