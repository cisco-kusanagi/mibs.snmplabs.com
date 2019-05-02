#
# PySNMP MIB module CALIX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CALIX-SMI
# Produced by pysmi-0.3.4 at Wed May  1 11:46:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibIdentifier, Counter64, Gauge32, enterprises, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, iso, ObjectIdentity, Bits, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Counter64", "Gauge32", "enterprises", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "iso", "ObjectIdentity", "Bits", "Counter32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
calixNetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 6321))
calixNetworks.setRevisions(('2000-08-31 00:26',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: calixNetworks.setRevisionsDescriptions(('Initial release.',))
if mibBuilder.loadTexts: calixNetworks.setLastUpdated('200008310026Z')
if mibBuilder.loadTexts: calixNetworks.setOrganization('Calix Networks, Inc.')
if mibBuilder.loadTexts: calixNetworks.setContactInfo(' Calix Networks, Inc. Postal: 1035 North McDowell Boulevard Petaluma, CA 94954-1173 USA Phone: +1 707 766 3000 Fax: +1 707 766 3100 E-mail: tech.support@calix.com')
if mibBuilder.loadTexts: calixNetworks.setDescription('The Structure of Management Information for Calix Networks')
calixRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 1))
if mibBuilder.loadTexts: calixRegistrations.setStatus('current')
if mibBuilder.loadTexts: calixRegistrations.setDescription('Sub-tree for product registrations.')
calixModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 1, 1))
if mibBuilder.loadTexts: calixModules.setStatus('current')
if mibBuilder.loadTexts: calixModules.setDescription('Sub-tree to register the values assigned to modules with the MODULE-IDENTITY construct.')
calixProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 1, 2))
if mibBuilder.loadTexts: calixProducts.setStatus('current')
if mibBuilder.loadTexts: calixProducts.setDescription('Sub-tree to register the values product families.')
calixManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 2))
if mibBuilder.loadTexts: calixManagement.setStatus('current')
if mibBuilder.loadTexts: calixManagement.setDescription('Sub-tree for specific object and event definitions.')
mibBuilder.exportSymbols("CALIX-SMI", PYSNMP_MODULE_ID=calixNetworks, calixRegistrations=calixRegistrations, calixManagement=calixManagement, calixNetworks=calixNetworks, calixModules=calixModules, calixProducts=calixProducts)
