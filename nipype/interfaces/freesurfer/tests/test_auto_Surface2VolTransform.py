# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.freesurfer.utils import Surface2VolTransform
def test_Surface2VolTransform_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    transformed_file=dict(name_source=['source_file'],
    hash_files=False,
    name_template='%s_asVol.nii',
    argstr='--outvol %s',
    ),
    hemi=dict(mandatory=True,
    argstr='--hemi %s',
    ),
    template_file=dict(argstr='--template %s',
    ),
    subject_id=dict(xor=['reg_file'],
    argstr='--identity %s',
    ),
    args=dict(argstr='%s',
    ),
    surf_name=dict(argstr='--surf %s',
    ),
    vertexvol_file=dict(name_source=['source_file'],
    hash_files=False,
    name_template='%s_asVol_vertex.nii',
    argstr='--vtxvol %s',
    ),
    reg_file=dict(mandatory=True,
    argstr='--volreg %s',
    xor=['subject_id'],
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    subjects_dir=dict(argstr='--sd %s',
    ),
    source_file=dict(copyfile=False,
    mandatory=True,
    argstr='--surfval %s',
    ),
    projfrac=dict(argstr='--projfrac %s',
    ),
    mkmask=dict(argstr='--mkmask',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = Surface2VolTransform.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Surface2VolTransform_outputs():
    output_map = dict(transformed_file=dict(),
    vertexvol_file=dict(),
    )
    outputs = Surface2VolTransform.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
