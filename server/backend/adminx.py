import xadmin
from respositoy import models
from xadmin import views

#### 用户管理类
class UserProfileAdmin(object):
    ### 显示的字段名称
    list_display = ['id', 'name', 'email', 'phone', 'mobile']

    # 搜索时可输入的字段内容
    search_fields = ['id', 'name', 'email', 'phone']

    # 点击id可进入详细界面进行编辑（默认的）
    list_display_links = ('id',)

    ## 可编辑的列名
    list_editable = ['name', 'email', 'phone', 'mobile']
    # list_filter = ['name' ,'email','phone','mobile']

    # 每页显示多少条
    list_per_page = 20

    # 根据id排序
    ordering = ('id',)
    # 设置只读字段　
    # readonly_fields = ('email',)

    # 显示本条数据的所有信息
    # show_detail_fields = ['asset_name']


xadmin.site.register(models.UserProfile, UserProfileAdmin)



class GlobalSettings(object):
    # 修改title
    site_title = 'xxx后台管理界面'
    # 修改footer
    site_footer = 'xxx的公司'
    # 收起菜单
    menu_style = 'accordion'

    # 设置 models图标
    # https://v3.bootcss.com/components/
    # http://www.yeahzan.com/fa/facss.html
    global_search_models = [models.UserProfile]
    global_models_icon = {
        # Server: "glyphicon glyphicon-tree-conifer", Pool: "fa fa-cloud"
        models.UserProfile: "fa fa-linux"
    }


# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)