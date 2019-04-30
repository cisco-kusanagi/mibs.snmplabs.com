#
# PySNMP MIB module HM2-OEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-OEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
hm2ConfigurationMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, Gauge32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, IpAddress, Integer32, Bits, Counter64, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Gauge32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "IpAddress", "Integer32", "Bits", "Counter64", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2OemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 15))
hm2OemMib.setRevisions(('2011-03-31 00:00',))
if mibBuilder.loadTexts: hm2OemMib.setLastUpdated('201103310000Z')
if mibBuilder.loadTexts: hm2OemMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2OemMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 15, 1))
hm2OemID = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2OemID.setStatus('current')
mibBuilder.exportSymbols("HM2-OEM-MIB", hm2OemID=hm2OemID, PYSNMP_MODULE_ID=hm2OemMib, hm2OemMibObjects=hm2OemMibObjects, hm2OemMib=hm2OemMib)
