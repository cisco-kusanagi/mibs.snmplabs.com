#
# PySNMP MIB module Dlink-GREEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dlink-GREEN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:43:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Bits, Counter32, Counter64, TimeTicks, ObjectIdentity, Gauge32, IpAddress, Unsigned32, MibIdentifier, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Bits", "Counter32", "Counter64", "TimeTicks", "ObjectIdentity", "Gauge32", "IpAddress", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
rlGreenEth = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134))
rlGreenEth.setRevisions(('2008-08-15 00:00',))
if mibBuilder.loadTexts: rlGreenEth.setLastUpdated('200808150000Z')
if mibBuilder.loadTexts: rlGreenEth.setOrganization('Dlink Semiconductor, Inc.')
rlGreenEthEnergyDetectEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthEnergyDetectEnable.setStatus('current')
rlGreenEthShortReachEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthShortReachEnable.setStatus('current')
rlGreenEthCurrentEnergyConsumption = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 3), Unsigned32()).setUnits('mWatt').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCurrentEnergyConsumption.setStatus('current')
rlGreenEthCurrentMaxEnergyConsumption = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 4), Unsigned32()).setUnits('mWatt').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCurrentMaxEnergyConsumption.setStatus('current')
rlGreenEthCumulativePowerSaveMeter = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 5), Unsigned32()).setUnits('Watt*Hour').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeter.setStatus('current')
rlGreenEthShortReachThreshold = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 70))).setUnits('meter').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthShortReachThreshold.setStatus('current')
rlGreenEthCumulativePowerSaveMeterReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeterReset.setStatus('current')
class RlGreenSavingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("energyDetect", 1), ("shortReach", 2))

class NonOperReasonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("np", 1), ("lt", 2), ("lu", 3), ("ls", 4), ("ll", 5), ("er", 6), ("ld", 7), ("unknown", 8))

rlGreenEthPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 8), )
if mibBuilder.loadTexts: rlGreenEthPortTable.setStatus('current')
rlGreenEthPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "Dlink-GREEN-MIB", "rlGreenEthPortSavingTypeValue"))
if mibBuilder.loadTexts: rlGreenEthPortEntry.setStatus('current')
rlGreenEthPortSavingTypeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 8, 1, 1), RlGreenSavingType())
if mibBuilder.loadTexts: rlGreenEthPortSavingTypeValue.setStatus('current')
rlGreenEthPortAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 8, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthPortAdminState.setStatus('current')
rlGreenEthPortOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 8, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortOperState.setStatus('current')
rlGreenEthPortNonOperReason = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 8, 1, 4), NonOperReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortNonOperReason.setStatus('current')
rlGreenEthForceShortReachIfIndexList = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 134, 9), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthForceShortReachIfIndexList.setStatus('current')
mibBuilder.exportSymbols("Dlink-GREEN-MIB", rlGreenEthPortTable=rlGreenEthPortTable, RlGreenSavingType=RlGreenSavingType, rlGreenEthPortEntry=rlGreenEthPortEntry, rlGreenEthPortAdminState=rlGreenEthPortAdminState, rlGreenEthPortOperState=rlGreenEthPortOperState, rlGreenEthCurrentEnergyConsumption=rlGreenEthCurrentEnergyConsumption, rlGreenEthCurrentMaxEnergyConsumption=rlGreenEthCurrentMaxEnergyConsumption, rlGreenEthShortReachThreshold=rlGreenEthShortReachThreshold, rlGreenEthEnergyDetectEnable=rlGreenEthEnergyDetectEnable, rlGreenEthForceShortReachIfIndexList=rlGreenEthForceShortReachIfIndexList, rlGreenEthCumulativePowerSaveMeterReset=rlGreenEthCumulativePowerSaveMeterReset, rlGreenEth=rlGreenEth, PYSNMP_MODULE_ID=rlGreenEth, rlGreenEthPortNonOperReason=rlGreenEthPortNonOperReason, NonOperReasonType=NonOperReasonType, rlGreenEthPortSavingTypeValue=rlGreenEthPortSavingTypeValue, rlGreenEthCumulativePowerSaveMeter=rlGreenEthCumulativePowerSaveMeter, rlGreenEthShortReachEnable=rlGreenEthShortReachEnable)
