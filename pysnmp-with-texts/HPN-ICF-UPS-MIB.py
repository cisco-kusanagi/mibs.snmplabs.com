#
# PySNMP MIB module HPN-ICF-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-UPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:41:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Counter64, NotificationType, Counter32, Gauge32, iso, MibIdentifier, Bits, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Counter64", "NotificationType", "Counter32", "Gauge32", "iso", "MibIdentifier", "Bits", "IpAddress", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfUps = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82))
if mibBuilder.loadTexts: hpnicfUps.setLastUpdated('200709041452Z')
if mibBuilder.loadTexts: hpnicfUps.setOrganization('')
if mibBuilder.loadTexts: hpnicfUps.setContactInfo('')
if mibBuilder.loadTexts: hpnicfUps.setDescription('This MIB describes the general information of UPS(Uninterrupted Power Supply) device.')
hpnicfUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1))
class HpnicfActionType(TextualConvention, Integer32):
    description = 'A control variable used to trigger an operator events, when read, always returns a value of invalid.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

hpnicfUpsConfigEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 1), HpnicfActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUpsConfigEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfUpsConfigEnable.setDescription("This object identifies the operation which will make the UPS(Uninterrupted Power Supply)'s new configure become effective.")
hpnicfUpsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2), )
if mibBuilder.loadTexts: hpnicfUpsConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfUpsConfigTable.setDescription('This table contains an entry for user to get some information about the UPS device.')
hpnicfUpsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-UPS-MIB", "hpnicfUpsIndex"))
if mibBuilder.loadTexts: hpnicfUpsConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfUpsConfigEntry.setDescription('An entry containing management information applicable to a particular UPS.')
hpnicfUpsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfUpsIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfUpsIndex.setDescription('This object identifies the index of hpnicfUpsConfigTable. The object identified by this index is the same object as identified by the same value of entPhysicalIndex.')
hpnicfUpsType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("emersonUart", 1), ("mge", 2), ("common", 3), ("emersonEth", 4), ("liebert", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfUpsType.setStatus('current')
if mibBuilder.loadTexts: hpnicfUpsType.setDescription("This object identifies the type of UPS. The value 'emersonUart' means an EMERSON UPS support UART interface. The value 'mge' means a MGE UPS support ethernet interface. The value 'common' means a common UPS support standard UPSMIB. The value 'emersonEth' means an EMERSON UPS support ethernet interface. The value 'liebert' means a Liebert UPS support ethernet interface.")
hpnicfUpsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUpsIpAddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfUpsIpAddress.setDescription('This object describes the address of UPS. The value of this object is invalid if the UPS do not support ethernet interface.')
hpnicfUpsIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82, 1, 2, 1, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfUpsIpAddressType.setStatus('current')
if mibBuilder.loadTexts: hpnicfUpsIpAddressType.setDescription('This object describes the address type of UPS. The value of this object is invalid if the UPS do not support ethernet interface.')
mibBuilder.exportSymbols("HPN-ICF-UPS-MIB", PYSNMP_MODULE_ID=hpnicfUps, hpnicfUpsMibObjects=hpnicfUpsMibObjects, hpnicfUpsConfigTable=hpnicfUpsConfigTable, hpnicfUpsConfigEntry=hpnicfUpsConfigEntry, hpnicfUpsIpAddressType=hpnicfUpsIpAddressType, hpnicfUps=hpnicfUps, hpnicfUpsIpAddress=hpnicfUpsIpAddress, HpnicfActionType=HpnicfActionType, hpnicfUpsType=hpnicfUpsType, hpnicfUpsConfigEnable=hpnicfUpsConfigEnable, hpnicfUpsIndex=hpnicfUpsIndex)
