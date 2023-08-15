import toml
from setuptools import setup


def extract_dependencies_from_pyproject():
    with open("pyproject.toml", "r") as pyproject_file:
        pyproject_content = toml.load(pyproject_file)

    dependencies = pyproject_content.get("tool", {}).get("poetry", {}).get("dependencies", {})
    return [f"{pkg}=={version}" for pkg, version in dependencies.items()]


def main():
    dependencies = extract_dependencies_from_pyproject()

    setup(
        name="crawler",
        version="0.1.0",
        description="",
        author="Lior Zamir",
        author_email="liorzam@gmail.com",
        install_requires=dependencies,
        # Other setup options
    )


if __name__ == "__main__":
    main()
