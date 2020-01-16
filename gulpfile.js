const gulp = require('gulp');
const cp = require("child_process")

gulp.task('start', function () {
  return cp.exec('/usr/local/bin/pm2 startOrReload pm2.json')
})

gulp.task('default', function () {
  gulp.start('start')
})
