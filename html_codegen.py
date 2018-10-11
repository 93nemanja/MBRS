
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)
    entity_mm = get_entity_mm(debug)

    Car_model = entity_mm.model_from_file(join(this_folder, 'html.ent'))
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    template = jinja_env.get_template('html.template')

    for entity in Car_model.entities:
        with open(join(srcgen_folder,
                       "%s.html" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

if __name__ == "__main__":
    main()
