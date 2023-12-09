from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import get_object_or_404

from shared.models import NixpkgsIssue
from shared.models.cve import Container

from django.contrib.postgres.search import SearchVector


class HomeView(TemplateView):
    template_name = "home_view.html"


class TriageView(ListView):
    template_name = "triage_view.html"
    model = Container
    paginate_by = 25

    def get_queryset(self):
        qs = (
            Container.objects.prefetch_related("descriptions", "affected", "cve")
            .exclude(title="")
            .order_by("id", "-date_public")
        )
        search_query = self.request.GET.get("search_query")
        if not search_query:
            return qs.all()
        else:
            return (
                qs.annotate(
                    search=SearchVector(
                        "title",
                        "descriptions__value",
                        "affected__vendor",
                        "affected__product",
                        "affected__package_name",
                        "affected__repo",
                        "affected__cpes__name",
                    )
                )
                .filter(search=search_query)
                .distinct("id")
            )


class NixpkgsIssueView(DetailView):
    template_name = "issue_detail.html"
    model = NixpkgsIssue

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, **{"code": self.kwargs.get("code")})


class NixpkgsIssueListView(ListView):
    template_name = "issue_list.html"
    model = NixpkgsIssue

    def get_queryset(self):
        return NixpkgsIssue.objects.all()
