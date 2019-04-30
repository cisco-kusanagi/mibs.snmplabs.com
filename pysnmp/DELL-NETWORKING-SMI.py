#
# PySNMP MIB module DELL-NETWORKING-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DELL-NETWORKING-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:22:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, MibIdentifier, NotificationType, ObjectIdentity, enterprises, iso, Counter64, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "MibIdentifier", "NotificationType", "ObjectIdentity", "enterprises", "iso", "Counter64", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dellNet = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027))
dellNet.setRevisions(('2007-06-15 12:00', '1900-10-10 00:00',))
if mibBuilder.loadTexts: dellNet.setLastUpdated('200706151200Z')
if mibBuilder.loadTexts: dellNet.setOrganization('Dell Inc')
dellNetProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 1))
if mibBuilder.loadTexts: dellNetProducts.setStatus('current')
dellNetCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 2))
if mibBuilder.loadTexts: dellNetCommon.setStatus('current')
dellNetMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 3))
if mibBuilder.loadTexts: dellNetMgmt.setStatus('current')
dellNetModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 4))
if mibBuilder.loadTexts: dellNetModules.setStatus('current')
dellNetExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 20))
if mibBuilder.loadTexts: dellNetExperiment.setStatus('current')
mibBuilder.exportSymbols("DELL-NETWORKING-SMI", dellNetModules=dellNetModules, dellNetExperiment=dellNetExperiment, dellNetCommon=dellNetCommon, dellNetMgmt=dellNetMgmt, dellNet=dellNet, PYSNMP_MODULE_ID=dellNet, dellNetProducts=dellNetProducts)
