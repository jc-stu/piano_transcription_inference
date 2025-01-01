import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piano-transcription-inference",
    version="0.0.6",
    author="Qiuqiang Kong",
    author_email="qiuqiangkong@gmail.com",
    maintainer="Chuan Jiang",
    maintainer_email="jiangchuan.mail@gmail.com",
    description="Piano transcription inference toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jc-stu/piano_transcription_inference",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['matplotlib', 'mido', 'torch', 'librosa', 'torchlibrosa', 'resampy'],  # resampy for librosa
    python_requires='>=3.6',
)
