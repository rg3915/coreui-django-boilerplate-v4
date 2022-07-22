from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def _list(request):
    template_name = '_list.html'
    return render(request, template_name)


def _detail(request):
    template_name = '_detail.html'
    return render(request, template_name)


def _create(request):
    template_name = '_form.html'
    return render(request, template_name)


def colors(request):
    template_name = 'colors.html'
    return render(request, template_name)


def typography(request):
    template_name = 'typography.html'
    return render(request, template_name)


def blank(request):
    template_name = 'blank.html'
    return render(request, template_name)


def accordion(request):
    template_name = 'base/accordion.html'
    return render(request, template_name)


def breadcrumb(request):
    template_name = 'base/breadcrumb.html'
    return render(request, template_name)


def cards(request):
    template_name = 'base/cards.html'
    return render(request, template_name)


def carousel(request):
    template_name = 'base/carousel.html'
    return render(request, template_name)


def collapse(request):
    template_name = 'base/collapse.html'
    return render(request, template_name)


def list_group(request):
    template_name = 'base/list-group.html'
    return render(request, template_name)


def navs_tabs(request):
    template_name = 'base/navs-tabs.html'
    return render(request, template_name)


def pagination(request):
    template_name = 'base/pagination.html'
    return render(request, template_name)


def placeholders(request):
    template_name = 'base/placeholders.html'
    return render(request, template_name)


def popovers(request):
    template_name = 'base/popovers.html'
    return render(request, template_name)


def progress(request):
    template_name = 'base/progress.html'
    return render(request, template_name)


def spinners(request):
    template_name = 'base/spinners.html'
    return render(request, template_name)


def tables(request):
    template_name = 'base/tables.html'
    return render(request, template_name)


def tooltips(request):
    template_name = 'base/tooltips.html'
    return render(request, template_name)


def buttons(request):
    template_name = 'buttons/buttons.html'
    return render(request, template_name)


def button_group(request):
    template_name = 'buttons/button-group.html'
    return render(request, template_name)


def dropdowns(request):
    template_name = 'buttons/dropdowns.html'
    return render(request, template_name)


def charts(request):
    template_name = 'charts.html'
    return render(request, template_name)


def form_control(request):
    template_name = 'forms/form-control.html'
    return render(request, template_name)


def select(request):
    template_name = 'forms/select.html'
    return render(request, template_name)


def checks_radios(request):
    template_name = 'forms/checks-radios.html'
    return render(request, template_name)


def range(request):
    template_name = 'forms/range.html'
    return render(request, template_name)


def input_group(request):
    template_name = 'forms/input-group.html'
    return render(request, template_name)


def floating_labels(request):
    template_name = 'forms/floating-labels.html'
    return render(request, template_name)


def layout(request):
    template_name = 'forms/layout.html'
    return render(request, template_name)


def validation(request):
    template_name = 'forms/validation.html'
    return render(request, template_name)


def coreui_icons_free(request):
    template_name = 'icons/coreui-icons-free.html'
    return render(request, template_name)


def coreui_icons_brand(request):
    template_name = 'icons/coreui-icons-brand.html'
    return render(request, template_name)


def coreui_icons_flag(request):
    template_name = 'icons/coreui-icons-flag.html'
    return render(request, template_name)


def alerts(request):
    template_name = 'notifications/alerts.html'
    return render(request, template_name)


def badge(request):
    template_name = 'notifications/badge.html'
    return render(request, template_name)


def modals(request):
    template_name = 'notifications/modals.html'
    return render(request, template_name)


def toasts(request):
    template_name = 'notifications/toasts.html'
    return render(request, template_name)


def widgets(request):
    template_name = 'widgets.html'
    return render(request, template_name)


def login(request):
    template_name = 'login.html'
    return render(request, template_name)


def register(request):
    template_name = 'register.html'
    return render(request, template_name)


def page404(request):
    template_name = '404.html'
    return render(request, template_name)


def page500(request):
    template_name = '500.html'
    return render(request, template_name)
