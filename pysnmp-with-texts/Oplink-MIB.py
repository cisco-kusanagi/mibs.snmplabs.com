#
# PySNMP MIB module Oplink-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Oplink-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:35:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, iso, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Bits, ObjectIdentity, Unsigned32, MibIdentifier, Counter32, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "iso", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Counter32", "NotificationType", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oplink = ModuleIdentity((1, 3, 6, 1, 4, 1, 19547))
oplink.setRevisions(('2013-04-02 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oplink.setRevisionsDescriptions((' reorg oplink mib ',))
if mibBuilder.loadTexts: oplink.setLastUpdated('201304021500Z')
if mibBuilder.loadTexts: oplink.setOrganization('OPLINK')
if mibBuilder.loadTexts: oplink.setContactInfo(' oplink ems ')
if mibBuilder.loadTexts: oplink.setDescription(' oplink mib ')
mngdproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 19547, 1))
mibBuilder.exportSymbols("Oplink-MIB", oplink=oplink, mngdproducts=mngdproducts, PYSNMP_MODULE_ID=oplink)
