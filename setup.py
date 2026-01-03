from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ai-chatbot',
    version='1.0.0',
    author='Your Team',
    author_email='team@example.com',
    description='AI Chatbot application built with Flask and integrated with AWS services',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ai-chatbot',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'Flask>=3.0.0',
        'Flask-CORS>=4.0.0',
        'SQLAlchemy>=2.0.23',
        'PyMySQL>=1.1.0',
        'boto3>=1.34.10',
        'python-dotenv>=1.0.0',
        'requests>=2.31.0',
        'cryptography>=41.0.7',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.7.0',
            'flake8>=6.1.0',
            'mypy>=1.5.0',
        ],
    },
)
