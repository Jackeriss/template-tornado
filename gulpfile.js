const gulp = require('gulp');
const cp = require("child_process")

gulp.task('install', function () {
  return cp.exec('pipenv install --deploy')
})

gulp.task('start', function () {
  return cp.exec('/usr/local/bin/pm2 startOrReload pm2.json')
})

exports.default = gulp.series('install', 'start')
