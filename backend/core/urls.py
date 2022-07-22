from django.urls import include, path

from backend.core import views as v

app_name = 'core'

url_coreui = [
    path('colors', v.colors, name='colors'),
    path('typography', v.typography, name='typography'),
    path('accordion', v.accordion, name='accordion'),
    path('breadcrumb', v.breadcrumb, name='breadcrumb'),
    path('cards', v.cards, name='cards'),
    path('carousel', v.carousel, name='carousel'),
    path('collapse', v.collapse, name='collapse'),
    path('list-group', v.list_group, name='list_group'),
    path('navs-tabs', v.navs_tabs, name='navs_tabs'),
    path('pagination', v.pagination, name='pagination'),
    path('placeholders', v.placeholders, name='placeholders'),
    path('popovers', v.popovers, name='popovers'),
    path('progress', v.progress, name='progress'),
    path('spinners', v.spinners, name='spinners'),
    path('tables', v.tables, name='tables'),
    path('tooltips', v.tooltips, name='tooltips'),
    path('buttons', v.buttons, name='buttons'),
    path('button-group', v.button_group, name='button_group'),
    path('dropdowns', v.dropdowns, name='dropdowns'),
    path('charts', v.charts, name='charts'),
    path('form-control', v.form_control, name='form_control'),
    path('select', v.select, name='select'),
    path('checks-radios', v.checks_radios, name='checks_radios'),
    path('range', v.range, name='range'),
    path('input-group', v.input_group, name='input_group'),
    path('floating-labels', v.floating_labels, name='floating_labels'),
    path('layout', v.layout, name='layout'),
    path('validation', v.validation, name='validation'),
    path('coreui-icons-free', v.coreui_icons_free, name='coreui_icons_free'),
    path('coreui-icons-brand', v.coreui_icons_brand, name='coreui_icons_brand'),
    path('coreui-icons-flag', v.coreui_icons_flag, name='coreui_icons_flag'),
    path('alerts', v.alerts, name='alerts'),
    path('badge', v.badge, name='badge'),
    path('modals', v.modals, name='modals'),
    path('toasts', v.toasts, name='toasts'),
    path('widgets', v.widgets, name='widgets'),
    path('login', v.login, name='login'),
    path('register', v.register, name='register'),
    path('page404', v.page404, name='page404'),
    path('page500', v.page500, name='page500'),
]


urlpatterns = [
    path('', v.index, name='index'),
    path('list/', v._list, name='list'),
    path('detail/', v._detail, name='detail'),
    path('add/', v._create, name='create'),
    path('blank/', v.blank, name='blank'),
    path('coreui/', include(url_coreui)),
]
