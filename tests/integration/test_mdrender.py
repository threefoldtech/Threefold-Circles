# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# Copyright (C) 2014-2017 Anler Hernández <hello@anler.me>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest

from taiga.mdrender.service import render, render_and_extract

from unittest.mock import MagicMock

from .. import factories

pytestmark = pytest.mark.django_db

dummy_project = MagicMock()
dummy_project.id = 1
dummy_project.slug = "test"


def test_proccessor_valid_user_mention():
    factories.UserFactory(username="user1", full_name="test name")
    result = render(dummy_project, "**@user1**")
    expected_result = "<p><strong><a class=\"mention\" href=\"http://localhost:9001/profile/user1\" title=\"test name\">@user1</a></strong></p>"
    assert result == expected_result


def test_proccessor_valid_user_mention_with_dashes():
    factories.UserFactory(username="user1_text_after_dash", full_name="test name")
    result = render(dummy_project, "**@user1_text_after_dash**")
    expected_result = "<p><strong><a class=\"mention\" href=\"http://localhost:9001/profile/user1_text_after_dash\" title=\"test name\">@user1_text_after_dash</a></strong></p>"
    assert result == expected_result


def test_proccessor_invalid_user_mention():
    result = render(dummy_project, "**@notvaliduser**")
    assert result == '<p><strong>@notvaliduser</strong></p>'


def test_render_and_extract_mentions():
    user = factories.UserFactory(username="user1", full_name="test")
    (_, extracted) = render_and_extract(dummy_project, "**@user1**")
    assert extracted['mentions'] == [user]

def test_render_and_extract_mentions_with_capitalized_username():
    user = factories.UserFactory(username="User1", full_name="test")
    (_, extracted) = render_and_extract(dummy_project, "**@User1**")
    assert extracted['mentions'] == [user]


def test_proccessor_valid_email():
    result = render(dummy_project, "**beta.tester@threefold.io**")
    expected_result = "<p><strong><a href=\"mailto:beta.tester@threefold.io\" target=\"_blank\">beta.tester@threefold.io</a></strong></p>"
    assert result == expected_result
