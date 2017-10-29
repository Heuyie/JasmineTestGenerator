# JasmineTestGenerator
Python program to generate spec files to test a single variable for Jasmine

## Requirement
Python 3

## How to use this program.

**First**, Define variables in settings.py. You need to define following variables to use the program:

| variable | type | default | explanations |
| -------- | :--: | :--------: |------------ |
| beforeEach | string | '' | If you need the beforeEach function, add javascript codes as a string. If not, leave it to be ''.|
| afterEach | string | '' | If you need the afterEach function, add javascript codes as a string. If not, leave it to be ''.|
| testClass | string | '' | The first argument of a describe function. |
| functionHeaderDict | dictionary | {'default':''} | The argument of a expect function. You can define this variable for each testcase category. |
| toEqualDict | dictionary | {'default':''}  | The argument of a toEqual function. You can define this variable for each testcase category. |
| variableName | string | '' | The name of the variable you want to test. |
| included | array | [ ] | The array of testcase category names you want to include in a test. |
| accepted | array | [ ] | The array of testcase category names you want to accept in a test. |

For example, with 2 testcases, 
```
beforeEach = "email = undefined;\n    console.log('new test');"
afterEach = "console.log('A test is over!');"

testClass = 'Email'

variableName = 'email'

included = ['number', 'good email']
accepted = ['good email']
functionHeaderDict = {'all':'validateEmail(email)'}
toEqualDict = {'accepted':'true', 'rejected':'false'}

```
These values produce the following tests:

```
describe('Email', function() {
  var email;

  beforeEach(function() {
    email = undefined;
    console.log('new test');
  });

  afterEach(function() {
    console.log('A test is over!');
  });

  it('should reject number', function() {
    email = 123456;
    expect(validateEmail(email)).toEqual(false);
  });

  it('should accept good email', function() {
    email = 'myemail@gmail.com';
    expect(validateEmail(email)).toEqual(true);
  });

});

```

**Second**, place generateAndRunATest.py, settings.py and testcases.py in the same folder as SpecRunner.html in the default Jasmine file hierarchy. The program make a directory of the same name as variableName and place a spec file there. If this is a problem, rename the existing directory.

**Thrid**, place your test data in testcases.py. Each line in the file contains a category of an input and the input itself, which are separated by a comma. For example, 2 testcases for the example above are:

```
number, 123456
good email, myemail@gmail.com
```

**Forth**, open a terminal in the directory of this program

**Fifth**, type "python generateAndRunATest.py"

**Sixth**, open Spec.Runner.html in your browser.
