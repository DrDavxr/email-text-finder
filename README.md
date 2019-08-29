# :email: Email Finder.
> Find and display a list of all the valid emails that are found given a text file.

This email finder application searches for all the valid emails given a `.txt`file (aiming to support more file extensions in the future) by using the [RFC 5322 criteria](https://tools.ietf.org/html/rfc5322).

![alt text](https://imgur.com/oPrLbwr)

## Installation

OS X & Linux:

```sh
npm install my-crazy-module --save
```

Windows:

```sh
edit autoexec.bat
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.1.0
    * The first proper release
    * CHANGE: Rename email_checker to main.
    * CHANGE: Now all domains are accepted.
    * CHANGE: Now all the modules are packaged into mainPackage.
    * ADD: RFC 5322 email validation to show only valid emails.
    * ADD: GUI to select the file.
* 0.0.1
    * Work in progress: The first release, admitting only certain domains, without built-in email validation.

## Meta

David - davixrgithub@gmail.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

You can find me on _Github_ as [DrDavxr](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/DrDavxr/email-text-finder/fork>)
2. Create your feature branch (`git checkout -b feature/feature-name`)
3. Commit your changes (`git commit -am 'Add some features'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Create a new Pull Request

## Documentation:
- Python Pocket Reference: https://www.amazon.es/Python-Pocket-Reference-OReilly/dp/1449357016/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1797U3V1V37LH&keywords=python+pocket+reference&qid=1567020550&s=gateway&sprefix=python+pocke%2Caps%2C478&sr=8-1
- Regular expression operations: https://docs.python.org/3/library/re.html
- Tkinter documentation: https://pythonspot.com/tk-file-dialogs/
