#
# PySNMP MIB module ELTEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, Counter32, Gauge32, ObjectIdentity, Counter64, enterprises, iso, ModuleIdentity, TimeTicks, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "enterprises", "iso", "ModuleIdentity", "TimeTicks", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Percents(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class VlanPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

elt = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265))
elt.setRevisions(('2012-12-18 00:00',))
if mibBuilder.loadTexts: elt.setLastUpdated('201212180000Z')
if mibBuilder.loadTexts: elt.setOrganization('Eltex Enterprise Co, Ltd.')
eltNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 35265, 0))
if mibBuilder.loadTexts: eltNotifications.setStatus('current')
eltMng = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1))
eltDevParams = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 2))
eltCopy = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 3))
eltIpOspfMtu = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 4))
eltIpBfd = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 6))
eltIpUnnumbered = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 7))
eltDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 8))
eltLinkAgg = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 9))
eltQosTailDropMib = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 12))
eltTuning = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 29))
eltSwInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 43))
eltIpMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 46))
eltPhdTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 53))
eltMacMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 55))
eltStormCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 77))
eltRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 80))
eltQosCliMib = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 88))
eltPhy = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 90))
ipSpec = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 91))
eltdot1x = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 95))
eltBridgeSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 112))
eltEndOfMibGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1000))
mibBuilder.exportSymbols("ELTEX-MIB", eltDevParams=eltDevParams, eltIpUnnumbered=eltIpUnnumbered, VlanPriority=VlanPriority, eltTuning=eltTuning, eltRadius=eltRadius, Percents=Percents, eltMacMulticast=eltMacMulticast, eltCopy=eltCopy, PYSNMP_MODULE_ID=elt, eltEndOfMibGroup=eltEndOfMibGroup, elt=elt, eltNotifications=eltNotifications, eltIpBfd=eltIpBfd, ipSpec=ipSpec, eltdot1x=eltdot1x, eltPhdTransceiver=eltPhdTransceiver, eltStormCtrl=eltStormCtrl, eltIpOspfMtu=eltIpOspfMtu, eltDhcp=eltDhcp, eltSwInterfaces=eltSwInterfaces, NetNumber=NetNumber, eltQosCliMib=eltQosCliMib, eltBridgeSecurity=eltBridgeSecurity, eltPhy=eltPhy, eltLinkAgg=eltLinkAgg, eltQosTailDropMib=eltQosTailDropMib, eltMng=eltMng, eltIpMulticast=eltIpMulticast)
