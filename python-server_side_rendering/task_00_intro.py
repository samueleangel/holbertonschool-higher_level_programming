#!/usr/bin/env python3
import os
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    # Validación de tipos
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    # Validación de contenido vacío
    if template.strip() == "":
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # Generar invitaciones
    for idx, person in enumerate(attendees, start=1):
        filled_template = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = person.get(key)
            if value is None:
                value = "N/A"
            filled_template = filled_template.replace("{" + key + "}", str(value))
        
        output_filename = f"output_{idx}.txt"

        try:
            with open(output_filename, 'w') as f:
                f.write(filled_template)
            logging.info(f"Generated: {output_filename}")
        except Exception as e:
            logging.error(f"Error writing {output_filename}: {e}")
