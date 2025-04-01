from setuptools import setup, find_packages

setup(
    name='process-videos',
    version='0.2.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'imageio-ffmpeg'
    ],
    entry_points={
        'console_scripts': [
            'process-videos=process_videos.cli:main',
        ],
    },
    author='Your Name',
    author_email='you@example.com',
    description='Batch video processor with audio normalization and ffmpeg compression',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/process-videos',
    project_urls={
        'Bug Tracker': 'https://github.com/yourusername/process-videos/issues',
        'Source Code': 'https://github.com/yourusername/process-videos',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Multimedia :: Video',
        'Topic :: Utilities',
    ],
    keywords='ffmpeg video audio batch normalization cli loudnorm',
    python_requires='>=3.7',
)
