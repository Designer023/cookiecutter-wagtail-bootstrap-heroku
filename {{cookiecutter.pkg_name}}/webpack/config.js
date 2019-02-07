const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");


const BROWSER_LIST = [
    ">1%",
    "last 5 versions",
    'iOS >= 10',
    'Safari >= 7',
    "Explorer >= 10"
];


let common_config = {
    name: 'main',
    context: path.resolve(__dirname, '../'),
    plugins: [
        new MiniCssExtractPlugin({
            filename: "[name].css",
            chunkFilename: "[id].css"
        })
    ],

    entry: {
        style: ['./{{cookiecutter.pkg_name}}/frontend_src/scss/style'],
        app: ['./{{cookiecutter.pkg_name}}/frontend_src/js/app']
    },

    output: {
        filename: "[name].js",
        publicPath: '', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
    },

    resolve: {
        modules: ['node_modules', 'bower_components'],
        extensions: ['.js', '.jsx', '.ts', '.tsx', '.scss', '.woff', '.woff2', '.eot', '.ttf', '.svg']
    },

    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                use: [
                    {
                        loader: 'babel-loader',
                        options: {
                            babelrc: true,
                            // plugins: ['react-hot-loader/babel'],
                        },
                    },
                ]
            },
            {
                test: /\.(scss)$/,
                use: [
                    {loader: "style-loader"},
                    MiniCssExtractPlugin.loader,
                    {
                        loader: "css-loader",
                        options: {
                            url: false,
                        }
                    },
                    {
                        loader: "postcss-loader",
                        options: {
                            autoprefixer: {
                                browsers: BROWSER_LIST,
                                safe: true, // crucial in order not to break anything
                                add: true,
                                remove: false,
                                flexbox: true,
                            },
                            plugins: [
                                // precss,
                                require('autoprefixer')
                            ]
                        },
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            sourceMap: false
                        }
                    }
                ]
            },
            {
                test: /\.(woff|woff2|eot|ttf|svg)$/,
                exclude: /node_modules/,
                loader: 'file-loader',
                options: {
                    limit: 10240,
                    name: '[name].[ext]'
                }
            }
        ]
    }
};

module.exports = common_config;
