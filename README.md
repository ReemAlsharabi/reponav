# reponav 1.1.2
_reponav_ is a Python package that allows you to easily navigate the contents of a GitHub repository. Given a repository name or URL, _reponav_ will print out a tree-like structure of the repository's contents, including directories and files.


![reponav](https://user-images.githubusercontent.com/73318920/227341895-e16435c1-322e-4c83-ab04-87b35fa6e8f7.gif)



## Installation
**You can install _reponav_ using _pip_:**

`pip install reponav`


## Dependencies
`github`

`PyGithub`


## Usage
To use reponav, simply import the _get_struct_ function and pass in the name or URL of the repository you want to navigate:

`from reponav import get_struct`

`repo = 'username/repo'`

`get_struct(repo)`


or: 

`import reponav`

`reponav.get_struct('username/repo')`

_get_struct_ will print out a tree-like structure of the repository's contents to the console.


## PyPI
[reponav](https://pypi.org/project/reponav/)

## Contributing
Contributions are welcome! If you find any bugs or have any suggestions for new features, please start an issue or contact the author.

If you would like to contribute code to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch with a descriptive name (`git checkout -b my_new_feature`).
3. Write your code and tests, ensuring that they pass.
4. Push your changes to your fork (`git push origin my_new_feature`).
5. Open a pull request and describe your changes.

Thank you for your contributions!

## Author
[Reem Alsharabi](https://github.com/ReemAlsharabi)
