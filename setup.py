from setuptools import setup, find_packages

setup(
    name='continual_rl',
    version='1.0',
    description='Continual reinforcement learning baselines and standard experiments.',
    author='Sam Powers',
    author_email='snpowers@cs.cmu.edu',
    packages=find_packages(),
    py_modules=['continual_rl.available_policies', 'continual_rl.experiment_specs'],
    ## use python 3.10 to ensure consistency with gym
    install_requires=['setuptools==59.5.0',
                      'uuid',
                      'numpy==1.23.0',
                      'tensorboard',
                      'torch-ac',
                      'cmake',
                      'atari-py==0.2.5',
                      'gym[atari]<=0.25.2',
                      'moviepy',
                      'dotmap',
                      'psutil',
                      'opencv-python'
                    ]
)
