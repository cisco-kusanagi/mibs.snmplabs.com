#
# PySNMP MIB module ZYXEL-POWER-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-POWER-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Unsigned32, ObjectIdentity, MibIdentifier, Counter32, Counter64, IpAddress, Gauge32, ModuleIdentity, Bits, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Counter32", "Counter64", "IpAddress", "Gauge32", "ModuleIdentity", "Bits", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelPoe = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59))
if mibBuilder.loadTexts: zyxelPoe.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelPoe.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelPoe.setContactInfo('')
if mibBuilder.loadTexts: zyxelPoe.setDescription('The subtree for Power over Ethernet (PoE)')
zyxelPoeSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1))
zyxelPoeStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2))
zyxelPoeTrapInfoObject = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 3))
zyxelPoeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4))
zyPoeMode = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("consumption", 0), ("classification", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPoeMode.setStatus('current')
if mibBuilder.loadTexts: zyPoeMode.setDescription('Set POE Mode Setup Consumption mode (0), Classification mode (1).')
zyxelPoePsePortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2), )
if mibBuilder.loadTexts: zyxelPoePsePortTable.setStatus('current')
if mibBuilder.loadTexts: zyxelPoePsePortTable.setDescription('The table contains power ethernet port information. ')
zyxelPoePsePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelPoePsePortEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelPoePsePortEntry.setDescription('An entry contains power ethernet port information. ')
zyPoePsePortMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 1, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyPoePsePortMaxPower.setStatus('current')
if mibBuilder.loadTexts: zyPoePsePortMaxPower.setDescription('PoE PSE port user-defined max power expressed in milliwatt, Valid value should be between 1000 and 33000,in steps of 200. Value 0(Default) means to disable user-defined max power.')
zyxelPoePsePortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1), )
if mibBuilder.loadTexts: zyxelPoePsePortInfoTable.setStatus('current')
if mibBuilder.loadTexts: zyxelPoePsePortInfoTable.setDescription('The table contains power ethernet port information. ')
zyxelPoePsePortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelPoePsePortInfoEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelPoePsePortInfoEntry.setDescription('An entry contains power ethernet port information. ')
zyPoePsePortInfoPowerConsumption = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPoePsePortInfoPowerConsumption.setStatus('current')
if mibBuilder.loadTexts: zyPoePsePortInfoPowerConsumption.setDescription('PoE PSE port power consumption expressed in milliwatt.')
zyPoeTrapPsePowerSupplyFailedReason = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("internalPowerSupplyForPoeFailed", 0), ("rpsForPoeFailed", 1), ("rpsFanFailed", 2), ("rpsOverTemperature", 3))))
if mibBuilder.loadTexts: zyPoeTrapPsePowerSupplyFailedReason.setStatus('current')
if mibBuilder.loadTexts: zyPoeTrapPsePowerSupplyFailedReason.setDescription('Internal-power-supply-for-PoE-failed(0): Internal power supply for PoE has failed. RPS-for-PoE-failed(1): External power supply for PoE (RPS) has failed. RPS-fan-failed(2): RPS fan has failed. RPS-over-temperature(3): RPS temperature is out of the normal operation range.')
zyPoePowerPortOverload = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyPoePowerPortOverload.setStatus('current')
if mibBuilder.loadTexts: zyPoePowerPortOverload.setDescription('Port is off, due to the overload state according to 802.3af.')
zyPoePowerPortShortCircuit = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyPoePowerPortShortCircuit.setStatus('current')
if mibBuilder.loadTexts: zyPoePowerPortShortCircuit.setDescription('Port is off, due to short circuit.')
zyPoePowerPortOverSystemBudget = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyPoePowerPortOverSystemBudget.setStatus('current')
if mibBuilder.loadTexts: zyPoePowerPortOverSystemBudget.setDescription('Port is off, due to over system budget.')
zyPoePsePowerSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 4)).setObjects(("ZYXEL-POWER-ETHERNET-MIB", "zyPoeTrapPsePowerSupplyFailedReason"))
if mibBuilder.loadTexts: zyPoePsePowerSupplyFailed.setStatus('current')
if mibBuilder.loadTexts: zyPoePsePowerSupplyFailed.setDescription('PSE power supply failed, due to the reason of zyxelPoeTrapPsePowerSupplyFailedReason.')
zyPoePowerPortOverloadRecovered = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 5)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyPoePowerPortOverloadRecovered.setStatus('current')
if mibBuilder.loadTexts: zyPoePowerPortOverloadRecovered.setDescription('Port is on, since recovered from overload state.')
zyPoePowerPortShortCircuitRecovered = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 6)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyPoePowerPortShortCircuitRecovered.setStatus('current')
if mibBuilder.loadTexts: zyPoePowerPortShortCircuitRecovered.setDescription('Port is on, since recovered from short circuit.')
zyPoePowerPortOverSystemBudgetRecovered = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 59, 4, 7)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zyPoePowerPortOverSystemBudgetRecovered.setStatus('current')
if mibBuilder.loadTexts: zyPoePowerPortOverSystemBudgetRecovered.setDescription('Port is on, since recovered from over system budget.')
mibBuilder.exportSymbols("ZYXEL-POWER-ETHERNET-MIB", zyPoePsePortMaxPower=zyPoePsePortMaxPower, zyxelPoe=zyxelPoe, zyxelPoePsePortInfoTable=zyxelPoePsePortInfoTable, zyPoePowerPortOverload=zyPoePowerPortOverload, zyxelPoeSetup=zyxelPoeSetup, zyPoePowerPortOverloadRecovered=zyPoePowerPortOverloadRecovered, zyxelPoeTrapInfoObject=zyxelPoeTrapInfoObject, PYSNMP_MODULE_ID=zyxelPoe, zyPoeMode=zyPoeMode, zyPoePsePowerSupplyFailed=zyPoePsePowerSupplyFailed, zyxelPoePsePortInfoEntry=zyxelPoePsePortInfoEntry, zyPoePowerPortOverSystemBudgetRecovered=zyPoePowerPortOverSystemBudgetRecovered, zyxelPoeNotifications=zyxelPoeNotifications, zyPoeTrapPsePowerSupplyFailedReason=zyPoeTrapPsePowerSupplyFailedReason, zyxelPoePsePortEntry=zyxelPoePsePortEntry, zyPoePowerPortShortCircuit=zyPoePowerPortShortCircuit, zyPoePsePortInfoPowerConsumption=zyPoePsePortInfoPowerConsumption, zyPoePowerPortShortCircuitRecovered=zyPoePowerPortShortCircuitRecovered, zyxelPoeStatus=zyxelPoeStatus, zyxelPoePsePortTable=zyxelPoePsePortTable, zyPoePowerPortOverSystemBudget=zyPoePowerPortOverSystemBudget)