[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Email Finder :email:
> Find and display a list of all the valid emails that are found given a text file.

This email finder application searches for all the valid emails given a `.txt`file (aiming to support more file extensions in the future) by using the [RFC 5322 criteria](https://tools.ietf.org/html/rfc5322). The result is a set containing all the valid emails that were found on the text file chosen by the user.

![Program output](https://github.com/DrDavxr/email-text-finder/blob/master/email-text-finder.PNG)

## Installation and use :computer:

In order to run this program, the following modules are required:

* regular expression.
* system.
* tkinter.

Please, refer to the [References section](#references) for more information regarding these modules.

To run the program, simply clone the repository and run the main.py script using the following commands:

```sh
git clone https://github.com/DrDavxr/email-text-finder.git
python main.py
```
where the first command is ran in [Git Bash](https://git-scm.com/downloads) and the second one in the terminal.

## Release History :hammer_and_wrench:

* 0.1.2
    * BUG: Fixed a bug where the file was not closed.

* 0.1.1
    * ADD: Optimization tasks for opening large files.

* 0.1.0
    * CHANGE: Rename email_checker to main.
    * CHANGE: Now all the modules are packaged into mainPackage.
    * ADD: Now all domains are accepted.
    * ADD: RFC 5322 email validation to show only valid emails.
    * ADD: GUI to select the file.
* 0.0.1
    * Work in progress: The first release, admitting only certain domains, without built-in email validation.

## Meta :mag_right:

David - Any suggestion? Contact me! davixrgithub@gmail.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

You can find me on _Github_ as [DrDavxr](https://github.com/dbader/)

## Contributing 🤝

1. Fork it (<https://github.com/DrDavxr/email-text-finder/fork>)
2. Create your feature branch (`git checkout -b feature/feature-name`)
3. Commit your changes (`git commit -am 'Add some features'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Create a new Pull Request

## References :green_book:
- Python Documentation: https://docs.python.org/3/
- Regular expression operations: https://docs.python.org/3/library/re.html
- Tkinter documentation: https://pythonspot.com/tk-file-dialogs/
