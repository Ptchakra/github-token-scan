# -*- encoding: utf-8 -*-
import os
import random
import logging

logger = logging.getLogger(__name__)


'''
Based on
https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/master/MobSF/init.py
'''


def first_run(secret_file, base_dir):
    if 'APP_SECRET_KEY' in os.environ:
        secret_key = os.environ['APP_SECRET_KEY']
    elif os.path.isfile(secret_file):
        secret_key = open(secret_file).read().strip()
    else:
        try:
            secret_key = get_random()
            with open(secret_file, 'w') as secret:
                secret.write(secret_key)
        except IOError:
            raise Exception('Secret file generation failed' % secret_file)
    return secret_key



def get_random():
    choice = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join([random.SystemRandom().choice(choice) for _ in range(50)])
