const path = require("path");
const merge = require('webpack-merge');

const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');

const common_config = require('./config');

module.exports = merge( common_config, {
    mode: 'production',
    devtool: "none",

    output: {
        path: path.resolve('./{{cookiecutter.pkg_name}}/static/prod/bundles/'),
    },

    plugins: [
        new MiniCssExtractPlugin({
            filename: "[name].css",
            chunkFilename: "[id].css"
        }),
    ],

    optimization: {
        minimizer: [
            new UglifyJsPlugin({
                sourceMap: false,
                // test: /\.js$/,
                uglifyOptions: {
                    output: {
                        comments: false,
                    },
                },
            }),
            new OptimizeCssAssetsPlugin({
                assetNameRegExp: /\.(css)$/,
                cssProcessor: require('cssnano'),
                cssProcessorPluginOptions: {
                    preset: ['default', { discardComments: { removeAll: true } }],
                },
                canPrint: true
            })
        ]
    }
});

