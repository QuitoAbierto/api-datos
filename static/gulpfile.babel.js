'use strict';

const gulp = require('gulp')
const babel = require('gulp-babel')
const watch = require('gulp-watch')
const shell = require('gulp-shell')

gulp.task('dist', () =>
  gulp.src('public/src/*.js')
    .pipe(babel({
      presets: ['es2015']
    }))
    .pipe(gulp.dest('public/dist'))
)

gulp.task('watch-js', () =>
  watch('public/src/*.js', () =>
    gulp.start('dist')
  )
)

gulp.task('app', shell.task([
  'node app.js'
]))

gulp.task('feature', shell.task([
  'cucumber'
]))
