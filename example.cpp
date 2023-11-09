#include <iostream>
using namespace std;

class MyClass
{
public:
  MyClass( int x, int y )
    : x_( x )
    , y_( y )
  {
  }
  int
  getX() const
  {
    return x_;
  }
  int
  getY() const
  {
    return y_;
  }
  void
  setX( int x )
  {
    x_ = x;
  }
  void
  setY( int y )
  {
    y_ = y;
  }

private:
  int x_;
  int y_;
};

int
main()
{
  MyClass obj( 10, 20 );
  cout << "Initial values: x = " << obj.getX() << ", y = " << obj.getY() << endl;
  obj.setX( 30 );
  obj.setY( 40 );
  cout << "Updated values: x = " << obj.getX() << ", y = " << obj.getY() << endl;
  return 0;
}
