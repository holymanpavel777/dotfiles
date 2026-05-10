#!/bin/bash

# Путь к твоей папке с обоями
DIR=$HOME/Pictures/wallpapers
# Выбираем случайный файл (поддерживает jpg, png, webp)
PICS=($(ls $DIR | grep -E ".jpg|.png|.jpeg|.webp"))
RANDOM_PIC=${PICS[$RANDOM % ${#PICS[@]}]}

# Полный путь к выбранной картинке
WALLPAPER=$DIR/$RANDOM_PIC

# Команды для hyprpaper:
# 1. Загружаем новую картинку в память
hyprctl hyprpaper preload "$WALLPAPER"
# 2. Устанавливаем её на основной экран (eDP-1)
hyprctl hyprpaper wallpaper "eDP-1,$WALLPAPER"
# 3. Выгружаем старые картинки, чтобы не ели оперативку
hyprctl hyprpaper unload all
