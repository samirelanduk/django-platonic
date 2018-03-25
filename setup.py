from setuptools import setup

setup(
 name="platonic",
 version="0.1.0",
 description="Django forms",
 url="https://platonic.samireland.com",
 author="Sam Ireland",
 author_email="mail@samireland.com",
 license="MIT",
 classifiers=[
  "Development Status :: 4 - Beta",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.6",
 ],
 keywords="django forms",
 packages=["platonic"],
 install_requires=["django"]
)
