'use strict';

const gulp = require('gulp')
const clean = require('gulp-clean');
const babel = require('gulp-babel')
const watch = require('gulp-watch')
const shell = require('gulp-shell')
const rename = require('gulp-rename')
const webpack = require('gulp-webpack')
const sequence = require('gulp-sequence')

const settings = {
  env: process.env.ENV || 'production',
  configFodler: 'public/config',
  srcFolder: 'public/src',
  distFolder: 'public/dist'
}

gulp.task('clean', (cb) =>
  gulp.src(settings.distFolder, {read: false})
    .pipe(clean())
)

gulp.task('translate', () =>
  gulp.src('public/src/*.js')
    .pipe(babel({
      presets: ['es2015']
    }))
    .pipe(gulp.dest(settings.distFolder))
)

gulp.task('config', () =>
  gulp.src(`${settings.configFodler}/${settings.env}.js`)
    .pipe(rename('config.js'))
    .pipe(gulp.dest(settings.distFolder))
)

gulp.task('build', () =>
  gulp.src('public/dist/api.js')
    .pipe(webpack({
      output: {
        filename: 'api.bundle.js'
      }
    }))
    .pipe(gulp.dest(settings.distFolder))
)

gulp.task('default', sequence(
  'clean',
  'translate',
  'config',
  'build'
))

gulp.task('watch-js', () =>
  watch('public/src/*.js', () =>
    gulp.start('default')
  )
)
