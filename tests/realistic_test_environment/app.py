from tests.realistic_test_environment.components.example_component import MyComponent1, MyComponent3
from slobypy.react.component import *

class MyApp(AppComponent):
    def body(self):
        yield MyComponent3()


MyApp()
