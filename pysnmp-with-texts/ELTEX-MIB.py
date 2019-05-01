#
# PySNMP MIB module ELTEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:00:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, ModuleIdentity, Bits, Unsigned32, Gauge32, MibIdentifier, Counter64, enterprises, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32", "Gauge32", "MibIdentifier", "Counter64", "enterprises", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class Percents(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class VlanPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

elt = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265))
elt.setRevisions(('2012-12-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: elt.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: elt.setLastUpdated('201212180000Z')
if mibBuilder.loadTexts: elt.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: elt.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: elt.setDescription("This private MIB module defines Eltex's private MIBs.")
eltNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 35265, 0))
if mibBuilder.loadTexts: eltNotifications.setStatus('current')
if mibBuilder.loadTexts: eltNotifications.setDescription(" All the Eltex notifications will reside under this branch as specified in RFC2578 'Structure of Management Information Version 2 (SMIv2)' 8.5")
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
mibBuilder.exportSymbols("ELTEX-MIB", PYSNMP_MODULE_ID=elt, eltEndOfMibGroup=eltEndOfMibGroup, eltPhy=eltPhy, elt=elt, eltRadius=eltRadius, eltdot1x=eltdot1x, eltCopy=eltCopy, eltNotifications=eltNotifications, Percents=Percents, eltMacMulticast=eltMacMulticast, eltTuning=eltTuning, eltDevParams=eltDevParams, eltIpOspfMtu=eltIpOspfMtu, eltQosTailDropMib=eltQosTailDropMib, eltQosCliMib=eltQosCliMib, eltIpUnnumbered=eltIpUnnumbered, VlanPriority=VlanPriority, eltStormCtrl=eltStormCtrl, eltPhdTransceiver=eltPhdTransceiver, ipSpec=ipSpec, NetNumber=NetNumber, eltMng=eltMng, eltIpMulticast=eltIpMulticast, eltSwInterfaces=eltSwInterfaces, eltBridgeSecurity=eltBridgeSecurity, eltDhcp=eltDhcp, eltIpBfd=eltIpBfd, eltLinkAgg=eltLinkAgg)
