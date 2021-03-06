# -*- coding: utf-8 -*-
# Copyright 2018 Twitter, Inc.
# Licensed under the MIT License
# https://opensource.org/licenses/MIT
import re
from setuptools import setup, find_packages

with open("./searchtweets/_version.py") as f:
    VERSION = re.search(r'\d+.\d+.\d+', f.read()).group()

setup(name='searchtweets',
      description="Wrapper for Twitter's Premium and Enterprise search APIs",
      url='https://github.com/twitterdev/search-tweets-python',
      author='Fiona Pigott, Jeff Kolb, Josh Montague, Aaron Gonzales',
      long_description=open('README.rst', 'r', encoding="utf-8").read(),
      author_email='agonzales@twitter.com',
      license='MIT',
      version=VERSION,
      python_requires='>=3.3',
      install_requires=["requests", "tweet_parser", "pyyaml"],
      packages=find_packages(),
      scripts=["tools/search_tweets.py"],
      )
