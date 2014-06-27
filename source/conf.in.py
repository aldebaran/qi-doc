project = u'qi SDK Documentation'

extensions.append('sphinx.ext.autodoc')
extensions.append("qiapidoc")
extensions.append("qiapidoc.cppbrief")

templates_path = ['../source/_templates']

html_additional_pages = {
    'contents' : 'contents.html'
}

html_theme_path = ["../source/_themes"]
html_theme = "alcodedocs"
