#
# PySNMP MIB module A3COM-HUAWEI-LPBKDT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-LPBKDT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, NotificationType, iso, ModuleIdentity, Integer32, Counter32, Counter64, TimeTicks, Unsigned32, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "NotificationType", "iso", "ModuleIdentity", "Integer32", "Counter32", "Counter64", "TimeTicks", "Unsigned32", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cLpbkdt = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95))
h3cLpbkdt.setRevisions(('2009-03-30 17:41', '2008-09-27 15:04',))
if mibBuilder.loadTexts: h3cLpbkdt.setLastUpdated('200903301741Z')
if mibBuilder.loadTexts: h3cLpbkdt.setOrganization('H3C Technologies Co., Ltd.')
h3cLpbkdtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1))
h3cLpbkdtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 2))
h3cLpbkdtTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0))
h3cLpbkdtTrapLoopbacked = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: h3cLpbkdtTrapLoopbacked.setStatus('current')
h3cLpbkdtTrapRecovered = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: h3cLpbkdtTrapRecovered.setStatus('current')
h3cLpbkdtTrapPerVlanLoopbacked = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("A3COM-HUAWEI-LPBKDT-MIB", "h3cLpbkdtVlanID"))
if mibBuilder.loadTexts: h3cLpbkdtTrapPerVlanLoopbacked.setStatus('current')
h3cLpbkdtTrapPerVlanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("A3COM-HUAWEI-LPBKDT-MIB", "h3cLpbkdtVlanID"))
if mibBuilder.loadTexts: h3cLpbkdtTrapPerVlanRecovered.setStatus('current')
h3cLpbkdtVlanID = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 2, 1), VlanId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cLpbkdtVlanID.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-LPBKDT-MIB", PYSNMP_MODULE_ID=h3cLpbkdt, h3cLpbkdtTrapRecovered=h3cLpbkdtTrapRecovered, h3cLpbkdtTrapPerVlanLoopbacked=h3cLpbkdtTrapPerVlanLoopbacked, h3cLpbkdt=h3cLpbkdt, h3cLpbkdtNotifications=h3cLpbkdtNotifications, h3cLpbkdtTrapPrefix=h3cLpbkdtTrapPrefix, h3cLpbkdtTrapPerVlanRecovered=h3cLpbkdtTrapPerVlanRecovered, h3cLpbkdtObjects=h3cLpbkdtObjects, h3cLpbkdtTrapLoopbacked=h3cLpbkdtTrapLoopbacked, h3cLpbkdtVlanID=h3cLpbkdtVlanID)
