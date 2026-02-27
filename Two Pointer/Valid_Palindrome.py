class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = 0
        s = s.strip()
        R = len(s) - 1

        if s == "" or s == " ":
            return True

        # while the pointers don't lie on same position
        while L < R:
            # check if each is alphanumeric

            # if (ord(s[L].lower()) >= 97 and ord(s[L].lower()) <= 122):
            if s[L].lower().isalnum():
                if s[R].lower().isalnum():
                    # if (ord(s[R].lower()) >= 97 and ord(s[R].lower()) <= 122):

                    if s[L].lower() == s[R].lower():
                        L += 1
                        R -= 1
                    else:
                        return False

                elif s[R] == " ":
                    R -= 1
                else:
                    R -= 1

            elif s[L] == " ":
                L += 1
            else:
                L += 1
        return True
