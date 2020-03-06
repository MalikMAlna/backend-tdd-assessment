#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
import subprocess
import echo

# Your test case class goes here


class TestEcho(unittest.TestCase):
    def setUp(self):
        """This function is called only once for all tests"""
        self.parser = echo.create_parser()
        self.pystring = "python2"
        if sys.version_info[0] == 3:
            self.pystring = "python3"

    def test_help(self):
        """ Running the program without arguments should show usage. """
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            [self.pystring, "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf8")
        with open("./USAGE") as f:
            usage = f.read()

        self.assertEquals(stdout, usage)

    def test_upper_short(self):
        args = ["-u", "hello world"]
        ns = self.parser.parse_args(args)
        result = echo.main(args)
        expected = "HELLO WORLD"

        self.assertTrue(ns.upper)
        self.assertEqual(result, expected)

    def test_lower_short(self):
        args = ["-l", "HELLO WORLD"]
        ns = self.parser.parse_args(args)
        result = echo.main(args)
        expected = "hello world"

        self.assertTrue(ns.lower)
        self.assertEqual(result, expected)

    def test_title_short(self):
        args = ["-t", "hello world"]
        ns = self.parser.parse_args(args)
        result = echo.main(args)
        expected = "Hello World"

        self.assertTrue(ns.title)
        self.assertEqual(result, expected)

    def test_upper_long(self):
        args = ["--upper", "hello world"]
        ns = self.parser.parse_args(args)
        result = echo.main(args)
        expected = "HELLO WORLD"

        self.assertTrue(ns.upper)
        self.assertEqual(result, expected)

    def test_lower_long(self):
        args = ["--lower", "HELLO WORLD"]
        ns = self.parser.parse_args(args)
        result = echo.main(args)
        expected = "hello world"

        self.assertTrue(ns.lower)
        self.assertEqual(result, expected)

    def test_title_long(self):
        args = ["--title", "hello world"]
        ns = self.parser.parse_args(args)
        result = echo.main(args)
        expected = "Hello World"

        self.assertTrue(ns.title)
        self.assertEqual(result, expected)

    def test_all(self):
        args = ["-tul", "HeLlO wOrLd"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_no_args(self):
        args = ["hello world"]
        ns = self.parser.parse_args(args)
        result = echo.main(args)
        expected = "hello world"

        self.assertTrue(ns)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
