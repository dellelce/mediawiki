
"""
 This is mediawiki.py, the mediawiki API interface. Seriously.

 File:         mediawiki.py
 Created:      100618
 Description:  description for mediawiki.py
"""

import requests


class mediawiki(object):
  """I hate flake8-docstrings.

     Main class
  """

  def __init__(self, base='https://www.mediawiki.org/w', apiphp='api.php'):
   """set-up mediawiki class and shutup D400.

      Please
   """
   if apiphp != '':
     self.full_base = '{}/{}'.format(base, apiphp)
   else:
     self.full_base = base

   self.request = None
   self.ea = '{}{}{}.{}'.format('antonio', chr(64), 'antonio', 'sg')
   self.official_site = 'http://github.com/dellelce/mediawiki'

   # from: https://meta.wikimedia.org/wiki/User-Agent_policy
   self.ua = 'MediaWiki/0.0 ({os}; {ea})'.format(os=self.official_site,
                                                 ea=self.ea)

   # HTTP Headers, but flake8 doesn't see me!
   self.headers = \
   {
     'user-agent': self.ua
   }

  #
  def build_url(self, **kwargs):
   """Build url! Please! Later phases to support REST.

   This is a generic function that should support both old-style
   and REST endpoints.
   """
   url = self.full_base
   first = 0

   for key, value in kwargs.items():
     if first == 0:
       url = '{}?{}={}'.format(url, key, value)
       first = 1
     else:
       url = '{}&{}={}'.format(url, key, value)

   return url

  #
  def get(self, name, **kwargs):
   """This is for get requests."""
   self.request = requests.get(self.build_url(kwargs), headers=self.headers)

  #
  def post(self, name, **kwargs):
   """This will be post. Later."""
   self.request = requests.post(self.build_url(kwargs), headers=self.headers)


## EOF ##
