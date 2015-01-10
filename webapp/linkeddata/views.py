# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, RedirectView
from .utils.mediatypes import order_by_precedence, media_type_matches


class Home(TemplateView):
    template_name = 'base.html'


class About(TemplateView):
    template_name = 'linkeddata/about.html'


class Ontology(TemplateView):
    template_name = 'linkeddata/ontology.html'


class OntologyRedirect(RedirectView):
    permanent = False
    pattern_name = 'ontology'

    #! TODO: Como no sé hacer el content-negotiation en Nginx lo meto aquí :/
    def get_redirect_url(self, *args, **kwargs):
        try:
            header = self.request.META.get('HTTP_ACCEPT', '*/*')
            accepts = [token.strip() for token in header.split(',')]
            media_type_set = order_by_precedence(accepts)

            for media_type in media_type_set:
                if media_type_matches('text/turtle', media_type):
                    return "/datosabiertos/def/rafco.ttl"
                elif media_type_matches('application/rdf+xml', media_type):
                    return "/datosabiertos/def/rafco.rdf"
                elif media_type_matches('application/owl+xml', media_type):
                    return "/datosabiertos/def/rafco.owl"
                """
                ... y otros que ahora no tenemos
                elif media_type_matches('application/n-triples', media_type):
                elif media_type_matches('application/ld+json', media_type):
                """

        except:
            pass
        # by default, return html view
        return super(OntologyRedirect, self).get_redirect_url(*args, **kwargs)