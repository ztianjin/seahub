from django.conf.urls.defaults import *

from django.views.decorators.csrf import csrf_exempt

from views import *


urlpatterns = patterns('',
    url(r'^ping/$', Ping.as_view()),
    url(r'^login/$', csrf_exempt(api_login)),
    url(r'^account/info/$', Account.as_view()),
    url(r'^$', csrf_exempt(ReposView.as_view())),
    url(r'^repo/list/$', csrf_exempt(ReposView.as_view()), name='repos'),
    (r'^repo/(?P<repo_id>[^/]+)/$', csrf_exempt(RepoView.as_view())),

    url(r'^dir/(?P<repo_id>[^/]+)/$', csrf_exempt(RepoDirPathView.as_view()), name='repo-dir-path'),
    url(r'^dir/(?P<repo_id>[^/]+)/(?P<dir_id>[^/]+)/$', csrf_exempt(RepoDirIdView.as_view()), name='repo-dir-id'),
    url(r'^file/(?P<repo_id>[^/]+)/$', csrf_exempt(RepoFilePathView.as_view()), name='repo-file-path'),
    url(r'^file/(?P<repo_id>[^/]+)/(?P<file_id>[^/]+)/$', csrf_exempt(RepoFileIdView.as_view()), name='repo-file-id'),

    url(r'^op/delete/(?P<repo_id>[^/]+)/$', csrf_exempt(OpDeleteView.as_view()), name='delete'),
    url(r'^op/rename/(?P<repo_id>[^/]+)/$', csrf_exempt(OpRenameView.as_view()), name='rename'),
    url(r'^op/move/$', csrf_exempt(OpMoveView.as_view()), name='move'),
    url(r'^op/mkdir/(?P<repo_id>[^/]+)/$', csrf_exempt(OpMkdirView.as_view()), name='mkdir'),
    url(r'^op/upload/(?P<repo_id>[^/]+)/$', csrf_exempt(OpUploadView.as_view()), name='upload'),
    url(r'^starredfiles/', csrf_exempt(StarredFileView.as_view()), name='starredfiles'),
)

