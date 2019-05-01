#
# PySNMP MIB module EdgeSwitch-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:10:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, Unsigned32, iso, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ObjectIdentity, MibIdentifier, ModuleIdentity, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Unsigned32", "iso", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Counter64", "NotificationType")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
fastPathQOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3))
fastPathQOS.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00', '2003-11-21 00:00', '2002-01-30 15:44',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathQOS.setRevisionsDescriptions(('Postal address updated.', 'Ubiquiti branding related changes.', 'Revisions made for new release.', 'Initial revision.',))
if mibBuilder.loadTexts: fastPathQOS.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathQOS.setOrganization('Broadcom Inc')
if mibBuilder.loadTexts: fastPathQOS.setContactInfo('')
if mibBuilder.loadTexts: fastPathQOS.setDescription('The MIB definitaions for Quality of Service Flex package.')
mibBuilder.exportSymbols("EdgeSwitch-QOS-MIB", PYSNMP_MODULE_ID=fastPathQOS, fastPathQOS=fastPathQOS)
