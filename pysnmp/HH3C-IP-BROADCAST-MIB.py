#
# PySNMP MIB module HH3C-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-IP-BROADCAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, Bits, MibIdentifier, TimeTicks, Counter32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Bits", "MibIdentifier", "TimeTicks", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cIpBroadcast = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 33))
hh3cIpBroadcast.setRevisions(('2004-12-13 19:36',))
if mibBuilder.loadTexts: hh3cIpBroadcast.setLastUpdated('200412131936Z')
if mibBuilder.loadTexts: hh3cIpBroadcast.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cIpBdstScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 33, 1))
hh3cIpBdstForwardBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 33, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpBdstForwardBroadcast.setStatus('current')
hh3cIpReceiveBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 33, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receive", 1), ("notReceive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpReceiveBroadcast.setStatus('current')
hh3cIpBdstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 33, 2))
hh3cIpBdstTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 33, 3))
hh3cIpBdstTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 33, 3, 0))
mibBuilder.exportSymbols("HH3C-IP-BROADCAST-MIB", hh3cIpBroadcast=hh3cIpBroadcast, PYSNMP_MODULE_ID=hh3cIpBroadcast, hh3cIpBdstForwardBroadcast=hh3cIpBdstForwardBroadcast, hh3cIpBdstTrapPrex=hh3cIpBdstTrapPrex, hh3cIpBdstTrap=hh3cIpBdstTrap, hh3cIpReceiveBroadcast=hh3cIpReceiveBroadcast, hh3cIpBdstScalarGroup=hh3cIpBdstScalarGroup, hh3cIpBdstGroup=hh3cIpBdstGroup)
