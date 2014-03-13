# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from zen import router

def index(_handler):
    path = router.to_path(form,"Silvio","Lima")
    _handler.redirect(path)


def form(_resp,nome,sobrenome):
    _resp.write("Ola %s %s !"%(nome,sobrenome))
