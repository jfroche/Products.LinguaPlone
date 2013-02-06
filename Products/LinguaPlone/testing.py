# -*- coding: utf-8 -*-
from zope.configuration import xmlconfig
from plone.testing import z2
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.testing import PloneSandboxLayer, PLONE_FIXTURE, applyProfile
from plone.app.bbb_testing.plonetestcasecompat import PTCCompatTestCase


class LinguaPloneSandboxLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # load ZCML
        import Products.LinguaPlone
        xmlconfig.file('testing.zcml', Products.LinguaPlone,
                       context=configurationContext)
        z2.installProduct(app, 'Products.LinguaPlone')

    def setUpPloneSite(self, portal):
        # install into the Plone site
        applyProfile(portal, 'Products.CMFPlone:testfixture')
        applyProfile(portal, 'Products.LinguaPlone:LinguaPlone')
        applyProfile(portal, 'Products.LinguaPlone:LinguaPlone_tests')


LINGUAPLONE_FIXTURE = LinguaPloneSandboxLayer()

LINGUAPLONE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LINGUAPLONE_FIXTURE, ),
    name="LinguaPloneLayer:Integration")
LINGUAPLONE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LINGUAPLONE_FIXTURE, ),
    name="LinguaPloneLayer:Functional")


class LinguaPloneTestCase(PTCCompatTestCase):
    layer = LINGUAPLONE_INTEGRATION_TESTING

    def addLanguage(self, language):
        portal = self.layer['portal']
        portal.portal_languages.addSupportedLanguage(language)

    def setLanguage(self, language):
        app = self.layer['app']
        request = app.REQUEST
        request['set_language'] = language
        portal = self.layer['portal']
        portal.portal_languages.setLanguageBindings()


class LinguaPloneFunctionalTestCase(LinguaPloneTestCase):
    layer = LINGUAPLONE_FUNCTIONAL_TESTING
