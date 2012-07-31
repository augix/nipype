"""Autogenerated file - DO NOT EDIT         
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os
from nipype.interfaces.slicer.base import SlicerCommandLine


class DiffusionTensorTestInputSpec(CommandLineInputSpec):
    inputVolume = File(position="0", desc="Input tensor volume to be filtered", exists=True, argstr="%s")
    outputVolume = traits.Either(traits.Bool, File(), position="1", hash_files=False, desc="Filtered tensor volume", argstr="%s")


class DiffusionTensorTestOutputSpec(TraitedSpec):
    outputVolume = File(position="1", desc="Filtered tensor volume", exists=True)


class DiffusionTensorTest(SlicerCommandLine):
    """title: 
  Simple IO Test
  

category: 
  Legacy.Work in Progress.Diffusion Tensor.Test
  

description: 
  Simple test of tensor IO
  

version: 0.1.0.$Revision: 18864 $(alpha)

contributor: Bill Lorensen

"""

    input_spec = DiffusionTensorTestInputSpec
    output_spec = DiffusionTensorTestOutputSpec
    _cmd = " DiffusionTensorTest "
    _outputs_filenames = {'outputVolume':'outputVolume.nii'}
