from django.conf.urls.defaults import *

from views import group_info, group_member_operations, group_add_admin, \
    group_manage, msg_reply, msg_reply_new, group_recommend, \
    create_group_repo, group_joinrequest, attention, group_message_remove, \
    group_remove_admin

urlpatterns = patterns('',
    url(r'^(?P<group_id>\d+)/$', group_info, name='group_info'),
    url(r'^reply/(?P<msg_id>[\d]+)/$', msg_reply, name='msg_reply'),
    url(r'^reply/new/$', msg_reply_new, name='msg_reply_new'),
    url(r'^(?P<group_id>\d+)/manage/$', group_manage, name='group_members'),
    url(r'^(?P<group_id>[\d]+)/create-repo/$', create_group_repo, name='create_group_repo'),
    (r'^(?P<group_id>[\d]+)/member/(?P<user_name>[^/]+)/$', group_member_operations),
    url(r'^(?P<group_id>\d+)/msgdel/(?P<msg_id>\d+)/$', group_message_remove, name='group_message_remove'),
    url(r'^(?P<group_id>\d+)/admin/add/$', group_add_admin, name='group_add_admin'),
    url(r'^(?P<group_id>\d+)/admin/remove/$', group_remove_admin, name='group_remove_admin'),
    url(r'^recommend/$', group_recommend, name='group_recommend'),
    url(r'^attention/$', attention, name='group_attention'),
    url(r'^joinrequest/(?P<group_id>[\d]+)/$', group_joinrequest, name='group_joinrequest'),
)
