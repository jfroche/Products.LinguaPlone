# -*- coding: utf-8 -*-
from Products.LinguaPlone.tests.base import LinguaPloneTestCase
from Products.LinguaPlone.tests.utils import makeContent
from Products.LinguaPlone.tests.utils import makeTranslation


class TestFolderTranslation(LinguaPloneTestCase):

    def afterSetUp(self):
        self.setRoles(['Manager'])
        self.portal.portal_setup.runAllImportStepsFromProfile(
            'profile-plone.app.iterate:plone.app.iterate')

    def testIterateDraftWithLinguaPlone(self):
        self.addLanguage('fr')
        self.setLanguage('en')
        self.folder_en = makeContent(self.folder, 'SimpleFolder', 'folder')
        self.folder_en.setLanguage('en')
        self.english = makeContent(self.folder, 'SimpleType', 'doc')
        self.french = makeTranslation(self.english, 'fr')
