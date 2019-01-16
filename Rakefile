# encoding: UTF-8
require "rubygems"
require "tmpdir"

# Change your GitHub reponame
GITHUB_REPONAME = "blparker/learn-linear-algebra"
GITHUB_REPO_BRANCH = "gh-pages"

NOTEBOOKS = '_notebooks'
NBCONVERT_CONFIG_FILE = 'ipython_nbconvert_config.py'
NBCONVERT_CONFIG = <<-CONFIG
c = get_config()

# Export all the notebooks in the current directory to the sphinx_howto format.
#c.NbConvertApp.notebooks = ['*.ipynb']
c.Exporter.preprocessors = ['extract_images.ExtractAttachmentsPreprocessor', 'hide_code.HideCodePreprocessor']
#c.Exporter.preprocessors = ['extract_images.ExtractAttachmentsPreprocessor']
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

      system "jupyter nbconvert #{item} --to markdown --config #{NBCONVERT_CONFIG_FILE} --output-dir ./rendered"
    end

    Dir.chdir pwd
  #end
end

def is_notebook(path)
  return File.extname(path) == '.ipynb'
end

