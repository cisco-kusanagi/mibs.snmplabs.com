#
# PySNMP MIB module A3COM-HUAWEI-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-IP-BROADCAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, ModuleIdentity, MibIdentifier, Integer32, iso, Unsigned32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Integer32", "iso", "Unsigned32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cIpBroadcast = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33))
h3cIpBroadcast.setRevisions(('2004-12-13 19:36',))
if mibBuilder.loadTexts: h3cIpBroadcast.setLastUpdated('200412131936Z')
if mibBuilder.loadTexts: h3cIpBroadcast.setOrganization('Huawei 3Com Technologies Co., Ltd.')
h3cIpBdstScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 1))
h3cIpBdstForwardBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpBdstForwardBroadcast.setStatus('current')
h3cIpReceiveBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receive", 1), ("notReceive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpReceiveBroadcast.setStatus('current')
h3cIpBdstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 2))
h3cIpBdstTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 3))
h3cIpBdstTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 3, 0))
mibBuilder.exportSymbols("A3COM-HUAWEI-IP-BROADCAST-MIB", h3cIpBdstForwardBroadcast=h3cIpBdstForwardBroadcast, h3cIpBdstTrap=h3cIpBdstTrap, PYSNMP_MODULE_ID=h3cIpBroadcast, h3cIpBroadcast=h3cIpBroadcast, h3cIpBdstScalarGroup=h3cIpBdstScalarGroup, h3cIpBdstGroup=h3cIpBdstGroup, h3cIpBdstTrapPrex=h3cIpBdstTrapPrex, h3cIpReceiveBroadcast=h3cIpReceiveBroadcast)
