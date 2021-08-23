# -*- coding:utf-8 -*-
from app.pages.app import App
from pages.member_invite_page import MemberInvite


class TestContact:
	def setup(self):
		# 实例化首页
		self._app = App()
		self._start = self._app.start()
		self._main = self._app.main()

	def teatdown(self):
		pass

	def test_contact(self):
		self._main.goto_addresslist().\
			add_member().\
			addmember_by_manul().\
			input_name().\
			input_gender().\
			input_phone().\
			click_save()

		assert '成功' in MemberInvite().get_toast()
