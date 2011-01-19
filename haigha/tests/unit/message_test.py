import mox
from cStringIO import StringIO

from haigha.message import Message


class MessageTest(mox.MoxTestBase):

  def test_init_no_args(self):
    m = Message()
    self.assertEquals( '', m._body.read() )
    self.assertEquals( None, m._delivery_info )
    self.assertEquals( {}, m._properties )

  def test_init_with_args(self):
    m = Message( 'foo', 'delivery', foo='bar' )
    self.assertEquals( 'foo', m._body.read() )
    self.assertEquals( 'delivery', m._delivery_info )
    self.assertEquals( {'foo':'bar'}, m._properties )

    m = Message( u'D\xfcsseldorf' )
    self.assertEquals( 'D\xc3\xbcsseldorf', m._body.read() )
    self.assertEquals( {'content_encoding':'utf-8'}, m._properties )

  def test_init_raises_typeerror_on_bad_body(self):
    self.assertRaises( TypeError, Message, 1 )

  def test_properties(self):
    m = Message( 'foo', 'delivery', foo='bar' )
    self.assertEquals( 'foo', m.body.read() )
    self.assertEquals( 'foo', m.body_text )
    self.assertEquals( 3, m.body_len )
    self.assertEquals( 'delivery', m.delivery_info )
    self.assertEquals( {'foo':'bar'}, m.properties )

  def test_len(self):
    m = Message('foobar')
    self.assertEquals( 6, len(m) )

  def test_nonzero(self):
    m = Message()
    self.assertTrue( m )

  def test_eq(self):
    l=Message(); r=Message()
    self.assertEquals( l, r )

    l=Message('foo'); r=Message('foo')
    self.assertEquals( l, r )

    l=Message(foo='bar'); r=Message(foo='bar')
    self.assertEquals( l, r )

    l=Message('hello', foo='bar'); r=Message('hello', foo='bar')
    self.assertEquals( l, r )

    l=Message('foo'); r=Message('bar')
    self.assertNotEquals( l, r )

    l=Message(foo='bar'); r=Message(foo='brah')
    self.assertNotEquals( l, r )

    l=Message('hello', foo='bar'); r=Message('goodbye', foo='bar')
    self.assertNotEquals( l, r )

    l=Message('hello', foo='bar'); r=Message('hello', foo='brah')
    self.assertNotEquals( l, r )


  def test_str(self):
    m = Message( 'foo', 'delivery', foo='bar' )
    str(m)
