#
# PySNMP MIB module HH3C-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-UPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:17:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, Counter32, Integer32, TimeTicks, MibIdentifier, Bits, Unsigned32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Counter32", "Integer32", "TimeTicks", "MibIdentifier", "Bits", "Unsigned32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cUps = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 82))
if mibBuilder.loadTexts: hh3cUps.setLastUpdated('200709041452Z')
if mibBuilder.loadTexts: hh3cUps.setOrganization('H3C Technologies Co., Ltd.')
hh3cUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 82, 1))
class Hh3cActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

hh3cUpsConfigEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 1), Hh3cActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUpsConfigEnable.setStatus('current')
hh3cUpsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2), )
if mibBuilder.loadTexts: hh3cUpsConfigTable.setStatus('current')
hh3cUpsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2, 1), ).setIndexNames((0, "HH3C-UPS-MIB", "hh3cUpsIndex"))
if mibBuilder.loadTexts: hh3cUpsConfigEntry.setStatus('current')
hh3cUpsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cUpsIndex.setStatus('current')
hh3cUpsType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("emersonUart", 1), ("mge", 2), ("common", 3), ("emersonEth", 4), ("liebert", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUpsType.setStatus('current')
hh3cUpsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUpsIpAddress.setStatus('current')
hh3cUpsIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2, 1, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cUpsIpAddressType.setStatus('current')
mibBuilder.exportSymbols("HH3C-UPS-MIB", hh3cUpsType=hh3cUpsType, hh3cUpsConfigEnable=hh3cUpsConfigEnable, hh3cUpsIpAddress=hh3cUpsIpAddress, PYSNMP_MODULE_ID=hh3cUps, hh3cUps=hh3cUps, hh3cUpsIpAddressType=hh3cUpsIpAddressType, hh3cUpsConfigEntry=hh3cUpsConfigEntry, hh3cUpsIndex=hh3cUpsIndex, hh3cUpsConfigTable=hh3cUpsConfigTable, Hh3cActionType=Hh3cActionType, hh3cUpsMibObjects=hh3cUpsMibObjects)
