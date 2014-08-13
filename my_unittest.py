import unittest

from check_email import check_email

class Test(unittest.TestCase):

    def test_basic_email_true(self):
        #check "@"
        self.assertTrue(check_email("username@domain.com"))
    def test_basic_email_false(self):
        #check "@"
        self.assertFalse(check_email("usernamedomain.com"))
    def test_domain_true(self):
        #domain [a-z 0-9_-]
        self.assertTrue(check_email("username@do_main-007.com"))
    def test_domain_false(self):
        #domain {3,256}
        self.assertFalse(check_email("username@co"))
    def test_domain_symbol(self):
        #domain [^-]
        self.assertFalse(check_email("username@-domain_007.com"))
    def test_domain_symbol_error(self):
        #domain [^-]
        self.assertFalse(check_email("username@domain_007-.com"))
    def test_name_error(self):
        #name {128}
        my_email = 'a'*129 + "@domain.com"
        self.assertFalse(check_email(my_email))
    def test_name_double_dot(self):
        #double dot error
        self.assertFalse(check_email("user..name@domain.com"))
    def test_name_even_quotes(self):
        #even quotes
        self.assertTrue(check_email('"us"er"name"@domain.com'))
    def test_name_odd_quotes(self):
        #odd quotes error
        self.assertFalse(check_email('us"er"name"@domain.com'))
    def test_name_symbol1_check(self):
        # "!" rule
        self.assertTrue(check_email('username"!"@domain.com'))
    def test_name_symbol1_false(self):
        # "!" rule
        self.assertFalse(check_email('user!name@domain.com'))
    def test_name_symbol2_check(self):
        # "," rule
        self.assertTrue(check_email('user","name@domain.com'))
    def test_name_symbol2_false(self):
        # "," rule
        self.assertFalse(check_email('user,name@domain.com'))
    def test_name_symbol3_check(self):
        # ":" rule
        self.assertTrue(check_email('us":"ername@domain.com'))
    def test_name_symbol3_false(self):
        # ":" rule
        self.assertFalse(check_email('us:ername@domain.com'))


if __name__ == '__main__':
    unittest.main()