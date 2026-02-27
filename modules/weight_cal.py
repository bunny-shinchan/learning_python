import converter

print(converter.kg_to_lbs(65))
print(converter.lbs_to_kg(70))

# There is one more syntax.
# In order to import a specific function, we can use from

from converter import kg_to_lbs

print(kg_to_lbs(76))
