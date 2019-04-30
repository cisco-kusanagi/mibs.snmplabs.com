#
# PySNMP MIB module HPN-ICF-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-UPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, ModuleIdentity, IpAddress, Counter32, NotificationType, Bits, TimeTicks, Integer32, iso, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter32", "NotificationType", "Bits", "TimeTicks", "Integer32", "iso", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfUps = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82))
if mibBuilder.loadTexts: hpnicfUps.setLastUpdated('200709041452Z')
if mibBuilder.loadTexts: hpnicfUps.setOrganization('')
hpnicfUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1))
class HpnicfActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

hpnicfUpsConfigEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 1), HpnicfActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUpsConfigEnable.setStatus('current')
hpnicfUpsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2), )
if mibBuilder.loadTexts: hpnicfUpsConfigTable.setStatus('current')
hpnicfUpsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-UPS-MIB", "hpnicfUpsIndex"))
if mibBuilder.loadTexts: hpnicfUpsConfigEntry.setStatus('current')
hpnicfUpsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfUpsIndex.setStatus('current')
hpnicfUpsType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("emersonUart", 1), ("mge", 2), ("common", 3), ("emersonEth", 4), ("liebert", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfUpsType.setStatus('current')
hpnicfUpsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUpsIpAddress.setStatus('current')
hpnicfUpsIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUpsIpAddressType.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-UPS-MIB", HpnicfActionType=HpnicfActionType, hpnicfUpsConfigEnable=hpnicfUpsConfigEnable, hpnicfUpsConfigEntry=hpnicfUpsConfigEntry, hpnicfUpsType=hpnicfUpsType, hpnicfUpsIpAddress=hpnicfUpsIpAddress, hpnicfUpsIndex=hpnicfUpsIndex, PYSNMP_MODULE_ID=hpnicfUps, hpnicfUpsConfigTable=hpnicfUpsConfigTable, hpnicfUpsIpAddressType=hpnicfUpsIpAddressType, hpnicfUpsMibObjects=hpnicfUpsMibObjects, hpnicfUps=hpnicfUps)
