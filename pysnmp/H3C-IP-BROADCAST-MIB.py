#
# PySNMP MIB module H3C-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-IP-BROADCAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:09:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, ModuleIdentity, Counter32, Bits, TimeTicks, Gauge32, MibIdentifier, NotificationType, Counter64, Integer32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "ModuleIdentity", "Counter32", "Bits", "TimeTicks", "Gauge32", "MibIdentifier", "NotificationType", "Counter64", "Integer32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cIpBroadcast = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33))
h3cIpBroadcast.setRevisions(('2004-12-13 19:36',))
if mibBuilder.loadTexts: h3cIpBroadcast.setLastUpdated('200412131936Z')
if mibBuilder.loadTexts: h3cIpBroadcast.setOrganization('Huawei 3Com Technologies Co., Ltd.')
h3cIpBdstScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 1))
h3cIpBdstForwardBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpBdstForwardBroadcast.setStatus('current')
h3cIpReceiveBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receive", 1), ("notReceive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpReceiveBroadcast.setStatus('current')
h3cIpBdstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 2))
h3cIpBdstTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 3))
h3cIpBdstTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 33, 3, 0))
mibBuilder.exportSymbols("H3C-IP-BROADCAST-MIB", PYSNMP_MODULE_ID=h3cIpBroadcast, h3cIpBroadcast=h3cIpBroadcast, h3cIpBdstForwardBroadcast=h3cIpBdstForwardBroadcast, h3cIpReceiveBroadcast=h3cIpReceiveBroadcast, h3cIpBdstTrap=h3cIpBdstTrap, h3cIpBdstTrapPrex=h3cIpBdstTrapPrex, h3cIpBdstGroup=h3cIpBdstGroup, h3cIpBdstScalarGroup=h3cIpBdstScalarGroup)
