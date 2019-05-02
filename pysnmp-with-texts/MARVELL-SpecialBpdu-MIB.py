#
# PySNMP MIB module MARVELL-SpecialBpdu-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-SpecialBpdu-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, NotificationType, Integer32, IpAddress, Counter32, MibIdentifier, Counter64, ModuleIdentity, Gauge32, ObjectIdentity, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "NotificationType", "Integer32", "IpAddress", "Counter32", "MibIdentifier", "Counter64", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
MacAddress, DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
rlSpecialBpdu = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 144))
rlSpecialBpdu.setRevisions(('2008-05-03 12:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSpecialBpdu.setRevisionsDescriptions(('The private MIB module definition Traffic Segmentation MIB.',))
if mibBuilder.loadTexts: rlSpecialBpdu.setLastUpdated('200805031234Z')
if mibBuilder.loadTexts: rlSpecialBpdu.setOrganization('MARVELL Semiconductor, Inc.')
if mibBuilder.loadTexts: rlSpecialBpdu.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlSpecialBpdu.setDescription('<description>')
class EncapType(TextualConvention, Integer32):
    description = 'The L2 encapsulation type. In case the entry contains MAC only, the encapsulation will be none(1), otherwisw: EthernetV2 (2), LLC (2) or LLC-Snap (3)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("ethernet-v2", 2), ("llc", 3), ("llc-snap", 4))

class Action(TextualConvention, Integer32):
    description = 'Action to be taken. Bridge(1) or Discard (2)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bridge", 1), ("discard", 2))

class HwAction(TextualConvention, Integer32):
    description = 'Configured action in the HW. Forward(1), Drop (2) or Trap(3)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forward", 1), ("drop", 2), ("trap", 3))

rlSpecialBpduTable = MibTable((1, 3, 6, 1, 4, 1, 89, 144, 1), )
if mibBuilder.loadTexts: rlSpecialBpduTable.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduTable.setDescription('A table contains entries of Special BPDU configuration')
rlSpecialBpduEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 144, 1, 1), ).setIndexNames((0, "MARVELL-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"), (0, "MARVELL-SpecialBpdu-MIB", "rlSpecialBpduEncap"), (0, "MARVELL-SpecialBpdu-MIB", "rlSpecialBpduProtId"))
if mibBuilder.loadTexts: rlSpecialBpduEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduEntry.setDescription('An entry of Special BPDU configuration table')
rlSpecialBpduMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setDescription('Reserved MAC Mc 01:80:C2:00:00:00 - 01:80:C2:00:00:2F.')
rlSpecialBpduEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 1, 1, 2), EncapType())
if mibBuilder.loadTexts: rlSpecialBpduEncap.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduEncap.setDescription('L2 Encapsulation Type: Ethernet-V2, LLC or LLC-Snap.')
rlSpecialBpduProtId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5))
if mibBuilder.loadTexts: rlSpecialBpduProtId.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduProtId.setDescription('Protocol ID. For Ethernet-V2: 0x600 - 0xFFFF; For LLC: 0 - 0xFFFF; For LLC-Snap: 0 - 0xFFFFFFFFFF.')
rlSpecialBpduAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 1, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpecialBpduAction.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduAction.setDescription('Action to be taken on the incoming frame: Discard or Bridge.')
rlSpecialBpduRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setDescription('This object indicates the status of this entry.')
rlSpecialBpduHwTable = MibTable((1, 3, 6, 1, 4, 1, 89, 144, 2), )
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setDescription('A table contains entries of Special BPDU Hw status')
rlSpecialBpduHwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 144, 2, 1), ).setIndexNames((0, "MARVELL-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"))
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setDescription('An entry of Special BPDU Hw status table')
rlSpecialBpduHwAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 144, 2, 1, 2), HwAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setDescription('HW action per MAC address: Forward, Drop or Trap.')
mibBuilder.exportSymbols("MARVELL-SpecialBpdu-MIB", rlSpecialBpduEntry=rlSpecialBpduEntry, rlSpecialBpduHwEntry=rlSpecialBpduHwEntry, EncapType=EncapType, rlSpecialBpduRowStatus=rlSpecialBpduRowStatus, rlSpecialBpduEncap=rlSpecialBpduEncap, HwAction=HwAction, rlSpecialBpduMacAddr=rlSpecialBpduMacAddr, PYSNMP_MODULE_ID=rlSpecialBpdu, rlSpecialBpduProtId=rlSpecialBpduProtId, rlSpecialBpduHwTable=rlSpecialBpduHwTable, rlSpecialBpduTable=rlSpecialBpduTable, rlSpecialBpdu=rlSpecialBpdu, rlSpecialBpduHwAction=rlSpecialBpduHwAction, rlSpecialBpduAction=rlSpecialBpduAction, Action=Action)
