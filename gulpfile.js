const gulp = require('gulp');
const run = require("gulp-run")

function start() {
  return run('/usr/local/bin/pm2 startOrGracefulReload pm2.json').exec()
}

exports.start = start
exports.deploy = gulp.series(
  start
)
