#
#  Temperature converters
#  Celsius, Farenheit, and Kelvin temperature convertors
#  Copyright Arjun Sahlot 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

Celsius = float(input("Enter temprature in Celsius: "))

Fahrenheit = 1.8 * Celsius + 32

print ( "Temprature C %.2f Farenheit = %.2f " % (Celsius, Fahrenheit))