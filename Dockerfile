FROM odoo:19.0

USER root

COPY requirements.txt /tmp/requirements.txt

RUN pip install --break-system-packages --no-cache-dir -r /tmp/requirements.txt

COPY ./addons /mnt/extra-addons
RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo

EXPOSE 8069