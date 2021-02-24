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

Fahrenheit = float(input("Enter temprature in Fahrenheit: "))

Celsius = (Fahrenheit-32)/1.8

print("Temprature F %.2f Fahrenheit = %.2f C" % (Fahrenheit, Celsius))