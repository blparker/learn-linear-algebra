# encoding: UTF-8
require "rubygems"
require "tmpdir"

# Change your GitHub reponame
GITHUB_REPONAME = "blparker/learn-linear-algebra"
GITHUB_REPO_BRANCH = "gh-pages"

RENDERED_NB_DIR = "_guides"

NOTEBOOKS = '_notebooks'
NBCONVERT_CONFIG_FILE = 'ipython_nbconvert_config.py'
NBCONVERT_CONFIG = <<-CONFIG
c = get_config()

# Export all the notebooks in the current directory to the sphinx_howto format.
#c.NbConvertApp.notebooks = ['*.ipynb']
c.Exporter.preprocessors = ['extract_images.ExtractAttachmentsPreprocessor', 'hide_code.HideCodePreprocessor']
c.TemplateExporter.template_file = 'markdown.tpl'
c.NbConvertApp.export_format = 'markdown'
CONFIG

desc 'Publish notebooks'
task :publish do
  puts 'Publishing notebooks'

  pwd = Dir.pwd

  # Make a temp dir to hold the files
  #Dir.mktmpdir do |tmp|
  tmp = './tmp'
  Dir.mkdir(tmp, 0700)
    # Copy all the notebooks to the tmp
    cp_r File.join(NOTEBOOKS, '.'), tmp
    cp_r File.join(pwd, '_scripts', '.'), tmp

    Dir.chdir tmp

    # Create the jupyter nbconvert config file in the tmp directory
    File.write(NBCONVERT_CONFIG_FILE, NBCONVERT_CONFIG)

    # For each notebook, generate it
    Dir.foreach('.') do |item|
      next if not is_notebook(item)

      puts item
      puts "Publishing #{item}"

      system "jupyter nbconvert #{item} --config #{NBCONVERT_CONFIG_FILE} --output-dir ./rendered"
    end

    # Once the notebooks have been converted, we need to add the appropriate front matter and copy them into the _guides directory
    # Prepend the front matter to beginning of the new markdown file

    Dir.chdir './rendered'

    add_front_matter()
    copy_to_dir(pwd)

    Dir.chdir pwd
  #end
end

def is_notebook(path)
  return File.extname(path) == '.ipynb'
end

def copy_to_dir(pwd)
  cp_r Dir.glob('*.md'), File.join(pwd, RENDERED_NB_DIR)
  cp_r 'outputs', File.join(pwd, RENDERED_NB_DIR)
end

def add_front_matter()
  Dir.glob('*.md') do |file|
    front_matter = make_front_matter(file)

    File.open(file, 'r+') do |f|
      lines = f.each_line.to_a
      lines.unshift(front_matter)
      f.rewind
      f.write(lines.join)
    end
  end
end

def make_front_matter(file)
  fname = File.basename(file, File.extname(file))

  # Check to see if the first character is a number (to indicate order)
  #first_char = fname[0]
  #if first_char.to_i.to_s == first_char
    # First character is a number, so replace it
  #end

  title = fname
  if title.include? '_'
    title = title.gsub '_', ' '
  end

  permalink_title = fname.downcase.gsub '_', '-'
  permalink = "/guides/#{permalink_title}"

  front_matter = <<-FM
---
layout: post
title: #{title}
permalink: #{permalink}
---
FM

  return front_matter
end
