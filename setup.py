from setuptools import setup,find_packages

setup(
        name='TicTacToe',
        version='1.0',
        author='Sayam Goswami',
        url='https://github.com/sayampy/TicTacToe-Game/',
        license='MIT',
        description='a tictactoe game using curses',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        packages=find_packages(),
        classifiers=[
        "License :: OSI Approved :: MIT License"],
        python_requires='>=3.10',
        entry_points='''
            [console_scripts]
                tictactoe=src.cli:main
            '''
        )
