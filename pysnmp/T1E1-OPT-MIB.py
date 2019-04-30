#
# PySNMP MIB module T1E1-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/T1E1-OPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:07:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Unsigned32, NotificationType, Integer32, Gauge32, Bits, TimeTicks, enterprises, ModuleIdentity, IpAddress, Counter32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Unsigned32", "NotificationType", "Integer32", "Gauge32", "Bits", "TimeTicks", "enterprises", "ModuleIdentity", "IpAddress", "Counter32", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1))
cdx6500PCTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1))
cdx6500PCTT1E1PortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1))
cdx6500PSTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1))
cdx6500PSTT1E1PortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25))
class DisplayString(OctetString):
    pass

class PhysicalPortNumber(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(49, 50)

class VirtualPortNumber(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(100, 255)

cdx6500VPCTT1E1PortTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3), )
if mibBuilder.loadTexts: cdx6500VPCTT1E1PortTable.setStatus('mandatory')
cdx6500VPCTT1E1PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1), ).setIndexNames((0, "T1E1-OPT-MIB", "cdx6500VPCTT1E1CfgIndex"))
if mibBuilder.loadTexts: cdx6500VPCTT1E1PortEntry.setStatus('mandatory')
cdx6500VPCTT1E1CfgPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPortNumber.setStatus('mandatory')
cdx6500VPCTT1E1CfgPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 100))).clone(namedValues=NamedValues(("voice", 1), ("data", 2), ("switchedVoice", 3), ("switchedData", 4), ("bypassVoice", 5), ("bypassData", 6), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPortType.setStatus('mandatory')
cdx6500VPCTT1E1CfgPhyPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPhyPortNumber.setStatus('mandatory')
cdx6500VPCTT1E1CfgTimeSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgTimeSlotNumber.setStatus('mandatory')
cdx6500VPCTT1E1CfgDS0Rate = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("ds056k", 1), ("ds064k", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgDS0Rate.setStatus('mandatory')
cdx6500VPCTT1E1CfgAggregateType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 100))).clone(namedValues=NamedValues(("t1e1", 1), ("so", 2), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgAggregateType.setStatus('mandatory')
cdx6500VPCTT1E1CfgSOPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgSOPortNumber.setStatus('mandatory')
cdx6500VPCTT1E1CfgBChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgBChannel.setStatus('mandatory')
cdx6500VPCTT1E1CfgLocalSubscriberAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgLocalSubscriberAddress.setStatus('mandatory')
cdx6500VPCTT1E1CfgNetSpecCall = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 9, 17, 100))).clone(namedValues=NamedValues(("none", 1), ("attSdn", 2), ("attMc800", 3), ("attMc", 4), ("ntFx", 5), ("ntTieTrunk", 6), ("attAccunet", 7), ("attInt800", 9), ("attMq", 17), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgNetSpecCall.setStatus('mandatory')
cdx6500VPCTT1E1CfgPartyNumberType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5, 7, 100))).clone(namedValues=NamedValues(("unknown", 1), ("international", 2), ("national", 3), ("subscriber", 5), ("abbreviated", 7), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPartyNumberType.setStatus('mandatory')
cdx6500VPCTT1E1CfgPartyNumberPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 10, 100))).clone(namedValues=NamedValues(("unknown", 1), ("isdn", 2), ("telephony", 3), ("private", 10), ("nc", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgPartyNumberPlan.setStatus('mandatory')
cdx6500VPCTT1E1CfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPCTT1E1CfgIndex.setStatus('mandatory')
mibBuilder.exportSymbols("T1E1-OPT-MIB", cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, cdx6500VPCTT1E1CfgTimeSlotNumber=cdx6500VPCTT1E1CfgTimeSlotNumber, cdx6500VPCTT1E1CfgPartyNumberType=cdx6500VPCTT1E1CfgPartyNumberType, cdx6500Configuration=cdx6500Configuration, cdx6500VPCTT1E1PortEntry=cdx6500VPCTT1E1PortEntry, cdx6500PSTT1E1PortTable=cdx6500PSTT1E1PortTable, cdx6500=cdx6500, cdx6500VPCTT1E1CfgNetSpecCall=cdx6500VPCTT1E1CfgNetSpecCall, cdx6500VPCTT1E1CfgAggregateType=cdx6500VPCTT1E1CfgAggregateType, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, cdx6500VPCTT1E1CfgPartyNumberPlan=cdx6500VPCTT1E1CfgPartyNumberPlan, cdx6500PCTT1E1PortTable=cdx6500PCTT1E1PortTable, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, cdx6500VPCTT1E1CfgIndex=cdx6500VPCTT1E1CfgIndex, PhysicalPortNumber=PhysicalPortNumber, cdx6500VPCTT1E1CfgLocalSubscriberAddress=cdx6500VPCTT1E1CfgLocalSubscriberAddress, cdxProductSpecific=cdxProductSpecific, cdx6500VPCTT1E1CfgDS0Rate=cdx6500VPCTT1E1CfgDS0Rate, cdx6500VPCTT1E1CfgBChannel=cdx6500VPCTT1E1CfgBChannel, DisplayString=DisplayString, VirtualPortNumber=VirtualPortNumber, cdx6500VPCTT1E1CfgPortNumber=cdx6500VPCTT1E1CfgPortNumber, cdx6500VPCTT1E1CfgPhyPortNumber=cdx6500VPCTT1E1CfgPhyPortNumber, codex=codex, cdx6500VPCTT1E1CfgPortType=cdx6500VPCTT1E1CfgPortType, cdx6500VPCTT1E1CfgSOPortNumber=cdx6500VPCTT1E1CfgSOPortNumber, cdx6500Statistics=cdx6500Statistics, cdx6500VPCTT1E1PortTable=cdx6500VPCTT1E1PortTable, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup)
