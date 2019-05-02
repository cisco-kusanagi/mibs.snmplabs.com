#
# PySNMP MIB module ARISTA-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-SMI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:24:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, enterprises, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Counter64, ObjectIdentity, Integer32, Unsigned32, Counter32, TimeTicks, Gauge32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "enterprises", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Counter64", "ObjectIdentity", "Integer32", "Unsigned32", "Counter32", "TimeTicks", "Gauge32", "NotificationType", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arista = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065))
arista.setRevisions(('2014-08-15 00:00', '2011-03-31 13:00', '2008-10-27 18:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arista.setRevisionsDescriptions(('Updated postal and e-mail addresses', 'Updated postal address and telephone', 'Initial version.',))
if mibBuilder.loadTexts: arista.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: arista.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: arista.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: arista.setDescription('The Structure of Management Information for the Arista Networks enterprise.')
aristaProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 1))
if mibBuilder.loadTexts: aristaProducts.setStatus('current')
if mibBuilder.loadTexts: aristaProducts.setDescription('aristaProducts is the root object identifier from which sysObjectID values are assigned. Values are defined in ARISTA-PRODUCTS-MIB.')
aristaModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 2))
if mibBuilder.loadTexts: aristaModules.setStatus('current')
if mibBuilder.loadTexts: aristaModules.setDescription('aristaModules provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
aristaMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3))
if mibBuilder.loadTexts: aristaMibs.setStatus('current')
if mibBuilder.loadTexts: aristaMibs.setDescription('aristaMibs provides a root object identifier for management-related MIBs.')
aristaExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 4))
if mibBuilder.loadTexts: aristaExperiment.setStatus('current')
if mibBuilder.loadTexts: aristaExperiment.setDescription('aristaExperiment provides a root object identifier for experimental MIBs. The structure of information for these MIBs can not be guaranteed between releases.')
mibBuilder.exportSymbols("ARISTA-SMI-MIB", PYSNMP_MODULE_ID=arista, aristaModules=aristaModules, aristaProducts=aristaProducts, arista=arista, aristaMibs=aristaMibs, aristaExperiment=aristaExperiment)
