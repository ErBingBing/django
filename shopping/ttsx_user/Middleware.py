class UrlMiddleware(object):
    def process_view(self,request,view_name,view_args,view_kwargs):
        # print '.................' + request.path
        if request.path not in ['/user/register/',
                                '/user/register_handle/',
                                '/user/login/',
                                '/user/login_handle/',
                                '/user/loginout/',
                                ]:
            request.session['url_path'] = request.get_full_path()
