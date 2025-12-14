/* eslint-disable no-undef */
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');
// Anda mungkin juga perlu mengimpor plugin ini jika Anda menggunakannya di proyek Anda
// const MiniCssExtractPlugin = require('mini-css-extract-plugin'); 

module.exports = (env, argv) => {
  const isProd = argv && argv.mode === 'production';

  return {
    // 1. ENTRY: Titik awal bundling
    entry: path.resolve(__dirname, 'reaction.ts'),
    
    // 2. DEVTOOL: Konfigurasi Source Map untuk debugging
    devtool: isProd ? false : 'inline-source-map',
    
    // 3. OUTPUT: Lokasi dan nama file hasil build
    output: {
      // ** PENTING: Folder output hasil build yang harus disetel di Vercel **
      path: path.resolve(__dirname, 'dist'), 
      
      filename: isProd ? 'js/[name].[contenthash:8].js' : 'js/bundle.js',
      
      // Menghapus file di folder output ('dist') sebelum setiap build baru
      clean: true, 
      
      // Konfigurasi untuk aset (gambar, font, dll.)
      assetModuleFilename: 'assets/[hash][ext][query]' 
    },
    
    // 4. RESOLVE: Ekstensi yang akan otomatis dicari saat mengimpor
    resolve: {
      extensions: ['.ts', '.js', '.json']
    },
    
    // 5. MODULE: Aturan untuk Loader (mengubah tipe file menjadi modul)
    module: {
      rules: [
        // Aturan untuk TypeScript (.ts)
        {
          test: /\.ts$/,
          use: 'ts-loader',
          exclude: /node_modules/
        },
        // Aturan untuk CSS (.css)
        {
          test: /\.css$/i,
          use: ['style-loader', 'css-loader']
          // Jika Anda menggunakan MiniCssExtractPlugin untuk memisahkan CSS menjadi file terpisah:
          // use: [MiniCssExtractPlugin.loader, 'css-loader']
        },
        // Aturan untuk Aset (Gambar/Media)
        {
          test: /\.(png|jpe?g|gif|svg|webp)$/i,
          type: 'asset/resource' // Menggunakan type: 'asset/resource' adalah pendekatan modern Webpack 5
        }
      ]
    },
    
    // 6. PLUGINS: Tugas di luar bundling (seperti menghasilkan HTML, menyalin aset)
    plugins: [
      // Menghasilkan file index.html dan menyuntikkan script JS yang di-build
      new HtmlWebpackPlugin({
        template: path.resolve(__dirname, 'index.html'),
        inject: 'body',
        minify: isProd
          ? {
              collapseWhitespace: true,
              removeComments: true,
              removeRedundantAttributes: true
            }
          : false
      }),
      // Menyalin file/folder ke folder output ('dist')
      new CopyPlugin({
        patterns: [
          { from: path.resolve(__dirname, 'landing.page'), to: 'landing.page' },
          { from: path.resolve(__dirname, 'kimia1.png'), to: 'kimia1.png', noErrorOnMissing: true }
        ]
      })
      // Jika menggunakan MiniCssExtractPlugin:
      // new MiniCssExtractPlugin({
      //   filename: isProd ? 'css/[name].[contenthash:8].css' : 'css/styles.css',
      // }),
    ],
    
    // 7. DEVSERVER: Konfigurasi untuk lingkungan pengembangan lokal (hanya saat development)
    devServer: {
      static: {
        directory: path.join(__dirname)
      },
      compress: true,
      port: 3000,
      open: true,
      hot: true
    }
  };
};