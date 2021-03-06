from django.conf.urls import patterns, include, url
from django.shortcuts import redirect
from members import views

#urlpatterns = patterns('gather.views',
#	url(r'^events/$', 'upcoming_events'),
#)

urlpatterns = patterns('members.views',
	(r'^$', 'home'),
	(r'^view/$', 'view_members'),
	(r'^profile/$', 'profile_redirect'),
	(r'^events/$', 'events_google'),
#	(r'^events/today/$', 'events_today'),
#	(r'^events/(?P<year>\d+)/(?P<month>\d+)/$', 'events'),
#	(r'^event/(?P<event_id>\d+)/$', 'view_event'),
#	(r'^event/add/$', 'add_event'),
	(r'^chat/$', 'chat'),
	(r'^tags/$', 'tags'),
	(r'^tag_cloud/$', 'tag_cloud'),
	(r'^not_active/$', 'not_active'),
	(r'^t/(?P<tag>[^/]+)/$', 'tag'),
	(r'^u/(?P<username>[^/]+)/$', 'user'),
	(r'^u/(?P<username>[^/]+)/manage/$', 'manage_member'),
	(r'^u/(?P<username>[^/]+)/tags/$', 'user_tags'),
	(r'^u/(?P<username>[^/]+)/deltag/(?P<tag>[^/]+)$', 'delete_tag'),
	(r'^devices/$', 'user_devices'),
	(r'^lists/$', 'mail'),
	(r'^u/(?P<username>[^/]+)/edit/$', 'edit_profile'),
	(r'^u/(?P<username>[^/]+)/r/(?P<id>\d+)/$', 'receipt'),
	(r'^help/(?P<slug>[^/]+)/$', 'help_topic'),
	(r'^mail/(?P<id>\d+)/$', 'mail_message'),
	(r'^connect/(?P<username>[^/]+)/$', 'connect'),
	(r'^notifications/$', 'notifications'),
	(r'^notifications/add/(?P<username>[^/]+)/$', 'add_notification'),
	(r'^notifications/delete/(?P<username>[^/]+)/$', 'delete_notification'),
	(r'^disable_billing/(?P<username>[^/]+)$', 'disable_billing'),
	(r'^new_billing/$', 'new_billing'),
	(r'^file/(?P<disposition>[^/]+)/(?P<username>[^/]+)/(?P<file_name>[^/]+)$', 'file_view'),
	#url(r'^events/create/(?P<location_slug>[^/]+)/$', 'my_create_event', name='gather_create_event'),
	#(r'^events/', include(gather.urls)),
)

# Copyright 2014 Office Nomads LLC (http://www.officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
