#
# PySNMP MIB module HPN-ICF-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-IP-BROADCAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, Counter64, Gauge32, IpAddress, Bits, Counter32, iso, TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Counter64", "Gauge32", "IpAddress", "Bits", "Counter32", "iso", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfIpBroadcast = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33))
hpnicfIpBroadcast.setRevisions(('2004-12-13 19:36',))
if mibBuilder.loadTexts: hpnicfIpBroadcast.setLastUpdated('200412131936Z')
if mibBuilder.loadTexts: hpnicfIpBroadcast.setOrganization('')
hpnicfIpBdstScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1))
hpnicfIpBdstForwardBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpBdstForwardBroadcast.setStatus('current')
hpnicfIpReceiveBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receive", 1), ("notReceive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpReceiveBroadcast.setStatus('current')
hpnicfIpBdstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 2))
hpnicfIpBdstTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 3))
hpnicfIpBdstTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 3, 0))
mibBuilder.exportSymbols("HPN-ICF-IP-BROADCAST-MIB", hpnicfIpBdstForwardBroadcast=hpnicfIpBdstForwardBroadcast, hpnicfIpBdstTrap=hpnicfIpBdstTrap, hpnicfIpBdstScalarGroup=hpnicfIpBdstScalarGroup, PYSNMP_MODULE_ID=hpnicfIpBroadcast, hpnicfIpBroadcast=hpnicfIpBroadcast, hpnicfIpBdstGroup=hpnicfIpBdstGroup, hpnicfIpReceiveBroadcast=hpnicfIpReceiveBroadcast, hpnicfIpBdstTrapPrex=hpnicfIpBdstTrapPrex)
