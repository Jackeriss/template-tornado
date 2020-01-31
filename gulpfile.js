const gulp = require('gulp');
const cp = require("child_process")

function install() {
  return cp.exec('pipenv install --deploy')
}

function start() {
  return cp.exec('/usr/local/bin/pm2 startOrReload pm2.json')
}

exports.default = gulp.series(install, start)
