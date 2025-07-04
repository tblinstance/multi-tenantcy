from entire.models import Tenant, Domain

# Create a new tenant
tenant = Tenant(schema_name='ai', name='AI Tenant')
tenant.save()

# Add a domain for the tenant
domain = Domain(domain='ai.localhost', tenant=tenant, is_primary=True)
domain.save()

print("Tenant created successfully!")
