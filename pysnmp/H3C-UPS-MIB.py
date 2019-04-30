#
# PySNMP MIB module H3C-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-UPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:11:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, ModuleIdentity, Counter32, Unsigned32, IpAddress, Bits, Gauge32, ObjectIdentity, Counter64, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "ModuleIdentity", "Counter32", "Unsigned32", "IpAddress", "Bits", "Gauge32", "ObjectIdentity", "Counter64", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cUps = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82))
if mibBuilder.loadTexts: h3cUps.setLastUpdated('200709041452Z')
if mibBuilder.loadTexts: h3cUps.setOrganization('H3C Technologies Co., Ltd.')
h3cUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1))
class H3cActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

h3cUpsConfigEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 1), H3cActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cUpsConfigEnable.setStatus('current')
h3cUpsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2), )
if mibBuilder.loadTexts: h3cUpsConfigTable.setStatus('current')
h3cUpsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1), ).setIndexNames((0, "H3C-UPS-MIB", "h3cUpsIndex"))
if mibBuilder.loadTexts: h3cUpsConfigEntry.setStatus('current')
h3cUpsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cUpsIndex.setStatus('current')
h3cUpsType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("emersonUart", 1), ("mge", 2), ("common", 3), ("emersonEth", 4), ("liebert", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cUpsType.setStatus('current')
h3cUpsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cUpsIpAddress.setStatus('current')
h3cUpsIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cUpsIpAddressType.setStatus('current')
mibBuilder.exportSymbols("H3C-UPS-MIB", h3cUpsConfigTable=h3cUpsConfigTable, h3cUpsConfigEntry=h3cUpsConfigEntry, h3cUpsIpAddressType=h3cUpsIpAddressType, h3cUpsIndex=h3cUpsIndex, h3cUpsMibObjects=h3cUpsMibObjects, PYSNMP_MODULE_ID=h3cUps, h3cUpsConfigEnable=h3cUpsConfigEnable, h3cUps=h3cUps, h3cUpsType=h3cUpsType, H3cActionType=H3cActionType, h3cUpsIpAddress=h3cUpsIpAddress)
