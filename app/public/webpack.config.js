const webpack = require('webpack');
const path = require('path');

module.exports = {
    target: "web",
    module: {
        rules: [
            {
                test: /\utils.js$/,
                use: {
                    loader: "file-loader",
                    options: {
                        name: "utils.js",
                        outputPath: "./"
                    }
                }
            },
            {
                test: /\.js$/,
                exclude: [
                    /node_modules/,
                    path.resolve(__dirname, "src/utils.js")
                ],
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.(scss)$/,
                use: [{
                    loader: 'style-loader'
                }, {
                    loader: 'css-loader'
                }, {
                    loader: 'postcss-loader',
                    options: {
                        plugins: function () {
                            return [
                                require('precss'),
                                require('autoprefixer')
                            ];
                        }
                    }
                }, {
                    loader: 'sass-loader'
                }]
            },
            {
                test: /\.(png|jpg)$/,
                loader: 'url-loader'
            },
        ]
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            Popper: ['popper.js', 'default'],
        })
    ]
};