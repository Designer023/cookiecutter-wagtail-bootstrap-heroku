const path = require("path");
const merge = require('webpack-merge');

const common_config = require('./config');

module.exports = merge( common_config, {
    mode: 'development',
    devtool: "source-map",

    output: {
        path: path.resolve('./{{cookiecutter.pkg_name}}/static/dev/bundles/'),
    }
});
