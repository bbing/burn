import web
import os

template_dir = os.path.join(os.environ['OPENSHIFT_REPO_DIR'],'wsgi','templates')
render=web.template.render(template_dir)

