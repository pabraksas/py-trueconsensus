#!/usr/bin/env python
#
# fastchain.py: BFT committee codebase
#
# Copyright (c) 2018 TrueChain Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import uuid
import random
from db.backends.level import LevelDB

from fastchain import ecdsa_sig as sig
from fastchain.log_maintainer import LedgerLog
from fastchain.config import config_yaml
# from logging import ledger

from fastchain.node import Node

from collections import OrderedDict, \
    defaultdict, \
    namedtuple  # for transaction tuple, use struct?

LAMBDA = config_yaml['bft_committee']['lambda']


def generate_block(genesis=True):
    pass


def generate_txns(R, l):
    """
    Returns randomly generated tuple of txns with
    day R, l(seq of txn) and tx (hash id)
    """
    return (R, l, random.getrandbits(128))
    uuid.uuid4().hex


# def genkey():
#     return uuid.uuid4().hex


class DailyOffChainConsensus(object):
    def __init__(self):
        self.chain = []
        self._lambda = None

    def preproess(self):
        pass


class NodeBFT(Node):
    '''
    @types:
    committee member
    committee non-member

    @state:
    corrup, honest(pre-corrupt, honest)

    '''
    R = 0
    LOGs = defaultdict(list)
    LOG = defaultdict()
    csize = LAMBDA
    state_map = []  # maps states of all nodes

    def __init__(self, id=None, type=None):
        self.NodeId = id
        self._type = 'BFTmember'
        self.new_row = namedtuple('row', ['R', 'l', 'txn'])
        # TODO: maybe use ctypes.Structure or struct.Struct ?
        self.nonce = 0

    def launch_boot_nodes(self):
        return

    def log_to_snailchain(self):
        return


class ViewChangeInit(object):
    '''
    '''

    def __init__(self):
        self.timeout = 300 # seconds? load from config

    def check_for_timeout(self, start):
        current = time.time()
        if current - start >= self.timeout:
            return True
        return False


class BFTcommittee(object):
    '''
    '''

    def __init__(self, R, view, node_addresses):
        self.committee_id = R
        self.view = view
        self.nodes = node_addresses
        self.log = []
        # TODO: calculate csize and sec_param
        sefl.chain_size = R * csize + LAMBDA

    def call_to_viewchange(self):
        """
        complains to snailchain, init viewchange
        """
        VC = ViewChangeInit(self.nodes)
        response = None
        start = time.time()
        while true:
            response = VC.wait_for_reply()
            if response is not None:
                break
        return

    def sign_transaction(self, txn_tuple):
        """
        """
        key = get_asymm_key(self.id, ktype="sign")
        signed_txn = sig.sign(key, txn_tuple)
        return signed_txn


    def log_to_slowchain(self):
        """
        """
        pass

    def fetch_LOG(self):
        """
        """
        pass

    def commit_txn(self):
        """
        """
        pass

    def genkey(self):
        """
        return (sk, vk) -> keypair generated by ECDSA
        """
        return sig.generate_keys()

    def sign_log(self):
        key = get_asymm_key(self.id, ktype="sign")
        # TODO: handle conversation of log to bytes (use struct?)
        signed_log = sig.sign(key, self.log)
        return signed_log

    def append_to_log(self, txn_tuple):
        self.log.append(txn_tuple)

    def gossip_to_snailchain(self):
        """
        use UDP protocol / P2P to gossip to chain
        """
        pass

    def fork_vbft(self):
        pass

    def update_mempool_subprotocol(self):
        pass
