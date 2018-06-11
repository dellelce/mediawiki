
"""
 This is mediawiki.py, the mediawiki API interface. Seriously.

 File:         mediawiki.py
 Created:      100618
 Description:  description for mediawiki.py
"""

import requests


class mediawiki(object):
  """I hate flake8-docstrings

     Main class
  """

  #
  def __init__(self, base='https://www.mediawiki.org/w', apiphp='api.php'):
   """set-up mediawiki class and shutup D400.

      Please
   """

   if apiphp != '':
     self.full_base = '{}/{}'.format(base, apiphp)
   else:
     self.full_base = base

   self.request = None

   # from: https://meta.wikimedia.org/wiki/User-Agent_policy
   self.ua = 'MediaWiki/0.0 (http://github.com/dellelce/mediawiki; antonio@antonio.sg)'

   # HTTP Headers, but flake8 doesn't see me!
   self.headers = \
   {
     'user-agent': self.ua
   }

  #
  def build_url(self, **kwargs):
   """Build url! Please! Later phases to support REST!"""
   pass

  #
  def get(self, name, **kwargs):
   """This is for get requests"""

   self.request = requests.get(self.build_url(kwargs), headers=self.headers)
   pass

  #
  def post(self, name, **kwargs):
   """This will be post. Later."""
   pass


## EOF ##
