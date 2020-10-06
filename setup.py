import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Weeb-Guidance',
    version='1.0.10',
    author='Chas McLaughlin',
    author_email='weebguidance@gmail.com',
    description='A random anime episode selector',
    long_description=long_description,
    url="https://github.com/vv020633/myAnimeListV2",
    license="MIT",
    packages= setuptools.find_packages(),
    install_requires=['PyQt5', 'beautifulsoup4','jikanpy'],
    python_requires='>=3.6',
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points = {
        'gui_scripts' : [
            "weeb-guidance = weeb_guidance.__main__:main"
            ],
    },

    package_dir={
        'weeb-guidance': 'weeb-guidance'
        },
    package_data = {
        'weeb-guidance' : ['forms/*.ui', 'icon/*.png' ],
    },
    # data_files = {
    #     ('share/applications/', ['weeb-guidance.desktop'])
    # }
    # cmdclass=cmdclass,
)